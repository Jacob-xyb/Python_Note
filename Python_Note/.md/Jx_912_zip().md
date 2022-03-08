# zip()

- 描述

    - zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象，这样做的好处是节约了不少的内存。

    - 我们可以使用 ```list()``` 转换来输出列表。

    - 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。

- 语法

```python
zip([iterable, ...])
```

- 参数说明

    - iterabl -- 一个或多个迭代器。
 
- 返回值
    
    - 返回一个对象

## function

1.返回一个对象


```python
a = [1, 2, 3]
b = [4, 5, 6]
c = [4, 5, 6, 7, 8]
zipped = zip(a, b)
print(zipped)  # 返回一个对象
```

    <zip object at 0x0000019CC8181BC0>
    

2.list()转换成列表来输出


```python
print(list(zipped))
```

    [(1, 4), (2, 5), (3, 6)]
    

3.长度与最短的对象相同


```python
print(list(zip(a, c)))
```

    [(1, 4), (2, 5), (3, 6)]
    

## ```*```的使用

- ```*```是将矩阵解压成多个列表


```python
 matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
print(zip(*matrix))  # 依旧返回一个对象
for col in zip(matrix):
    print(col)
for col in zip(*matrix):  # 遍历矩阵的每一个列
    print(col)    
```

    <zip object at 0x00000186509D4EC0>
    ([1, 2, 3],)
    ([4, 5, 6],)
    ([7, 8, 9],)
    (1, 4, 7)
    (2, 5, 8)
    (3, 6, 9)
    

# for循环的应用


```python
s = "abcd"
t = "bcdf"
for (i,j) in zip(s,t):
    print(i,j)
```

    a b
    b c
    c d
    d f
    
