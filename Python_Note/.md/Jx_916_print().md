# print()

python中格式化字符串的方式有两种，一种是使用"%s"的方式，一种是str.format()的方式

## %s

![](https://i.loli.net/2021/01/07/aHNbkBtmzpi3O6s.png)

 两种用法，第一种是在字符串中使用%s占位，在字符串后使用%替换值来替换
 
 该方式的优点是简单，缺点是影响可读性的，在数量多了以后，很难清楚哪一个占位符对应哪一个实参，排序很麻烦



```python
print("my name is %s and i am %d years old" %("xiaoming",18))
print("Hello,%s" % "Tom")
```

    my name is xiaoming and i am 18 years old
    Hello,Tom
    

另一种方式可以用字典的形式进行表示：


```python
print ("Hello,%(name)s" % {"name":"Tom"})
# 参数比较多的情况下这样用
value = {"greet": "Hello world", "language": "Python"}  
print("%(greet)s from %(language)s." % value)
print("%(greet)s from %(language)s." % {"greet": "Hello world", "language": "Python"})
```

    Hello,Tom
    Hello world from Python.
    Hello world from Python.
    

## format()方式

在python2.6开始，Python中新增加了一个字符串格式化字符的函数str.format(),此函数可以快速的处理各种字符串，增强了字符串格式化的功能。

基本语法是使用{}来替代%。format函数的实参位置可以不按照顺序

1. 使用位置参数

要点：位置参数不受顺序约束，且可以为{},只要format里有相对应的参数值即可,参数索引从0开，传入位置参数列表可用*列表


```python
"{} {}".format("hello", "world")  # 设置指定位置，按默认顺序
```




    'hello world'




```python
"{1} {0}".format("world", "hello")  # 设置指定位置
```




    'hello world'




```python
"{1} {0} {1}".format("hello", "world")  # 设置指定位置
```




    'world hello world'




```python
input = ["hello", "world"]  # 传入位置参数列表可用*列表
"{} {}".format(*input)
```




    'hello world'



2. 使用关键字参数，类似于使用字典key值占位，将字典作为参数传入字符串

要点：字符串中的关键字参数要与传入的参数值对得上，可用字典当关键字参数传入值，字典前加**即可


```python
'my name is {name},age is {age}'.format(name='Bingo', age=18)
```




    'my name is Bingo,age is 18'




```python
hash = {'name': 'Bingo', 'age': 18}
'my name is {name},age is {age}'.format(**hash)  # 通过关键字，并用字典当关键字传入值时，在字典前加**即可
```




    'my name is Bingo,age is 18'



### 填充与格式化(:[填充字符][对齐方式 <^>][宽度])

^、<、>分别是居中、左对齐、右对齐，:号后面带填充的字符，只能是一个字符，不指定的话默认是用空格填充，对齐方式后面紧跟一个整数可以限定该字段的宽度。


```python
print('{0:*>9}'.format("hello"))  # 右对齐
print('{0:*<9}'.format("hello"))  # 左对齐
print('{0:*^9}'.format("hello"))  # 居中
print('{0:^9}'.format("hello"))  # 居中 默认空格
```

    ****hello
    hello****
    **hello**
      hello  
    

### 精度与进制


```python
print('{0:.2f}'.format(1/3))
print('{0:b}'.format(10))  # 二进制
print('{0:o}'.format(10))  # 八进制
print('{0:x}'.format(10))  # 十六进制
print('{:,}'.format(12369132698))  # 千分位格式化
```

    0.33
    1010
    12
    a
    12,369,132,698
    

### 通过下标 


```python
my_list = ['xiaoming', 18]
"name {0[0]}, age {0[1]}".format(my_list)  # 通过列表索引设置参数
```




    'name xiaoming, age 18'



### 扩展

如果字符串里面含有 "{"  或者  "}"时，需要把 "{" 和 "}" 字符以 "{{" 和 "}}" 代替。


```python
"{{'name1':'{0}','name2':'{1}'}}".format('qpy','wjx')
```




    "{'name1':'qpy','name2':'wjx'}"


