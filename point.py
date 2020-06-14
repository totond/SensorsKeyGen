import pandas as pd
import os
import argparse
import pyperclip

# region 文案存储

HEAD_STR_JAVA = '''    @SensorsEventName(eventName = "%s")
	public static class %sEvent
	{
	'''

HEAD_STR_KOTLIN = '''@SensorsEventName(eventName = "%s")
object %sEvent {
'''

HEAD_ANNO_STR_JAVA = '''
	/**
	 * %s
	 */
'''

HEAD_ANNO_STR_KOTLIN = '''
/**
 * %s
 */
'''

ANNO_STR_JAVA = '''
		/**
		 * %s
		 */
'''

ANNO_STR_KOTLIN = '''
    /**
     * %s
     */
'''

PARAMS_STR_JAVA = '''	    public static final String PROPERTY_%s = "%s";
'''

PARAMS_STR_KOTLIN = '''    const val PROPERTY_%s = "%s"
'''

END_STR_JAVA = "\n    }"
END_STR_KOTLIN = "\n}"

LAN_KOTLIN = "kotlin"
LAN_JAVA = "java"

OUT_TYPE_CLIP = "clip"
OUT_TYPE_FILE = "file"

# endregion

class EventData(object):
    def __init__(self, event_name, event_annotation, paramsRaw):
        self._event_name = event_name
        self._event_annotation = event_annotation
        self._params = paramsRaw

    @property
    def name(self):
        return self._event_name

    @property
    def anno(self):
        return self._event_annotation

    @property
    def params(self):
        return self._params


excel_path = ""
language = LAN_KOTLIN
out_type = OUT_TYPE_CLIP
parser = argparse.ArgumentParser(description='用于把excel中的神策埋点数据转化为实际代码的工具')
parser.add_argument('--language', '-l', help='language 属性，可选kotlin、java。非必要参数,默认值kotlin')
parser.add_argument('--path', '-p', help='path 属性，代表输入数据的excel。非必要参数,默认值是当前目录下的xxx')
parser.add_argument('--out_type', '-t', help='out_type 属性，代表输出模式，可选clip（输出到剪切板）或者file（输出到当前目录下的point_out.txt）。非必要参数,'
                                            '默认值是clip')
args = parser.parse_args()


def parseParams(lan, path, type):
    global language
    global excel_path
    global out_type

    language = lan
    if lan != LAN_JAVA:
        language = LAN_KOTLIN

    out_type = type
    if out_type != OUT_TYPE_FILE:
        out_type = OUT_TYPE_CLIP

    excel_path = path
    if pd.isnull(excel_path) or excel_path == "":
        excel_path = os.path.abspath(os.path.dirname(__file__)) + "\\point_input.xlsx"


if __name__ == '__main__':
    try:
        parseParams(args.language, args.path, args.out_type)
    except Exception as e:
        print(e)

print('the language is', language)
print('the path is', excel_path)
print('the out_type is', out_type)

# 驼峰转下划线
def get_lower_case_name(text):
    lst = []
    for index, char in enumerate(text):
        if char.isupper() and index != 0:
            lst.append("_")
        lst.append(char)

    return "".join(lst).lower()


# 处理注释换行
def getAnno(anno):
    if language == LAN_KOTLIN:
        return anno.replace('\n', '\n     * ')
    else:
        return anno.replace('\n', '\n         * ')


def buildOutput(event_data):
    if language == LAN_KOTLIN:
        head_str = HEAD_STR_KOTLIN
        head_anno_str = HEAD_ANNO_STR_KOTLIN
        params_str = PARAMS_STR_KOTLIN
        params_anno_str = ANNO_STR_KOTLIN
        end_str = END_STR_KOTLIN
    else:
        head_str = HEAD_STR_JAVA
        head_anno_str = HEAD_ANNO_STR_JAVA
        params_str = PARAMS_STR_JAVA
        params_anno_str = ANNO_STR_JAVA
        end_str = END_STR_JAVA

    if pd.isnull(event_data.anno):
        head_anno_str = ""
    else:
        head_anno_str = (head_anno_str % getAnno(event_data.anno))

    head = head_str % (event_data.name, event_data.name)
    params = ''
    for p in event_data.params:
        params = params + params_anno_str % getAnno(p[1]) + params_str % (get_lower_case_name(p[0]).upper(), p[0])

    return head_anno_str + head + params + end_str


d = pd.read_excel(excel_path, sheet_name="Sheet2", na_values='blank')
hang = d.shape[0]
lie = d.shape[1]

event_list = []
event_next_start = True
first = True
paramsRaw = []

last_event = 0
last_head = ""
last_head_anno = ""

for i in range(hang):
    head = d.iloc[i, 0]
    head_anno = d.iloc[i, 1]

    event_next_start = not pd.isnull(head) and not first

    if event_next_start:
        last_event = EventData(last_head, last_head_anno, paramsRaw)
        event_list.append(last_event)
        paramsRaw = [[d.iloc[i, 2], d.iloc[i, 3]]]
    else:
        paramsRaw.append([d.iloc[i, 2], d.iloc[i, 3]])

    if not pd.isnull(head):
        last_head = head
        last_head_anno = head_anno

    first = False

last_event = EventData(last_head, last_head_anno, paramsRaw)
event_list.append(last_event)

out = ""
for e in event_list:
    # print("-------------------------------------")
    # print(buildOutput(e))
    # print("-------------------------------------")
    out = out + buildOutput(e) + '\n'

# print(out)
if out_type == OUT_TYPE_CLIP:
    pyperclip.copy(out)
else:
    with open(os.path.abspath(os.path.dirname(__file__)) + "\\point_output.txt", "wb") as f:
        f.write(out.encode())

print("已输出完毕")

class EventParamData(object):
    def __init__(self, param_name="", param_annotation=""):
        self._param_name = param_name
        self._param_annotation = param_annotation
