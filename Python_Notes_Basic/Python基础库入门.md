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

**该方法返回查找对象的索引位置，如果没有找到对象则抛出异常。**

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
s1 = {x for x in 'abra1-FSG_49Pprofile.txtcadabra' if x not in 'abc'}
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

#### str.endswith() & str.startswith()

endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回 True，否则返回 False。可选参数 "start" 与 "end" 为检索字符串的开始与结束位置。

语法：`str.endswith(suffix[, start[, end]])`

startswith() 方法用于判断开头。

#### str.expandtabs()

expandtabs() 方法把字符串中的 tab 符号 **\t** 转为空格，tab 符号 **\t** 默认的空格数是 8，在第 0、8、16...等处给出制表符位置，如果当前位置到开始位置或上一个制表符位置的字符数不足 8 的倍数则以空格代替。

语法：`str.expandtabs(tabsize=8)`

#### str.find() & str.rfind()

find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果指定范围内如果包含指定索引值，返回的是索引值在字符串中的起始位置。如果不包含索引值，返回-1。

语法：`str.find(str, beg=0, end=len(string))`

rfind() 返回字符串最后一次出现的位置，如果没有匹配项则返回-1。

语法：`str.rfind(str, beg=0 end=len(string))`

#### str.index() & str.rindex()

index() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。

rindex() 方法则是返回最后出现的位置。

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

判断十进制数字

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

- **isdigit 和 isnumeric的区别?**

```python
def dn():
    dgt=[]
    num=[]
    c=0
    for c in range(2**16):
            ch=chr(c)
            if ch.isdigit():dgt.append(ch)
            if ch.isnumeric():num.append(ch)
    print('digits:',dgt)
    print('numeric:',num)
dn()
```

```python
digits: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '²', '³', '¹', '٠', '١', '٢', '٣', '٤', '٥', '٦', '٧', '٨', '٩', '۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹', '߀', '߁', '߂', '߃', '߄', '߅', '߆', '߇', '߈', '߉', '०', '१', '२', '३', '४', '५', '६', '७', '८', '९', '০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯', '੦', '੧', '੨', '੩', '੪', '੫', '੬', '੭', '੮', '੯', '૦', '૧', '૨', '૩', '૪', '૫', '૬', '૭', '૮', '૯', '୦', '୧', '୨', '୩', '୪', '୫', '୬', '୭', '୮', '୯', '௦', '௧', '௨', '௩', '௪', '௫', '௬', '௭', '௮', '௯', '౦', '౧', '౨', '౩', '౪', '౫', '౬', '౭', '౮', '౯', '೦', '೧', '೨', '೩', '೪', '೫', '೬', '೭', '೮', '೯', '൦', '൧', '൨', '൩', '൪', '൫', '൬', '൭', '൮', '൯', '෦', '෧', '෨', '෩', '෪', '෫', '෬', '෭', '෮', '෯', '๐', '๑', '๒', '๓', '๔', '๕', '๖', '๗', '๘', '๙', '໐', '໑', '໒', '໓', '໔', '໕', '໖', '໗', '໘', '໙', '༠', '༡', '༢', '༣', '༤', '༥', '༦', '༧', '༨', '༩', '၀', '၁', '၂', '၃', '၄', '၅', '၆', '၇', '၈', '၉', '႐', '႑', '႒', '႓', '႔', '႕', '႖', '႗', '႘', '႙', '፩', '፪', '፫', '፬', '፭', '፮', '፯', '፰', '፱', '០', '១', '២', '៣', '៤', '៥', '៦', '៧', '៨', '៩', '᠐', '᠑', '᠒', '᠓', '᠔', '᠕', '᠖', '᠗', '᠘', '᠙', '᥆', '᥇', '᥈', '᥉', '᥊', '᥋', '᥌', '᥍', '᥎', '᥏', '᧐', '᧑', '᧒', '᧓', '᧔', '᧕', '᧖', '᧗', '᧘', '᧙', '᧚', '᪀', '᪁', '᪂', '᪃', '᪄', '᪅', '᪆', '᪇', '᪈', '᪉', '᪐', '᪑', '᪒', '᪓', '᪔', '᪕', '᪖', '᪗', '᪘', '᪙', '᭐', '᭑', '᭒', '᭓', '᭔', '᭕', '᭖', '᭗', '᭘', '᭙', '᮰', '᮱', '᮲', '᮳', '᮴', '᮵', '᮶', '᮷', '᮸', '᮹', '᱀', '᱁', '᱂', '᱃', '᱄', '᱅', '᱆', '᱇', '᱈', '᱉', '᱐', '᱑', '᱒', '᱓', '᱔', '᱕', '᱖', '᱗', '᱘', '᱙', '⁰', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹', '₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉', '①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧', '⑨', '⑴', '⑵', '⑶', '⑷', '⑸', '⑹', '⑺', '⑻', '⑼', '⒈', '⒉', '⒊', '⒋', '⒌', '⒍', '⒎', '⒏', '⒐', '⓪', '⓵', '⓶', '⓷', '⓸', '⓹', '⓺', '⓻', '⓼', '⓽', '⓿', '❶', '❷', '❸', '❹', '❺', '❻', '❼', '❽', '❾', '➀', '➁', '➂', '➃', '➄', '➅', '➆', '➇', '➈', '➊', '➋', '➌', '➍', '➎', '➏', '➐', '➑', '➒', '꘠', '꘡', '꘢', '꘣', '꘤', '꘥', '꘦', '꘧', '꘨', '꘩', '꣐', '꣑', '꣒', '꣓', '꣔', '꣕', '꣖', '꣗', '꣘', '꣙', '꤀', '꤁', '꤂', '꤃', '꤄', '꤅', '꤆', '꤇', '꤈', '꤉', '꧐', '꧑', '꧒', '꧓', '꧔', '꧕', '꧖', '꧗', '꧘', '꧙', '꧰', '꧱', '꧲', '꧳', '꧴', '꧵', '꧶', '꧷', '꧸', '꧹', '꩐', '꩑', '꩒', '꩓', '꩔', '꩕', '꩖', '꩗', '꩘', '꩙', '꯰', '꯱', '꯲', '꯳', '꯴', '꯵', '꯶', '꯷', '꯸', '꯹', '０', '１', '２', '３', '４', '５', '６', '７', '８', '９']
numeric: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '²', '³', '¹', '¼', '½', '¾', '٠', '١', '٢', '٣', '٤', '٥', '٦', '٧', '٨', '٩', '۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹', '߀', '߁', '߂', '߃', '߄', '߅', '߆', '߇', '߈', '߉', '०', '१', '२', '३', '४', '५', '६', '७', '८', '९', '০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯', '৴', '৵', '৶', '৷', '৸', '৹', '੦', '੧', '੨', '੩', '੪', '੫', '੬', '੭', '੮', '੯', '૦', '૧', '૨', '૩', '૪', '૫', '૬', '૭', '૮', '૯', '୦', '୧', '୨', '୩', '୪', '୫', '୬', '୭', '୮', '୯', '୲', '୳', '୴', '୵', '୶', '୷', '௦', '௧', '௨', '௩', '௪', '௫', '௬', '௭', '௮', '௯', '௰', '௱', '௲', '౦', '౧', '౨', '౩', '౪', '౫', '౬', '౭', '౮', '౯', '౸', '౹', '౺', '౻', '౼', '౽', '౾', '೦', '೧', '೨', '೩', '೪', '೫', '೬', '೭', '೮', '೯', '൘', '൙', '൚', '൛', '൜', '൝', '൞', '൦', '൧', '൨', '൩', '൪', '൫', '൬', '൭', '൮', '൯', '൰', '൱', '൲', '൳', '൴', '൵', '൶', '൷', '൸', '෦', '෧', '෨', '෩', '෪', '෫', '෬', '෭', '෮', '෯', '๐', '๑', '๒', '๓', '๔', '๕', '๖', '๗', '๘', '๙', '໐', '໑', '໒', '໓', '໔', '໕', '໖', '໗', '໘', '໙', '༠', '༡', '༢', '༣', '༤', '༥', '༦', '༧', '༨', '༩', '༪', '༫', '༬', '༭', '༮', '༯', '༰', '༱', '༲', '༳', '၀', '၁', '၂', '၃', '၄', '၅', '၆', '၇', '၈', '၉', '႐', '႑', '႒', '႓', '႔', '႕', '႖', '႗', '႘', '႙', '፩', '፪', '፫', '፬', '፭', '፮', '፯', '፰', '፱', '፲', '፳', '፴', '፵', '፶', '፷', '፸', '፹', '፺', '፻', '፼', 'ᛮ', 'ᛯ', 'ᛰ', '០', '១', '២', '៣', '៤', '៥', '៦', '៧', '៨', '៩', '៰', '៱', '៲', '៳', '៴', '៵', '៶', '៷', '៸', '៹', '᠐', '᠑', '᠒', '᠓', '᠔', '᠕', '᠖', '᠗', '᠘', '᠙', '᥆', '᥇', '᥈', '᥉', '᥊', '᥋', '᥌', '᥍', '᥎', '᥏', '᧐', '᧑', '᧒', '᧓', '᧔', '᧕', '᧖', '᧗', '᧘', '᧙', '᧚', '᪀', '᪁', '᪂', '᪃', '᪄', '᪅', '᪆', '᪇', '᪈', '᪉', '᪐', '᪑', '᪒', '᪓', '᪔', '᪕', '᪖', '᪗', '᪘', '᪙', '᭐', '᭑', '᭒', '᭓', '᭔', '᭕', '᭖', '᭗', '᭘', '᭙', '᮰', '᮱', '᮲', '᮳', '᮴', '᮵', '᮶', '᮷', '᮸', '᮹', '᱀', '᱁', '᱂', '᱃', '᱄', '᱅', '᱆', '᱇', '᱈', '᱉', '᱐', '᱑', '᱒', '᱓', '᱔', '᱕', '᱖', '᱗', '᱘', '᱙', '⁰', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹', '₀', '₁', '₂', '₃', '₄', '₅', '₆', '₇', '₈', '₉', '⅐', '⅑', '⅒', '⅓', '⅔', '⅕', '⅖', '⅗', '⅘', '⅙', '⅚', '⅛', '⅜', '⅝', '⅞', '⅟', 'Ⅰ', 'Ⅱ', 'Ⅲ', 'Ⅳ', 'Ⅴ', 'Ⅵ', 'Ⅶ', 'Ⅷ', 'Ⅸ', 'Ⅹ', 'Ⅺ', 'Ⅻ', 'Ⅼ', 'Ⅽ', 'Ⅾ', 'Ⅿ', 'ⅰ', 'ⅱ', 'ⅲ', 'ⅳ', 'ⅴ', 'ⅵ', 'ⅶ', 'ⅷ', 'ⅸ', 'ⅹ', 'ⅺ', 'ⅻ', 'ⅼ', 'ⅽ', 'ⅾ', 'ⅿ', 'ↀ', 'ↁ', 'ↂ', 'ↅ', 'ↆ', 'ↇ', 'ↈ', '↉', '①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧', '⑨', '⑩', '⑪', '⑫', '⑬', '⑭', '⑮', '⑯', '⑰', '⑱', '⑲', '⑳', '⑴', '⑵', '⑶', '⑷', '⑸', '⑹', '⑺', '⑻', '⑼', '⑽', '⑾', '⑿', '⒀', '⒁', '⒂', '⒃', '⒄', '⒅', '⒆', '⒇', '⒈', '⒉', '⒊', '⒋', '⒌', '⒍', '⒎', '⒏', '⒐', '⒑', '⒒', '⒓', '⒔', '⒕', '⒖', '⒗', '⒘', '⒙', '⒚', '⒛', '⓪', '⓫', '⓬', '⓭', '⓮', '⓯', '⓰', '⓱', '⓲', '⓳', '⓴', '⓵', '⓶', '⓷', '⓸', '⓹', '⓺', '⓻', '⓼', '⓽', '⓾', '⓿', '❶', '❷', '❸', '❹', '❺', '❻', '❼', '❽', '❾', '❿', '➀', '➁', '➂', '➃', '➄', '➅', '➆', '➇', '➈', '➉', '➊', '➋', '➌', '➍', '➎', '➏', '➐', '➑', '➒', '➓', '⳽', '〇', '〡', '〢', '〣', '〤', '〥', '〦', '〧', '〨', '〩', '〸', '〹', '〺', '㆒', '㆓', '㆔', '㆕', '㈠', '㈡', '㈢', '㈣', '㈤', '㈥', '㈦', '㈧', '㈨', '㈩', '㉈', '㉉', '㉊', '㉋', '㉌', '㉍', '㉎', '㉏', '㉑', '㉒', '㉓', '㉔', '㉕', '㉖', '㉗', '㉘', '㉙', '㉚', '㉛', '㉜', '㉝', '㉞', '㉟', '㊀', '㊁', '㊂', '㊃', '㊄', '㊅', '㊆', '㊇', '㊈', '㊉', '㊱', '㊲', '㊳', '㊴', '㊵', '㊶', '㊷', '㊸', '㊹', '㊺', '㊻', '㊼', '㊽', '㊾', '㊿', '㐅', '㒃', '㠪', '㭍', '一', '七', '万', '三', '九', '二', '五', '亖', '亿', '什', '仟', '仨', '伍', '佰', '億', '兆', '兩', '八', '六', '十', '千', '卄', '卅', '卌', '叁', '参', '參', '叄', '四', '壱', '壹', '幺', '廾', '廿', '弌', '弍', '弎', '弐', '拾', '捌', '柒', '漆', '玖', '百', '肆', '萬', '貮', '貳', '贰', '阡', '陆', '陌', '陸', '零', '꘠', '꘡', '꘢', '꘣', '꘤', '꘥', '꘦', '꘧', '꘨', '꘩', 'ꛦ', 'ꛧ', 'ꛨ', 'ꛩ', 'ꛪ', 'ꛫ', 'ꛬ', 'ꛭ', 'ꛮ', 'ꛯ', '꠰', '꠱', '꠲', '꠳', '꠴', '꠵', '꣐', '꣑', '꣒', '꣓', '꣔', '꣕', '꣖', '꣗', '꣘', '꣙', '꤀', '꤁', '꤂', '꤃', '꤄', '꤅', '꤆', '꤇', '꤈', '꤉', '꧐', '꧑', '꧒', '꧓', '꧔', '꧕', '꧖', '꧗', '꧘', '꧙', '꧰', '꧱', '꧲', '꧳', '꧴', '꧵', '꧶', '꧷', '꧸', '꧹', '꩐', '꩑', '꩒', '꩓', '꩔', '꩕', '꩖', '꩗', '꩘', '꩙', '꯰', '꯱', '꯲', '꯳', '꯴', '꯵', '꯶', '꯷', '꯸', '꯹', '參', '拾', '兩', '零', '六', '陸', '什', '０', '１', '２', '３', '４', '５', '６', '７', '８', '９']
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

#### str.ljust() & str.rjust()

ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。

```python
str = "Runoob example....wow!!!"
print (str.ljust(50, '*'))
# Runoob example....wow!!!**************************
```

rjust() 方法返回一个原字符串右对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。

#### str.lower() & str.upper()

 lower() 方法转换字符串中所有大写字符为小写；

upper() 方法将字符串中的小写字母转为大写字母。

#### str.lstrip() & str.rstrip()

lstrip() 方法用于截掉字符串左边的空格或指定字符。

注意：从左到右移除字符串的指定字符，无字符集参数或为 None 时移除空格，str 时移除所有属于字符集子串的字符一旦不属于则停止移除并返回字符串副本。

```python
'www.example.com'.lstrip('cmowz.')		# 'example.com'
```

rstrip() 方法方向从右到左。

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

语法：`str.replace(old, new[, max]) -> str`

**Tip：** `replace` 不会改变对象自身，而是返回一个副本，因此可以连续使用。 `str.replace().replace()`

#### str.split()

split() 通过指定分隔符对字符串进行切片，如果第二个参数 num 有指定值，则分割为 num+1 个子字符串。

语法：`str.split(str="", num=string.count(str))`

参数

- str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
- num -- 分割次数。默认为 -1, 即分隔所有。

返回：返回分割后的字符串列表

```python
str = "this is string example....wow!!!"
print(str.split( ))       # 以空格为分隔符	# ['this', 'is', 'string', 'example....wow!!!']
print(str.split('i',1))   # 以 i 为分隔符	# ['th', 's is string example....wow!!!']
print(str.split('w'))     # 以 w 为分隔符	# ['this is string example....', 'o', '!!!']

# 注意，split 包含在首尾时，会用空字符串分割
print(str.split("this"))	# ['', ' is string example....wow!!!']
s1 = 'Jacob'
print(s1.split('Jacob'))	# ['', '']
```

#### str.splitlines()

Python splitlines() 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。

参数：keepends -- 在输出结果里是否去掉换行符('\r', '\r\n', \n')，默认为 False，不包含换行符，如果为 True，则保留换行符。

```python
>>> 'ab c\n\nde fg\rkl\r\n'.splitlines()
['ab c', '', 'de fg', 'kl']
>>> 'ab c\n\nde fg\rkl\r\n'.splitlines(True)
['ab c\n', '\n', 'de fg\r', 'kl\r\n']
```

#### str.strip()

strip() 方法用于移除字符串头尾指定的字符（默认为空格）或字符序列。

**strip()** 处理的时候，如果不带参数，默认是清除两边的空白符，例如：**/n**, **/r**, **/t**, **' '**)。

**注意：**该方法只能删除开头或是结尾的字符，不能删除中间部分的字符。

```python
s1 = "*****this is **string** example....wow!!!*****"
print (s1.strip( '*' ))  # 指定字符串 *
# this is **string** example....wow!!!

s2 = "123abcrunoob321"
print (s2.strip( '12' ))  # 字符序列为 12
# 3abcrunoob3
```

#### str.swapcase()

**swapcase()** 方法用于对字符串的大小写字母进行转换，**即将大写字母转换为小写字母，小写字母会转换为大写字母**。

#### str.title()

```python
s1 = "this is string example from runoob....wow!!!"
print (s1.title())		# This Is String Example From Runoob....Wow!!!

# 请注意，非字母后的第一个字母将转换为大写字母：
s2 = "hello b2b2b2 and 3g3g3g"
print(s2.title())		# Hello B2B2B2 And 3G3G3G
```

#### str.translate()

translate() 方法根据参数 table 给出的表(包含 256 个字符)转换字符串的字符

参数

- table -- 翻译表，翻译表是通过 [maketrans()](https://www.runoob.com/python3/python3-string-maketrans.html) 方法转换而来。
- deletechars -- 字符串中要过滤的字符列表。

```python
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)   # 制作翻译表
 
str = "this is string example....wow!!!"
print (str.translate(trantab))
# th3s 3s str3ng 2x1mpl2....w4w!!!
```

#### str.upper()

小写转大写

#### str.zfill()

zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0。

`str.zfill(width)`

```python
str = "this is string example from runoob....wow!!!"
print ("str.zfill : ",str.zfill(40))	# this is string example from runoob....wow!!!
print ("str.zfill : ",str.zfill(50))	# 000000this is string example from runoob....wow!!!
```

### 转义字符

```python
# \(在行尾时)	续行符
print("line1 \
... line2 \
... line3")
# line1 line2 line3

# \\		反斜杠符号
# \'		单引号
# \"		双引号
# \a		哑铃，执行后电脑有声音
# \b		退格(Backspace)
# \000		空
# \n		换行

# \v		纵向制表符
print("Hello \v World!")
'''
Hello 
       World!
'''
# \t		横向制表符

# \r		将 \r 后面的内容移到字符串开头，并逐一替换开头部分的字符，直至将 \r 后面的内容完全替换完成。
print("Hello\rWorld!")		# World!
print('google runoob taobao\r123456')		# 123456 runoob taobao

# \f		换页(只在控制打印机的时候有用)

# \yyy		八进制数，y 代表 0~7 的字符，例如：\012 代表换行。
print("\110\145\154\154\157\40\127\157\162\154\144\41")		# Hello World!
# \xyy		十六进制数，以 \x 开头，y 代表的字符，例如：\x0a 代表换行
print("\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21")	# Hello World!
# \other	其它的字符以普通格式输出
```

### 格式化字符串

Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。

在 Python 中，字符串格式化使用与 C 中 sprintf 函数一样的语法。

```python
# %c	格式化字符及其ASCII码
print("%c" % 97)
# %s	格式化字符串，采用str()显示
# %r	格式化字符串，采用repr()显示
# %d	格式化整数
# %u	格式化无符号整数
# %o	格式化无符号八进制数
# %x	格式化无符号十六进制数
# %X	格式化无符号十六进制数(大写)
# %f	格式化浮点数字，可指定小数后的精度
# %e	用科学计数法格式化浮点数
# %E	同%e
# %g	至多保留6位有效数字，大于6位时以科学计数法输出
# %G	同%g, 科学计数法时为 'E'
# %p	用十六进制格式化变量的地址
```

格式化操作符辅助指令:

```python
# *		定义宽度或小数点精度
# -		用做左对齐
# +		在正数前面显示加号(+)
# <sp>	在正数前面显示空格
# #		在八进制数前面显示('0')，在十六进制数前面显示'0x' 或者'0X'
# 0		显示的数字前面填充'0'而不是默认的空格
# %		'%%'输出一个单一的'%'
# (var)	映射变量(字典参数)
# m.n.	m 是显示的最小总宽度，n 是小数点后的位数（如果可用的话）
```

- **% 操作符，格式如下：**

```
%[(name)][flags][width].[precision]typecode
```

-  **(name)** 为命名
-  **flags** 可以有 +，-，' '或 0。+ 表示右对齐。- 表示左对齐。' ' 为一个空格，表示在正数的左侧填充一个空格，从而与负数对齐。0 表示使用 0 填充。
-  **width** 表示显示宽度
-  **precision** 表示小数点后精度

**示例：**

```python
print("%6.3f" % 2.3)	# 最小宽度为6，显示小数点后3位，因此前面有一个空格
 2.300
print("%+10x" % 10)		# x 为表示 16 进制，显示宽度为 10，前面有 8 个空格。 
        +a
print("%-5x" % -10)		# %-5x 负号为左对齐，显示宽度为 5，故 -a 后面有 3 个空格
-a  
print("%10.*f" % (4, 1.2))	# 我们可以利用 *，来动态代入  width, precision 两个量。比如
  1.2000
```

#### format 格式化函数

Python2.6 开始，新增了一种格式化字符串的函数 **str.format()**，它增强了字符串格式化的功能。

基本语法是通过 **{}** 和 **:** 来代替以前的 **%** 。

format 函数可以接受不限个参数，位置可以不按顺序。

```python
>>>"{} {}".format("hello", "world")    # 不设置指定位置，按默认顺序
'hello world'
 
>>> "{0} {1}".format("hello", "world")  # 设置指定位置
'hello world'
 
>>> "{1} {0} {1}".format("hello", "world")  # 设置指定位置
'world hello world'

# 通过字典设置参数
site = {"name": "菜鸟教程", "url": "www.runoob.com"}
print("网站名：{name}, 地址 {url}".format(**site))
网站名：菜鸟教程, 地址 www.runoob.com
```

| 数字       | 格式                                                         | 输出                   | 描述                         |
| :--------- | :----------------------------------------------------------- | :--------------------- | :--------------------------- |
| 3.1415926  | {:.2f}                                                       | 3.14                   | 保留小数点后两位             |
| 3.1415926  | {:+.2f}                                                      | +3.14                  | 带符号保留小数点后两位       |
| -1         | {:+.2f}                                                      | -1.00                  | 带符号保留小数点后两位       |
| 2.71828    | {:.0f}                                                       | 3                      | 不带小数                     |
| 5          | {:0>2d}                                                      | 05                     | 数字补零 (填充左边, 宽度为2) |
| 5          | {:x<4d}                                                      | 5xxx                   | 数字补x (填充右边, 宽度为4)  |
| 10         | {:x<4d}                                                      | 10xx                   | 数字补x (填充右边, 宽度为4)  |
| 1000000    | {:,}                                                         | 1,000,000              | 以逗号分隔的数字格式         |
| 0.25       | {:.2%}                                                       | 25.00%                 | 百分比格式                   |
| 1000000000 | {:.2e}                                                       | 1.00e+09               | 指数记法                     |
| 13         | {:>10d}                                                      | 13                     | 右对齐 (默认, 宽度为10)      |
| 13         | {:<10d}                                                      | 13                     | 左对齐 (宽度为10)            |
| 13         | {:^10d}                                                      | 13                     | 中间对齐 (宽度为10)          |
| 11         | `'{:b}'.format(11) '{:d}'.format(11) '{:o}'.format(11) '{:x}'.format(11) '{:#x}'.format(11) '{:#X}'.format(11)` | `1011 11 13 b 0xb 0XB` | 进制                         |

**^**, **<**, **>** 分别是居中、左对齐、右对齐，后面带宽度， **:** 号后面带填充的字符，只能是一个字符，不指定则默认是用空格填充。

**+** 表示在正数前显示 **+**，负数前显示 **-**； （空格）表示在正数前加空格

b、d、o、x 分别是二进制、十进制、八进制、十六进制。

---

**!a** (应用 **ascii()**)， **!s** （应用 **str()** ）和 **!r** （应用 **repr()** ）可以在格式化之前转换值:

```python
>>> import math
>>> print('The value of PI is approximately {}.'.format(math.pi))
The value of PI is approximately 3.14159265359.
>>> print('The value of PI is approximately {!r}.'.format(math.pi))
The value of PI is approximately 3.141592653589793.
```

在字段后的 **:** 后面加一个整数会限定该字段的最小宽度，这在美化表格时很有用:

```python
>>> table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
>>> for name, phone in table.items():
...     print('{0:10} ==> {1:10d}'.format(name, phone))
...
Jack       ==>       4098
Dcab       ==>       7678
Sjoerd     ==>       4127
```

#### f字符串

算是python3最常用的字符串了吧，语法：`f'{变量}'`

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

#### 字符串与 ASCII码

语法：`ord(str)`

```python
print(ord('0'), ord('1'), ord('9'), ord('A'), ord('Z'), ord('a'), ord('z'))
# 48 49 57 65 90 97 122
```

#### 字符串与真值

```python
print(eval('0'))		# 0
print(eval('-999'))		# -999
print(eval("2 * 2"))		# 4
```

# 输入和输出

## 输入输出基础

最简单直接的输入来自键盘操作，比如下面这个例子。

```python
# 输入
name = input('your name:')				# your name:Jack
gender = input('you are a boy?(y/n)')	# you are a boy?(y/n)y

welcome_str = 'Welcome to the matrix {prefix} {name}.'
welcome_dic = {'prefix': 'Mr.' if gender == 'y' else 'Mrs','name': name}
print('authorizing...')
print(welcome_str.format(**welcome_dic))

'''
authorizing...
Welcome to the matrix Mr. Jack.
'''
```

input() 函数暂停程序运行，同时等待键盘输入；

直到回车被按下，函数的参数即为提示语，**输入的类型永远是字符串型（str）**。

注意，初学者在这里很容易犯错。

Python 对 int 类型没有最大限制（相比之下， C++ 的 int 最大为 2147483647，超过这个数字会产生溢出），但是对 float 类型依然有精度限制。这些特点，除了在一些算法竞赛中要注意，在生产环境中也要时刻提防，避免因为对边界条件判断不清而造成 bug 甚至0day（危重安全漏洞）。

- **input()**

```python
# 输入三角形的三边长
a,b,c = (input("请输入三角形三边的长：").split())
a= int(a)
b= int(b)
c= int(c)
```

## 输出格式美化

Python两种输出值的方式: 表达式语句和 print() 函数。

第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。

如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。

如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。

- **str()：** 函数返回一个用户易读的表达形式。
- **repr()：** 产生一个解释器易读的表达形式。

```python
>>> s = 'Hello, Runoob'
>>> str(s)
'Hello, Runoob'
>>> repr(s)
"'Hello, Runoob'"
>>> str(1/7)
'0.14285714285714285'
>>> x = 10 * 3.25
>>> y = 200 * 200
>>> s = 'x 的值为： ' + repr(x) + ',  y 的值为：' + repr(y) + '...'
>>> print(s)
x 的值为： 32.5,  y 的值为：40000...
>>> #  repr() 函数可以转义字符串中的特殊字符
... hello = 'hello, runoob\n'
>>> hellos = repr(hello)
>>> print(hellos)
'hello, runoob\n'
>>> # repr() 的参数可以是 Python 的任何对象
... repr((x, y, ('Google', 'Runoob')))
"(32.5, 40000, ('Google', 'Runoob'))"
```

## 文件输入输出

- **open()的函数原型**

常用形式：`open(file, mode='r')`

完整语法：

```python
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
```

从官方文档中我们可以看到open函数有很多的参数，我们常用的是file，mode和encoding，对于其它的几个参数，平时不常用，也简单介绍一下。

- file: 必需，文件路径（相对或者绝对路径）。
- mode: 可选，文件打开模式
- buffering: 设置缓冲; 可取值有0，1， >1三个，0代表buffer关闭（只适用于二进制模式），1代表line buffer（只适用于文本模式），>1表示初始化的buffer大小；
- encoding: 表示的是返回的数据采用何种编码，一般采用 `utf8` 或者 `gbk` ；
- errors: 报错级别，取值一般有 `strict`，`ignore`，当取 `strict` 的时候，字符编码出现问题的时候，会报错，当取 `ignore` 的时候，编码出现问题，程序会忽略而过，继续执行下面的程序。
- newline: 可以取的值有`None, \n, \r, '', ‘\r\n' `，用于区分换行符，但是这个参数只对文本模式有效；
- closefd: 传入的file参数类型，取值与传入的文件参数有关，默认情况下为True，传入的file参数为文件的文件名，取值为False的时候，file只能是文件描述符，什么是文件描述符，就是一个非负整数，在Unix内核的系统中，打开一个文件，便会返回一个文件描述符；
- opener: 设置自定义开启器，开启器的返回值必须是一个打开的文件描述符。

---

命令行的输入输出，只是 Python 交互的最基本方式，适用一些简单小程序的交互。 而生产级别的 Python 代码，大部分 I/O 则来自于文件、网络、其他进程的消息等等。

首先我们需要先了解一下，计算机中文件访问的基础知识。事实上，计算机内核（kernel）对文件的处理相对比较复杂，涉及到内核模式、虚拟文件系统、锁和指针等一系列概念，这些内容我不会深入讲解，我只说一些基础但足够使用的知识。

```python
with open("test.txt","r") as ifs:
    text = ifs.read()
text
# 'This is a test file.'
```

我们先要用 open() 函数拿到文件的指针。其中，第一个参数指定文件位置（相对位置或者绝对位置）；第二个参数，如果是 'r'表示读取，如果是'w' 则表示写入，当然也可以用'rw' ，表示读写都要。a 则是一个不太常用（但也很有用）的参数，表示追加（append），这样打开的文件，如果需要写入，会从原始文件的最末尾开始写入。

如果你只需要读取文件，就不要请求写入权限。这样在某种程度上可以降低 bug 对整个系统带来的风险。

代码 text = ifs.read() ，即表示把文件所有内容读取到内存中，并赋值给变量 text。这么做自然也是有利有弊：

优点是方便; 缺点是如果文件过大，一次性读取可能造成内存崩溃。

这时，我们可以给 read 指定参数 size ，用来表示读取的最大长度。还可以通过 readline()函数，每次读取一行，这种做法常用于数据挖掘（Data Mining）中的数据清洗，在写一些小的程序时非常轻便。如果每行之间没有关联，这种做法也可以降低内存的压力。而write() 函数，可以把参数中的字符串输出到文件中，也很容易理解。

这里我需要简单提一下 with 语句（后文会详细讲到）。open() 函数对应于 close() 函数，也就是说，如果你打开了文件，在完成读取任务后，就应该立刻关掉它。而如果你使用了with 语句，就不需要显式调用close()。在 with 的语境下任务执行完毕后，close() 函数会被自动调用，代码也会简洁很多。

最后需要注意的是，所有 I/O 都应该进行错误处理。因为 I/O 操作可能会有各种各样的情况出现，而一个健壮（robust）的程序，需要能应对各种情况的发生，而不应该崩溃（故意设计的情况除外）。

---

open() 将会返回一个 file 对象，基本语法格式如下:

```
open(filename, mode)
```

- filename：包含了你要访问的文件名称的字符串值。
- mode：决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。

不同模式打开文件的完全列表：

| 模式 | 描述                                                         |
| :--- | :----------------------------------------------------------- |
| r    | 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。 |
| rb   | 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。 |
| r+   | 打开一个文件用于读写。文件指针将会放在文件的开头。           |
| rb+  | 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。 |
| w    | 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| wb   | 以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| w+   | 打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| wb+  | 以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
| a    | 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| ab   | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
| a+   | 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。 |
| ab+  | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。 |

下图很好的总结了这几种模式：

![](https://www.runoob.com/wp-content/uploads/2013/11/2112205-861c05b2bdbc9c28.png)

### 文件输出

#### f.write() 直接输出

```python
# 打开一个文件
f = open("/tmp/foo.txt", "w")

f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )

# 关闭打开的文件
f.close()
```

- 第一个参数为要打开的文件名。
- 第二个参数描述文件如何使用的字符。 mode 可以是 'r' 如果文件只读, 'w' 只用于写 (如果存在同名文件则将被删除), 和 'a' 用于追加文件内容; 所写的任何数据都会被自动增加到末尾. 'r+' 同时用于读写。 mode 参数是可选的; 'r' 将是默认值。

---

f.write(string) 将 string 写入到文件中, 然后返回写入的字符数。

```python
# 打开一个文件
f = open("/tmp/foo.txt", "w")

num = f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
print(num)		# 29
# 关闭打开的文件
f.close()
```

### 读取文件

#### f.read()

为了读取一个文件的内容，调用 f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回。

size 是一个可选的数字类型的参数。 当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回。

```python
# 打开一个文件
f = open("/tmp/foo.txt", "r")

str = f.read()
print(str)

# 关闭打开的文件
f.close()

'''
Python 是一个非常好的语言。
是的，的确非常好!!
'''
```

#### f.readline()

f.readline() 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。

```python
# 打开一个文件
f = open("/tmp/foo.txt", "r")

str = f.readline()
print(str)

# 关闭打开的文件
f.close()

'''Python 是一个非常好的语言。'''
```

#### f.readlines()

f.readlines() 将返回该文件中包含的所有行。

如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。

```python
# 打开一个文件
f = open("/tmp/foo.txt", "r")

str = f.readlines()
print(str)

# 关闭打开的文件
f.close()

'''
['Python 是一个非常好的语言。\n', '是的，的确非常好!!\n']
'''
```

另一种方式是迭代一个文件对象然后读取每行:

```python
# 打开一个文件
f = open("/tmp/foo.txt", "r")

for line in f:
    print(line, end='')

# 关闭打开的文件
f.close()

'''
Python 是一个非常好的语言。
是的，的确非常好!!
'''
```

这个方法很简单, 但是并没有提供一个很好的控制。 因为两者的处理机制不同, 最好不要混用。

### 文件属性

一个文件被打开后，你有一个file对象，你可以得到有关该文件的各种信息。

以下是和file对象相关的所有属性的列表：

| 属性           | 描述                                                         |
| :------------- | :----------------------------------------------------------- |
| file.closed    | 返回true如果文件已被关闭，否则返回false。                    |
| file.mode      | 返回被打开文件的访问模式。                                   |
| file.name      | 返回文件的名称。                                             |
| file.softspace | 如果用print输出后，必须跟一个空格符，则返回false。否则返回true。 |

```python
# 打开一个文件
fo = open("/tmp/foo.txt", "w")
print "文件名: ", fo.name
print "是否已关闭 : ", fo.closed
print "访问模式 : ", fo.mode
print "末尾是否强制加空格 : ", fo.softspace
```

### 文件定位

#### f.tell()

f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。

#### f.seek()

如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。

from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：

- seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
- seek(x,1) ： 表示从当前位置往后移动x个字符
- seek(-x,2)：表示从文件的结尾往前移动x个字符

```python
>>> f = open('/tmp/foo.txt', 'rb+')
>>> f.write(b'0123456789abcdef')
16
>>> f.seek(5)     # 移动到文件的第六个字节
5
>>> f.read(1)
b'5'
>>> f.seek(-3, 2) # 移动到文件的倒数第三字节
13
>>> f.read(1)
b'd'
```

### 相关函数

#### f.close()

在文本文件中 (那些打开文件的模式下没有 b 的), 只会相对于文件起始位置进行定位。

当你处理完一个文件后, 调用 f.close() 来关闭文件并释放系统的资源，如果尝试再调用该文件，则会抛出异常。

### pickle 模块

python的pickle模块实现了基本的数据序列和反序列化。

通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。

通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。

基本接口：

```python
pickle.dump(obj, file, [,protocol])
```

有了 pickle 这个对象, 就能对 file 以读取的形式打开:

```python
x = pickle.load(file)
```

**注解：**从 file 中读取一个字符串，并将它重构为原来的python对象。

**file:** 类文件对象，有read()和readline()接口。

```python
import pickle

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('./tmp/data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()
```

```python
import pprint, pickle

#使用pickle模块从文件中重构python对象
pkl_file = open('./tmp/data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()
```

## JSON

TODO

# 条件与循环

习惯把“条件与循环”，叫做编程中的基本功。为什么称它为基本功呢？因为它控制着代码的逻辑，可以说是程序的中枢系统。如果把写程序比作盖楼房，那么条件与循环就是楼房的根基，其他所有东西都是在此基础上构建而成。

毫不夸张地说，写一手简洁易读的条件与循环代码，对提高程序整体的质量至关重要。

## 条件语句

Python 中用 **elif** 代替了 **else if**，所以if语句的关键字为：**if – elif – else**。

**注意：**

- 1、每个条件后面要使用冒号 **:**，表示接下来是满足条件后要执行的语句块。
- 2、使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
- 3、**在Python中没有switch – case语句**。

---

首先，我们一起来看一下 Python 的条件语句，用法很简单。比如，我想要表示 y=|x|这个函数，那么相应的代码便是：

```python
def Jx_abs(x):
    if x < 0:
        y = -x
    else:
        y = x
    return y

Jx_abs(-3)
```

和其他语言不一样，我们不能在条件语句中加括号，但需要注意的是，在条件语句的末尾必须加上冒号`:`，这是 Python 特定的语法规范。 由于 Python 不支持 switch 语句，因此，当存在多个条件判断时，我们需要用 else if 来实 现，这在 Python 中的表达是elif。语法如下：

```python
if condition_1:
	statement_1
elif condition_2:
	statement_2
...
elif condition_i:
	statement_i
else:
	statement_n
```

整个条件语句是顺序执行的，如果遇到一个条件满足，比如 condition_i 满足时，在执行完statement_i 后，便会退出整个 if、elif、else 条件语句，而不会继续向下执行。

关于省略判断条件的常见用法:

![](https://i.loli.net/2021/10/20/SlPedpLN2hcQiBv.png)

不过，切记，在实际写代码时，我们鼓励，除了 `bool` 类型的数据，条件判断最好是显性的。比如，在判断一个整型数是否为 0 时，我们最好写出判断的条件：

```python
if i != 0:
...
```

## 循环语句

**同样需要注意冒号和缩进。另外，在 Python 中没有 do..while 循环。**

---

所谓循环，顾名思义，本质上就是遍历集合中的元素。和其他语言一样，Python 中的循环一般通过 for 循环和 while 循环实现。

比如，我们有一个列表，需要遍历列表中的所有元素并打印输出，代码如下：

```python
l = [1, 2, 3, 4]
for item in l:
    print(item)
```

其实，Python 中的数据结构只要是可迭代的（iterable），比如列表、集合等等，那么都可以通过下面这种方式遍历：

```python
for item in <iterable>:
...
```

这里需要单独强调一下字典。**字典本身只有键是可迭代的**，如果我们要遍历它的值或者是键值对，就需要通过其内置的函数 values() 或者 items() 实现。其中，values() 返回字典的值的集合，items() 返回键值对的集合。

```python
d = {'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'}
for k in d: # 遍历字典的键
	print(k)
'''
name
dob
gender
'''
for v in d.values(): # 遍历字典的值
	print(v)
'''
jason
2000-01-01
male
'''
for k, v in d.items(): # 遍历字典的键值对
	print('key: {}, value: {}'.format(k, v))
'''
key: name, value: jason
key: dob, value: 2000-01-01
key: gender, value: male
'''
```

通过索引来遍历：

```python
l = [1, 2, 3, 4, 5, 6, 7]
for index in range(0, len(l)):
    if index < 3:
        print(l[index])
```

当我们同时需要索引和元素时，还有一种更简洁的方式，那就是通过 Python 内置的函数`enumerate()`。

用它来遍历集合，不仅返回每个元素，并且还返回其对应的索引，这样一来，上面的例子就可以写成:

```python
l = [1, 2, 3, 4, 5, 6, 7]
for index, item in enumerate(l):
    if index < 3:
        print(item)
```

### continue && break

在循环语句中，我们还常常搭配 `continue` 和 `break` 一起使用。

所谓 `continue`，就是让程序跳过当前这层循环，继续执行下面的循环；

而 `break` 则是指完全跳出所在的整个循环体。

在循环中适当加入 `continue` 和 `break`，往往能使程序更加简洁、易读。

## pass 语句

Python pass是空语句，是为了保持程序结构的完整性。

pass 不做任何事情，一般用做占位语句，

## 条件与循环的复用

在阅读代码的时候，你应该常常会发现，有很多将条件与循环并做一行的操作，例如：

```
expression1 if condition else expression2 for item in iterable
```

将这个表达式分解开来，其实就等同于下面这样的嵌套结构：

```py
for item in iterable:
    if condition:
        expression1
    else:
        expression2
```

而如果没有 else 语句，则需要写成：

```
expression for item in iterable if condition
```

举个例子，比如我们要绘制 y = 2*|x| + 5 的函数图像，给定集合 x 的数据点，需要计算出 y 的数据集合，那么只用一行代码，就可以很轻松地解决问题了：

```python
y = [value * 2 + 5 if value > 0 else -value * 2 + 5 for value in x]
```

再比如我们在处理文件中的字符串时，常常遇到的一个场景： 将文件中逐行读取的一个完整语句，按逗号分割单词，去掉首位的空字符，并过滤掉长度小于等于 3 的单词，最后返回由单词组成的列表。这同样可以简洁地表达成一行：

```python
text = "Today,  is, Sunday"
text_list = [s.strip() for s in text.split(',') if len(s.strip()) > 3]
print(text_list)	# ['Today', 'Sunday']
```

当然，这样的复用并不仅仅局限于一个循环。比如，给定两个列表 x、y，要求返回 x、y 中所有元素对组成的元祖，相等情况除外。那么，你也可以很容易表示出来：

```
[(xx, yy) for xx in x for yy in y if xx != yy]
```

熟练之后，你会发现这种写法非常方便。当然，如果遇到逻辑很复杂的复用，你可能会觉得写成一行难以理解、容易出错。那种情况下，用正常的形式表达，也不失为一种好的规范和选择。

## 区别

很多时候，for 循环和 while 循环可以互相转换，比如要遍历一个列表，我们用 while 循环同样可以完成：

```python
l = [1, 2, 3, 4]
index = 0
while index < len(l):
    print(l[index])
    index += 1
```

那么，两者的使用场景又有什么区别呢？

通常来说，如果你只是遍历一个已知的集合，找出满足条件的元素，并进行相应的操作，那么**使用 for 循环更加简洁**。

但如果你需要在满足某个条件前，不停地重复某些操作，并且没有特定的集合需要去遍历，那么一般则会使用 while 循环。

比如，某个交互式问答系统，用户输入文字，系统会根据内容做出相应的回答。

为了实现这个功能，我们一般会使用 while 循环，大致代码如下：

```python
while True:
    try:
        text = input('Please enter your questions, enter "q" to exit')
        if text == 'q':
            print('Exit system')
            break
        ...
        ...
        print(response)
    except as err:
        print('Encountered error: {}'.format(err))
        break
```

### for 循环和 while 循环的效率问题:

要知道，**range() 函数是直接由 C 语言写的，调用它速度非常快**。

而 while 循环中的“i+= 1”这个操作，得通过 Python 的解释器间接调用底层的 C 语言；

并且这个简单的操作，又涉及到了对象的创建和删除（因为 i 是整型，是 immutable，i += 1 相当于 i = new int(i + 1)）。

所以，显然，for 循环的效率更胜一筹。

## 思考题

给定下面两个列表 attributes 和 values，要求针对 values 中每一组子列表 value，输出其和 attributes 中的键对应后的字典，最后返回字典组成的列表。

你能分别用一行和多行条件循环语句，来实现这个功能吗？

```python
attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'],
['mike', '1999-01-01', 'male'],
['nancy', '2001-02-01', 'female']
]
# expected outout:
# [{'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'},
# {'name': 'mike', 'dob': '1999-01-01', 'gender': 'male'},
# {'name': 'nancy', 'dob': '2001-02-01', 'gender': 'female'}]
```

```python
# 一行
list_dict = [dict(zip(attributes, value)) for value in values]
print(list_dict)
```

```python
# 多行
list_dict = []
for value in values:
    temp = {}
    for index, v in enumerate(value):
        temp[attributes[index]] = v
    list_dict.append(temp)
print(list_dict)
```

# 错误和异常

## 语法错误

Python 有两种错误很容易辨认：语法错误和异常。

Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。

Python 的语法错误或者称之为解析错，是初学者经常碰到的，如下实例

```python
>>> while True print('Hello world')
  File "<stdin>", line 1, in ?
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
```

这个例子中，函数 print() 被检查到有错误，是它前面缺少了一个冒号 **:** 。

语法分析器指出了出错的一行，并且在最先找到的错误的位置标记了一个小小的箭头。

## 异常

和其他语言一样，异常处理是 Python 中一种很常见，并且很重要的机制与代码规范。

即便 Python 程序的语法是正确的，在运行它的时候，也有可能发生错误。运行期检测到的错误被称为异常。

大多数的异常都不会被程序处理，都以错误信息的形式展现在这里:

```python
>>> 10 * (1/0)             # 0 不能作为除数，触发异常
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
ZeroDivisionError: division by zero
>>> 4 + spam*3             # spam 未定义，触发异常
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
NameError: name 'spam' is not defined
>>> '2' + 2               # int 不能与 str 相加，触发异常
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```

异常以不同的类型出现，这些类型都作为信息的一部分打印出来: 例子中的类型有 ZeroDivisionError，NameError 和 TypeError。

错误信息的前面部分显示了异常发生的上下文，并以调用栈的形式显示具体信息。

---

Python3 内置异常类型的结构

```python
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- ResourceWarning
```

### 异常处理

#### **try/except**

异常捕捉可以使用 **try/except** 语句。

- **处理单个异常**

![](https://www.runoob.com/wp-content/uploads/2019/07/try_except.png)

以下例子中，让用户输入一个合法的整数，但是允许用户中断这个程序（使用 Control-C 或者操作系统提供的方法）。用户中断的信息会引发一个 KeyboardInterrupt 异常。

```python
while True:
    try:
        x = int(input("请输入一个数字: "))
        break
    except ValueError:
        print("您输入的不是数字，请再次尝试输入！")
```

try 语句按照如下方式工作；

- 首先，执行 try 子句（在关键字 try 和关键字 except 之间的语句）。
- 如果没有异常发生，忽略 except 子句，try 子句执行后结束。
- 如果在执行 try 子句的过程中发生了异常，那么 try 子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的 except 子句将被执行。
- 如果一个异常没有与任何的 except 匹配，那么这个异常将会传递给上层的 try 中。

**except block 只接受与它相匹配的异常类型并执行，如果程序抛出的异常并不匹配，那么程序照样会终止并退出。**

很显然，这样强调一种类型的写法有很大的局限性。那么，该怎么解决这个问题呢？

---

- **同时处理不同的特定的异常**

一种解决方案，是在 except block 中加入多种异常的类型，分别来处理不同的特定的异常，最多只有一个分支会被执行。

处理程序将只针对对应的 try 子句中的异常进行处理，而不是其他的 try 的处理程序中的异常。

一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组，例如:

```python
except (RuntimeError, TypeError, NameError):
    pass
```

不过，很多时候，我们很难保证程序覆盖所有的异常类型，所以，更通常的做法，是在最后一个 except block，声明其处理的异常类型是 Exception。Exception 是其他所有非系统异常的基类，能够匹配任意非系统异常。

那么这段代码就可以写成下面这样：

```python
except ValueError as err:
    print('Value Error: {}'.format(err))
except IndexError as err:
    print('Index Error: {}'.format(err))
except Exception as err:
    print('Other error: {}'.format(err))
```

或者，你也可以在 except 后面省略异常类型，这表示与任意异常相匹配（包括系统异常等）：

你可以使用这种方法打印一个错误信息，然后再次把异常抛出。

```python
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise
```

#### try/except...else

**try/except** 语句还有一个可选的 **else** 子句，如果使用这个子句，那么必须放在所有的 except 子句之后。

**else 子句将在 try 子句没有发生任何异常的时候执行。**

![](https://www.runoob.com/wp-content/uploads/2019/07/try_except_else.png)

以下实例在 try 语句中判断文件是否可以打开，如果打开文件时正常的没有发生异常则执行 else 部分的语句，读取文件内容：

```python
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
```

使用 else 子句比把所有的语句都放在 try 子句里面要好，这样可以避免一些意想不到，而 except 又无法捕获的异常。

---

异常处理并不仅仅处理那些直接发生在 try 子句中的异常，而且还能处理子句中调用的函数（甚至间接调用的函数）里抛出的异常。例如:

```python
>>> def this_fails():
        x = 1/0
   
>>> try:
        this_fails()
    except ZeroDivisionError as err:
        print('Handling run-time error:', err)
   
Handling run-time error: int division or modulo by zero
```

#### try-finally 语句

try-finally 语句无论是否发生异常都将执行最后的代码。

![](https://www.runoob.com/wp-content/uploads/2019/07/try_except_else_finally.png)

以下实例中 finally 语句无论异常是否发生都会执行：

```python
try:
    runoob()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('这句话，无论异常是否发生都会执行。')
```

无论发生什么情况，finally block 中的语句都会被执行，**哪怕前面的 try 和 excep block 中使用了 return 语句**。

### 抛出异常

Python 使用 raise 语句抛出一个指定的异常。

raise语法格式如下：

```python
raise [Exception [, args [, traceback]]]
```

![](https://www.runoob.com/wp-content/uploads/2019/07/raise.png)

```python
x = 10
if x > 5:
    raise Exception('x 不能大于 5。x 的值为: {}'.format(x))
```

触发异常：

```python
Traceback (most recent call last):
  File "test.py", line 3, in <module>
    raise Exception('x 不能大于 5。x 的值为: {}'.format(x))
Exception: x 不能大于 5。x 的值为: 10
```

raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）。

如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出。

```python
>>> try:
        raise NameError('HiThere')
    except NameError:
        print('An exception flew by!')
        raise
   
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in ?
NameError: HiThere
```

### 用户自定义异常

你可以通过创建一个新的异常类来拥有自己的异常。异常类继承自 Exception 类，可以直接继承，或者间接继承，例如:

```python
>>> class MyError(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr(self.value)
   
>>> try:
        raise MyError(2*2)
    except MyError as e:
        print('My exception occurred, value:', e.value)
   
My exception occurred, value: 4
>>> raise MyError('oops!')
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
__main__.MyError: 'oops!'
```

在这个例子中，类 Exception 默认的` __init__()` 被覆盖。

当创建一个模块有可能抛出多种不同的异常时，一种通常的做法是为这个包建立一个基础异常类，然后基于这个基础类为不同的错误情况创建不同的子类:

```python
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
```

大多数的异常的名字都以"Error"结尾，就跟标准的异常命名一样。

### 定义清理行为

try 语句还有另外一个可选的子句，它定义了无论在任何情况下都会执行的清理行为。 例如:

```python
>>> try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
...
Goodbye, world!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
KeyboardInterrupt
```

以上例子不管 try 子句里面有没有发生异常，finally 子句都会执行。

如果一个异常在 try 子句里（或者在 except 和 else 子句里）被抛出，而又没有任何的 except 把它截住，那么这个异常会在 finally 子句执行后被抛出。

下面是一个更加复杂的例子（在同一个 try 语句里包含 except 和 finally 子句）:

```python
>>> def divide(x, y):
        try:
            result = x / y
        except ZeroDivisionError:
            print("division by zero!")
        else:
            print("result is", result)
        finally:
            print("executing finally clause")
   
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in ?
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

一定要是 `except ` 将异常拦截住才行，不然会抛出。

### 预定义的清理行为

一些对象定义了标准的清理行为，无论系统是否成功的使用了它，一旦不需要它了，那么这个标准的清理行为就会执行。

下面这个例子展示了尝试打开一个文件，然后把内容打印到屏幕上:

```python
for line in open("myfile.txt"):
    print(line, end="")
```

以上这段代码的问题是，当执行完毕后，文件会保持打开状态，并没有被关闭。

关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法:

```python
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
```

以上这段代码执行完毕后，就算在处理过程中出问题了，文件 f 总是会关闭。

### 实用案例

#### 捕获所有异常

```python
try:
   ...
except Exception as e:
   ...
   log('Reason:', e)       # Important!
```

这个将会捕获除了 SystemExit 、 KeyboardInterrupt 和 GeneratorExit 之外的所有异常。 如果你还想捕获这三个异常，将 Exception 改成 BaseException 即可。

### 注意

- 对于 flow-control（流程控制）的代码逻辑，我们一般不用异常处理。

# 函数

函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。

函数能提高应用的模块性，和代码的重复利用率。你已经知道Python提供了许多内建函数，比如print()。但你也可以自己创建函数，这被叫做用户自定义函数。

一个规范的值得借鉴的 Python 程序，除非代码量很少（比如 10 行、20 行以下），基本都应该由多个函数组成，这样的代码才更加模块化、规范化。

函数是 Python 程序中不可或缺的一部分。

事实上，在前面的学习中，我们已经用到了很多Python 的内置函数，比如 sorted() 表示对一个集合序列排序，len() 表示返回一个集合序 列的长度大小等等。

## 自定义函数

你可以定义一个由自己想要功能的函数，以下是简单的规则：

- 函数代码块以 **def** 关键词开头，后接函数标识符名称和圆括号 **()**。
- 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
- 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
- 函数内容以冒号 **:** 起始，并且缩进。
- **return [表达式]** 结束函数，选择性地返回一个值给调用方，不带表达式的 return 相当于返回 None。

![](https://www.runoob.com/wp-content/uploads/2014/05/py-tup-10-26-1.png)

```python
def my_func(message):
    print('Got a message: {}'.format(message))
# 调用函数 my_func()
my_func('Hello World')
# 输出
# Got a message: Hello World
```

和其他需要编译的语言（比如 C 语言）不一样的是，def 是可执行语句，这意味着函数直到被调用前，都是不存在的。当程序调用函数时，def 语句才会创建一个新的函数对象，并赋予其名字。

需要注意，主程序调用函数时，必须保证这个函数此前已经定义过，不然就会报错，比如：

```python
my_func('hello world')
def my_func(message):
    print('Got a message: {}'.format(message))
# 输出
NameError: name 'my_func' is not defined
```

另外，Python 函数的参数可以设定默认值，比如下面这样的写法：

```python
def func(param = 0):
    ...
```

这样，在调用函数 func() 时，如果参数 param 没有传入，则参数默认为 0；而如果传入了参数 param，其就会覆盖默认值。

Python 和其他语言相比的一大特点是，Python 是 dynamically typed 的，可以接受任何数据类型（整型，浮点，字符串等等）。

```python
def my_sum(a, b):
    return a + b

print(my_sum(3, 5))  # 两数相加
print(my_sum([1, 2], [3, 4]))  # 列表拼接
print(my_sum("hello ", "world"))  # 字符串合并

"""
8
[1, 2, 3, 4]
hello world
"""
```

当然，两个数据类型不同，是无法相加的，此时就会报错。

Python 不用考虑输入的数据类型，而是将其交给具体的代码去判断执行，同样的一个函数（比如这边的相加函数 my_sum()），可以同时应用在整型、列表、字符串等等的操作中。

在编程语言中，我们把这种行为称为多态。这也是 Python 和其他语言，比如 Java、C 等很大的一个不同点。

当然，Python 这种方便的特性，在实际使用中也会带来诸多问题。因此，必要时请你在开头加上数据的类型检查。

Python 函数的另一大特性，是 Python 支持函数的嵌套。所谓的函数嵌套，就是指函数里面又有函数，比如：

```python
def f1():
    print('hello')
    def f2():
        print('world')
    f2()
f1()
# 输出
hello
world
```

- 函数嵌套有什么好处呢？

其实，函数的嵌套，主要有下面两个方面的作用。

第一，函数的嵌套能够保证内部函数的隐私。

内部函数只能被外部函数所调用和访问，不会暴露在全局作用域，因此，如果你的函数内部有一些隐私数据（比如数据库的用户、密码等），不想暴露在外，那你就可以使用函数的的嵌套，将其封装在内部函数中，只通过外部函数来访问。

比如：

```python
def connect_DB():
    def get_DB_configuration():
        ...
        return host, username, password
    conn = connector.connect(get_DB_configuration())
    return conn
```

这里的函数 get_DB_configuration，便是内部函数，它无法在 connect_DB() 函数以外被单独调用。

也就是说，下面这样的外部直接调用是错误的：

```python
get_DB_configuration()
# 输出
NameError: name 'get_DB_configuration' is not defined
```

第二，合理的使用函数嵌套，能够提高程序的运行效率。我们来看下面这个例子：

```python
def factorial(input):
    # validation check
    if not isinstance(input, int):
        raise Exception('input must be an integer.')
    if input < 0:
        raise Exception('input must be greater or equal to 0' )
    ...

    def inner_factorial(input):
        if input <= 1:
            return 1
        return input * inner_factorial(input-1)
    return inner_factorial(input)

print(factorial(5))
```

这里，使用递归的方式计算一个数的阶乘。因为在计算之前，需要检查输入是否合法，所以我写成了函数嵌套的形式，这样一来，输入是否合法就只用检查一次。

而如果不使用函数嵌套，那么每调用一次递归便会检查一次，这是没有必要的，也会降低程序的运行效率。

## 参数传递

在 python 中，类型属于对象，对象有不同类型的区分，变量是没有类型的：

变量没有类型，它仅仅是一个对象的引用（一个指针），可以是指向 List 类型对象，也可以是指向 String 类型对象。

### 可更改(mutable)与不可更改(immutable)对象

在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

- **不可变类型：**变量赋值 **a=5** 后再赋值 **a=10**，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a。
- **可变类型：**变量赋值 **la=[1,2,3,4]** 后再赋值 **la[2]=5** 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

python 函数的参数传递：

- **不可变类型：**类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。
- **可变类型：**类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响

python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。

## 函数变量作用域

Python 函数中变量的作用域和其他语言类似。如果变量是在函数内部定义的，就称为局部变量，只在函数内部有效。

一旦函数执行完毕，局部变量就会被回收，无法访问。

相对应的，全局变量则定义在函数体外部，此时函数内部可以直接调用。

不过，我们不能在函数内部随意改变全局变量的值。

比如，下面的写法就是错误的：

```python
MIN_VALUE = 1
def validation_check(value):
    MIN_VALUE += 1
validation_check(5)

# 报错
# UnboundLocalError: local variable 'MIN_VALUE' referenced before assignment
```

这是因为，Python 的解释器会默认函数内部的变量为局部变量，但是又发现局部变量 MIN_VALUE 并没有声明，因此就无法执行相关操作。

所以，如果我们一定要在函数内部改变全局变量的值，就必须加上 `global` 这个声明：
