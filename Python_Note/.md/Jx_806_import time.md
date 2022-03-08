```python
import time
```

# time()

## 获取时间

### time.time()

获取当前时间戳，即计算机内部时间值，浮点数


```python
time.time()
```




    1646708195.5627232



### time.ctime()

获取当前时间并以易读方式表示，返回字符串


```python
time.ctime()
```




    'Tue Mar  8 10:59:25 2022'



### time.gmtime()

获取当前时间，表示为计算机可处理的时间格式


```python
time.gmtime()
```




    time.struct_time(tm_year=2022, tm_mon=3, tm_mday=8, tm_hour=3, tm_min=11, tm_sec=26, tm_wday=1, tm_yday=67, tm_isdst=0)



## 时间格式化

### time.strftime(tpl,ts)

tpl是格式化模板字符串，用来定义输出效果；ts是计算机内部时间类型变量

![](https://img2020.cnblogs.com/blog/1423899/202004/1423899-20200410135538157-26457670.png)

![](https://img2020.cnblogs.com/blog/1423899/202004/1423899-20200410135555314-1136175802.png)


```python
t = time.gmtime()
time.strftime("%Y-%m-%d  %H:%M:%S", t)
```




    '2022-03-08  03:12:52'



### time.strptime(str,tpl)

str是字符串形式的时间值；tpl是格式化模板字符串，用来定义输入效果


```python
timeStr = '2018-01-26 12:55:20'
time.strptime(timeStr, "%Y-%m-%d  %H:%M:%S")
```




    time.struct_time(tm_year=2018, tm_mon=1, tm_mday=26, tm_hour=12, tm_min=55, tm_sec=20, tm_wday=4, tm_yday=26, tm_isdst=-1)



## 程序计时

### time.perf_counter()

- __Python 3.8 已移除 clock() 方法 可以使用 time.perf_counter() 或 time.process_time() 方法替代。__

---

- 以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。

这个需要注意，在不同的系统上含义不同。在UNIX系统上，它返回的是"进程时间"，它是用秒表示的浮点数（时间戳）。而在WINDOWS中，第一次调用，返回的是进程运行的实际时间。而第二次之后的调用是自第一次调用以后到现在的运行时间。（实际上是以WIN32上QueryPerformanceCounter()为基础，它比毫秒表示更为精确）

在win32系统下，这个函数返回的是真实时间（wall time），而在Unix/Linux下返回的是CPU时间。


```python
import time

def procedure():
    time.sleep(2.5)

# measure perfer time
t0 = time.perf_counter()
procedure()
print (time.perf_counter() - t0, "seconds perfer time")

# measure process time 
t0 = time.process_time()
procedure()
print (time.process_time() - t0, "seconds process time")

# measure wall time
t0 = time.time()
procedure()
print (time.time() - t0, "seconds wall time")
```

    2.5000456000000213 seconds perfer time
    0.0 seconds process time
    2.5125014781951904 seconds wall time
    

### time.sleep()

s拟休眠的时间，单位是秒，可以是浮点数

`time.sleep(3.3) # 程序将等待3.3秒`

## 小案例


```python
from timeit import Timer


def test1():
    l = []
    for i in range(1000):
        l = l + [i]
def test2():
    l = []
    for i in range(1000):
        l.append(i)
def test3():
    l = [i for i in range(1000)]
def test4():
    l = list(range(1000))



# print([i for i in range(100)])
t1 = Timer('test1()', 'from __main__ import test1')
print('concat %f seconds\n' % t1.timeit(1000))
t2 = Timer('test2()', 'from __main__ import test2')
print('append %f seconds\n' % t2.timeit(1000))
t3 = Timer('test3()', 'from __main__ import test3')
print('comprehension %f seconds\n' % t3.timeit(1000))
t4 = Timer('test4()', 'from __main__ import test4')
print('list range %f seconds\n' % t4.timeit(1000))

```

    concat 0.929149 seconds
    
    append 0.054986 seconds
    
    comprehension 0.028441 seconds
    
    list range 0.008794 seconds
    
    
