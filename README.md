# SensorsKeyGen

## 环境准备

#### Pyhton环境
 - excel解析，需要安装pandas库：`pip install pandas`
 - excel解析，需要安装xlrd库：`pip install xlrd`
 - 结果复制到剪切板，需要安装pyperclip库：`pip install pyperclip`
 
 
## 使用方式

### 输入
在在当前目录（脚本所在目录）或者自定义目录下，创建一个xlsx文件，用于存放产品需要的埋点数据。

#### 数据格式
所需要的数据为4列，从第二行开始放：

### 脚本使用

#### 步骤
 - 1.把point.py放到一个地方（如项目根目录）
 - 2.把输入的数据point_input.xlsx放到同一个目录
 - 3.执行'python point.py'
 - 4.脚本会把结果输出到剪切板，直接ctrl+v就可以放到需要的地方了

#### 参数说明
```
optional arguments:
  -h, --help            show this help message and exit
  --language LANGUAGE, -l LANGUAGE
                        language 属性，可选kotlin、java。非必要参数,默认值kotlin
  --path PATH, -p PATH  path 属性，代表输入数据的excel。非必要参数,默认值是当前目录下的xxx
  --out_type OUT_TYPE, -t OUT_TYPE
                        out_type 属性，代表输出模式，可选clip（输出到剪切板）或者file（输出到当前目录下的point_out.txt）。非必要参数,默认值是clip

```

### 例子