# os

其实该语句就是在python环境下对文件，文件夹执行操作的一个模块

## os.

### 获取查看操作

- 查看当前系统

```python
import os
print(os.name)  # nt
# Windows NT（New Technology）是微软公司发布的桌面端操作系统，于1993年7月27日发布，该操作系统适用于一部分Windows电脑
```

- 获取当前文件所在路径

  `os.getcwd()`

### 系统文件操作

#### 删除文件

`os.remove(path)`

```python
import os 
os.remove([path])	# 删除指定路径文件

# 1.remove 不能删除文件夹
PermissionError: [WinError 5] 拒绝访问。
# 2.path 不存在时也会报错
FileNotFoundError: [WinError 2] 系统找不到指定的文件。
```

#### 删除空目录

`os.rmdir(dir)`

```python
import os
os.rmdir([dir])

# 如果删除的目录不是空的，会报错
OSError: [WinError 145] 目录不是空的。
```

#### 删除非空目录

**慎用！！！删除时不会有任何提示**

`shutil.rmtree(dir)`

```python
import shutil
shutil.rmtree([dir])
```

## os.path.

![](https://img-blog.csdnimg.cn/20210406141640898.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1ODAyMDgx,size_16,color_FFFFFF,t_70)

# sys

# time

## 获取时间

### 计算机内部时间

`time.time() -> float`

获取当前时间戳，即计算机内部时间值，浮点数, 单位 s

```python
import time
time.time()		# 1655863478.715323
```

### 易读方式获取时间

`time.ctime() -> str`

```python
import time
time.ctime()	# 'Wed Jun 22 10:07:55 2022'
```

### 计算机可处理格式

`time.gmtime() -> object`

```python
import time
print(time.gmtime())	
# time.struct_time(tm_year=2022, tm_mon=6, tm_mday=22, tm_hour=2, tm_min=9, tm_sec=30, tm_wday=2, tm_yday=173, tm_isdst=0)

# 获取相应属性
print(time.gmtime().tm_year)	# 2022
```

## 格式化时间

### time.strftime(tpl,ts)

`time.strftime(tpl,ts) -> str`

tpl是格式化模板字符串，用来定义输出效果；ts是计算机内部时间类型变量

```python
import time

t = time.gmtime()
print(time.strftime("%Y-%m-%d  %H:%M:%S", t))
# 2022-06-22  02:17:38
```



