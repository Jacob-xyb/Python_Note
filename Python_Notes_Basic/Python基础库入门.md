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

进阶理解深浅拷贝

```python
l = ['0', [0, 1, 2, 3], ['x', 'y', 'z']]

# python 所有容器基本遵循一下规则
l1 = l    		# 浅拷贝：引用对象，会随原对象改变而改变
l2 = l[:]		# 浅拷贝： 深拷贝父对象（一级目录），子对象（二级目录）不拷贝，子对象是引用
l3 = l.copy()  	# 浅拷贝： 深拷贝父对象（一级目录），子对象（二级目录）不拷贝，子对象是引用
# 深拷贝需要引入 copy 模块
import copy
l4 = copy.deepcopy(l)

l[0] = '1'
l[1].remove(0)

print(l1)		# ['1', [1, 2, 3], ['x', 'y', 'z']]
print(l2)		# ['0', [1, 2, 3], ['x', 'y', 'z']]
print(l3)		# ['0', [1, 2, 3], ['x', 'y', 'z']]
print(l4)		# ['0', [0, 1, 2, 3], ['x', 'y', 'z']]
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

- **字典：**

字典是另一种可变容器模型，且可存储任意类型对象。

字典的每个键值 **key=>value** 对用冒号 **:** 分割，每个对之间用逗号(**,**)分割，整个字典包括在花括号 **{}** 中 ,格式如下所示：

`d = {key1 : value1, key2 : value2, key3 : value3 }`

**注意：** **dict** 作为 Python 的关键字和内置函数，变量名不建议命名为 **dict**。

```python
1 = {'name': 'jason', 'age': 20, 'gender': 'male'}
d2 = dict({'name': 'jason', 'age': 20, 'gender': 'male'})
d3 = dict([('name', 'jason'), ('age', 20), ('gender', 'male')])
d4 = dict(name='jason', age=20, gender='male')
d1 == d2 == d3 ==d4		# True
```

> 字典初始化进阶技巧：

1. 两个列表键对配合组成 dict

```python
l1 = ['1', '2', '3']
l2 = ['a', 'b', 'c']
d = dict(zip(l1, l2))	#  {'1': 'a', '2': 'b', '3': 'c'}
```

- **集合：**

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

#### 增和改

字典的增和改是相同的操作

```python
d = {'name': 'jacob', 'age': 20}
d["gender"] = "male"
print(d)		# {'name': 'jacob', 'age': 20, 'gender': 'male'}
d["age"] = 18
print(d)		# {'name': 'jacob', 'age': 18, 'gender': 'male'}
```

集合只能增加和删除，没法直接改元素

```python
s = {1, 2, 3, 4, 5}
s.add(6)
print(s)		# {1, 2, 3, 4, 5, 6}
# 集合是不重合的元素，因此 add 重复的元素不会报错，但是无效的
s.add(6)
print(s)		# {1, 2, 3, 4, 5, 6}

# 还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等:
s.update({1,7})
print(s)		# {1, 2, 3, 4, 5, 6, 7}
s.update([1,8], [1,4])
print(s)		# {1, 2, 3, 4, 5, 6, 7, 8}
# 字典比较特殊，只会更新字典的key值
s.update({0: 9})
print(s)		# {0, 1, 2, 3, 4, 5, 6, 7, 8}
```

#### 删

- 字典

`d.pop()` 和 `del d[]`

删除前需要确认key是否存在

```python
d = {'name': 'jacob', 'age': 20, 'gender': 'male'}
print(d.pop("gender"))	# male
print(d)				# {'name': 'jacob', 'age': 18}
del d["age"]
print(d)				# {'name': 'jacob'}

del d["a"]		# KeyError: 'a'

d.clear()		# 清空
print(d)				# {}
```

- 集合

`s.remove()` 和 `s.pop()`

```python
s = {1, 2, 3, 4, 5, 6}
s.remove(6)
print(s)		# {1, 2, 3, 4, 5}

# error
s.remove(7)		# KeyError: 7

s.clear()		# 清空
print(s)		# set()

# 不过要注意，集合的 pop() 操作是删除集合中最后一个元素，可是集合本身是无序的，你无法知道会删除哪个元素，因此这个操作得谨慎使用
s = {1, 4, 5, 2}
s.pop()		# 1
s = {4, 1, 2, 3}
s.pop()		# 1
```

还有个很安全的删除方法：`s.discard()`

如果元素不存在，不会发生错误。

```python
s = {1, 2, 3, 4, 5, 6}
s.discard(7)
```

### Dict 函数一览

#### len(dict)、str(dict)、type(variable)

```python
d =  {'Name': 'Jacob', 'Age': 18, 'Class': 'First'}

# len(dict) 计算字典元素个数，即键的总数。
print(len(d))		# 3

# str(dict) 字符串化字典
print(str(d))		# "{'Name': 'Jacob', 'Age': 18, 'Class': 'First'}"

# type(dict) 输出类型
print(type(d))		# <class 'dict'>
```

#### dict.items()

**Python 字典 items() 方法以列表返回视图对象，是一个可遍历的key/value 对。**

dict.keys()、dict.values() 和 dict.items() 返回的都是视图对象（ view objects），提供了字典实体的动态视图，这就意味着字典改变，视图也会跟着改变。

视图对象不是列表，不支持索引，可以使用 list() 来转换为列表。

我们不能对视图对象进行任何的修改，因为字典的视图对象都是只读的。

语法：`dict.items()`

```python
d = {'Name': 'Jacob', 'Age': 18}
print(d.items())		# dict_items([('Name', 'Jacob'), ('Age', 18)])
for i,j in d.items():
    print(i, "\t:", j)
'''
Name 	: Jacob
Age 	: 18
'''
```

#### dict.keys() & dict.values()

```python
d = {'user': 'jacob', 'num': [1, 2, 3]}
print(d.keys())  # dict_keys(['user', 'num'])
keys = d.keys()
print(d.values())  # dict_values(['jacob', [1, 2, 3]])
values = d.values()
for i, j in zip(keys, values):
    print(i, j)
'''
user jacob
num [1, 2, 3]
'''
```

#### dict.copy()

Python 字典 copy() 函数返回一个字典的浅复制。

```python
d =  {'user':'jacob','num':[1,2,3]}
 
d1 = d          # 浅拷贝: 引用对象
d2 = d.copy()   # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，子对象是引用
import copy
d3 = copy.deepcopy(d)  # 深拷贝
 
# 修改 data 数据
d['user']='root'
d['num'].remove(1)
 
# 输出结果
print(d)		# {'user': 'root', 'num': [2, 3]}
print(d1)		# {'user': 'root', 'num': [2, 3]}
print(d2)		# {'user': 'jacob', 'num': [2, 3]}
print(d3)		# {'user': 'jacob', 'num': [1, 2, 3]}
```

#### dict.setdefault()

语法：`dict.setdefault(key, default=None)`

参数：

- key -- 查找的键值。
- default -- 键不存在时，设置的默认键值。

返回：如果 key 在 字典中，返回对应的值。如果不在字典中，则插入 key 及设置的默认值 default，并返回 default ，default 默认值为 None。

```python
tinydict = {'Name': 'Runoob', 'Age': 7}
 
print ("Age 键的值为 : %s" %  tinydict.setdefault('Age', None))
print ("Sex 键的值为 : %s" %  tinydict.setdefault('Sex', None))
print ("新字典为：", tinydict)

'''
Age 键的值为 : 7
Sex 键的值为 : None
新字典为： {'Age': 7, 'Name': 'Runoob', 'Sex': None}
'''
```

**关于字典中 get() 和 setdefault() 的区别：**

主要在于当查找的键值 key 不存在的时候，setdefault()函数会返回默认值并更新字典，添加键值；

而 get() 函数只返回默认值，并不改变原字典。

#### dict.update()

语法：`dict.update(dict2)`

无返回值。

如果键值有重复，则 dict2 的内容更新替换到 dict 中。

```python
d1 = {'user': 'jacob', 'num': [1, 2, 3]}
d2 = {'sex': 'female'}
d1.update(d2)
print(d1)
# {'user': 'jacob', 'num': [1, 2, 3], 'sex': 'female'}
d3 = {'user': 'xyb', 'num': [6, 6, 6]}
d1.update(d3)
print(d1)
# {'user': 'xyb', 'num': [6, 6, 6], 'sex': 'female'}
```

#### pop()

语法：`pop(key[,default])`

参数：

- **key** - 要删除的键
- **default** - 当键 key 不存在时返回的值

返回：

返回被删除的值：

- 如果 `key` 存在 - 删除字典中对应的元素
- 如果 `key` 不存在 - 返回设置指定的默认值 default
- 如果 `key` 不存在且默认值 default 没有指定 - 触发 `KeyError` 异常

```python
site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}

element = site.pop('name')

print('删除的元素为:', element)
print('字典为:', site)

'''
删除的元素为: 不存在的 key
字典为: {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
'''
```

#### popitem()

Python 字典 popitem() 方法随机返回并删除字典中的最后一对键和值。

如果字典已经为空，却调用了此方法，就报出 KeyError 异常。

语法：`popitem()`

返回：

返回最后插入键值对(key, value 形式)，按照 LIFO（Last In First Out 后进先出法） 顺序规则，即最末尾的键值对。

**注意：**在 Python3.7 之前，popitem() 方法删除并返回任意插入字典的键值对。

```python
site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}

# ('url': 'www.runoob.com') 最后插入会被删除
result = site.popitem()

print('返回值 = ', result)
# 返回值 =  ('url', 'www.runoob.com')
print('site = ', site)
# site =  {'name': '菜鸟教程', 'alexa': 10000}

# 插入新元素
site['nickname'] = 'Runoob'
print('site = ', site)
# site =  {'name': '菜鸟教程', 'alexa': 10000, 'nickname': 'Runoob'}

# 现在 ('nickname', 'Runoob') 是最后插入的元素
result = site.popitem()

print('返回值 = ', result)
# 返回值 =  ('nickname', 'Runoob')
print('site = ', site)
# site =  {'name': '菜鸟教程', 'alexa': 10000}
```

### Set 函数一览

#### 集合推导式

Set comprehension

```python
s1 = {x for x in 'abracadabra' if x not in 'abc'}
s1	# {'r', 'd'}
```

#### 集合运算

```python
a = set('abracadabra')
b = set('alacazam')
# 集合是无序的
print(a)	# {'b', 'c', 'd', 'a', 'r'}
print(b)	# {'m', 'c', 'z', 'l', 'a'}

# a有 b没有
print(a - b)	# {'b', 'd', 'r'}
# a 或 b 有
print(a | b)	# {'l', 'm', 'b', 'c', 'z', 'd', 'a', 'r'}
# a 和 b 都有
print(a & b)	# {'c', 'a'}
# a b 不同时有
print(a ^ b)	# {'b', 'm', 'z', 'l', 'd', 'r'}
```

#### len(set)

返回集合长度

#### set.difference()、set.difference_update()

difference() 方法用于返回集合的差集，即返回的集合元素包含在第一个集合中，但不包含在第二个集合(方法的参数)中。

语法：`set.difference(set2)`

```python
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)	 
print(z)		# {'cherry', 'banana'}

# 其实就是：a有 b没有
print(x - y)	# {'cherry', 'banana'}
```

### 补充

#### 字典键的特性

字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。

两个重要的点需要记住：

1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：

```python
d = {"name": "jx", "age": 18, "name": "jacob"}
print(d)
# {'name': 'jacob', 'age': 18}
```

2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，如下实例：

```python
d = {[0]: "xxx"}
# TypeError: unhashable type: 'list'

# 元组都是可以的
d = {(0,): "xxx"}
print(d)
# {(0,): 'xxx'}
```

#### 字典的排序

- **按key排序，取value**

```python
d = {'2': 'FmThic:@2', '1': 'layer_1_thickness(A)'}
print(sorted(d.items()))		# [('1', 'layer_1_thickness(A)'), ('2', 'FmThic:@2')]
# 如果只想取value
print(list(zip(*sorted(d.items()))))	# [('1', '2'), ('layer_1_thickness(A)', 'FmThic:@2')]
```

#### 字典和集合的工作原理

不同于其他数据结构，字典和集合的内部结构都是一张哈希表。

- 对于字典而言，这张表存储了哈希值（hash）、键和值这 3 个元素。

- 而对集合来说，区别就是哈希表内没有键和值的配对，只有单一的元素了。

- 具体原理后期再补 # TODO

## 字符串

字符串是 Python 中最常用的数据类型。我们可以使用引号( **'** 或 **"** )来创建字符串。

创建字符串很简单，只要为变量分配一个值即可。

```python
var1 = 'Hello World!'
var2 = "Jacob-xyb"
```

**Python 不支持单字符类型，单字符在 Python 中也是作为一个字符串使用。**

### 基础

#### 初始化

以下多种方式创建字符串都是一致的：

```python
s1 = 'hello'
s2 = "hello"
s3 = '''hello'''
s4 = """hello"""
s1 == s2 == s3 == s4		# True
```

Python 同时支持这三种表达方式，很重要的一个原因就是，这样方便你在字符串中，内嵌带引号的字符串。比如：`"I'm a student"`

三引号字符串主要常用于函数注释等等。

同时，Python 也支持转义字符。所谓的转义字符，就是用反斜杠开头的字符串，来表示一些特定意义的字符。我把常见的的转义字符，总结成了下面这张表格。

![image-20211020145458829](https://i.loli.net/2021/10/20/YJu1Fs9odDC2yzq.png)

### 增删查改

#### 查

Python 访问子字符串，可以使用方括号 **[]** 来截取字符串，字符串的截取的语法格式如下：

`变量[头下标:尾下标]`

```python
var1 = 'Hello World!'
print(var1[0:5])	# Hello
print(var1[0])		# H
print(var1[-6:])	# World!
```

#### 增

```python
var1 = 'Hello World!'
print ("已更新字符串 : ", var1[:6] + 'Jaocb!')	# Hello Jacob!
```

#### 删 & 改

```python
var1 = 'Hello World!'
var1 = var1[:-1]	# del var[-1]
print(var1)			# Hello World

var1 = var1.replace('H', 'h')
print(var1)			# hello World
```

**特别要注意，Python 的字符串是不可变的（immutable）。因此，用下面的操作，来改变一个字符串内部的字符是错误的，不允许的。**

```python
s = 'hello'
s[0] = 'H'
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

### 字符串运算符

| 操作符 | 描述                                                         | 实例                            |
| :----: | :----------------------------------------------------------- | :------------------------------ |
|   +    | 字符串连接                                                   | a + b 输出结果： HelloPython    |
|   *    | 重复输出字符串                                               | a*2 输出结果：HelloHello        |
|   []   | 通过索引获取字符串中字符                                     | a[1] 输出结果 **e**             |
| [ : ]  | 截取字符串中的一部分，遵循**左闭右开**原则，str[0:2] 是不包含第 3 个字符的。 | a[1:4] 输出结果 **ell**         |
|   in   | 成员运算符 - 如果字符串中包含给定的字符返回 True             | **'H' in a** 输出结果 True      |
| not in | 成员运算符 - 如果字符串中不包含给定的字符返回 True           | **'M' not in a** 输出结果 True  |
|  r/R   | 原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母 **r**（可以大小写）以外，与普通字符串有着几乎完全相同的语法。 | `print( r'\n' ) print( R'\n' )` |
|   %    | 格式字符串                                                   | 请看下一节内容。                |

### String 函数一览

#### str.capitalize()

Python capitalize() 将字符串的第一个字母变成大写，其他字母变小写。

返回值：该方法返回一个首字母大写的字符串。

需要注意的是：

```python
# 1、首字符会转换成大写，其余字符会转换成小写。
str="hello PYTHON"
print(str.capitalize())  # Hello python

# 2、首字符如果是非字母，首字母不会转换成大写，会转换成小写。
str="123 Hello PYTHON"
print(str.capitalize())  # 123 hello python
```

#### str.center()

center() 方法返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。

语法：`str.center(width[, fillchar])`

返回值：返回一个指定的宽度 width 居中的字符串，如果 width 小于字符串宽度直接返回字符串，否则使用 fillchar 去填充。

需要注意的是：

```python
# 1、如果 width 小于字符串宽度直接返回字符串，不会截断:
str = "[www.runoob.com]"
print(str.center(4, '*'))	# [www.runoob.com]

# 2、fillchar 默认是空格
str = "[www.runoob.com]"
print(str.center(20))		#   [www.runoob.com]  

# 3、fillchar 只能是单个字符

# 4、奇数个字符时优先向右边补*
print('123'.center(4, '*'))		# 123*

# 5、偶数个字符时优先向左边补*
print('1234'.center(5, '*'))	# *1234
```

#### str.count()

语法：`str.count(sub, start= 0,end=len(string))`

```python
str="www.runoob.com"
sub='o'
print (str.count(sub))			# 3
print (str.count(sub,0,10))		# 2
```

#### str.encode() & bytes.decode()

decode() 方法以指定的编码格式解码 bytes 对象。默认编码为 'utf-8'。

语法：`bytes.decode(encoding="utf-8", errors="strict")`

参数：

- encoding -- 要使用的编码，如"UTF-8"。
- errors -- 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。 其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。

```python
str = "菜鸟教程";
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")
print(str)
print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)
print("UTF-8 解码：", str_utf8.decode('UTF-8','strict'))
print("GBK 解码：", str_gbk.decode('GBK','strict'))

"""
菜鸟教程
UTF-8 编码： b'\xe8\x8f\x9c\xe9\xb8\x9f\xe6\x95\x99\xe7\xa8\x8b'
GBK 编码： b'\xb2\xcb\xc4\xf1\xbd\xcc\xb3\xcc'
UTF-8 解码： 菜鸟教程
GBK 解码： 菜鸟教程
"""
```

**UTF-8 和 GBK 的区别**

**先给结论：**现在基本都用 UTF-8，建议采用这个。

GB 指代的“国标”，即“国家标准”。

UTF-8 是一种国际化的编码方式，包含了世界上大部分的语种文字（简体中文字、繁体中文字、英文、日文、韩文等语言），也兼容 ASCII 码。

GBK 是在国家标准 GB2312 基础上扩容后兼容 GB2312 的标准（好像还不是国家标准），专门用来解决中文编码的，是双字节的，不论中英文都是双字节的。

UTF－8 编码是用以解决国际上字符的一种多字节编码，它对英文使用 8 位（即一个字节），中文使用 24 位（三个字节）来编码。

对于英文字符较多的论坛则用 UTF－8 节省空间。

另外，如果是外国人访问你的 GBK 网页，需要下载中文语言包支持。访问 UTF-8 编码的网页则不出现这问题，可以直接访问。

GBK 包含全部中文字符。

UTF-8 则包含全世界所有国家需要用到的字符。

#### str.endswith()

endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回 True，否则返回 False。可选参数 "start" 与 "end" 为检索字符串的开始与结束位置。

语法：`str.endswith(suffix[, start[, end]])`

#### str.expandtabs()

expandtabs() 方法把字符串中的 tab 符号 **\t** 转为空格，tab 符号 **\t** 默认的空格数是 8，在第 0、8、16...等处给出制表符位置，如果当前位置到开始位置或上一个制表符位置的字符数不足 8 的倍数则以空格代替。

语法：`str.expandtabs(tabsize=8)`

#### str.find() & str.rfind()

find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果指定范围内如果包含指定索引值，返回的是索引值在字符串中的起始位置。如果不包含索引值，返回-1。

语法：`str.find(str, beg=0, end=len(string))`

rfind() 返回字符串最后一次出现的位置，如果没有匹配项则返回-1。

语法：`str.rfind(str, beg=0 end=len(string))`

#### str.index()

index() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。

#### str.isalnum()

isalnum() 方法检测字符串是否由字母和数字组成。如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False.

注意：如果字符串里面有汉字的话，也返回 True:

```python
a = 'ssdfghjk24汉字'
b = a.isalnum()
print(b)	# True
```

#### str.isalpha()

isalpha() 方法检测字符串是否只由字母或文字组成。如果字符串至少有一个字符并且所有字符都是字母或文字则返回 True，否则返回 False。

#### str.islower()

如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False

注意：这个函数的判断非常迷。。

```python
'aaab32'.islower()			# True
'aaab32你好'.islower()		# True
'aaab32~'.islower()			# True
'aaab32~+'.islower()		# True
'aaab32~?'.islower()		# True
'aaab32...'.islower()		# True
'a\nb'.islower()			# True
r'\b'.islower()				# True
'\b'.islower()				# False		# 就很迷
```

#### str.isupper()

isupper() 方法检测字符串中所有的字母是否都为大写。

#### str.isdigit()、s.isdecimal()、str.isnumeric()、

**str.isdigit()** 检测字符串是否只包含数字（即不接受其他一切非 **[0-9]** 元素）。

**s.isdigit、isdecimal 和 s.isnumeric 区别**

**isdigit()**

**True**: Unicode数字，byte数字（单字节），全角数字（双字节）

**False**: 汉字数字，罗马数字，小数

**Error**: 无

**isdecimal()**

**True**: Unicode数字，，全角数字（双字节）

**False**: 罗马数字，汉字数字，小数

**Error**: byte数字（单字节）

**isnumeric()**

**True**: Unicode 数字，全角数字（双字节），汉字数字

**False**: 小数，罗马数字

**Error**: byte数字（单字节）

```python
num = "1"  #unicode
num.isdigit()   # True
num.isdecimal() # True
num.isnumeric() # True

num = "1" # 全角
num.isdigit()   # True
num.isdecimal() # True
num.isnumeric() # True

num = b"1" # byte
num.isdigit()   # True
num.isdecimal() # AttributeError 'bytes' object has no attribute 'isdecimal'
num.isnumeric() # AttributeError 'bytes' object has no attribute 'isnumeric'

num = "IV" # 罗马数字
num.isdigit()   # False
num.isdecimal() # False
num.isnumeric() # False

num = "四" # 汉字
num.isdigit()   # False
num.isdecimal() # False
num.isnumeric() # True
```

#### str.isspace()

isspace() 方法检测字符串是否只由空白字符组成。

#### str.istitle()

istitle() 方法检测字符串中所有的单词拼写首字母是否为大写，且其他字母为小写。

#### str.join(seq)

join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。

语法：`str.join(sequence)`

```python
s1 = "-"
s2 = ""
seq = ("r", "u", "n", "o", "o", "b") # 字符串序列
print (s1.join( seq ))		# r-u-n-o-o-b
print (s2.join( seq ))		# runoob
```

1. str.join(sequence) 函数中的 sequence 中的元素必须的字符串，否则会报错，

2. 字符串也属于序列
3. 如果链接的序列是字典，会将所有key连接起来

#### str.ljust()

ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。

```python
str = "Runoob example....wow!!!"
print (str.ljust(50, '*'))
# Runoob example....wow!!!**************************
```

#### str.lower() & str.upper()

 lower() 方法转换字符串中所有大写字符为小写；

upper() 方法将字符串中的小写字母转为大写字母。

#### str.lstrip()

lstrip() 方法用于截掉字符串左边的空格或指定字符。

注意：从左到右移除字符串的指定字符，无字符集参数或为 None 时移除空格，str 时移除所有属于字符集子串的字符一旦不属于则停止移除并返回字符串副本。

```python
'www.example.com'.lstrip('cmowz.')		# 'example.com'
```

#### str.maketrans()

maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。

两个字符串的长度必须相同，为一一对应的关系。

**注：**Python3.4 已经没有 string.maketrans() 了，取而代之的是内建函数: **bytearray.maketrans()、bytes.maketrans()、str.maketrans()** 。

```python
# 1.一个参数，该参数必须为字典
d = {'a':'1','b':'2','c':'3','d':'4','e':'5','s':'6'}
trantab = str.maketrans(d)
st='just do it'
print(st.translate(trantab))	# ju6t 4o it

# 2.两个参数 x 和 y，x、y 必须是长度相等的字符串，并且 x 中每个字符映射到 y 中相同位置的字符
x = 'abcdefs'
y = '1234567'
st='just do it'
trantab = str.maketrans(x,y)
print(st.translate(trantab))	# ju6t 4o it

# 3.三个参数 x、y、z，第三个参数 z 必须是字符串，其字符将被映射为 None，即删除该字符；如果 z 中字符与 x 中字符重复，该重复的字符在最终结果中还是会被删除。也就是无论是否重复，只要有第三个参数 z，z 中的字符都会被删除。
x = 'abcdefs'
y='1234567'
z='ot'
st='just do it'
trantab = str.maketrans(x,y,z)
print(st.translate(trantab))	# ju7 4 i

x = 'abst'
y = '1234'
z = 's'
st = 'just do it'
trantab = str.maketrans(x,y,z)
print(st.translate(trantab))	# ju4 do i4
```

#### max(str) & min(str)

查看ASCII码：`ord(str)`

大致顺序：`0~9,A~Z,a~z`

```python
print(ord('0'), ord('1'), ord('9'), ord('A'), ord('Z'), ord('a'), ord('z'))

# 48 49 57 65 90 97 122
```

#### str.replace()

replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。

语法：`str.replace(old, new[, max])`

#### TODO

### 补充

#### 字符串拼接效率问题

你可能了解到，在其他语言中，如 Java，有可变的字符串类型，比如 StringBuilder，每次添加、改变或删除字符（串），无需创建新的字符串，时间复杂度仅为 O(1)。这样就大大提高了程序的运行效率。

但可惜的是，Python 中并没有相关的数据类型，我们还是得老老实实创建新的字符串。因此，每次想要改变字符串，往往需要 O(n) 的时间复杂度，其中，n 为新字符串的长度。

你可能注意到了，上述例子的说明中，我用的是“往往”、“通常”这样的字眼，并没有说“一定”。这是为什么呢？显然，随着版本的更新，Python 也越来越聪明，性能优化得越来越好了。

这里，我着重讲解一下，使用加法操作符'+='的字符串拼接方法。因为它是一个例外，打破了字符串不可变的特性。

操作方法如下所示：

`str1 += str2 # 表示 str1 = str1 + str2`

对于下面这个例子：

```python
s = ''
for n in range(0, 100000):
s += str(n)
```

每次循环，似乎都得创建一个新的字符串；而每次创建一个新的字符串，都需要 O(n) 的时间复杂度。因此，总的时间复杂度就为 O(1) + O(2) + … + O(n) = O(n^2)。这样到底对不对呢？

自从 Python2.5 开始，每次处理字符串的拼接操作时（str1 += str2），Python 首先会检测 str1 还有没有其他的引用。如果没有的话，就会尝试原地扩充字符串 buffer 的大小，而不是重新分配一块内存来创建新的字符串并拷贝。这样的话，上述例子中的时间复杂度就仅为 O(n) 了。

因此，以后你在写程序遇到字符串拼接时，如果使用’+='更方便，就放心地去用吧，不用过分担心效率问题了。

另外，对于字符串拼接问题，除了使用加法操作符，我们还可以使用字符串内置的 join 函数。`string.join(iterable)`，表示把每个元素都按照指定的格式连接起来。

```python
l = []
for n in range(0, 100000):
l.append(str(n))
l = ' '.join(l)
```

由于列表的 append 操作是 O(1) 复杂度，字符串同理。因此，这个含有 for 循环例子的时 间复杂度为 n*O(1)=O(n)。

