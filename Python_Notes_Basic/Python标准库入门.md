# calendar

## 输出文本日历

```python
import calendar
print(calendar.month(2022, 11))

"""
   November 2022
Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
 7  8  9 10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30
"""
```

# datetime

Python处理日期和时间的标准库

## 获取时间

### 获取当天日期

```python
import datetime
print(datetime.datetime.now())  # 2023-01-31 16:29:15.576684
print(datetime.datetime.today())  # 2023-01-31 16:29:15.576684
```

### 单独获取年月日

```python
import datetime
t = datetime.datetime.now()  # t 为 datetime.datetime 对象
print(t)  # 2023-01-31 16:35:12.599288
print(t.year, t.month, t.day, t.hour, t.minute, t.second)  # 2023 1 31 16 35 12
```

## 计算时间

### 计算几天后的时间

```python
import datetime
t1 = datetime.datetime.now()
t2 = t1 + datetime.timedelta(days=7)
print(t1)  # 2023-01-31 17:08:55.330287
print(t2)  # 2023-02-07 17:08:55.330287
```

### 计算时间差

```python
import datetime
t1 = datetime.datetime(2023, 2, 1, 17)
t2 = datetime.datetime(2023, 2, 7, 17)
delta = t2 - t1
print(delta, type(delta))  # 6 days, 0:00:00 <class 'datetime.timedelta'>
print(delta.total_seconds())  # 518400.0
```

# math

## 数学常数

```python
import math

# 自然底数
print(math.e)  # 2.718281828459045
# 圆周率 π
print(math.pi)  # 3.141592653589793
```

## 数学运算

### 取绝对值

```python
import math

# math.fabs() 用于获得绝对值：
print(math.fabs(98.6))  # 98.6
print(math.fabs(-271.1))  # 271.1

# abs() 更为方便
print(abs(-271.1))  # 271.1
```

### 取整

```python
import math

# math.floor() 向下取整， 
print(math.floor(98.6))  # 98
print(math.floor(-271.1))  # -272

# math.ceil() 向上取整
print(math.ceil(98.6))  # 99
print(math.ceil(-271.1))  # -271
```

### math.factorial() 阶乘

```python
print(math.factorial(0))  # 1
print(math.factorial(1))  # 1
print(math.factorial(2))  # 2
print(math.factorial(3))  # 6
print(math.factorial(10))  # 3628800
```

### 底数和指数运算

```python
# log() 计算自然对数（以e为底）：
print(math.log(1.0))  # 0.0
print(math.log(math.e))  # 1.0
# log(a, b) 以 b 为底，a 的对数
print(math.log(8, 2))  # 3.0
# pow() 做的工作与上面正好相反，它用于计算一个数的指数：
print(math.pow(2, 3))  # 8.0
#     python 内置的指数运算符 ** 也可以进行同样的计算，
#     只不过当底数和指数都是整数时，用 ** 计算得到的结果也是整数，不会被自动转化为浮点数
print(2 ** 3)  # 8
print(2.0 ** 3)  # 8.0
```

### math.sqrt() 开平方根

```python
print(math.sqrt(100.0))  # 10.0
```

### 三角函数

```python
# 常见的三角函数都可以使用，例如：sin()、 cos()、 tan()、 asin()、 acos()、 atan()、 atan2()。
# hypot() 函数计算两直角边对应斜边长（勾股定理）
print(math.hypot(3.0, 4.0))  # 5.0
```

### 坐标转换

```python
# 角坐标转换：
print(math.radians(180.0))  # 3.141592653589793
print(math.degrees(math.pi))  # 180.0
```

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
  
-  获取指定路径文件列表

  `os.listdir(path)`

  - path = os.getcwd()；默认为当前文件所在路径

```python
import os
p = os.getcwd()
print(os.listdir(p))
# ['.ipynb_checkpoints', '1.os.ipynb', '2.sys.ipynb', '3.time.ipynb']
```

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

#### 删除空文件夹

`os.rmdir(dir)`

```python
import os
os.rmdir([dir])

# 如果删除的目录不是空的，会报错
OSError: [WinError 145] 目录不是空的。
```

#### 删除非空文件夹

**慎用！！！删除时不会有任何提示**

`shutil.rmtree(dir)`

```python
import shutil
shutil.rmtree([dir])
```

#### 创建目录

`os.makedirs(path, exist_ok=False)`  创建多级目录

注意：如果 path 形如： `D:tmp\\data.txt` 就会创建名为 `data.txt` 的文件夹。

## os.path.

![](https://img-blog.csdnimg.cn/20210406141640898.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1ODAyMDgx,size_16,color_FFFFFF,t_70)

### 查看当前路径所在目录

`os.dirname(path)`

```python
import os
p = os.getcwd()
print(p)					# ..\Python_Note\Python_Notes_Basic\Python标准库入门
print(os.path.dirname(p))	# ..\Python_Note\Python_Notes_Basic
```

### 查看当前路径所在文件(夹)名

`os.path.basename(path)`

```python
import os
p = os.getcwd()
print(p)					# ..\Python_Note\Python_Notes_Basic\Python标准库入门
print(os.path.basename(p))	# Python标准库入门

# 反斜也支持
p = 'xxx/yyy/data.txt'
print(os.path.basename(p))	# data.txt
```

### 路径判断函数

- `os.path.isdir(path)`

  ```python
  import os
  p = os.getcwd()
  l = os.listdir(p)
  print(l)
  for i in l:
      if os.path.isdir(i):
          print(i)
  
  # ['.ipynb_checkpoints', '1.os.ipynb', '2.sys.ipynb', '3.time.ipynb']
  # .ipynb_checkpoints
  ```

# random

## random.random()

返回随机生成的一个实数，它在`[0, 1)`范围内。

```python
import random

for i in range(5):
    print(random.random())
```

```python
0.5405287820078251
0.17121787001100985
0.5918719771646924
0.9789330771107267
0.20310452117281652
```

## random.randint(a, b)

返回随机生成的一个整数，它在`[a, b]`范围内。

```python
import random
for i in range(5):
    print(random.randint(1, 10))
```

## random.seed()

`random.seed(a=无限制, version=2)`

随机种子，固定产生的随机数 

**Docstring：**

The only supported seed types are None, int, float, str, bytes, and bytearray.

注意：a=1 和  a='1' 的随机种子意义是不同的

```python
import random

for i in range(3):
    random.seed(1)
    print(random.random())

for i in range(3):
    random.seed('1')
    print(random.random())
```

```python
0.13436424411240122
0.13436424411240122
0.13436424411240122
0.4782479962566343
0.4782479962566343
0.4782479962566343
```

## random.uniform(a, b)

返回随机生成的一个实数，它在`[a, b]`范围内。

```python
for i in range(5):
    print(random.uniform(1.1, 5.4))  
```

## random.randrange(a, b=None, step=1)

- random.randrange(a, b, step)

  返回随机生成的一个整数，它在`[a, b)`范围内, 间隔为 step。

  ```python
  for i in range(5):
    print(random.randrange(1, 100, 2)) 
  ```
  
- random.randrange(a)

  返回随机生成的一个整数，它在`[0, a)`范围内。

  ```python
  for i in range(5):
      print(random.randrange(20)) 
  ```

## random.choice(seq)

返回非空序列seq中的随机元素

```python
print(random.choice('tomorrow'))
print(random.choice('tomorrow'))
```

## random.sample(*population*, *k*, *, counts=None)

用于无替换的随机抽样。

- 常规用法

  ```python
  print(random.sample('zyxwvutsrqponmlkjihgfedcba',5))
  
  # ['n', 'q', 't', 'g', 'i']
  ```

- counts 参数使用方法

  ```python
  print(random.sample(['red', 'green', 'blue'], 5, counts=[3, 1, 3]))
  print(random.sample(['red', 'green', 'blue'], 5, counts=[3, 1, 3]))
  
  # ['green', 'blue', 'red', 'red', 'red']
  # ['blue', 'red', 'blue', 'red', 'blue']
  ```

*Changed in version 3.9:* Added the *counts* parameter.

*Changed in version 3.11:* The *population* must be a sequence. Automatic conversion of sets to lists is no longer supported.

## random.shuffle(x)

随机打乱自身序列，如果想不改变原序列，请使用 random.sample() 生成新的副本。

```python
sample = list(range(10))
random.shuffle(sample)
print(sample)
# [6, 0, 3, 7, 5, 2, 8, 9, 1, 4]
```

## 应用

### 生成随机字符串

```python
# 从a-zA-Z0-9生成指定数量的随机字符：
import string
import random
ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
print(ran_str)  # TrgJicEe
```

# string

```python
import string
print(string.ascii_letters)
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.ascii_lowercase)
# abcdefghijklmnopqrstuvwxyz
print(string.ascii_uppercase)
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)
# 0123456789
print(string.hexdigits)
# 0123456789abcdefABCDEF
print(string.octdigits)
# 01234567
```


# sys

# time

提供了处理时间和表示之间转换的功能

## 获取时间

### 时间戳(timestamp)

通常来说，时间戳表示的是从**格林威治时间1970年1月1日00:00:00**  (**北京时间1970年01月01日08时00分00秒**)  开始按秒计算的偏移量

`time.time() -> float`

获取当前时间戳，即计算机内部时间值，浮点数, 单位 s

```python
import time
time.time()		# 1655863478.715323
```

### 进程运行时间

`time.perf_counter()`  单位: s

Python3.8 不再支持time.clock

```python
import time
a = time.perf_counter()
time.sleep(3)
b = time.perf_counter()
print(b-a)  # 3.0083799999999883
```

### struct_time 时间元组

struct_time元组共有9个元素，返回struct_time的函数主要有 `gmtime()` ，`localtime()` 

| 索引（Index） | 属性（Attribute）         | 值（Values）       |
| :------------ | :------------------------ | :----------------- |
| 0             | tm_year（年）             | 比如2011           |
| 1             | tm_mon（月）              | 1 - 12             |
| 2             | tm_mday（日）             | 1 - 31             |
| 3             | tm_hour（时）             | 0 - 23             |
| 4             | tm_min（分）              | 0 - 59             |
| 5             | tm_sec（秒）              | 0 - 61             |
| 6             | tm_wday（weekday）        | 0 - 6（0表示周日） |
| 7             | tm_yday（一年中的第几天） | 1 - 366            |
| 8             | tm_isdst（是否是夏令时）  | 默认为-1           |

#### struct_time()

时间的一个类

```python
class struct_time(tuple):
	...
```

可以通过属性直接获取值

```python
import time

struct_time = time.localtime()
print(struct_time)
# time.struct_time(tm_year=2022, tm_mon=7, tm_mday=12, tm_hour=20, tm_min=20, tm_sec=20, tm_wday=1, tm_yday=193, tm_isdst=0)
print(struct_time.tm_year)  # 2022
print(struct_time.tm_hour)  # 20
```

#### localtime()

`time.localtime([secs])`：将一个时间戳转换为当前时区的struct_time。secs参数未提供，则以当前时间为准。

```python
import time 
print(time.localtime(0))
# time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=8, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
```

```python
import time

print(time.localtime())
print(time.localtime(time.time()))

# 输出一致
time.struct_time(tm_year=2022, tm_mon=7, tm_mday=12, tm_hour=19, tm_min=46, tm_sec=25, tm_wday=1, tm_yday=193, tm_isdst=0)
```

#### gmtime()

`time.gmtime([secs])`：和localtime()方法类似，gmtime()方法是将一个时间戳转换为UTC时区（0时区）的struct_time。

#### asctime()

`time.asctime([t])`：把一个表示时间的元组或者struct_time表示为这种形式：**'Tue Jul 12 19:54:06 2022'**。如果没有参数，将会将time.localtime()作为参数传入。

#### ctime()

`time.ctime([secs])`：把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式。如果参数未给或者为None的时候，将会默认time.time()为参数。它的作用相当于time.asctime(time.localtime(secs))。

```python
print(time.ctime())
print(time.ctime(time.time()))

# 输出一致
Tue Jul 12 20:00:16 2022
```

#### strftime()

`time.strftime(format[, t])`：把一个代表时间的元组或者struct_time（如由time.localtime()和time.gmtime()返回）转化为格式化的时间字符串。

**如果t未指定，将传入time.localtime()。**

如果元组中任何一个元素越界，ValueError的错误将会被抛出。

| 格式 | 含义                                                         | 备注 |
| :--- | :----------------------------------------------------------- | :--- |
| %a   | 本地（locale）简化星期名称                                   |      |
| %A   | 本地完整星期名称                                             |      |
| %b   | 本地简化月份名称                                             |      |
| %B   | 本地完整月份名称                                             |      |
| %c   | 本地相应的日期和时间表示                                     |      |
| %d   | 一个月中的第几天（01 - 31）                                  |      |
| %H   | 一天中的第几个小时（24小时制，00 - 23）                      |      |
| %I   | 第几个小时（12小时制，01 - 12）                              |      |
| %j   | 一年中的第几天（001 - 366）                                  |      |
| %m   | 月份（01 - 12）                                              |      |
| %M   | 分钟数（00 - 59）                                            |      |
| %p   | 本地am或者pm的相应符                                         |      |
| %S   | 秒（00 - 61）                                                |      |
| %U   | 一年中的星期数。（00 - 53星期天是一个星期的开始。）第一个星期天之前的所有天数都放在第0周。 |      |
| %w   | 一个星期中的第几天（0 - 6，0是星期天）                       |      |
| %W   | 和%U基本相同，不同的是%W以星期一为一个星期的开始。           |      |
| %x   | 本地相应日期                                                 |      |
| %X   | 本地相应时间                                                 |      |
| %y   | 去掉世纪的年份（00 - 99）                                    |      |
| %Y   | 完整的年份                                                   |      |
| %Z   | 时区的名字（如果不存在为空字符）                             |      |
| %%   | ‘%’字符                                                      |      |

**备注**：

1. “%p”只有与“%I”配合使用才有效果。
2. 文档中强调确实是0 - 61，而不是59，闰年秒占两秒（汗一个）。
3. 当使用strptime()函数时，只有当在这年中的周数和天数被确定的时候%U和%W才会被计算。

```python
import time

print(time.strftime("%Y-%m-%d %X"))
print(time.strftime("%Y-%m-%d %H:%M:%S"))

# 输出一致
2022-07-12 20:09:30
```

#### strptime()

`time.strptime(string[, format])`：把一个格式化时间字符串转化为struct_time。实际上它和strftime()是逆操作。

```python
print(time.strptime("2022-07-12 20:09:30", "%Y-%m-%d %X"))

# time.struct_time(tm_year=2022, tm_mon=7, tm_mday=12, tm_hour=20, tm_min=9, tm_sec=30, tm_wday=1, tm_yday=193, tm_isdst=-1)
```

#### mktime()

`time.mktime(t)`：将一个struct_time转化为时间戳。

```python
time.mktime(time.localtime())  # 1657626741.0
```

## 计算时间间隔

**Python 3.8 已移除 clock() 方法 可以使用 time.perf_counter() 或 time.process_time() 方法替代。**

### time.time()、time.perf_counter() 、time.process_time()

- **time.time()**

返回自纪元以来的秒数作为浮点数，但是时期的具体日期和闰秒的处理取决于使用的平台。比如：在Windows和大多数Unix系统上，纪元是1970年1月1日00:00:00（UTC），并且闰秒不计入自纪元以来的秒数，这也通常被称为Unix时间。我们要可以通过 `time.gmtime(0)` 查看自己平台上的纪元。

```python
print(time.gmtime(0))		
# time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
print(time.asctime(time.gmtime(0)))  # Thu Jan  1 00:00:00 1970
```

通常用time()来做时间的格式输出，也会用在一些测试代码时间上面。在我们测试代码的时候需要调用两次，做差值，`注意它会把sleep()的时间也算进去`。

- **time.perf_counter()**

返回性能计数器的值（以小数秒为单位）作为浮点数，即具有最高可用分辨率的时钟，以测量短持续时间。 它确实包括睡眠期间经过的时间，并且是系统范围的。
通常perf_counter()用在测试代码时间上，具有最高的可用分辨率。不过因为返回值的参考点是以进程开始进行计算，因此我们测试代码的时候需要调用两次，做差值。
`perf_counter()会包含sleep()休眠时间`，适用测量短持续时间

- **time.process_time()**

也是返回进程经过时间，但是 `time.process_time()不包含sleep()休眠时间` 。

```python
import time

def procedure():
    time.sleep(2.5)

# measure wall time
t0 = time.time()
procedure()
print (time.time() - t0, "seconds wall time")
    
# measure perfer time
t0 = time.perf_counter()
procedure()
print (time.perf_counter() - t0, "seconds perfer time")

# measure process time 
t0 = time.process_time()
procedure()
print (time.process_time() - t0, "seconds process time")



"""
2.501197099685669 seconds wall time
2.511219500000001 seconds perfer time
0.0 seconds process time
"""
```

### 纳秒计时

此外Python3.7开始还提供了以上三个方法精确到纳秒的计时。分别是：

`time.time_ns()`、`time.perf_counter_ns()` 、`time.process_time_ns()`

**返回的均是整型。**

```python
import time

def procedure():
    time.sleep(2.5)

# measure wall time
t0 = time.time_ns()
procedure()
print (time.time_ns() - t0, "seconds wall time")
    
# measure perfer time
t0 = time.perf_counter_ns()
procedure()
print (time.perf_counter_ns() - t0, "seconds perfer time")

# measure process time 
t0 = time.process_time_ns()
procedure()
print (time.process_time_ns() - t0, "seconds process time")


"""
2513770100 seconds wall time
2508415400 seconds perfer time
0 seconds process time
"""
```

