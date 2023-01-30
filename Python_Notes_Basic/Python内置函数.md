# eval()

eval() 函数用来执行一个字符串表达式，并返回表达式的值。

语法：`eval(expression[, globals[, locals]])`

- expression -- 表达式。
- globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
- locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。

## eval(expression)

只提供一个参数，eval的作用就是将expression的引号去掉，保留引号中字符的原有属性

```python
a = '12'
print(eval(a))			# 12
print(type(eval(a)))	# class 'int'>
print(eval('a')) 		# 12
print(type(eval('a')))	# <class 'str'>
```

```python
b = 4
print(eval('b * 2'))		# 8
print(eval('pow(b, 2)'))	# 16
```

```python
abc = 123
c = 'abc'
print(eval(c))		# 123
```

## eval(expression, globals)

```python
a = 1
b = 2
c = 3
dict1 = {'a':12, 'b':3}
# 设置全局命名空间并不影响解析字符串
print(eval('4 ** 2', dict1))  # 16

print(eval('a'))  # 1
print(eval('a', dict1))  # 12  # == dict1['a']
# print(eval('c', dict1))  # NameError: name 'c' is not defined

print(eval('a+b'))  # 3 # == a + b
print(eval('a+b', dict1))   # 15 # == dict1['a'] + dict2['b']
```

## eval(expression, globals, locals)

目前只发现可以起到一个优先级的作用

```python
a = 1
b = 2
c = 3
dict1 = {'a': 12, 'b': 3}
dict2 = {'a': 100, 'c': 200}
# dict2的优先级高于dict1，先从dict2中查找变量，未找到的再从dict1中查找。
print(eval("a + b + c", dict1, dict2))  # 303
```

# round()

round() 函数用对一个数进行四舍五入，并返回表达式的值。

语法：`round(num[, n])`

- n: 表示四舍五入的位数

```python
num = 1.6347
print(round(num))  # 2
print(round(num, 3))  # 1.635
```

## round 取舍的问题

python内部的round函数在5是否入时，要考虑奇数和偶数。

因为对于一个数字的以为小数来说有：

1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9

如果我们对一个小数进行取整，最合适的方法是一半舍，一半入。但是我们可以看到上面的小数却是9个，我们无法做到舍入相等。如果我们只是单纯的使用四舍五入，那么总会导致数值最后偏小，所以我们必须引入奇偶，对这个机制进行平衡，所以就出现了我们上面看到的那种“匪夷所思”的现象。

我们可以通过记住一个口诀来加强记忆：奇进偶舍。

```python
num = 1.5345
print(round(num))  # 2
print(round(num, 3))  # 1.534
```

## 自己实现真正的四舍五入

- int 实现

  ```python
  def my_round(num,ndigits=0):     
      return (int(pow(10, ndigits) * num - 0.5)+1) / pow(10, ndigits)
  ```


# sorted()

对可迭代对象进行排序

语法: `sorted(iterable,  key=None, reverse=False)`

- key: 排序关键字，值为一个函数，此函数只有一个参数且返回一个值

返回：排序后的列表

## sorted(iterable)

```python
sorted("fgbofaof")
# ['a', 'b', 'f', 'f', 'f', 'g', 'o', 'o']

names = [('jx1', 18), ('jx2', 30), ('jx3', 20), ('jx4', 15)]
sorted(names)  # 默认是元组的第一个元素进行排序
# [('jx1', 18), ('jx2', 30), ('jx3', 20), ('jx4', 15)]
```

## sorted(iterable, key=None)

```python
def getKey(x):
    return x[1]

names = [('jx1', 18), ('jx2', 30), ('jx3', 20), ('jx4', 15)]
sorted(names, key=getKey) 
# [('jx4', 15), ('jx1', 18), ('jx3', 20), ('jx2', 30)]
```



