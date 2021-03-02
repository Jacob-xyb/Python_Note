# Dictionary


## object


```python
dict = {}  # Create an empty dictionary
print(dict)
```

    {}
    


```python
dict['one'] = "1 - hello,world"  # Create a value with a key of 'one'
print(dict)
```

    {'one': '1 - hello,world'}
    


```python
dict[2] = "2 - 嘿嘿"  # Create a value with a key of 2
print(dict)
```

    {'one': '1 - hello,world', 2: '2 - 嘿嘿'}
    

- __字典的无序性__


```python
d1 = {'a': 0, 'b': 1}
d2 = {'b': 1, 'a': 0}
d1 == d2
```




    True



## dict()

- dict()将包含双值子序列的序列转换成字典。__列表和元组都可以__


```python
lol = [['a','b'],['c','d'],['e','f']]
print(dict(lol))
```

    {'a': 'b', 'c': 'd', 'e': 'f'}
    


```python
lol = [('a','b'),('c','d'),('e','f')]
print(dict(lol))
```

    {'a': 'b', 'c': 'd', 'e': 'f'}
    

## items()

- 描述

    - Python 字典 items() 方法以列表返回可遍历的(键, 值) 元组数组。
- 语法： 

    - ```dict.items()``` 参数：NA

- 返回值：

    - 返回可遍历的(键, 值) 元组数组。


```python
numdict = {'a': 8, 'c': 10, 'b': 2}
print(numdict.items())
```

    dict_items([('a', 8), ('c', 10), ('b', 2)])
    

- 可以将字典的键值组成一个新的列表


```python
numdict = {'a': 8, 'c': 10, 'b': 2}
res = []
for key,value in numdict.items():
    res.append(key)
    res.append(value)
print(res)
```

    ['a', 8, 'c', 10, 'b', 2]
    

- 应用：当键值一一对应时，可以实现键值互转:


```python
numdict = {'a': 8, 'c': 10, 'b': 2}
res = {}
for key,value in numdict.items():
    res[value] = key
print(res)
```

    {8: 'a', 10: 'c', 2: 'b'}
    

## get()

- 描述

    - Python 字典 get() 函数返回指定键的值。
- 语法

    - ```dict.get(key, default=None)```
    
- 参数

    - key -- 字典中要查找的键。
    - default -- 如果指定的键不存在时，返回该默认值。

- 返回值：

    - 返回可遍历的(键, 值) 元组数组。


```python
dict = {'Name': 'Runoob', 'Age': 27}

print("Age 值为 : %s" %  dict.get('Age'))
print("Sex 值为 : %s" %  dict.get('Sex', "NA"))
print("Height 值为：%s" % dict.get('Height', "180"))
```

    Age 值为 : 27
    Sex 值为 : NA
    Height 值为：180
    


```python
dict = {'Name': 'Runoob', 'Age': 27}

print("一年后 Age值为：%s" % (dict.get('Age') + 1))
```

    一年后 Age值为：28
    

## # index


```python
surface_tar = {'TP': [0.01, 0.025, 0.05, 0.1, 0.2],
               'TN': [0.2, 0.5, 1.0, 1.5, 2.0]}
print(surface_tar['TP'])  # Output the value with a key of 'TP' # list
print(surface_tar['TP'][0])  # Output a value
print(surface_tar.keys(),type(surface_tar.keys()))  # Output all keys
print(surface_tar.values(),type(surface_tar.values()))  # Output all values
```

    [0.01, 0.025, 0.05, 0.1, 0.2]
    0.01
    dict_keys(['TP', 'TN']) <class 'dict_keys'>
    dict_values([[0.01, 0.025, 0.05, 0.1, 0.2], [0.2, 0.5, 1.0, 1.5, 2.0]]) <class 'dict_values'>
    

## sorted()

- sorted()会返回排好序的列表副本，原列表内容不变。

- 对于字典而言：依据字典的key进行排序，返回key的排序结果


```python
numdict = {'a': 8, 'c': 10, 'b': 2}
res = sorted(numdict)
print(res)
```

    ['a', 'b', 'c']
    

## u need konw

- 如何根据值找键


```python
numdict = {'a': 8, 'c': 10, 'b': 2}
key_list = []
value_list = []
for key,value in numdict.items():
    key_list.append(key)
    value_list.append(value)

```

- 判断键值是否存在


```python
numdict = {'a': 8, 'c': 10, 'b': 2}
if "d" not in numdict:
    print('1')
```

    1
    

- 一种新的创建字典的方式：常用于算法中。


```python
A = [1, 2, 3]
D = {i:True for i in A}
print(D)：
```

    {1: True, 2: True, 3: True}
    


```python
from collections import defaultdict
bc= defaultdict(bool,D)
print(c)
```

    defaultdict(<class 'bool'>, {1: True, 2: True, 3: True})
    
