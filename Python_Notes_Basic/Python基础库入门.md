# Python简介

Python 是一个高层次的结合了解释性、编译性、互动性和面向对象的脚本语言。

Python 的设计具有很强的可读性，相比其他语言经常使用英文关键字，其他语言的一些标点符号，它具有比其他语言更有特色语法结构。

- **Python 是一种解释型语言：** 这意味着开发过程中没有了编译这个环节。类似于PHP和Perl语言。
- **Python 是交互式语言：** 这意味着，您可以在一个 Python 提示符 **>>>** 后直接执行代码。
- **Python 是面向对象语言:** 这意味着Python支持面向对象的风格或代码封装在对象的编程技术。
- **Python 是初学者的语言：** Python 对初级程序员而言，是一种伟大的语言，它支持广泛的应用程序开发，从简单的文字处理到 WWW 浏览器再到游戏。

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

## 数字

Python 支持三种不同的数值类型：

- **整型(int)** - 通常被称为是整型或整数，是正或负整数，不带小数点。Python3 整型是没有限制大小的，可以当作 Long 类型使用，所以 Python3 没有 Python2 的 Long 类型。布尔(bool)是整型的子类型。
- **浮点型(float)** - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
- **复数( (complex))** - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。

我们可以使用十六进制和八进制来代表整数：

```python
>>> number = 0xA0F # 十六进制
>>> number
2575

>>> number=0o37 # 八进制
>>> number
31
```

- Python支持复数，复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。

### 数字类型转换

有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。

- **int(x)** 将x转换为一个整数。
- **float(x)** 将x转换到一个浮点数。
- **complex(x)** 将x转换到一个复数，实数部分为 x，虚数部分为 0。
- **complex(x, y)** 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。

### 数字运算

#### 数字计算表

```python
运算符  描述         示例      运算结果  
+       加法         5 + 8        13  
-       减法         90 - 80      80  
*       乘法         4 * 7        28  
/       浮点数除法   7 / 2        3.5  
//      整数除法     7 // 2       3  
%       模（求余）   7 % 3        1  
**      幂           3 ** 4       81  
```

#### 运算符

- 位运算符

以下假设变量a为60，变量b为13：

```python
a = 0011 1100

b = 0000 1101

-----------------

a&b = 0000 1100

a|b = 0011 1101

a^b = 0011 0001

~a  = 1100 0011
```

![](https://i.loli.net/2021/05/06/RGdbjl5uhk1rK3g.png)

- 赋值运算符

  `:=` 海象运算符，可在表达式内部为变量赋值。**Python3.8 版本新增运算符**

  ```python
  # 赋值表达式可以避免调用 len() 两次:
  if (n := len(a)) > 10:
      print(f"List is too long ({n} elements, expected <= 10)")
  ```

- 逻辑运算符

| 运算符 | 逻辑表达式 |                             描述                             | 实例                    |
| :----: | :--------: | :----------------------------------------------------------: | :---------------------- |
|  and   |  x and y   | 布尔"与" - **如果 x 为 False，x and y 返回 x 的值，否则返回 y 的计算值**。 | (a and b) 返回 20。     |
|   or   |   x or y   | 布尔"或" - **如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。** | (a or b) 返回 10。      |
|  not   |   not x    | 布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。 | not(a and b) 返回 False |

- 身份运算符

  身份运算符用于比较两个对象的存储单元

| 运算符 | 描述                                        | 实例                                                         |
| :----- | :------------------------------------------ | :----------------------------------------------------------- |
| is     | is 是判断两个标识符是不是引用自一个对象     | **x is y**, 类似 **id(x) == id(y)** , 如果引用的是同一个对象则返回 True，否则返回 False |
| is not | is not 是判断两个标识符是不是引用自不同对象 | **x is not y** ， 类似 **id(x) != id(y)**。如果引用的不是同一个对象则返回结果 True，否则返回 False。 |

- 运算符优先级

  以下表格列出了从最高到最低优先级的所有运算符， 相同单元格内的运算符具有相同优先级。 运算符均指二元运算，除非特别指出。 相同单元格内的运算符从左至右分组（除了幂运算是从右至左分组）：

| 运算符                                                       | 描述                               |
| :----------------------------------------------------------- | :--------------------------------- |
| `(expressions...)`,`[expressions...]`, `{key: value...}`, `{expressions...}` | 圆括号的表达式                     |
| `x[index]`, `x[index:index]`, `x(arguments...)`, `x.attribute` | 读取，切片，调用，属性引用         |
| await x                                                      | await 表达式                       |
| `**`                                                         | 乘方(指数)                         |
| `+x`, `-x`, `~x`                                             | 正，负，按位非 NOT                 |
| `*`, `@`, `/`, `//`, `%`                                     | 乘，矩阵乘，除，整除，取余         |
| `+`, `-`                                                     | 加和减                             |
| `<<`, `>>`                                                   | 移位                               |
| `&`                                                          | 按位与 AND                         |
| `^`                                                          | 按位异或 XOR                       |
| `|`                                                          | 按位或 OR                          |
| `in,not in, is,is not, <, <=, >, >=, !=, ==`                 | 比较运算，包括成员检测和标识号检测 |
| `not x`                                                      | 逻辑非 NOT                         |
| `and`                                                        | 逻辑与 AND                         |
| `or`                                                         | 逻辑或 OR                          |
| `if -- else`                                                 | 条件表达式                         |
| `lambda`                                                     | lambda 表达式                      |
| `:=`                                                         | 赋值表达式                         |

and 拥有更高优先级:

```python
x = True
y = False
z = False
 
if x or y and z:
    print("yes")
else:
    print("no")
    
# 输出： yes
```

以上实例先计算 **y and z** 并返回 False ，然后 **x or False** 返回 True，输出结果：

#### 注意事项

- 不同类型的数混合运算时会将整数转换为浮点数：

```python
>>> 3 * 3.75 / 1.5
7.5
>>> 7.0 / 2
3.5
```

- 在交互模式中，最后被输出的表达式结果被赋值给变量 **_** 。例如：

```python
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
```

此处， **_** 变量应被用户视为只读变量。

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

### List 技巧和应用

1. **一行代码生成列表**

```python
arr = [[0] * w for _ in range(h)]
```

常见错误：

```python
# 以下方式是复制了当前数组的引用
arr = [[1, 5]] * 3
print(arr)		# [[1, 5], [1, 5], [1, 5]]
arr[0][0] = 9
print(arr)		# [[9, 5], [9, 5], [9, 5]]
```

2. **两个列表排序**

```python
l1 = [1, 2, 3, 4]
l2 = ['c', 'a', 'b', 'd']

l = list(zip(l1, l2))
l.sort(key=lambda x:x[1])
print(l)		# [(2, 'a'), (3, 'b'), (1, 'c'), (4, 'd')]

# 还原
tmp = list(zip(*l))
l1 = list(tmp[0])
l2 = list(tmp[1])
print(l1)		# [2, 3, 1, 4]
print(l2)		# ['a', 'b', 'c', 'd']
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

### Dict 技巧和应用

1. **字典推导式**

```python
d = {k: k for k in range(3)}
print(d)  # {0: 0, 1: 1, 2: 2}
```

### Set 函数一览

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

### Set 技巧和应用

1. **集合推导式**

```python
s1 = {x for x in 'abracadabra' if x not in 'abc'}
s1	# {'d', 'r'}
```

2. **集合运算**

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

```python
d = {'2': 'FmThic:@2', '1': 'layer_1_thickness(A)'}

d_sorted_by_key = sorted(d.items(), key=lambda x: x[0]) # 根据字典键的升序排序
d_sorted_by_value = sorted(d.items(), key=lambda x: x[1]) # 根据字典值的升序排序

# 默认是键
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

#### str.isdigit()、s.isdecimal()、str.isnumeric()

**str.isdigit()** 检测字符串是否只包含数字（即不接受其他一切非 **[0-9]** 元素）。

**s.isdigit、isdecimal 和 s.isnumeric 区别**

**isdigit()**

**True**: Unicode数字，byte数字（单字节），全角数字（双字节）

**False**: 汉字数字，罗马数字，小数

**Error**: 无

**isdecimal()**

判断十进制数字

**True**: Unicode数字，全角数字（双字节）

**False**: 罗马数字，汉字数字，小数

**Error**: byte数字（单字节）

**isnumeric()**

**True**: Unicode 数字，全角数字（双字节），汉字数字

**False**: 小数，罗马数字

**Error**: byte数字（单字节）

```python
num = "1"  #unicode
print(num.isdigit())   # True
print(num.isdecimal()) # True
print(num.isnumeric()) # True

num = "1" # 全角
print(num.isdigit())   # True
print(num.isdecimal()) # True
print(num.isnumeric()) # True

num = b"1" # byte
print(num.isdigit())   # True
print(num.isdecimal()) # AttributeError 'bytes' object has no attribute 'isdecimal'
print(num.isnumeric()) # AttributeError 'bytes' object has no attribute 'isnumeric'

num = "IV" # 罗马数字
print(num.isdigit())   # False
print(num.isdecimal()) # False
print(num.isnumeric()) # False

num = "四" # 汉字
print(num.isdigit())   # False
print(num.isdecimal()) # False
print(num.isnumeric()) # True
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

- **科学计数法的转换**

  ```python
  x = 1e22
  y1 = "{:G}".format(x)	# 1E22
  y2 = "%G" % x			# 1E22
  ```

#### f字符串

算是python3最常用的字符串了吧，语法：`f'{变量}'`

### 通配符匹配

- `fnmatch` 模块

```python
from fnmatch import fnmatch, fnmatchcase
print(fnmatch('hello.py', '*.py'))      # True
print(fnmatch('hello.py', '?ello.py'))  # True
print(fnmatch('nginx-access-20180609.log', 'nginx-access-2018060[0-9]*'))	# True
```

​		但是有一个问题fnmatch()函数在不同底层操作系统下使用的时候对大小写敏感, 不同的系统表现情况不同，如下所示:

```python
from fnmatch import fnmatch, fnmatchcase

# On OS X (Mac)
print(fnmatch('test.txt', '*.TXT'))		# False

# On Windows
print(fnmatch('test.txt', '*.TXT'))		# True
```

​		fnmatchcase() 会严格按照大小写来匹配

```python
from fnmatch import fnmatch, fnmatchcase

# On OS X (Mac)
print(fnmatchcase('test.txt', '*.TXT'))		# False

# On Windows
print(fnmatchcase('test.txt', '*.TXT'))		# False
```

- `glob` 模块

  如果代码需要做文件名的匹配，最好使用glob模块

```python
# 假设文件列表为： file1.py  file2.py  file3.py  file4.py

import glob
pyfiles = glob.glob('/opt/*.py')
print(pyfiles)		# ['/opt/file1.py', '/opt/file2.py', '/opt/file3.py', '/opt/file4.py']
```

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

#### pickle 对类的处理 

```python
import pickle
class JxTool:
    def __init__(self):
        self.name = 'jacob'
    
    def test(self):
        print("hello, world!")

obj_a = JxTool()
obj_a.test()
output = open('./tmp/obj.pkl', 'wb')
pickle.dump(obj_a, output)
output.close()

# read pkl
pkl_file = open('./tmp/obj.pkl', 'rb')
data = pickle.load(pkl_file)
pkl_file.close()

print(data.name)
print(type(data))

'''
hello, world!
jacob
<class '__main__.JxTool'>
'''
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

## 参数

在 python 中，类型属于对象，对象有不同类型的区分，变量是没有类型的：

变量没有类型，它仅仅是一个对象的引用（一个指针），可以是指向 List 类型对象，也可以是指向 String 类型对象。

### 参数传递

#### 可更改(mutable)与不可更改(immutable)对象

在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

- **不可变类型：**变量赋值 **a=5** 后再赋值 **a=10**，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a。
- **可变类型：**变量赋值 **la=[1,2,3,4]** 后再赋值 **la[2]=5** 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

python 函数的参数传递：

- **不可变类型：**类似 C++ 的值传递，如整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a) 内部修改 a 的值，则是新生成一个 a 的对象。
- **可变类型：**类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响

python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说 `传不可变对象` 和 `传可变对象` 。

### 参数类型

以下是调用函数时可使用的正式参数类型：

- 必需参数
- 关键字参数
- 默认参数
- 不定长参数

#### 必需参数

**必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。**

#### 关键字参数

关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。

使用**关键字参数允许函数调用时参数的顺序与声明时不一致**，因为 Python 解释器能够用参数名匹配参数值。

```python
# 形如：
def func(name, age):
    ···

func(age=18, name='jacob')
```

#### 默认参数

调用函数时，如果没有传递参数，则会使用默认参数。

```python
def func(name, age=35):
    ···

func(name='jacob')
```

#### 不定长参数

你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名。基本语法如下：

```python
def functionname([formal_args,] *var_args_tuple ):
   "函数_文档字符串"
   function_suite
   return [expression]
```

- 单星号参数

**加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。**

```python
# 可写函数说明
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vartuple)
 
# 调用printinfo 函数
printinfo( 70, 60, 50 )

'''
输出: 
70
(60, 50)
'''
```

如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。如下实例：

```python
# 可写函数说明
def printinfo( arg1, *vartuple ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   for var in vartuple:
      print (var)
   return
 
# 调用printinfo 函数
printinfo( 10 )
printinfo( 70, 60, 50 )

'''
输出:
10
输出:
70
60
50
'''
```

- 双星号参数

```python
# 可写函数说明
def printinfo( arg1, **vardict ):
   "打印任何传入的参数"
   print ("输出: ")
   print (arg1)
   print (vardict)
 
# 调用printinfo 函数
printinfo(1, a=2,b=3)

'''
输出: 
1
{'a': 2, 'b': 3}
'''
```

#### 强制关键字传入

声明函数时，参数中星号 ***** 可以单独出现，例如:

```python
def f(a,b,*,c):
    return a+b+c
```

如果单独出现星号 *****，则星号 ***** 后的参数必须用关键字传入：

```python
# *号参数后必须使用关键字传入

def func(a, b, *, c):
    return a+b+c

def func2(*, a, b, c):
    return a+b+c

print(func(1, 2, c=3))		# 6

# print(func2(1, 2, c=3))
# TypeError: func2() takes 0 positional arguments but 2 positional arguments (and 1 keyword-only argument) were given

print(func2(a=1, b=2, c=3))	# 6
```

#### 强制位置参数

Python3.8 新增了一个函数形参语法 `/` 用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式。

在以下的例子中，形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或关键字形参，而 e 和 f 要求为关键字形参:

```python
def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
```

以下使用方法是正确的:

```python
f(10, 20, 30, d=40, e=50, f=60)
```

以下使用方法会发生错误:

```python
f(10, b=20, c=30, d=40, e=50, f=60)   # b 不能使用关键字参数的形式
f(10, 20, 30, 40, 50, f=60)           # e 必须使用关键字参数的形式
```

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

```python
MIN_VALUE = 1
def validation_check(value):
    global MIN_VALUE
    MIN_VALUE += 1
validation_check(5)
```

这里的 `global` 关键字，并不表示重新创建了一个全局变量 MIN_VALUE，而是告诉 Python 解释器，函数内部的变量 MIN_VALUE，就是之前定义的全局变量，并不是新的全局变量，也不是局部变量。

这样，程序就可以在函数内部访问全局变量，并修改它的值了。

另外，如果遇到函数内部局部变量和全局变量同名的情况，那么在函数内部，局部变量会覆盖全局变量，比如下面这种：

```python
MIN_VALUE = 1
def validation_check(value):
    MIN_VALUE = 3
    print(MIN_VALUE)
validation_check(5)		# 3
```

类似的，对于嵌套函数来说，内部函数可以访问外部函数定义的变量，但是无法修改，若要修改，必须加上 `nonlocal` 这个关键字：

```python
def outer():
    x = "local"
    def inner():
        nonlocal x # nonlocal 关键字表示这里的 x 就是外部函数 outer 定义的变量 x
        x = 'nonlocal'
        print("inner:", x)
    inner()
    print("outer:", x)
    
outer()
'''
inner: nonlocal
outer: nonlocal
'''

# 如果不加上 nonlocal 这个关键字，而内部函数的变量又和外部函数变量同名，那么同样的，内部函数变量会覆盖外部函数的变量。
'''
inner: nonlocal
outer: local
'''
```

## 闭包

闭包（closure）其实和刚刚讲的嵌套函数类似，不同的是，这里外部函数返回的是一个函数，而不是一个具体的值。

返回的函数通常赋于一个变量，这个变量可以在后面被继续执行调用。

比如，我们想计算一个数的 n 次幂，用闭包可以写成下面的代码：

```python
def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent
    return exponent_of # 返回值是 exponent_of 函数

square = nth_power(2) # 计算一个数的平方
cube = nth_power(3) # 计算一个数的立方

print(square)
print(cube)

print(square(2))  # 计算2的平方
print(cube(2))  # 计算2的立方

'''
<function nth_power.<locals>.exponent_of at 0x000001DC2FD330D0>
<function nth_power.<locals>.exponent_of at 0x000001DC2FD33280>
4
8
'''
```

这里外部函数 nth_power() 返回值，是函数 exponent_of()，而不是一个具体的数值。

需要注意的是，在执行完square = nth_power(2)和cube = nth_power(3)后，外部函数 nth_power() 的参数 exponent，仍然会被内部函数 exponent_of() 记住。

这样，之后我们调用 square(2) 或者 cube(2) 时，程序就能顺利地输出结果，而不会报错说参数 exponent 没有定义了。

看到这里，你也许会思考，为什么要闭包呢？上面的程序，我也可以写成下面的形式啊！

```python
def nth_power_rewrite(base, exponent):
    return base ** exponent
```

确实可以，不过，要知道，**使用闭包的一个原因，是让程序变得更简洁易读。**

设想一下，比如你需要计算很多个数的平方，那么你觉得写成下面哪一种形式更好呢？

```python
# 不适用闭包
res1 = nth_power_rewrite(base1, 2)
res2 = nth_power_rewrite(base2, 2)
res3 = nth_power_rewrite(base3, 2)
...
# 使用闭包
square = nth_power(2)
res1 = square(base1)
res2 = square(base2)
res3 = square(base3)
...
```

显然是第二种，是不是？首先直观来看，第二种形式，让你每次调用函数都可以少输入一个参数，表达更为简洁。

其次，和上面讲到的嵌套函数优点类似，函数开头需要做一些额外工作，而你又需要多次调用这个函数时，将那些额外工作的代码放在外部函数，就可以减少多次调用导致的不必要的开销，提高程序的运行效率。

另外还有一点，后面再讲，闭包常常和装饰器（decorator）一起使用。

## 总结

1. Python 中函数的参数可以接受任意的数据类型，使用起来需要注意，必要时请在函数开头加入数据类型的检查；
2. 和其他语言不同，Python 中函数的参数可以设定默认值；
3. 嵌套函数的使用，能保证数据的隐私性，提高程序运行效率；
4. 合理地使用闭包，则可以简化程序的复杂度，提高可读性。

# 匿名函数

不过，除了常规函数，你应该也会在代码中见到一些“非常规”函数，它们往往很简短，就一行，并且有个很酷炫的名字——`lambda`，没错，这就是匿名函数。

匿名函数在实际工作中同样举足轻重，正确地运用匿名函数，能让我们的代码更简洁、易读。

- **lambda** 只是一个表达式，函数体比 **def** 简单很多。
- lambda 的主体是一个表达式，而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去。
- lambda 函数拥有自己的命名空间，且**不能访问自己参数列表之外或全局命名空间里的参数**。
- 虽然 lambda 函数看起来只能写一行，却不等同于 C 或 C++ 的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

## 匿名函数基础

```
lambda argument1, argument2,... argumentN : expression
```

我们可以看到，匿名函数的关键字是 `lambda`，之后是一系列的参数，然后用冒号隔开，最后则是由这些参数组成的表达式。我们通过几个例子看一下它的用法：

```python
square = lambda x: x**2
square(3)		# 9
```

可以看到，匿名函数 lambda 和常规函数一样，返回的都是一个函数对象（function object），它们的用法也极其相似，不过还是有下面几点区别。

- 第一，lambda 是一个表达式（expression），并不是一个语句（statement）。

  所谓的表达式，就是用一系列“公式”去表达一个东西，比如x + 2、 x**2等等；

  而所谓的语句，则一定是完成了某些功能，比如赋值语句x = 1完成了赋值，print 语句 print(x) 完成了打印，条件语句 if x < 0:完成了选择功能等等。

  因此，lambda 可以用在一些常规函数 def 不能用的地方，比如，lambda 可以用在列表内部，而常规函数却不能：

  ```python
  [(lambda x: x*x)(x) for x in range(10)]
  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
  ```

  再比如，lambda 可以被用作某些函数的参数，而常规函数 def 也不能：

  ```python
  l = [(1, 20), (3, 0), (9, 10), (2, -1)]
  l.sort(key=lambda x: x[1])  # 按列表中元祖的第二个元素排序
  print(l)
  # [(2, -1), (3, 0), (9, 10), (1, 20)]
  ```

  常规函数 def 必须通过其函数名被调用，因此必须首先被定义。但是作为一个表达式的 lambda ，返回的函数对象就不需要名字了

- 第二，lambda 的主体是只有一行的简单表达式，并不能扩展成一个多行的代码块。

  这其实是出于设计的考虑。Python 之所以发明 lambda，就是为了让它和常规函数各司其职：lambda 专注于简单的任务，而常规函数则负责更复杂的多行逻辑。

  关于这点，Python 之父 Guido van Rossum 曾发了一篇文章解释，有兴趣的话可以自己阅读。

## 为什么要使用匿名函数？

理论上来说，Python 中有匿名函数的地方，都可以被替换成等价的其他表达形式。

一个Python 程序是可以不用任何匿名函数的。

不过，在一些情况下，使用匿名函数 lambda，可以帮助我们大大简化代码的复杂度，提高代码的可读性。

通常，我们用函数的目的无非是这么几点：

1. 减少代码的重复性；
2. 模块化代码。

对于第一点，如果你的程序在不同地方包含了相同的代码，那么我们就会把这部分相同的代码写成一个函数，并为它取一个名字，方便在相对应的不同地方调用。

对于第二点，如果你的一块儿代码是为了实现一个功能，但内容非常多，写在一起降低了代码的可读性，那么通常我们也会把这部分代码单独写成一个函数，然后加以调用。

不过，再试想一下这样的情况。你需要一个函数，但它非常简短，只需要一行就能完成；同时它在程序中只被调用一次而已。

那么请问，你还需要像常规函数一样，给它一个定义和名字吗？

答案当然是否定的。这种情况下，函数就可以是匿名的，你只需要在适当的地方定义并使用，就能让匿名函数发挥作用了。

举个例子，如果你想对一个列表中的所有元素做平方操作，而这个操作在你的程序中只需要进行一次，用 lambda 函数可以表示成下面这样：

```python
# lambda
s = map(lambda x: x**2, [1, 2, 3, 4, 5])
print(*s)
# 1 4 9 16 25
```

```python
def square(x):
    return x**2
s = map(square, [1, 2, 3, 4, 5])
print(*s)
```

- 简单解释一下:

  函数 map(function, iterable) 的第一个参数是函数对象，第二个参数是一个可以遍历的集合，它表示对 iterable 的每一个元素，都运用 function 这个函数。

  两者一对比，我们很明显地发现，lambda 函数让代码更加简洁明了。

## Python 函数式编程

Python 的函数式编程特性，与匿名函数 lambda 有着密切的联系。

所谓函数式编程，是指代码中每一块都是不可变的（immutable），都由纯函数（pure function）的形式组成。

这里的**纯函数**，是指函数本身相互独立、互不影响，对于相同的输入，总会有相同的输出，没有任何副作用。

---

举个很简单的例子，比如对于一个列表，我想让列表中的元素值都变为原来的两倍，我们可以写成下面的形式：

```python
def multiply_2(l):
    for index in range(0, len(l)):
        l[index] *= 2
    return l
```

这段代码就不是一个纯函数的形式，因为列表中元素的值被改变了，如果我多次调用multiply_2() 这个函数，那么每次得到的结果都不一样。

要想让它成为一个纯函数的形式，就得写成下面这种形式，重新创建一个新的列表并返回。

```python
def multiply_2_pure(l):
    new_list = []
    for item in l:
        new_list.append(item * 2)
    return new_list
```

函数式编程的优点，主要在于其纯函数和不可变的特性使程序更加健壮，易于调试（debug）和测试；**缺点主要在于限制多，难写**。

当然，Python 不同于一些语言（比如Scala），它并不是一门函数式编程语言，不过，Python 也提供了一些函数式编程的特性，值得我们了解和学习。

Python 主要提供了这么几个函数：map()、filter() 和 reduce()，通常结合匿名函数 lambda 一起使用。这些都是需要掌握的东西，接下来逐一介绍。

- map(function, iterable)

  首先是 map(function, iterable) 函数，前面的例子提到过，它表示，对 iterable 中的每个元素，都运用 function 这个函数，最后返回一个新的可遍历的集合。

  比如刚才列表的例子，要对列表中的每个元素乘以 2，那么用 map 就可以表示为下面这样：

  ```python
  l = [1, 2, 3, 4, 5]
  new_list = map(lambda x: x * 2, l)  # [2， 4， 6， 8， 10]
  print(*new_list)
  ```

  我们可以以 map() 函数为例，看一下 Python 提供的函数式编程接口的性能。还是同样的列表例子，它还可以用 for 循环和 list comprehension（目前没有统一中文叫法，你也可以直译为列表理解等）实现，

  我们来比较一下它们的速度：

  ```python
  python3 -mtimeit -s'xs=range(1000000)' 'map(lambda x: x*2, xs)'
  2000000 loops, best of 5: 171 nsec per loop
  python3 -mtimeit -s'xs=range(1000000)' '[x * 2 for x in xs]'
  5 loops, best of 5: 62.9 msec per loop
  python3 -mtimeit -s'xs=range(1000000)' 'l = []' 'for i in xs: l.append(i * 2)'
  5 loops, best of 5: 92.7 msec per loop
  ```

  你可以看到，map() 是最快的。因为 map() 函数直接由 C 语言写的，运行时不需要通过 Python 解释器间接调用，并且内部做了诸多优化，所以运行速度最快。

- filter(function, iterable)

  接下来来看 filter(function, iterable) 函数，它和 map 函数类似，function 同样表示一个函数对象。

  filter() 函数表示对 iterable 中的每个元素，都使用 function 判断，并返回True 或者 False，最后将返回 True 的元素组成一个新的可遍历的集合。

  举个例子，比如我要返回一个列表中的所有偶数，可以写成下面这样：

  ```python
  l = [1, 2, 3, 4, 5]
  new_list = filter(lambda x: x % 2 == 0, l)  # [2, 4]
  print(*new_list)
  ```

- reduce(function, iterable)

  reduce() 函数在 python2 中是内置函数，在 python3 中放到了 functools 模块下

  它通常用来对一个集合做一些累积操作，function 同样是一个函数对象，规定它有两个参数，表示对 iterable 中的每个元素以及上一次调用后的结果，运用 function 进行计算，所以最后返回的是一个单独的数值。

  举个例子，我想要计算某个列表元素的乘积，就可以用 reduce() 函数来表示：

  ```python
  from functools import reduce
  l = [1, 2, 3, 4, 5]
  product = reduce(lambda x, y: x * y, l) # 1*2*3*4*5 = 120
  print(product)
  ```

当然，类似的，filter() 和 reduce() 的功能，也可以用 for 循环或者 list comprehension 来实现。

通常来说，在我们想对集合中的元素进行一些操作时，如果操作非常简单，比如相加、累积这种，那么我们优先考虑 map()、filter()、reduce() 这类或者 list comprehension 的形式。

至于这两种方式的选择：

在数据量非常多的情况下，比如机器学习的应用，那我们一般更倾向于函数式编程的表示，因为效率更高；

在数据量不多的情况下，并且你想要程序更加 Pythonic 的话，那么 list comprehension 也不失为一个好选择。

不过，如果你要对集合中的元素，做一些比较复杂的操作，那么，考虑到代码的可读性，我们通常会使用 for 循环，这样更加清晰明了。

  ## 应用

### 字典排序

对一个字典，根据值进行由高到低的排序，该怎么做呢？

```python
d = {'mike': 10, 'lucy': 2, 'ben': 30}
sorted(d.items(), key=lambda x:x[1], reverse=True)
# [('ben', 30), ('mike', 10), ('lucy', 2)]
```

# 面向对象

## 什么是对象

```python
class Document():
    def __init__(self, title, author, context):
        print('init function called')
        self.title = title
        self.author = author
        self.__context = context # __ 开头的属性是私有属性
    def get_context_length(self):
        return len(self.__context)
    def intercept_context(self, length):
        self.__context = self.__context[:length]
        
harry_potter_book = Document('Harry Potter', 'J. K. Rowling', '... Forever Do not believe')
# init function called

print(harry_potter_book.title)		# Harry Potter
print(harry_potter_book.author)		# J. K. Rowling
print(harry_potter_book.get_context_length())	# 26


harry_potter_book.intercept_context(10)		
print(harry_potter_book.get_context_length())	# 10
# print(harry_potter_book.__context)
# AttributeError: 'Document' object has no attribute '__context'
```

类：一群有着相似性的事物的集合，这里对应 Python 的 class。

对象：集合中的一个事物，这里对应由 class 生成的某一个 object，比如代码中的harry_potter_book。

属性：对象的某个静态特征，比如上述代码中的 title、author 和 __context。

函数：对象的某个动态能力，比如上述代码中的 intercept_context () 函数。

当然，这样的说法既不严谨，也不充分，但如果你对面向对象编程完全不了解，它们可以让你迅速有一个直观的了解。

- 类，一群有着相同属性和函数的对象的集合。

这里唯一需要强调的一点是，如果一个属性以 __ `（注意，此处有两个 _）` 开头，我们就默认这个属性是私有属性。

私有属性，是指不希望在类的函数之外的地方被访问和修改的属性。

所以，你可以看到，title 和 author 能够很自由地被打印出来，但是`print(harry_potter_book.__context)`就会报错。

## 对象的进阶应用

### 类常量 和 静态函数

- **如何在一个类中定义一些常量，每个对象都可以方便访问这些常量而不用重新构造？**

一种很常规的做法，是用全大写来表示常量，因此我们可以在类中使用 `self.WELCOME_STR` ，或者在类外使用 `Entity.WELCOME_STR` ，来表达这个字符串。

- **如果一个函数不涉及到访问修改这个类的属性，而放到类外面有点不恰当，怎么做才能更优雅呢？**

而静态函数则与类没有什么关联，最明显的特征便是，静态函数的第一个参数没有任何特殊性。

一般而言，静态函数可以用来做一些简单独立的任务，既方便测试，也能优化代码结构。静态函数还可以通过在函数前一行加上 `@staticmethod` 来表示，代码中也有相应的示例。这其实使用了装饰器的概念，我们会在后面的章节中详细讲解。

```python
class ObjectTest():
    CONST_STR = "这是一个类的常量"
    
    @staticmethod
    def print_text():
        print("hello world")
    
    # 成员函数可以正常用 self.function() 调用 静态函数 和 常量
    def test1(self):
        self.print_text()
        print(self.CONST_STR)
    
    # 静态函数没有 self 函数，只能靠 类对象 来调用 类的 静态函数 和 常量
    @staticmethod
    def test2():
        ObjectTest.print_text()
        print(ObjectTest.CONST_STR)
```

### 成员函数 和 类函数

类函数的第一个参数一般为 cls，表示必须传一个类进来。

类函数最常用的功能是实现不同的 `init` 构造函数，比如下文代码中，我们使用 create_empty_book 类函数，来创造新的书籍对象，其 context 一定为 'nothing'。这样的代码，就比你直接构造要清晰一些。类似的，类函数需要装饰器 `@classmethod` 来声明。

成员函数则是我们最正常的类的函数，它不需要任何装饰器声明，第一个参数 `self` 代表当前对象的引用，可以通过此函数，来实现想要的查询 / 修改类的属性等功能。

```python
class Document():
    WELCOME_STR = 'Welcome! The context for this book is {}.'
    def __init__(self, title, author, context):
        print('init function called')
        self.title = title
        self.author = author
        self.__context = context
    # 类函数
    @classmethod
    def create_empty_book(cls, title, author):
        return cls(title=title, author=author, context='nothing')
    
    # 成员函数
    def get_context_length(self):
        return len(self.__context)
    
    # 静态函数
    @staticmethod
    def get_welcome(context):
        return Document.WELCOME_STR.format(context)

empty_book = Document.create_empty_book('What Every Man Thinks About Apart from Sex', 'Potter')
# init function called
print(empty_book.get_context_length())		# 7
print(empty_book.get_welcome('indeed nothing'))		
# Welcome! The context for this book is indeed nothing.
```



### 类的继承

- **既然类是一群相似的对象的集合，那么可不可以是一群相似的类的集合呢？**

类的继承，顾名思义，指的是一个类既拥有另一个类的特征，也拥有不同于另一个类的独特特征。在这里的第一个类叫做子类，另一个叫做父类，特征其实就是类的属性和函数。

```python
class Entity():
    def __init__(self, object_type):
        print('parent class init called')
        self.object_type = object_type
        self.title = None
        
    def get_context_length(self):
        raise Exception('get_context_length not implemented')
        
    def print_title(self):
        print(self.title)

class Document(Entity):
    def __init__(self, title, author, context):
        print('Document class init called')
        Entity.__init__(self, 'document')
        self.title = title
        self.author = author
        self.__context = context
        
    def get_context_length(self):
        return len(self.__context)
    
class Video(Entity):
    def __init__(self, title, author, video_length):
        print('Video class init called')
        Entity.__init__(self, 'video')
        self.title = title
        self.author = author
        self.__video_length = video_length
        
    def get_context_length(self):
        return self.__video_length
    
harry_potter_book = Document('Harry Potter(Book)', 'J. K. Rowling', '... Forever Do not ...')
# Document class init called
# parent class init called
harry_potter_movie = Video('Harry Potter(Movie)', 'J. K. Rowling', 120)
# Video class init called
# parent class init called
print(harry_potter_book.object_type)	# document
print(harry_potter_movie.object_type)	# video

harry_potter_book.print_title()		# Harry Potter(Book)
harry_potter_movie.print_title()	# Harry Potter(Movie)

print(harry_potter_book.get_context_length())	# 22
print(harry_potter_movie.get_context_length())	# 120
```

首先需要注意的是构造函数。每个类都有构造函数，继承类在生成对象的时候，是不会自动调用父类的构造函数的，因此你必须在 `__init__()` 函数中显式调用父类的构造函数。它们的执行顺序是 子类的构造函数 -> 父类的构造函数。

```python
class father():
    def __init__(self, obj):
        self.obj = obj
        print(self.obj)


class son(father):
    def __init__(self, name):
        father.__init__(self, f"{name}'s father")
        self.name = name
        print(self.name)
        
Jx = son('Jx')	
'''
Jx's father
Jx
'''
```

### 抽象类

抽象类生来就是父类，创建对象就会报错，抽象函数必须重写

```python
from abc import ABCMeta, abstractclassmethod
class Entity(metaclass=ABCMeta):
    @abstractclassmethod
    def get_title(self):
        pass
    
    @abstractclassmethod
    def set_title(self, title):
        pass
    
class Document(Entity):
    def get_title(self):
        return self.title
    
    def set_title(self, title):
        self.title = title

document = Document()
document.set_title('Harry Potter')
print(document.get_title())		# Harry Potter
# entity = Entity()  # 就会报错
```

Entity 本身是没有什么用的，只需拿来定义 Document 和 Video 的一些基本元素就够了。不过，万一你不小心生成 Entity 的对象该怎么办呢？为了防止这样的手误，必须要介绍一下抽象类。

抽象类是一种特殊的类，它生下来就是作为父类存在的，一旦对象化就会报错。同样，抽象函数定义在抽象类之中，子类必须重写该函数才能使用。相应的抽象函数，则是使用装饰器 `@abstractmethod` 来表示。

这其实正是软件工程中一个很重要的概念，定义接口。大型工程往往需要很多人合作开发，比如在 Facebook 中，在 idea 提出之后，开发组和产品组首先会召开产品设计会，PM（Product Manager，产品经理） 写出产品需求文档，然后迭代；TL（TeamLeader，项目经理）编写开发文档，开发文档中会定义不同模块的大致功能和接口、每个模块之间如何协作、单元测试和集成测试、线上灰度测试、监测和日志等等一系列开发流程。

抽象类就是这么一种存在，它是一种自上而下的设计风范，你只需要用少量的代码描述清楚要做的事情，定义好接口，然后就可以交给不同开发人员去开发和对接。

## 面向对象案例

### 如何实现一个搜索引擎？

#### “高大上”的搜索引擎

引擎一词尤如其名，听起来非常酷炫。搜索引擎，则是新世纪初期互联网发展最重要的入口
之一，依托搜索引擎，中国和美国分别诞生了百度、谷歌等巨型公司。

搜索引擎极大地方便了互联网生活，也成为上网必不可少的刚需工具。依托搜索引擎发展起
来的互联网广告，则成了硅谷和中国巨头的核心商业模式；而搜索本身，也在持续进步着，
Facebook 和微信也一直有意向在自家社交产品架设搜索平台。

关于搜索引擎的价值我不必多说了，今天我们主要来看一下搜索引擎的核心构成。

听 Google 的朋友说，他们入职培训的时候，有一门课程叫做 The life of a query，内容
是讲用户在浏览器中键入一串文字，按下回车后发生了什么。今天我也按照这个思路，来简
单介绍下。

我们知道，**一个搜索引擎由搜索器、索引器、检索器和用户接口四个部分组成。**

搜索器，通俗来讲就是我们常提到的 `爬虫（scrawler）`，它能在互联网上大量爬取各类网站
的内容，送给索引器。索引器拿到网页和内容后，会对内容进行处理，形成索引（index），存储于内部的数据库等待检索。

最后的用户接口很好理解，是指网页和 App 前端界面，例如百度和谷歌的搜索页面。用户
通过用户接口，向搜索引擎发出询问（query），询问解析后送达检索器；检索器高效检索
后，再将结果返回给用户。

爬虫知识不是我们今天学习的重点，这里我就不做深入介绍了。我们假设搜索样本存在于本
地磁盘上。

为了方便，我们只提供五个文件的检索，内容我放在了下面这段代码中：

```python
# 1.txt
txt1 = I have a dream that my four litle children will one day live in a nation ...

# 2.txt
txt2 = I have a dream that one day in Alabama, with its vicious racists ...

# 3.txt
txt3 = I have a dream that one day every valley shall be exalted ...

# 4.txt
txt4 = This is our hope ... with this faith we will be able to hew out of mountain

# 5.txt
txt5 = And when this happens, and when we allow freedom ring, when we let it ring from ...
```

#### 先定义一个基类

首先先定义 `SearchEngineBase` 基类，这里先给出具体代码：

```python
class SearchEngineBase(object):
    def __init__(self):
        pass
    
    def add_corpus(self, file_path):
        with open(file_path, 'r') as fin:
            text = fin.read()
        self.process_corpus(file_path, text)
    
    def process_corpus(self, id, text):
        raise Exception('process_corpus not implement.')
        
    def search(self, query):
        raise Exception('search not implemented.')
    
def main(search_engine):
    for file_path in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']:
        search_engine.add_corpus("tmp\\search_txt\\" + file_path)
    while True:
        query = input()
        results = search_engine.search(query)
        print('found {} result(s):'.format(len(results)))
        for result in results:
            print(result)
```

SearchEngineBase 可以被继承，继承的类分别代表不同的算法引擎。每一个引擎都应该实现 `process_corpus()` 和 `search()` 两个函数，对应我们刚刚提到的索引器和检索器。main()函数提供搜索器和用户接口，于是一个简单的包装界面就有了。

`add_corpus()` 函数负责读取文件内容，将文件路径作为 ID，连同内容一起送到`process_corpus` 中。

`process_corpus` 需要对内容进行处理，然后文件路径为 ID ，将处理后的内容存下来。处理后的内容，就叫做索引（index）。

`search` 则给定一个询问，处理询问，再通过索引检索，然后返回。

#### 最基本的搜索引擎

```python
class SimpleEngine(SearchEngineBase):
    def __init__(self):
        super(SimpleEngine, self).__init__()
        self.__id_to_texts = {}
    
    def process_corpus(self, id, text):
        self.__id_to_texts[id] = text
    
    def search(self, query):
        results = []
        for id, text in self.__id_to_texts.items():
            if query in text:
                results.append(id)
        return results

search_engine = SimpleEngine()
main(search_engine)

"""
simple
found 0 result(s):
dream
found 3 result(s):
tmp\search_txt\1.txt
tmp\search_txt\2.txt
tmp\search_txt\3.txt
"""
```

SimpleEngine 实现了一个继承 SearchEngineBase 的子类，继承并实现了process_corpus 和 search 接口，同时，也顺手继承了 add_corpus 函数（当然你想重写也是可行的），因此我们可以在 main() 函数中直接调取。

在我们新的构造函数中，self.__id_to_texts = {} 初始化了自己的私有变量，也就是这个用来存储文件名到文件内容的字典。

process_corpus() 函数则非常直白地将文件内容插入到字典中。这里注意，ID 需要是唯一的，不然相同 ID 的新内容会覆盖掉旧的内容。

search 直接枚举字典，从中找到要搜索的字符串。如果能够找到，则将 ID 放到结果列表中，最后返回。

这种实现方式简单，但显然是一种很低效的方式：每次索引后需要占用大量空间，因为索引函数并没有做任何事情；每次检索需要占用大量时间，因为所有索引库的文件都要被重新搜索一遍。如果把语料的信息量视为 n，那么这里的时间复杂度和空间复杂度都应该是 O(n) 级别的。

而且，还有一个问题：这里的 query 只能是一个词，或者是连起来的几个词。如果你想要搜索多个词，它们又分散在文章的不同位置，我们的简单引擎就无能为力了。

#### Bag of Words 和 Inverted Index

- **Bag of Words**

优化最基本的搜索引擎。

最直接的一个想法，就是把语料分词，看成一个个的词汇，这样就只需要对每篇文章存储它所有词汇的 set 即可。根据齐夫定律（Zipf’s law，https://en.wikipedia.org/wiki/Zipf%27s_law），在自然语言的语料库里，一个单词出现的频率与它在频率表里的排名成反比，呈现幂律分布。因此，语料分词的做法可以大大提升我们的存储和搜索效率。

```python
import re

class SearchEngineBase(object):
    def __init__(self):
        pass
    
    def add_corpus(self, file_path):
        with open(file_path, 'r') as fin:
            text = fin.read()
        self.process_corpus(file_path, text)
    
    def process_corpus(self, id, text):
        raise Exception('process_corpus not implement.')
        
    def search(self, query):
        raise Exception('search not implemented.')
    
    
def main(search_engine):
    for file_path in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']:
        search_engine.add_corpus("tmp\\search_txt\\" + file_path)
    while True:
        query = input()
        results = search_engine.search(query)
        print('found {} result(s):'.format(len(results)))
        for result in results:
            print(result)


class BOWEngine(SearchEngineBase):
    def __init__(self):
        super(BOWEngine, self).__init__()
        self.__id_to_word = {}
        
    def process_corpus(self, id, text):
        self.__id_to_word[id] = self.parse_text_to_words(text)
    
    def search(self, query):
        query_words = self.parse_text_to_words(query)
        results = []
        for id, words in self.__id_to_word.items():
            if self.query_match(query_words, words):
                results.append(id)
        return results
    
    @staticmethod
    def query_match(query_words, words):
        for query_word in query_words:
            if query_word not in words:
                return False
        return True
    
    @staticmethod
    def parse_text_to_words(text):
        # 使用正则表达式去除标点符号和换行符
        text = re.sub(r'[^\w]', ' ', text)
        # 转为小写
        text = text.lower()
        # 生成所有单词的列表
        word_list = text.split(' ')
        # 去除空白单词
        word_list = filter(None, word_list)
        # 返回单词的 set
        return set(word_list)

    
search_engine = BOWEngine()
main(search_engine)

"""
simple
found 0 result(s):
dream
found 3 result(s):
tmp\search_txt\1.txt
tmp\search_txt\2.txt
tmp\search_txt\3.txt
"""
```

这里我们先来理解一个概念，**BOW Model**，即 `Bag of Words Model`，中文叫做词袋模
型。这是 NLP 领域最常见最简单的模型之一。

假设一个文本，不考虑语法、句法、段落，也不考虑词汇出现的顺序，只将这个文本看成这些词汇的集合。于是相应的，我们把 id_to_texts 替换成 id_to_words，这样就只需要存这些单词，而不是全部文章，也不需要考虑顺序。

其中，process_corpus() 函数调用类静态函数 parse_text_to_words，将文章打碎形成词袋，放入 set 之后再放到字典中。

search() 函数则稍微复杂一些。这里我们假设，想得到的结果，是所有的搜索关键词都要出现在同一篇文章中。那么，我们需要同样打碎 query 得到一个 set，然后把 set 中的每一个词，和我们的索引中每一篇文章进行核对，看一下要找的词是否在其中。而这个过程由静态函数  query_match 负责。

- **Inverted Index**

可是，即使这样做，每次查询时依然需要遍历所有 ID，虽然比起 Simple 模型已经节约了大量时间，但是互联网上有上亿个页面，每次都全部遍历的代价还是太大了。到这时，又该如何优化呢？

我们每次查询的 query 的单词量不会很多，一般也就几个、最多十几个的样子。那可不可以从这里下手呢？

再有，词袋模型并不考虑单词间的顺序，但有些人希望单词按顺序出现，或者希望搜索的单词在文中离得近一些，这种情况下词袋模型现任就无能为力了。

针对这两点，其实可以继续优化：

```python
import re

class SearchEngineBase(object):
    def __init__(self):
        pass
    
    def add_corpus(self, file_path):
        with open(file_path, 'r') as fin:
            text = fin.read()
        self.process_corpus(file_path, text)
    
    def process_corpus(self, id, text):
        raise Exception('process_corpus not implement.')
        
    def search(self, query):
        raise Exception('search not implemented.')
    
def main(search_engine):
    for file_path in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']:
        search_engine.add_corpus("tmp\\search_txt\\" + file_path)
    while True:
        query = input()
        results = search_engine.search(query)
        print('found {} result(s):'.format(len(results)))
        for result in results:
            print(result)

class BOWInvertedIndexEngine(SearchEngineBase):
    def __init__(self):
        super(BOWInvertedIndexEngine, self).__init__()
        self.inverted_index = {}
        
    def process_corpus(self, id, text):
        words = self.parse_text_to_words(text)  # word 集合
        for word in words:
            if word not in self.inverted_index:
                self.inverted_index[word] = []
            else:
                self.inverted_index[word].append(id)
    
    @staticmethod
    def parse_text_to_words(text):
        # 使用正则表达式去除标点符号和换行符
        text = re.sub(r'[^\w]', ' ', text)
        # 转为小写
        text = text.lower()
        # 生成所有单词的列表
        word_list = text.split(' ')
        # 去除空白单词
        word_list = filter(None, word_list)
        # 返回单词的 set
        return set(word_list)
        
    def search(self, query):
        query_words = list(self.parse_text_to_words(query))
        # query_words_index = []
        # for query_word in query_words:
        # query_words_index.append(0)
        query_words_index = [0] * len(query_words)
        
        # 如果某一个查询单词的倒序索引为空，我们就立刻返回
        for query_word in query_words:
            if query_word not in self.inverted_index:
                return []
        
        result = []
        while True:
            # 首先，获得当前状态下所有倒序索引的 index
            current_ids = []
            
            for idx, query_word in enumerate(query_words):
                current_index = query_words_index[idx]
                current_inverted_list = self.inverted_index[query_word]
                
                # 已经遍历到了某一个倒序索引的末尾，结束 search
                if current_index >= len(current_inverted_list):
                    return result
                
                current_ids.append(current_inverted_list[current_index])
            
            # 然后，如果 current_ids 的所有元素都一样，那么表明这个单词在这个元素对应的文档中
            if all(x == current_ids[0] for x in current_ids):
                result.append(current_ids[0])
                query_words_index = [x+1 for x in query_words_index]
                continue
            
            # 如果不是，我们就把最小的元素加一
            min_val = min(current_ids)
            min_val_pos = current_ids.index(min_val)
            query_words_index[min_val_indx] += 1
                
search_engine = BOWInvertedIndexEngine()
main(search_engine)

"""
simple
found 0 result(s):
dream
found 2 result(s):
tmp\search_txt\2.txt
tmp\search_txt\3.txt
"""
```

`Inverted Index Model`，即倒序索引，是非常有名的搜索引擎方法，倒序索引，一如其名，也就是说这次反过来，我们保留的是 word -> id 的字典。于是情况就豁然开朗了，在 search 时，我们只需要把想要的 query_word 的几个倒序索引单独拎出来，然后从这几个列表中找共有的元素，那些共有的元素，即 ID，就是我们想要的查询结果。这样，我们就避免了将所有的 index 过一遍的尴尬。

process_corpus 建立倒序索引。注意，这里的代码都是非常精简的。在工业界领域，需要一个 unique ID 生成器，来对每一篇文章标记上不同的 ID，倒序索引也应该按照这个unique_id 来进行排序。

至于 search() 函数，你大概了解它做的事情即可。它会根据 query_words 拿到所有的倒序索引，如果拿不到，就表示有的 query word 不存在于任何文章中，直接返回空；拿到之后，运行一个“合并 K 个有序数组”的算法，从中拿到我们想要的 ID，并返回。

注意，这里用到的算法并不是最优的，最优的写法需要用最小堆来存储index。

那第二个问题，如果我们想要实现搜索单词按顺序出现，或者希望搜索的单词在文中离得近一些呢？我们需要在 Inverted Index 上，对于每篇文章也保留单词的位置信息，这样一来，在合并操作的时候处理一下就可以了。

#### LRU 和 多重继承

大量重复性搜索占据了 90% 以上的流量，于是，需要给搜索引擎加一个缓存。

```python
import pylru
import re

class SearchEngineBase(object):
    def __init__(self):
        pass
    
    def add_corpus(self, file_path):
        with open(file_path, 'r') as fin:
            text = fin.read()
        self.process_corpus(file_path, text)
    
    def process_corpus(self, id, text):
        raise Exception('process_corpus not implement.')
        
    def search(self, query):
        raise Exception('search not implemented.')
    
def main(search_engine):
    for file_path in ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt']:
        search_engine.add_corpus("tmp\\search_txt\\" + file_path)
    while True:
        query = input()
        results = search_engine.search(query)
        print('found {} result(s):'.format(len(results)))
        for result in results:
            print(result)

class BOWInvertedIndexEngine(SearchEngineBase):
    def __init__(self):
        super(BOWInvertedIndexEngine, self).__init__()
        self.inverted_index = {}
        
    def process_corpus(self, id, text):
        words = self.parse_text_to_words(text)  # word 集合
        for word in words:
            if word not in self.inverted_index:
                self.inverted_index[word] = []
            else:
                self.inverted_index[word].append(id)
    
    @staticmethod
    def parse_text_to_words(text):
        # 使用正则表达式去除标点符号和换行符
        text = re.sub(r'[^\w]', ' ', text)
        # 转为小写
        text = text.lower()
        # 生成所有单词的列表
        word_list = text.split(' ')
        # 去除空白单词
        word_list = filter(None, word_list)
        # 返回单词的 set
        return set(word_list)
        
    def search(self, query):
        query_words = list(self.parse_text_to_words(query))
        # query_words_index = []
        # for query_word in query_words:
        # query_words_index.append(0)
        query_words_index = [0] * len(query_words)
        
        # 如果某一个查询单词的倒序索引为空，我们就立刻返回
        for query_word in query_words:
            if query_word not in self.inverted_index:
                return []
        
        result = []
        while True:
            # 首先，获得当前状态下所有倒序索引的 index
            current_ids = []
            
            for idx, query_word in enumerate(query_words):
                current_index = query_words_index[idx]
                current_inverted_list = self.inverted_index[query_word]
                
                # 已经遍历到了某一个倒序索引的末尾，结束 search
                if current_index >= len(current_inverted_list):
                    return result
                
                current_ids.append(current_inverted_list[current_index])
            
            # 然后，如果 current_ids 的所有元素都一样，那么表明这个单词在这个元素对应的文档中
            if all(x == current_ids[0] for x in current_ids):
                result.append(current_ids[0])
                query_words_index = [x+1 for x in query_words_index]
                continue
            
            # 如果不是，我们就把最小的元素加一
            min_val = min(current_ids)
            min_val_pos = current_ids.index(min_val)
            query_words_index[min_val_indx] += 1

class LRUCache(object):
    def __init__(self, size=32):
        self.cache = pylru.lrucache(size)
    
    def has(self, key):
        return key in self.cache
    
    def get(self, key):
        return self.cache[key]
    
    def set(self, key, value):
        self.cache[key] = value
    
class BOWInvertedIndexEngineWithCache(BOWInvertedIndexEngine, LRUCache):
    def __init__(self):
        super(BOWInvertedIndexEngineWithCache, self).__init__()
        LRUCache.__init__(self)
    
    def search(self, query):
        if self.has(query):
            print('cache hit!')
            return self.get(query)
        result = super(BOWInvertedIndexEngineWithCache, self).search(query)
        self.set(query, result)
        return result

search_engine = BOWInvertedIndexEngineWithCache()
main(search_engine)

"""
simple
found 0 result(s):
random
found 0 result(s):
dream
found 2 result(s):
tmp\search_txt\2.txt
tmp\search_txt\3.txt
dream
cache hit!
found 2 result(s):
tmp\search_txt\2.txt
tmp\search_txt\3.txt
"""
```

LRUCache 定义了一个缓存类，你可以通过继承这个类来调用其方法。LRU 缓存是一种很经典的缓存（同时，LRU 的实现也是硅谷大厂常考的算法面试题，这里为了简单，我直接使用 pylru 这个包），它符合自然界的局部性原理，可以保留最近使用过的对象，而逐渐淘汰掉很久没有被用过的对象。

因此，这里的缓存使用起来也很简单，调用 has() 函数判断是否在缓存中，如果在，调用
get 函数直接返回结果；如果不在，送入后台计算结果，然后再塞入缓存。

我们可以看到，BOWInvertedIndexEngineWithCache 类，多重继承了两个类。首先需要
注意的是构造函数。多重继承有两种初始化方法：

- 第一种，`super(BOWInvertedIndexEngineWithCache, self).__init__()`直接初始化该类的第一个父类，不过使用这种方法时，要求继承链的最顶层父类必须要继承object；
- 第二种，对于多重继承，如果有多个构造函数需要调用， 我们就必须用传统的方法`LRUCache.__init__(self) `。

# Python 模块化

## 简单模块化

可以把函数、类、常量拆分到不同的文件，把它们放在同一个文件夹，然后使用 from  our_file import function_name, class_name 的方式调用。之后，这些函数和类就可以在文件内直接使用了。

```python
# utils.py

def get_sum(a, b):
    return a + b

# class_utils.py

class Encoder(object):
    def encode(self, s):
        return s[::-1]

class Decoder(object):
    def decode(self, s):
        return ''.join(reversed(list(s)))
    
# main.py

from utils import get_sum
from class_utils import *

print(get_sum(1, 2))	# 3
encoder = Encoder()
decoder = Decoder()
print(encoder.encode('abcde'))	# edcba
print(encoder.encode('edcba'))	# abcde
```

如果我们想调用上层目录呢？注意，`sys.path.append("..") `表示将当前程序所在位
置向上提了一级。

import 同一个模块只会被执行一次，这样就可以防止重复导入模块出现问题。当然，良好的编程习惯应该杜绝代码多次导入的情况。在 Facebook 的编程规范中，除了一些极其特殊的情况，import 必须位于程序的最前端。

在许多教程中看到过这样的要求：我们还需要在模块所在的文件夹新建一个 `__init__.py`，内容可以为空，也可以用来表述包对外暴露的模块接口。不过，事实上，这是 Python 2 的规范。在 Python 3 规范中，`__init__.py`并不是必须的，很多教程里没提过这一点，或者没讲明白，我希望你还是能注意到这个地方。

整体而言，这就是最简单的模块调用方式了。但是做大型项目时，一个项目组的 workspace 可能有上千个文件，有几十万到几百万行代码。这种调用方式已经完全不够用了，学会新的组织方式迫在眉睫。

接下来，我们就系统学习下，模块化的科学组织方式。

## 项目模块化

相对路径和绝对路径：

在 Linux 系统中，每个文件都有一个绝对路径，以 / 开头，来表示从根目录到叶子节点的路径，例如 `/home/ubuntu/Desktop/my_project/test.py`，这种表示方法叫作绝对路径。

另外，对于任意两个文件，我们都有一条通路可以从一个文件走到另一个文件，例如`/home/ubuntu/Downloads/example.json`。再如，我们从 test.py 访问到example.json，需要写成 `../../Downloads/example.json`，其中 `..` 表示上一层目录。这种表示方法，叫作相对路径。

通常，一个 Python 文件在运行的时候，都会有一个运行时位置，最开始时即为这个文件所在的文件夹。当然，这个运行路径以后可以被改变。运行 `sys.path.append("..") `，则可以改变当前 Python 解释器的位置。不过，一般而言我并不推荐，固定一个确定路径对大型工程来说是非常必要的。

但是 `sys.path.append("..") ` 并没有改变当前文件所在路径：

```python
import os
import sys

print(os.getcwd())
sys.path.append("../")
print(os.getcwd())

"""
...\Python_Note\Python_Notes_Basic\Python基础库入门\9.Python 模块化
...\Python_Note\Python_Notes_Basic\Python基础库入门\9.Python 模块化
"""
```

首先，你会发现，相对位置是一种很不好的选择。因为代码可能会迁移，相对位置会使得重
构既不雅观，也易出错。因此，在大型工程中尽可能使用绝对位置是第一要义。对于一个独
立的项目，所有的模块的追寻方式，最好从项目的根目录开始追溯，这叫做相对的绝对路
径。

在做项目的时候，虽然你不可能把全世界的代码都放到一个文件夹下，但是类似模块化的思
想还是要有的——那就是以项目的根目录作为最基本的目录，所有的模块调用，都要通过
根目录一层层向下索引的方式来 import。

### 示例

一个项目结构如下所示：

```python
.
|-- proto
|  |-- mat.py
|-- utils
|  |-- mat_mul.py
|-- src
|-- main.py
```

```python
# proto/mat.py
class Matrix(object):
    ···

# utils/mat_mul.py
from proto.mat import Matrix
def mat_mul():
    ···

# src/main.py
from proto.mat import Matrix
from utils.mat_mul import mat_mul
```

这样的架构直接用 `Pycharm` 创建，是可以直接运行 `main.py` 的，但是尝试使用命令行进入 src 文件夹，直接输入 `Python main.py`，报错，找不到 `proto`。返回上一级目录，输入 `Python src/main.py` ，继续报错，找不到 proto。

为什么 `Pycharm` 可以正常运行呢？

实际上，Python 解释器在遇到 import 的时候，它会在一个特定的列表中寻找模块。这个
特定的列表，可以用下面的方式拿到：

```python
import sys

print(sys.path)

# ['', '/usr/lib/python36.zip', ...]
```

请注意，它的第一项为空。其实，Pycharm 做的一件事，就是将第一项设置为项目根目录
的绝对地址。这样，每次你无论怎么运行 main.py，import 函数在执行的时候，都会去项
目根目录中找相应的包。

---

如何使普通的 Python 运行环境也能正常运行呢？

- 方法一：直接强行修改这个位置

  ```python
  import sys
  sys.path[0] = '/home/ubuntu/workspace/your_projects'
  ```

  但这显然不是最佳解决方案，把绝对路径写到代码里，是非常不推荐的方式（你可以写到配置文件中，但找配置文件也需要路径寻找，于是就会进入无解的死循环）。
  
- 方法二：修改 `PYTHONHONE`

  Python 的 `Virtual Environment`: Python 可以通过 `Virtualenv` 工具，非常方便地创建一个全新的 Python 运行环境。
  
  事实上，提倡对于每一个项目，最好要有一个独立的运行环境来保持包和模块的纯净性。
  
  在 `Virtual Environment` 中可以找到一个文件叫 `active` ，在文件末尾，填入下面的内容：
  
  ```python
  export PYTHONPATH="/home/ubuntu/workspace/your_projects"
  ```
  

# 装饰器

装饰器一直以来都是 Python 中很有用、很经典的一个feature，在工程中的应用也十分广泛，比如日志、缓存等等的任务都会用到。然而，在平常工作生活中，许多人常常因为其相对复杂的表示，对装饰器望而生畏，认为它“too fancy to learn”，实际并不如此。

  ## 函数装饰器

### 函数核心

1. 在 Python 中，函数是一等公民（first-class citizen），函数也是对象。我们可以把函数赋予变量，比如下面这段代码：

   ```python
   def func(message):
   	print('Got a message: {}'.format(message))
   send_message = func
   send_message('hello world')
   
   # Got a message: hello world
   ```

   这个例子中，我们把函数 func() 赋予了变量 send_message，这样之后你调用 send_message，就相当于是调用函数 func()。

2. 可以把函数当作参数，传入另一个函数中，比如下面这段代码：

   ```python
   def get_message(message):
   	return 'Got a message: ' + message
   def root_call(func, message):
   	print(func(message))
   root_call(get_message, 'hello world')
   
   # Got a message: hello world
   ```


3. 在函数中定义函数，也就是函数的嵌套。

   ```python
   def func(message):
       def get_message(message):
           print('Got a message: {}'.format(message))
       return get_message(message)
   
   func('hello world')
   
   # 输出
   Got a message: hello world
   ```

4. 函数的返回值也可以是函数对象（闭包）：

   ```python
   def func_colsure():
       def get_message(message):
   		print('Got a message: {}'.format(message))
   	return get_message
   send_message = func_closure()
   send_message('hello world')
   
   # 输出
   Got a message: hello world        
   ```

### 简单的装饰器

装饰器的简单例子：

```python
def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()
    return wrapper

def greet():
	print('hello world')
    
greet = my_decorator(greet)
greet()

# 输出
wrapper of decorator
hello world
```

`my_decorator()` 就是一个装饰器，它把真正需要执行的函数 greet() 包裹住，并且改变它的行为，但是原函数 greet() 不变。

---

上述代码在 Python 中更简单、更优雅的表示方式：

```python
def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()
    return wrapper

@my_decorator
def greet():
	print('hello world')
    
greet()

# 输出
wrapper of decorator
hello world
```

这里的`@`，称之为语法糖，`@my_decorator` 就相当于前面的 `greet=my_decorator(greet)`语句，只不过更加简洁。因此，如果你的程序中有其它函数需要做类似的装饰，你只需在它们的上方加上@decorator就可以了，这样就大大提高了函数的重复利用和程序的可读性。

#### 带参数的装饰器

如果原函数 `greet()` 中有参数需要传递给装饰器，最简单的方式就是在对应的装饰器函数 `wrapper()` 上，加上相应的参数：

```python
def my_decorator(func):
    def wrapper(message):
        print('wrapper of decorator')
        func(message)
    return wrapper

@my_decorator
def greet(message):
	print(message)
    
greet('hello world')

# 输出
wrapper of decorator
hello world
```

如果还有另外一个函数，也需要使用 `my_decorator()` 装饰器，但是这个新的函数有两个或者多个参数，应该怎么办呢？

```python
@my_decorator
def celebrate(name, message):
    ...
```

事实上，通常情况下，会把 `*args` 和 `**kwargs`，作为装饰器内部函数 `wrapper()` 的参数。

```python'
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('wrapper of decorator')
        func(*args, **kwargs)
    return wrapper
```

### 带自定义参数的装饰器

比如想要定义一个参数，来表示装饰器内部函数被执行的次数，那么就可以写成下面这种形式：

```python
def repeat(num):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                print('wrapper of decorator')
                func(*args, **kwargs)
        return wrapper
    return my_decorator

@repeat(4)
def greet(message):
    print(message)
    
greet("hello world")
```

### 原函数还是原函数吗？

```python
print(greet.__name__)	# 'wrapper'
```

`greet()` 函数被装饰以后，它的`元信息`变了。元信息告诉我们“它不再是以前的那个 greet() 函数，而是被`wrapper() `函数取代了”。

可以用内置的装饰器 `@functool.wrap`， 

```python
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('wrapper of decorator')
        func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(message):
    print(message)
   
print(greet.__name__)	# greet
```

## 类有关装饰器

### 类装饰器

类也可以作为装饰器，类装饰器主要依赖于函数 `__call__()`，每当你调用一个类的示例时，函数 `__call__()` 就会被执行一次。

```python
class Count:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
    
    def __call__(self, *args, **kwargs):
        self,num_calls += 1
        print('num of calls is : {}'.format(self.num_calls))
        return self.func(*args, **kwargs)

@Count		# example = Count(example)
def example():
    print("hello world")

example()

# 输出
num of calls is: 1
hello world

example()
# 输出
num of calls is: 2
hello world
```

我们定义了类 Count，初始化时传入原函数 func()，而 `__call__()` 函数表示让变量 num_calls 自增 1，然后打印，并且调用原函数。因此，在我们第一次调用函数example() 时，num_calls 的值是 1，而在第二次调用时，它的值变成了 2。

### 类函数装饰其他函数

在类里面定义个函数，用来装饰其它函数，严格意义上说不属于类装饰器。

```python
import functools

class SimpleClass(object):
    @staticmethod
    def my_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('wrapper of decorator')
            func(*args, **kwargs)
        return wrapper

@SimpleClass.my_decorator
def greet(message):
    print(message)
    
greet('hello world')

# 输出
wrapper of decorator
hello world
```

### 装饰器装饰同一个类里的函数

背景：想要通过装饰器修改类里的self属性值。

```python
import functools

class SimpleClass(object):
    def __init__(self):
        self.message_call = 0
    
    # @staticmethod  
    # 此处不能含有 staticmethod，因为装饰器需要传入 类实例
    # 也不能写成 my_decorator(self, func), 因为传入参数只有func
    def my_decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):  # self,接收 SimpleClass 里的self,也就是类实例
            self.message_call += 1
            print('message_call is {}'.format(self.message_call))
            return func(self, *args, **kwargs)
        return wrapper

    @my_decorator
    def greet(self, message):
        print(message)
    
test = SimpleClass()
test.greet('hello world')
test.greet('hello world')

# 输出
message_call is 1
hello world
message_call is 2
hello world
```

其中类在初始化时，会装饰每个需要被装饰的函数

```python
import functools

class SimpleClass(object):
    def __init__(self):
        self.message_call = 0
    
    # @staticmethod  
    # 此处不能含有 staticmethod，因为装饰器需要传入 类实例
    # 也不能写成 my_decorator(self, func), 因为传入参数只有func
    def my_decorator(func):
        print("弄懂调用次数")
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):  # self,接收 SimpleClass 里的self,也就是类实例
            self.message_call += 1
            print('message_call is {}'.format(self.message_call))
            return func(self, *args, **kwargs)
        return wrapper

    @my_decorator
    def greet1(self, message):
        print(message)
        
    @my_decorator
    def greet2(self, message):
        print(message)
    
test = SimpleClass()

# 输出
弄懂调用次数
弄懂调用次数
```

### 定义一个类装饰器，装饰类中的函数，默认调用__get__方法

实际上把类方法变成属性了，还记得类属性装饰器吧，@property

下面自已做一个property

```python
class Decrator(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        '''
        instance:代表实例，sum中的self
        owner：代表类本身，Test类
        
        '''
        print('调用的是get函数')
        return self.func(instance)     # instance就是Test类的self


class Test(object):
    def __init__(self):
        self.result = 0

    @Decrator
    def sum(self):
        print('There is the Func in the Class !')

t = Test()
print(t.sum)            # 众所周知，属性是不加括号的,sum真的变成了属性

# 输出
调用的是get函数
There is the Func in the Class !
None
```

做一个求和属性sum，统计所有输入的数字的和

```python
class Decrator(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        print('调用的是get函数')
        return self.func(instance)


class Test(object):
    def __init__(self, *args, **kwargs):
        self.value_list = []
        if args:
            for i in args:
                if str(i).isdigit():
                    self.value_list.append(i)
        if kwargs:
            for v in kwargs.values():
                if str(v).isdigit():
                    self.value_list.append(v)

    @Decrator
    def sum(self):
        result = 0
        print(self.value_list)
        for i in self.value_list:
            result += i

        return result


t = Test(1, 2, 3, 4, 5, 6, 7, 8, i=9, ss=10, strings='lll')

print(t.sum)

# 输出
调用的是get函数
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
55
```

## 装饰器的嵌套

实际上，Python也支持多个装饰器，比如：

```python
@decorator1
@decorator2
@decorator3
def func():
	...
```

等效于：

```python
decorator1(decorator2(decorator3(func)))
```

之前的单个 ’hello world' 可以写成：

```python
import functools
def my_decorator1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('execute decorator1')
        func(*args, **kwargs)
    return wrapper

def my_decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('execute decorator2')
        func(*args, **kwargs)
        return wrapper
    
@my_decorator1
@my_decorator2
def greet(message):
	print(message)
    
greet('hello world')

# 输出
execute decorator1
execute decorator2
hello world
```

## 装饰器的用法实例

### 身份认证

```python
import functools

def authenticate(func):
    @functools.wraps(func):
        def wrapper(*args, **kwargs):
            request = args[0]
            if check_user_logged_in(request):  # 如果用户处于登陆状态
                return func(*args, **kwargs)  # 执行函数 post_comment
            else:
                raise Exception('Authentication failed')
        return wrapper

@authenticate
def post_comment(request, ...)
	...
```

这段代码中，我们定义了装饰器 `authenticate`；而函数 `post_comment()` ，则表示发表用户对某篇文章的评论。每次调用这个函数前，都会先检查用户是否处于登录状态，如果是登录状态，则允许这项操作；如果没有登录，则不允许。

### 日志记录

日志记录同样是很常见的一个案例。在实际工作中，如果你怀疑某些函数的耗时过长，导致整个系统的 latency（延迟）增加，所以想在线上测试某些函数的执行时间，那么，装饰器就是一种很常用的手段。

```python
import time
import functools

def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print('{} took {} ms'.format(func.__name__, (end - start) * 1e-3))
        return res
    return wrapper

@log_execution_time
def calculate_similarity(items):
    ...
```

这里，装饰器 log_execution_time 记录某个函数的运行时间，并返回其执行结果。如果你想计算任何函数的执行时间，在这个函数上方加上@log_execution_time即可。

### 输入合理性检测

在大型公司的机器学习框架中，我们调用机器集群进行模型训练前，往往会用装饰器对其输入（往往是很长的 json 文件）进行合理性检查。这样就可以大大避免，输入不正确对机器造成的巨大开销。

```python
import functools

def validation_check(input):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        ...  # 检查输入是否合法
        
@validation_check
def neural_network_training(param1, param2, ...):
    ...
```

### 缓存

LRU cache，在 Python 中的表示形式是 `@lru_cache`。`@lru_cache` 会缓存进程中的函数参数和结果，当缓存满了以后，会删除 least recenly used 的数据。

大型公司服务器端的代码中往往存在很多关于设备的检查，比如你使用的设备是安卓还是 iPhone，版本号是多少。这其中的一个原因，就是一些新的 feature，往往只在某些特定的手机系统或版本上才有（比如 Android v200+）。

这样一来，我们通常使用缓存装饰器，来包裹这些检查函数，避免其被反复调用，进而提高程序运行效率，比如写成下面这样：

```python
@lru_cache
def check(param1, param2, ...)：  # 检查用户设备类型，版本号
	...
```

# metaclass

meta-class 的 meta 这个词根，起源于希腊语词汇 meta，包含下面两种意思：

1. **“Beyond”**，例如技术词汇 metadata，意思是描述数据的超越数据；
2. **“Change”**，例如技术词汇 metamorphosis，意思是改变的形态。

## Python 底层语言设计层面是如何实现metaclass 的？

metaclass 能够拦截 Python 类的定义

要理解 metaclass 的底层原理，你需要深入理解 Python 类型模型。

### 第一，所有的 Python 的用户定义类，都是 type 这个类的实例。

事实上，类本身不过是一个名为 type 类的实例。在 Python 的类型世界里，type 这个类就是造物的上帝。

```python
class MyClass:
    pass

instance = MyClass()

print(type(instance))  # <class '__main__.MyClass'>
print(type(MyClass))  # <class 'type'>
```

### 第二，用户自定义类，只不过是 type 类的 \__call__ 运算符重载。

当我们定义一个类的语句结束时，真正发生的情况，是Python 调用 type 的 `__call__`  运算符。简单来说，当你定义一个类时，写成下面这样时：

```python
class MyClass:
    data = 1
```

Python 真正执行的是下面这段代码：

```python
class = type(classname, superclasses, attributedict)
```

这里等号右边的type(classname, superclasses,attributedict)，就是 type 的 `__call__` 运算符重载，它会进一步调用：

```python
type.__new__(typeclass, classname, superclasses, attributedict)
type.__init__(class, classname, superclasses, attributedict)
```

代码验证:

```python
class MyClass:
    data = 1
    
instance = MyClass()
print(instance)  # <__main__.MyClass object at 0x000002016D084880>

print(instance.data)  # 1
```

```python
MyClass = type('MyClass', (), {'data': 1})

instance = MyClass()
print(instance)  # <__main__.MyClass object at 0x0000016ED1D51640>

print(instance.data)  # 1
```

### 第三，metaclass 是 type 的子类，通过替换type 的 \__call__ 运算符重载机制，“超越变形”正常的类。

其实，理解了以上几点，我们就会明白，正是 Python 的类创建机制，给了 metaclass 大展身手的机会。一旦你把一个类型 MyClass 的 metaclass 设置成 MyMeta，MyClass 就不再由原生的 type 创建，而是会调用 MyMeta 的 `__call__` 运算符重载。

```python
class = type(classname, superclasses, attributedict)
# 变为了
class = MyMeta(classname, superclasses, attributedict)
```

## 使用 metaclass 的风险

前面的篇幅，我都是在讲 metaclass 的原理和优点。的的确确，只有深入理解 metaclass 的本质，你才能用好 metaclass。而不幸的是，正如我开头所说，深入理解 metaclass 的 Python 开发者，只占了 0.1% 不到。

不过，凡事有利必有弊，尤其是 metaclass 这样“逆天”的存在。正如你所看到的那样，metaclass 会"扭曲变形"正常的 Python 类型模型。所以，如果使用不慎，对于整个代码库造成的风险是不可估量的。

换句话说，metaclass 仅仅是给小部分 Python 开发者，在开发框架层面的 Python 库时使用的。而在应用层，metaclass 往往不是很好的选择。

也正因为这样，据我所知，在很多硅谷一线大厂，使用Python metaclass 需要特例特批。

# 迭代器和生成器

Python 在处理 for in 语句的时候，具体发生了什么吗？什么样的对象可以被 for in 来枚举呢？

## 你肯定用过的容器、可迭代对象和迭代器

容器这个概念非常好理解。我们说过，在 Python 中一切皆对象，对象的抽象就是类，而对象的集合就是容器。

列表（list: [0, 1, 2]），元组（tuple: (0, 1, 2)），字典（dict: {0:0, 1:1, 2:2}），集合（set: set([0, 1, 2])）都是容器。对于容器，你可以很直观地想象成多个元素在一起的单元；而不同容器的区别，正是在于内部数据结构的实现方法。然后，你就可以针对不同场景，选择不同时间和空间复杂度的容器。

所有的容器都是可迭代的（iterable）。这里的迭代，和枚举不完全一样。迭代可以想象成是你去买苹果，卖家并不告诉你他有多少库存。这样，每次你都需要告诉卖家，你要一个苹果，然后卖家采取行为：要么给你拿一个苹果；要么告诉你，苹果已经卖完了。你并不需要知道，卖家在仓库是怎么摆放苹果的。

严谨地说，迭代器（iterator）提供了一个 next 的方法。调用这个方法后，你要么得到这个容器的下一个对象，要么得到一个 StopIteration 的错误（苹果卖完了）。你不需要像列表一样指定元素的索引，因为字典和集合这样的容器并没有索引一说。比如，字典采用哈希表实现，那么你就只需要知道，next 函数可以不重复不遗漏地一个一个拿到所有元素即可。

而可迭代对象，通过 iter() 函数返回一个迭代器，再通过next() 函数就可以实现遍历。for in 语句将这个过程隐式化，所以，你只需要知道它大概做了什么就行了。

我们来看下面这段代码，主要向你展示怎么判断一个对象是否可迭代。当然，这还有另一种做法，是 `isinstance(obj,Iterable)`。

```python
def is_iterable(param):
    try:
        iter(param)
        return True
    except TypeError:
        return False

params = [
    1234,
    '1234',
    [1, 2, 3, 4],
    set([1, 2, 3, 4]),
    {1:1, 2:2, 3:3, 4:4},
    (1, 2, 3, 4)
]

for param in params:
    print('{} is iterable? {}'.format(param, is_iterable(param)))
    
"""
1234 is iterable? False
1234 is iterable? True
[1, 2, 3, 4] is iterable? True
{1, 2, 3, 4} is iterable? True
{1: 1, 2: 2, 3: 3, 4: 4} is iterable? True
(1, 2, 3, 4) is iterable? True
"""
```

由结果可知，给出的类型中，除了数字1234 之外，其它的数据类型都是可迭代的。

## 生成器，又是什么？

生成器这个概念会比较陌生，因为生成器在很多常用语言中，并没有相对应的模型。

其实只需要记着一点：**生成器是懒人版本的迭代器。**

在迭代器中，如果我们想要枚举它的元素，这些元素需要事先生成。

声明一个迭代器很简单，`[i for i in range(100000000)]` 就可以生成一个包含一亿元素的列表。每个元素在生成后都会保存到内存中，你通过代码可以看到，它们占用了巨量的内存，内存不够的话就会出现OOM 错误。

不过，我们并不需要在内存中同时保存这么多东西，比如对元素求和，我们只需要知道每个元素在相加的那一刻是多少就行了，用完就可以扔掉了。

于是，生成器的概念应运而生，在你调用 next() 函数的时候，才会生成下一个变量。生成器在 Python 的写法是用小括号括起来，`(i for i in range(100000000))` ，即初始化了一个生成器。

这样一来，你可以清晰地看到，生成器并不会像迭代器一样占用大量内存，只有在被使用的时候才会调用。而且生成器在初始化的时候，并不需要运行一次生成操作，相比于 `迭代器` ，`生成器` 节省了一次生成一亿个元素的过程，因此耗时明显比 `迭代器` 短。

### 生成器的进阶应用

#### 验证数学恒等式

数学中有一个恒等式，`(1 + 2 + 3 + ... + n)^2 = 1^3 + 2^3 + 3^3 + ... + n^3`，现在来验证一下这个公式的正确性。

首先自定义一个生成器：

```python
def generator(k):
    i = 1
    while True:
        yield i ** k
        i += 1
gen_1 = generator(1)
gen_3 = generator(3)

print(gen_1)	# <generator object generator at 0x000001C8E1DDF580>
print(gen_3)	# <generator object generator at 0x000001C8E1DDF6D0>
```

验证公式:

```python
def generator(k):
    i = 1
    while True:
        yield i ** k
        i += 1

def get_sum(n):
    gen_1 = generator(1)
    gen_3 = generator(3)
    sum_1, sum_3 = 0, 0
    for i in range(n):
        next_1 = next(gen_1)
        next_3 = next(gen_3)
        print('next_1 = {}, next_3 = {}'.format(next_1, next_3))
        sum_1 += next_1
        sum_3 += next_3
    print(sum_1 * sum_1, sum_3)
                                                
get_sum(8)

"""
next_1 = 1, next_3 = 1
next_1 = 2, next_3 = 8
next_1 = 3, next_3 = 27
next_1 = 4, next_3 = 64
next_1 = 5, next_3 = 125
next_1 = 6, next_3 = 216
next_1 = 7, next_3 = 343
next_1 = 8, next_3 = 512
1296 1296
"""
```

其中的 `yield` 是魔术的关键。对于初学者来说，可以理解为函数运行到这一行的时候，程序会从这里暂停，然后跳出，不过跳到哪里呢？答案是 `next()` 函数。那么 i ** k是干什么的呢？它其实成了 next() 函数的返回值。

这样，每次 `next(gen)` 函数被调用的时候，暂停的程序就又复活了，从 yield 这里向下继续执行；同时注意，局部变量 `i` 并没有被清除掉，而是会继续累加。我们可以看到 next_1从 1 变到 8，next_3 从 1 变到 512。

生成器可以一直进行下去！没错，事实上，迭代器是一个有限集合，生成器则可以成为一个无限集。只管调用 next()，生成器根据运算会自动生成新的元素，然后返回给你，非常便捷。

#### 查看数字在 list 中的位置

常规做法：枚举每个元素和它的 index，判断后加入 result，最后返回。

```python
def index_normal(L, target):
	result = []
	for i, num in enumerate(L):
		if num == target:
			result.append(i)
	return result

print(index_normal([1, 6, 2, 4, 5, 2, 8, 6, 3, 2], 2))
# [2, 5, 9]
```

使用生成器：

```python
def index_generator(L, target):
	for i, num in enumerate(L):
		if num == target:
			yield i
print(list(index_generator([1, 6, 2, 4, 5, 2, 8, 6, 3, 2], 2)))
# [2, 5, 9]
```

在 Python 语言规范中，用更少、更清晰的代码实现相同功能，一直是被推崇的做法，因为这样能够很有效提高代码的可读性，减少出错概率，也方便别人快速准确理解你的意图。

#### 判断一个序列是否为另一个序列的子序列

先来解读一下这个问题本身。序列就是列表，子序列则指的是，一个列表的元素在第二个列表中都按顺序出现，但是并不必挨在一起。举个例子，[1, 3, 5] 是 [1, 2, 3, 4, 5] 的子序列，[1, 4, 3] 则不是。

常规算法是贪心算法。我们维护两个指针指向两个列表的最开始，然后对第二个序列一路扫过去，如果某个数字和第一个指针指的一样，那么就把第一个指针前进一步。第一个指针移出第一个序列最后一个元素的时候，返回 True，否则返回 False。

不过，这个算法正常写的话，写下来怎么也得十行左右。

那么如果我们用迭代器和生成器呢？

```python
def is_subsequence(a, b):
    b = iter(b)
    return all(i in b for i in a)

print(is_subsequence([1, 3, 5], [1, 2, 3, 4, 5]))	# True
print(is_subsequence([1, 4, 3], [1, 2, 3, 4, 5]))	# False
```

这简短的几行代码，你是不是看得一头雾水，先将代码分解：

```python
def is_subsequence(a, b):
    b = iter(b)
    print(b)
    
    gen = (i for i in a)
    print(gen)
    for i in gen:
        print(i)
        
    gen = ((i in b) for i in a)
    print(gen)
    for i in gen:
        print(i)
        
    return all(((i in b) for i in a))

print(is_subsequence([1, 3, 5], [1, 2, 3, 4, 5]))
print()
print(is_subsequence([1, 4, 3], [1, 2, 3, 4, 5]))

"""
<list_iterator object at 0x0000024FEC08A490>
<generator object is_subsequence.<locals>.<genexpr> at 0x0000024FED46F890>
1
3
5
<generator object is_subsequence.<locals>.<genexpr> at 0x0000024FED46FB30>
True
True
True
False

<list_iterator object at 0x0000024FEC08A460>
<generator object is_subsequence.<locals>.<genexpr> at 0x0000024FED46FB30>
1
4
3
<generator object is_subsequence.<locals>.<genexpr> at 0x0000024FED46F890>
True
True
False
False
"""
```

首先，第二行的 `b = iter(b)`，把列表 b 转化成了一个迭代器，为了后面的指针操作。

接下来的 `gen = (i for i in a)` 产生一个生成器，这个生成器可以遍历对象 a，因此能够输出 1, 3, 5。而  (i in b) 需要好好揣摩，这里你是不是能联想到 for in 语句？

没错，这里的 `(i in b)` ，大致等价于下面这段代码：

```python
while True:
	val = next(b)
	if val == i:
		yield True
```

这里非常巧妙地利用生成器的特性，next() 函数运行的时候，保存了当前的指针。比如再看下面这个示例：

```python
b = (i for i in range(5))

print(2 in b)	# True	
print(4 in b)	# True
print(3 in b)	# False
```

至于最后的 all() 函数，就很简单了。它用来判断一个迭代器的元素是否全部为 True，如果是则返回 True，否则就返回 False.

## 总结

此节讲了四种不同的对象，分别是容器、可迭代对象、迭代器和生成器。

容器是可迭代对象，可迭代对象调用 iter() 函数，可以得到一个迭代器。迭代器可以通过 next() 函数来得到下一个元素，从而支持遍历。

生成器是一种特殊的迭代器（注意这个逻辑关系反之不成立）。使用生成器，你可以写出来更加清晰的代码；合理使用生成器，可以降低内存占用、优化程序结构、提高程序速度。

生成器在 Python 2 的版本上，是协程的一种重要实现方式；而 Python 3.5 引入 async await 语法糖后，生成器实现协程的方式就已经落后了。

# Python 协程

## 从一个爬虫说起

```python
import time

def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    time.sleep(sleep_time)
    print('OK {}'.format(url))
    
def main(urls):
    for url in urls:
        crawl_page(url)
        
%time main(['url_1', 'url_2', 'url_3', 'url_4'])

"""
crawling url_1
OK url_1
crawling url_2
OK url_2
crawling url_3
OK url_3
crawling url_4
OK url_4
CPU times: total: 0 ns
Wall time: 10 s
"""
```

注意：本节的主要目的是协程的基础概念，因此我们简化爬虫的 `scrawl_page` 函数为休眠数秒，休眠时间取决于 `url`最后的那个数字。

这是一个很简单的爬虫，main() 函数执行时，调取 crawl_page() 函数进行网络通信，经过若干秒等待后收到结果，然后执行下一个。

看起来很简单，但你仔细一算，它也占用了不少时间，五个页面分别用了 1 秒到 4 秒的时间，加起来一共用了 10 秒。这显然效率低下，该怎么优化呢？

于是，一个很简单的思路出现了——我们这种爬取操作，完全可以并发化。我们就来看看使用协程怎么写。

```python
import asyncio
import time

async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))
    
async def main(urls):
    for url in urls:
        await crawl_page(url)
        
# jupyter
t1 = time.time()
await main(['url_1', 'url_2', 'url_3', 'url_4'])
t2 = time.time()
print(t2 -t1) 

# Ipython
# %time asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))

"""
crawling url_1
OK url_1
crawling url_2
OK url_2
crawling url_3
OK url_3
crawling url_4
OK url_4
10.015552520751953
"""
```

### TODO

