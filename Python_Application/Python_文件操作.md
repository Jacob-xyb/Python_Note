# 文件读写操作

读写文件最基本的参数:

- filePath : 文件完整路径
- context : 文本内容
- mode : 文件打开模式

| 模式 | 描述                                                         |
| :--- | :----------------------------------------------------------- |
| t    | 文本模式 (默认)。                                            |
| x    | 写模式，新建一个文件，如果该文件已存在则会报错。             |
| b    | 二进制模式。                                                 |
| +    | 打开一个文件进行更新(可读可写)。                             |
| U    | 通用换行模式（不推荐）。                                     |
| r    | 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。 |
| rb   | 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。 |
| r+   | 打开一个文件用于读写。文件指针将会放在文件的开头。           |
| rb+  | 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。 |
| w    | 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| wb   | 以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。 |
| w+   | 打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| wb+  | 以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。 |
| a    | 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| ab   | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| a+   | 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。 |
| ab+  | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。 |

## STL

不采用任何第三方库来读写文件

### 写txt

```python
filePath = "test.txt"
context = "try try try"
mode = 'w'
```

- 最简单的写文件方式

```python
# 一次性写入
f = open(filePath, mode)
f.write(context)
f.close()
```

结果：

```python
try try try
```

---

```python
# 一次性写入多行
f = open(filePath, mode)
for i in range(5):
    f.write(context)
    f.write("\n")
f.close()
```

结果：

```python
try try try
try try try
try try try
try try try
try try try

```

### 读txt

```python
filePath = "test.txt"
```

- 最简单的读文件方式

```python
context = ""
f = open(filePath, 'r')
line = f.readline()
while line:
    context += line
    line = f.readline()
f.close()
```

结果：

```python
try try try
try try try
try try try
try try try
try try try

```

- 第二种，for循环读完

```python
context = ""
f = open(filePath, 'r')
for line in f:
    context += line
f.close()
```

- 第三种，

```python
context = ""
f = open(filePath, 'r')
lines = f.readlines()	# lines 是 list 类型
for line in lines:
    context += line
    f.close()
```

