# map()

map() 会根据提供的函数对指定序列做映射。

第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。

- 语法：

    `map(function, iterable, ...)`
    
- 参数：

    function -- 函数

    iterable -- 一个或多个序列


```python
def square(x) :         # 计算平方数
    return x ** 2
```


```python
map(square, [1,2,3,4,5])  # 返回迭代器
```




    <map at 0x17900749e50>




```python
list(map(square, [1,2,3,4,5]))
```




    [1, 4, 9, 16, 25]




```python
list(map(lambda x: x ** 2, [1, 2, 3, 4, 5]))  # 使用 lambda 匿名函数
```




    [1, 4, 9, 16, 25]


