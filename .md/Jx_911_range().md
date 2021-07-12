# range()
## 语法
> range([start,] stop [, step=1])

- 这个BIF有三个参数，其中括起来的参数是可选的。
- 生成一个从[start,stop)的数字序列


```python
print(range(1,10))
```

    range(1, 10)
    

### class list([iterable])
- 构造函数生成一个列表，该列表的项与iterable的项相同且顺序相同。iterable可以是序列，支持迭代的容器或迭代器对象。如果iterable已经是一个列表，则复制并返回一个副本，类似于iterable[:]。
- 例如，list('abc')return ['a', 'b', 'c']和list( (1, 2, 3) )return [1, 2, 3]。如果未提供任何参数，则构造函数将创建一个新的空列表[]。


```python
list(range(10))  # list[]
```




    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




```python
'''常用于for循环'''
# for i in range(5):
#     print(i)
```




    '常用于for循环'



## 步长 step


```python
# 这里不用写关键字 step=2,会报错的！ 直接range(start,stop,step)就OK
list(range(0,9,2))
```




    [0, 2, 4, 6, 8]




```python
# 步长是可以负着写的哟
list1 = list(range(9,0,-1))
print(list1)
```

    [9, 8, 7, 6, 5, 4, 3, 2, 1]
    
