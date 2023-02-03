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

流程：

```python
# 1.打开文件
f = open(path, mode)
# 2.读写文件
...
# 3.关闭文件
f.close()

# ========= 或者 =============
with open(path, mode) as :
    # 读写操作 ...
```

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

- 第二种，for循环读完

```python
context = ""
f = open(filePath, 'r')
for line in f:
    context += line
f.close()
```

- 第三种，一次性读完

```python
context = ""
f = open(filePath, 'r')
lines = f.readlines()	# lines 是 list 类型
for line in lines:
    context += line
    f.close()
```

### 读写csv

csv 文件由 `,` 隔开

- 写

```python
with open('data.csv', 'w') as f:
    f.write("Name,Gender,Age\n")
    f.write("Jacob,Male,18\n")
```

![image-20220713111212956](https://s2.loli.net/2022/07/13/uqgQRLxOUWpKiYz.png)

- 读

```python
with open('data.csv', 'r') as f:
    context = f.read()		# 'Name,Gender,Age\nJacob,Male,18\n'
    print(context)
    
"""
Name,Gender,Age
Jacob,Male,18

"""
```

### 文件定位

- **tell()**

  获取当前指针位置。

- **seek()**

  语法：`seek(offset, sign=0)`

  offset: 根据 sign 的不同，表示不同的含义
  
  文档开始的偏移字节数，注意，是字节数，所以除了二进制的场景外，其他常见均不推荐使用。
  
  最常用的是，`seek(0)` 指针移动到起始位置。
  
  - 0: start of stream (the deafult)，因此 offset 只能是非负的
  - 1: current stream position，可正可负，但是只支持二进制模式
  - 2: end of stream，offset只能是非正的，但是只支持二进制模式

### 相关函数详解

#### f.read()

语法：`f.read(字节数)`

- 字节数：默认是文件内容长度

#### f.readline()

语法：`f.readline([limit])`

- limit：限制的最大字节数

**注意：** limit 虽然限制最大字节数，但是转义符是一个整体不可分。即 `'123\n'` 是5个字符，但是limit=4时，会全部输出，偏移5个字节。

#### f.readable()

判断当前文件是否可读

#### f.flush()

立即清空缓冲区的数据内容到磁盘文件。

清空后还可以继续写入：

```python
f.write("123")
f.flush()
f.write("456")
```

# 文件基础操作

## 重命名

1. `os.rename(old, new)`

   Rename a file or directory

   不能重命名路径上的中间节点。

2. `renames(old, new)`

   用法1：和 os.rename() 功能一致

   用法2：如果中间路径不同，则会先删除空目录，然后创建出目标路径。

   ```python
   os.renames('sample1/test_rename1.txt', 'sample/test_rename.txt')
   ```

   如果 sample1 为空，则删除，然后创建 sample，再创建 test_rename.txt。

## 删除目录

1. `os.rmdir(path)`

   删除目录 path，path必须是个空目录，否则抛出OSError异常。

2. `os.removedirs(path)`

   递归地删除目录。要求每一级目录都为空，才能递归删除全部目录。子目录被成功删除，才删除父目录；如果子目录没有成功删除，将抛出OSError异常

   ```python
   import os
   # test2是test的子文件夹，如果test2不为空，则抛出异常；
   # 如果test2为空，test不为空，则test2删除成功，test不删除，但不报异常
   os.removedirs('./test/test2)
   ```

3. `shutil.rmtree(path)`

   不管目录path是否为空，都删除。

## 创建目录

1. `os.mkdir(path[, mode])`

   不能创建多级目录.

   mode: 数字权限，可执行：1，写：2，读：3，三位八进制码分别代表【文件拥有者, 同组用户, 其他用户】

   ​	mode = 0o777 代表三种用户均拥有 可执行读写的权限。

2. `os.makedirs(name, mode=0o777, exist_ok=False)`

   递归创建目录

   exist_ok：False时，如果递归时发现目录存在，则报错；True时，递归时发现目录存在，则正常返回。

## 获取目录

1. `os.getcwd()`

   获取当前目录

2. `os.chdir()`

   改变当前目录

3. `os.listdir()`

   获取目录内容列表

## 文件复制

1. `shutil.copyfile(src, dst)`

   只有当目标是可写的，这个方法才会将源内容复制到目标位置。如果你没有写入权限，则会导致 IOError 异常。

   它会打开输入文件进行读取并忽略其文件类型。接下来，它不会以任何不同的方式处理特殊文件，也不会将它们复制为新的特殊文件。

   Copyfile() 方法使用下面的低级函数 copyfileobj()。

   **以下是关于 copyfile() 方法的要点：**

   - 它将源内容复制到目标文件中。

   - 如果目标文件不可写入，那么复制操作将导致 IOError 异常。

   - 如果源文件和目标文件都相同，它将会返回 SameFileError。

   - 但是，如果目标文件之前有不同的内容，那么该副本将会覆盖其内容。

   - 如果目标是一个目录，这意味着此方法不会复制到目录，那么会发生 Error 13。

   - 它不支持复制诸如字符或块驱动以及管道等文件。

   ```python
   from shutil import copyfile
   from sys import exit
   
   source = input("Enter source file with full path: ")
   target = input("Enter target file with full path: ")
   
   # adding exception handling
   try:
      copyfile(source, target)
   except IOError as e:
      print("Unable to copy file. %s" % e)
      exit(1)
   except:
      print("Unexpected error:", sys.exc_info())
      exit(1)
   ```

2. `shutil.copy(src, [destination_file or dest_dir])`

   opy() 方法的功能类似于 Unix 中的“cp”命令。这意味着如果目标是一个文件夹，那么它将在其中创建一个与源文件具有相同名称（基本名称）的新文件。此外，该方法会在复制源文件的内容后同步目标文件权限到源文件。

   **copy() vs copyfile() :**

   copy() 还可以在复制内容时设置权限位，而 copyfile() 只复制数据。

   如果目标是目录，则 copy() 将复制文件，而 copyfile() 会失败，出现 Error 13。

   有趣的是，copyfile() 方法在实现过程中使用 copyfileobj() 方法，而 copy() 方法则是依次使用 copyfile() 和 copymode() 函数。

   在 Potion-3 可以很明显看出 copyfile() 会比 copy() 快一点，因为后者会有一个附加任务（保留权限）。

   ---

3. `shutil.copyfileobj(fsrc, fdst, length=0)`

   以文件流对象的方式作为传参，length可以指定缓冲的长度。

   ```python
   import shutil
   src = open('sample/test_rename.txt', 'rb')
   target = open('sample/test_rename1.txt', 'wb')
   shutil.copyfileobj(src, target)
   src.close()
   target.close()
   ```

   源码：

   ```python
   def copyfileobj(fsrc, fdst, length=0):
       """copy data from file-like object fsrc to file-like object fdst"""
       if not length:
           length = COPY_BUFSIZE
       # Localize variable access to minimize overhead.
       fsrc_read = fsrc.read
       fdst_write = fdst.write
       while True:
           buf = fsrc_read(length)
           if not buf:
               break
           fdst_write(buf)
   ```

4. `shutil.copy2(src, [destination_file or dest_dir])`

   虽然 copy2() 方法的功能类似于 copy()。但是它可以在复制数据时获取元数据中添加的访问和修改时间。复制相同的文件会导致 SameFileError 异常。

   **copy() vs copy2() :**

   copy() 只能设置权限位，而 copy2() 还可以使用时间戳来更新文件元数据。

   copy() 在函数内部调用 copyfile() 和 copymode(), 而 copy2() 是调用 copystat() 来替换copymode()。

   ---

   查看文件元数据：

   ```python
   from shutil import *
   import os 
   import time
   from os.path import basename
   
   def displayFileStats(filename):
      file_stats = os.stat(basename(filename))
      print('\tMode    :', file_stats.st_mode)
      print('\tCreated :', time.ctime(file_stats.st_ctime))
      print('\tAccessed:', time.ctime(file_stats.st_atime))
      print('\tModified:', time.ctime(file_stats.st_mtime))
   ```

[更多方法](https://www.cnblogs.com/yibeimingyue/p/16676345.html)
