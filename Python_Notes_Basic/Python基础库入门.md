# Python简介

Python 是一个高层次的结合了解释性、编译性、互动性和面向对象的脚本语言。

Python 的设计具有很强的可读性，相比其他语言经常使用英文关键字，其他语言的一些标点符号，它具有比其他语言更有特色语法结构。

- **Python 是一种解释型语言：** 这意味着开发过程中没有了编译这个环节。类似于PHP和Perl语言。
- **Python 是交互式语言：** 这意味着，您可以在一个 Python 提示符 **>>>** 后直接执行代码。
- **Python 是面向对象语言:** 这意味着Python支持面向对象的风格或代码封装在对象的编程技术。
- **Python 是初学者的语言：**Python 对初级程序员而言，是一种伟大的语言，它支持广泛的应用程序开发，从简单的文字处理到 WWW 浏览器再到游戏。

## Python 发展历史

Python 是由 Guido van Rossum 在八十年代末和九十年代初，在荷兰国家数学和计算机科学研究所设计出来的。

Python 本身也是由诸多其他语言发展而来的,这包括 ABC、Modula-3、C、C++、Algol-68、SmallTalk、Unix shell 和其他的脚本语言等等。

像 Perl 语言一样，Python 源代码同样遵循 GPL(GNU General Public License)协议。

现在 Python 是由一个核心开发团队在维护，Guido van Rossum 仍然占据着至关重要的作用，指导其进展。

Python 2.0 于 2000 年 10 月 16 日发布，增加了实现完整的垃圾回收，并且支持 Unicode。

Python 3.0 于 2008 年 12 月 3 日发布，此版不完全兼容之前的 Python 源代码。不过，很多新特性后来也被移植到旧的Python 2.6/2.7版本。

Python 3.0 版本，常被称为 Python 3000，或简称 Py3k。相对于 Python 的早期版本，这是一个较大的升级。

Python 2.7 被确定为最后一个 Python 2.x 版本，它除了支持 Python 2.x 语法外，还支持部分 Python 3.1 语法。

# 基本数据类型

## 列表和元组

列表和元组，都是一个可以**放置任意数据类型的有序集合**。

列表（list）是动态的，长度大小不固定，可以随意地增加、删减或者改变元素（mutable）;

而元组（tuple）是静态的，长度大小固定，无法增加删减或者改变（immutable）。

- 改变元素

```python
# 列表可以很轻松的更改元素
l = [1, 2, 3, 4]
l[3] = 40
print(l)
# [1, 2, 3, 40]

# 改变元组的元素就会报错
t = (1, 2, 3, 4)
t[3] = 40
print(t)
TypeError: 'tuple' object does not support item assignment
```

- 增加元素

```python
# 如果想对元组做任何改变，就只能重新开辟一片内存空间，创建新的元组
t = (1, 2, 3, 4)
new_t = t + (5,)
print(new_t)
# (1, 2, 3, 4, 5)

# 但是列表就显得很轻松
l = [1, 2, 3, 4]
l.append(5)
print(l)
# [1, 2, 3, 4, 5]
```

### 基本操作

- 首先，和其他语言不同，Python中的列表和元组都支持负数索引，-1表示最后一个元素，-2表示倒数第二个元素，以此类推。

```python
# 初始化操作
l = [1, 2, 3, 4]
t = (1, 2, 3, 4)
# 取索引
print("l[-1]:", l[-1])		# l[-1]: 4
print("t[-1]:", t[-1])		# t[-1]: 4
```

- 除了基本的初始化，索引外，**列表和元组都支持切片操作**：

```python
l = [1, 2, 3, 4]
t = (1, 2, 3, 4)	
print("l[0:2]:", l[0:2])		# l[0:2]: [1, 2]
print("t[0:2]:", t[0:2])		# t[0:2]: (1, 2)
```

- 另外，列表和元组都可以随意嵌套：

```python
l = [[1, 2, 3], [4, 5]]  		# 列表的每一个元素也是一个列表
tup = ((1, 2, 3), (4, 5, 6))  	# 元组的每一个元素也是一元组
```

- 当然，两者也可以通过 list() 和 tuple() 函数相互转换：

```python
l = list((1, 2, 3))
t = tuple([1, 2, 3])
print("l:", l, "\nt:", t)

'''
l: [1, 2, 3] 
t: (1, 2, 3)
'''
```

- 常用的内置函数：

  `count(item)`  表示统计列表 / 元组中 item 出现的次数。

  `index(item)` 表示返回列表 / 元组中 item 第一次出现的索引。

  `list.reverse()` 和 `list.sort()` 分别表示原地倒转列表和排序（注意，元组没有内置的这两个函数)。

  `reversed()` 和 `sorted()` 同样表示对列表 / 元组进行倒转和排序，但是会返回一个倒转后或者排好序的新的列表 / 元组，注意：reversed()返回的是一个迭代器对象。

````python
l = [3, 2, 3, 7, 8, 1]
print("l.count(3):", l.count(3))
print("l.index(7):", l.index(7))
l.reverse()
print("l.reverse():", l)
l.sort()
print("l.sort():", l)
print("reversed(l): ", reversed(l))

```
l.count(3): 2
l.index(7): 3
l.reverse(): [1, 8, 7, 3, 2, 3]
l.sort(): [1, 2, 3, 3, 7, 8]
reversed(l): <list_reverseiterator object at 0x000001F80DA55160>
```
````

````python
tup = (3, 2, 3, 7, 8, 1)
print("tup.count(3):", tup.count(3))
print("tup.index(7):", tup.index(7))
print("list(reversed(tup)):", list(reversed(tup)))
print("sorted(tup):", sorted(tup))

```
tup.count(3): 2
tup.index(7): 3
list(reversed(tup)): [1, 8, 7, 3, 2, 3]
sorted(tup): [1, 2, 3, 3, 7, 8]
```
````

### 列表和元组存储方式的差异

列表和元组最重要的区别就是，列表是动态的、可变的，而元组是静态的、不可变的。这样的差异，势必会影响两者存储方式。

```python
l = [1, 2, 3]
print("l.__sizeof__():", l.__sizeof__())		# 64
tup = (1, 2, 3)
print("tup.__sizeof__():", tup.__sizeof__())	# 48
```

对列表和元组，我们放置了相同的元素，但是元组的存储空间，却比列表要少16 字节。这是为什么呢？

事实上，由于列表是动态的，所以它需要存储指针，来指向对应的元素（上述例子中，对于int 型，8 字节）。另外，由于列表可变，所以需要额外存储已经分配的长度大小（8 字节），这样才可以实时追踪列表空间的使用情况，当空间不足时，及时分配额外空间。

- 列表分析

```python
l1 = []
print("l1 = []:", l1.__sizeof__())
l1.append(1)
print("l1 = [1]:", l1.__sizeof__())  # 72；入了元素 1 之后，列表为其分配了可以存储 4 个元素的空间 (72 - 40)/8 = 4
l1.append(2)
print("l1 = [1, 2]:", l1.__sizeof__())  # 72；由于之前分配了空间，所以加入元素 2，列表空间不变
l1.append(3)
l1.append(4)
print("l1 = [1, 2, 3, 4]:", l1.__sizeof__())  # 72；同上
l1.append(5)
print("l1 = [1, 2, 3, 4, 5]:", l1.__sizeof__())  # 104；因为空间已经超过4个，所以列表又分配了 4 个元素的空间

'''
l1 = []: 40
l1 = [1]: 72
l1 = [1, 2]: 72
l1 = [1, 2, 3, 4]: 72
l1 = [1, 2, 3, 4， 5]: 104
'''
```

​		再次验证

```python
l2 = [1]
print("l2 = [1]:", l2.__sizeof__())  # 48；空列表占据40字节，一个元素占据8个字节，一共40+8=48个字节。
l2.append(2)
print("l2 = [1, 2]:", l2.__sizeof__())  # 80；依旧是在原列表的基础上，分配了可以存储4个元素的空间

'''
l2 = [1]: 48
l2 = [1, 2]: 80
'''
```

- 元组分析

```python
# 元组的空间分配就很线性
t1 = ()
print("t1 = ():", t1.__sizeof__())
t1 = (1,)
print("t1 = (1,):", t1.__sizeof__())
t1 = (1, 2)
print("t1 = (1, 2):", t1.__sizeof__())
t1 = (1, 2, 3)
print("t1 = (1, 2, 3):", t1.__sizeof__())
t1 = (1, 2, 3, 4)
print("t1 = (1, 2, 3, 4):", t1.__sizeof__())
t1 = (1, 2, 3, 4, 5)
print("t1 = (1, 2, 3, 4, 5):", t1.__sizeof__())

'''
t1 = (): 24
t1 = (1): 32
t1 = (1, 2): 40
t1 = (1, 2, 3): 48
t1 = (1, 2, 3, 4): 56
t1 = (1, 2, 3, 4, 5): 64
'''
```

上面的例子，大概描述了列表空间分配的过程。我们可以看到，为了减小每次增加 / 删减操作时空间分配的开销，Python 每次分配空间时都会额外多分配一些，这样的机制（over-allocating）保证了其操作的高效性：增加 / 删除的时间复杂度均为 O(1)。

但是对于元组，情况就不同了。元组长度大小固定，元素不可变，所以存储空间固定。

看了前面的分析，你也许会觉得，这样的差异可以忽略不计。但是想象一下，如果列表和元组存储元素的个数是一亿，十亿甚至更大数量级时，你还能忽略这样的差异吗？

### 列表和元组的性能

通过学习列表和元组存储方式的差异，我们可以得出结论：元组要比列表更加轻量级一些，所以总体上来说，元组的性能速度要略优于列表。

另外，Python 会在后台，对静态数据做一些`资源缓存（resource caching）`。

通常来说，因为垃圾回收机制的存在，如果一些变量不被使用了，Python 就会回收它们所占用的内存，返还给操作系统，以便其他变量或其他应用使用。

但是对于一些静态变量，比如元组，如果它不被使用并且占用空间不大时，Python 会暂时缓存这部分内存。这样，下次我们再创建同样大小的元组时，Python 就可以不用再向操作系统发出请求，去寻找内存，而是可以直接分配之前缓存的内存空间，这样就能大大加快程序的运行速度。

下面的例子，是计算初始化一个相同元素的列表和元组分别所需的时间。我们可以看到，元组的初始化速度，要比列表快接近 5 倍。

```python
timeit x=(1,2,3,4,5,6)
# 11.2 ns ± 0.0243 ns per loop (mean ± std. dev. of 7 runs, 100,000,000 loops each)
timeit x=[1,2,3,4,5,6]
# 51.9 ns ± 0.191 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)
```

### 总结

- 总的来说，列表和元组都是有序的，可以存储任意数据类型的集合，区别主要在于下面这两点。
- 列表是动态的，长度可变，可以随意的增加、删减或改变元素。列表的存储空间略大于元组，性能略逊于元组。
- 元组是静态的，长度大小固定，不可以对元素进行增加、删减或者改变操作。元组相对于列表更加轻量级，性能稍优。

### List 函数一览

#### del: 删除元素

```python
l = [0, 1, 2, 3, 4]
del l[2]
print(l)
# [0, 1, 3, 4]

l = [0, 1, 2, 3, 4]
del l[:]
print(l)
# []
```

报错：

```python
# 注意：del 整个对象后，对象就不存在了
l = [0, 1, 2, 3, 4]
del l
print(l)
# NameError: name 'l' is not defined
```



#### len(l): 返回列表长度

```python
l = [0, 1, 2, 3, 4]
print(len(l))		# 5
```

#### +: 拼接列表

```python
# 同级列表拼接
l1 = [0, 1, 2]
l2 = [3, 4, 5]
l1 + l2
# [0, 1, 2, 3, 4, 5]

# 不同级别拼接
l1 = [[0, 1, 2]]
l2 = [3, 4, 5]
l1 + l2
# [[0, 1, 2], 3, 4, 5]
l2 + l1
# [3, 4, 5, [0, 1, 2]]
```

原理：

```python
# 存在两个列表 l1, l2
l1 + l2
# 等价于
t = l1.copy()
for i in l2:
    t.append(i)
return t
```

再返回去看一遍不同级别拼接就很好理解了

#### [] * n: 重复

```python
l = [0] * 5
l
# [0, 0, 0, 0, 0]

# Tips: 空列表即为空，无法重复，也不会报错
l = [] * 10
l
# []
```

#### element in l: 判断元素是否存在

```python
l = [1, 2, 3]
1 in l		# True
```

#### for: 迭代

列表的迭代方式单一，比较简单

```python
for x in [1, 2, 3]: print(x, end=" ")
# 1 2 3
```

#### max(list) & min(list)

返回最大最小值

#### list.append(obj)

在列表末尾添加新的对象

```python
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
l1.append(l2)
print(l1)	# [1, 2, 3, 4, [5, 6, 7, 8]]
# list.append() 方法是将参数一整个作为对象，放入列表中

# 注意！！！压入列表等容器时，是压入的对象地址，浅拷贝，只传入了对象的首地址，并没有拷贝对象本身
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
l1.append(l2)
print(l1)		# [1, 2, 3, 4, [5, 6, 7, 8]]
l2[0] = 0
print(l1)		# [1, 2, 3, 4, [0, 6, 7, 8]]

# 简单的深拷贝的方式
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
l1.append(l2[:])
print(l1)		# [1, 2, 3, 4, [5, 6, 7, 8]]
l2[0] = 0
print(l1)		# [1, 2, 3, 4, [5, 6, 7, 8]]
```

#### list.extend(seq)

在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）

```python
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
l1.extend(l2)
print(l1)		# [1, 2, 3, 4, 5, 6, 7, 8]

# extend()原理和+是相同的，需要注意，扩展的是容器时需要深拷贝一下
l1 = [1, 2, 3, 4]
l2 = [[5, 6, 7, 8]]
l1.extend(l2)
print(l1)		# [1, 2, 3, 4, [5, 6, 7, 8]]
l2[0][0] = 0
print(l1)		# [1, 2, 3, 4, [0, 6, 7, 8]]
```

#### list.count(obj)

统计某个元素在列表中出现的次数

```python
l = [1, 2, 3, 3, 3, 4]
l.count(3)		# 3
```

#### list.index(obj)

语法： `list.index(x[, start[, end]])`

参数：

- x-- 查找的对象。
- start-- 可选，查找的起始位置。
- end-- 可选，查找的结束位置。

返回：

该方法返回查找对象的索引位置，如果没有找到对象则抛出异常。

```python
l = [3, 2, 1, 3, 4]
l.index(3)			# 0
l.index(3, 1)		# 3
l.index(3, 1, 4)	# 3
# Tips:如果在范围内没有找到对象，就会抛出异常
```

#### list.insert(index, obj)

insert() 函数用于将指定对象插入列表的指定位置。

语法：`list.insert(index, obj)`

```python
# list.insert()
l = [0, 1, 2, 3]
l.insert(0, 9)
l
# [9, 0, 1, 2, 3]

# 如果 index 超出了 list 范围，也不会报错，而是插入末尾
#   或许这是为了兼容 append() ?
l = [0, 1, 2, 3]
l.insert(10, 9)
l
# [0, 1, 2, 3, 9]

# 支持负数索引
l = [0, 1, 2, 3]
l.insert(-1, 9)
l
# [0, 1, 2, 9, 3]
```

#### list.pop([index=-1])

pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。

语法：`list.pop([index=-1])`

参数：

- index -- 可选参数，要移除列表元素的索引值，不能超过列表总长度，默认为 index=-1，删除最后一个列表值。

返回：

该方法返回从列表中移除的元素对象。

```python
l = [0, 1, 2, 3]
print(l.pop())		# 3
print(l)			# [0, 1, 2]
```

当然也可以指定 index 删除特定的元素

```python
l = [0, 1, 2, 3]
print(l.pop(2))		# 2
print(l)			# [0, 1, 3]
```

报错：

```python
# list.pop()
l = [0, 1, 2, 3]
print(l.pop(5))
# IndexError: pop index out of range
```

#### list.remove(obj)

remove() 函数用于**移除列表中某个值的第一个匹配项**。

语法：`list.remove(obj)`

返回：无返回值。

```python
l = [0, 1, 2, 3, 0]
l.remove(0)
l		# [1, 2, 3, 0]
```

报错：

```python
# 1.if obj not in list
l = [0, 1, 2, 3, 0]
l.remove(4)
# ValueError: list.remove(x): x not in list
```

#### list.reverse()

reverse() 函数用于反向列表中元素。

```python
l = [0, 3, 5, 1]
l.reverse()
l		# [1, 5, 3, 0]
```

#### list.sort()

sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。

语法：`list.sort( key=None, reverse=False)`

参数：

- key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
- reverse -- 排序规则，**reverse = True** 降序， **reverse = False** 升序（默认）。

最基本用法：

```python
l = [0, 3, 5, 1]
l.sort()
l		# [0, 1, 3, 5]
l.sort(reverse=True)
l		# [5, 3, 1, 0]
```

进阶用法：

1. 层叠列表

```python
# key 可以选择固定位置
l = [(1, 3), (4, 7), (0, 4), (2, 9)]
l.sort(key=lambda x : x[1])
print(l)	# [(1, 3), (0, 4), (4, 7), (2, 9)]
l.sort(key=lambda x : x[1], reverse=True)
print(l)	# [(2, 9), (4, 7), (0, 4), (1, 3)]
l.sort(key=lambda x : x[0])
print(l)	# [(0, 4), (1, 3), (2, 9), (4, 7)]
```

2. 字典

   字典用起来就稍显复杂，比字典更复杂的类型以此类推

```python
l = [{1: 3}, {4: 7}, {0: 4}, {2: 9}]
l.sort(key=lambda x : list(x.keys())[0])
print(l)	# [{0: 4}, {1: 3}, {2: 9}, {4: 7}]
```

#### list.clear()

clear() 函数用于清空列表，类似于 `del a[:]` 。

```python
l = [0, 1, 2, 3]
l.clear()
l	# []
```

#### list.copy()

copy() 函数用于复制列表，类似于 **a[:]**。

理解深浅拷贝就很容易掌握

```python
l = [0, 1, 2, 3]
l1 = l			# 浅拷贝
l1[0] = -1
print(l)		# [-1, 1, 2, 3]

l = [0, 1, 2, 3]
l2 = l[:]		# 深拷贝
l2[0] = -1
print(l)		# [0, 1, 2, 3]

l = [0, 1, 2, 3]
l3 = l.copy()	# 深拷贝
l3[0] = -1
print(l)  		# [0, 1, 2, 3]
```

### Tuple 函数一览

元组的函数 几乎被 列表给覆盖，唯一区别就是使元组发生改变的函数元组没有。

#### 初始化

元组中只包含一个元素时，需要在元素后面添加逗号 `,` ，否则括号会被当作运算符使用：

```python
t = ()
print(type(t))		# <class 'tuple'>
t = (1)
print(type(t))		# <class 'int'>
t = (1,)
print(type(t))		# <class 'tuple'>

# 当然不需要括号也是可以的
t = 1, 2, 3, 4, 5
print(type(t))		# <class 'tuple'>
```

#### +: 拼接元组

元组中的元素值是不允许修改的，但我们可以对元组进行连接组合。

```python
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
tup3 = tup1 + tup2
print (tup3)		# (12, 34.56, 'abc', 'xyz')
```

## 字典和集合

### 基础

究竟什么是字典，什么是集合呢？

字典是一系列由键（key）和值（value）配对组成的元素的集合，在 Python3.7+，字典被确定为有序（注意：在 3.6 中，字典有序是一个implementation detail，在 3.7 才正式成为语言特性，因此 3.6 中无法 100% 确保其有序性），而 3.6 之前是无序的，其长度大小可变，元素可以任意地删减和改变。

相比于列表和元组，字典的性能更优，特别是对于查找、添加和删除操作，字典都能在常数时间复杂度内完成。

而集合和字典基本相同，唯一的区别，就是集合没有键和值的配对，是一系列无序的、唯一的元素组合。

####  初始化

首先我们来看字典和集合的创建，通常有下面这几种方式：

字典：

```python
1 = {'name': 'jason', 'age': 20, 'gender': 'male'}
d2 = dict({'name': 'jason', 'age': 20, 'gender': 'male'})
d3 = dict([('name', 'jason'), ('age', 20), ('gender', 'male')])
d4 = dict(name='jason', age=20, gender='male')
d1 == d2 == d3 ==d4		# True
```

集合：

```python
s1 = {1, 2, 3}
s2 = set([1, 2, 3])
s1 == s2							# True
```

#### 判断是否存在

- 字典

    in 对于 dict 而言，只能判断 key 是否存在，不能判断 value 是否存在。

```python
d = {'name': 'jason', 'age': 20}
print("name" in d)		# True
print("jason" in d)		# False
```

- 集合

    集合的判断就相对简单。

```python
s = {1, 2, 3}
print(1 in s)		# True
print(10 in s)		# False
```

### 增删查改

#### 查

- 字典

    1. 直接用 [] 操作符查询：

    注意查询不存在的键值时会抛出异常。

    ```python
    d = {'name': 'jacob', 'age': 20}
    print(d["name"])		# jacob
    print(d["location"])		# KeyError: 'location'
    ```

    2. 采用 get(key, default)  函数查询：

        如果键不存在，调用 get() 函数可以返回一个默认值。

    ```python
    d = {'name': 'jacob', 'age': 20}
    print(d.get("name"))				# jacob
    print(d.get("location"))			# None
    print(d.get("location", "null"))	# null
    ```

- 集合

    集合并不支持索引，因为集合本质上是一个哈希表。

    对集合采用索引，会抛出异常。

	```python
	s = {1, 2, 3}
	s[0]
	# TypeError: 'set' object is not subscriptable
	```

