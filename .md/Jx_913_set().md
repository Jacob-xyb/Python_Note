# Python set() 函数

- 描述

    - set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
    - ```似乎对纯数字是有序的，升序```
- 语法

    - class set([iterable])
 
- 参数

    - iterable -- 可迭代对象对象；
- 返回值

    - 返回新的集合对象。


- 实例

- ```set()```后的对象是无序的,字典类型


```python
x = set('runoob')
print(set(x), type(set(x)))
```

    {'u', 'n', 'o', 'r', 'b'} <class 'set'>
    

- 可以转换成列表


```python
print(list(set(x)))
```

    ['u', 'n', 'o', 'r', 'b']
    

- 可以计算差集

    - 只能大的```－```小的哟


```python
l1 = [0,1,2,3,4,5,6]
l2 = [3,4,5]
print(set(l1)-set(l2))
```

    {0, 1, 2, 6}
    


```python
set(range(10))
```




    {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}



- 多维列表

不能set()多维列表


```python
ln = [[1,2],[2,3],[1,2]]
set(ln)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-2-6c3334f0d139> in <module>
          1 ln = [[1,2],[2,3],[1,2]]
    ----> 2 set(ln)
    

    TypeError: unhashable type: 'list'


# 集合:set()

- 描述

    - set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
    - ```似乎对纯数字是有序的，升序```


## add()

- 添加新的元素到集合中。

"如果添加的元素已经存在于set中，add()不会报错，但是不会加进去了"


```python
even_number = {0, 2, 4, 6, 8}
even_number.add(2)  # 添加重复元素并不会改变原集合
print(even_number)
even_number.add(10)
print(even_number)
```

    {0, 2, 4, 6, 8}
    {0, 2, 4, 6, 8, 10}
    

如果是纯数字集合，添加的时候会自动排序


```python
number = {3, 4, 6, 7}
number.add(5)
print(number)
```

    {3, 4, 5, 6, 7}
    

显然字符串就是乱序的


```python
word = {'c', 'd', 'x', 'z'}
word.add('f')
print(word)
```

    {'c', 'f', 'z', 'd', 'x'}
    
