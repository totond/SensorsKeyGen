# SensorsKeyGen

## 背景

项目里面最近很多需求都需要加上神策埋点，神策埋点需要我们根据产品给的表来写出对应的埋点key代码，做多了之后发现，这些代码是：

- 大量重复性的
- 逻辑性比较一致的
- 结构比较简单的

这就想着像之前的批量string工具一样，搞一个一键生成神策代码的工具。


## 环境准备

#### Pyhton环境

 - excel解析，需要安装pandas库：`pip install pandas`
 - excel解析，需要安装xlrd库：`pip install xlrd`
 - 结果复制到剪切板，需要安装pyperclip库：`pip install pyperclip`



## 效果展示

#### 输入

![https://github.com/totond/SensorsKeyGen/blob/master/pic/%E8%BE%93%E5%85%A5%E4%BE%8B%E5%AD%901.png?raw=true]()

#### 执行脚本后，输出

![https://github.com/totond/SensorsKeyGen/blob/master/pic/%E8%BE%93%E5%87%BA%E4%BE%8B%E5%AD%902.png?raw=true]()



#### 输出方式支持

- 支持Java和Kotlin语言
- 输出结果到剪切板or输出到当前目录下的文件




## 使用方式

### 输入

在在当前目录（脚本所在目录）或者自定义目录下，创建一个xlsx文件，用于存放产品需要的埋点数据。

#### 数据格式

需要转化为埋点的数据，从第二行开始放：分为ABCD4列

![https://github.com/totond/SensorsKeyGen/blob/master/pic/%E8%BE%93%E5%85%A5%E4%BE%8B%E5%AD%901.png?raw=true]()

如果有一个埋点事件对应多个属性，请像上面那样合并单元格

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
