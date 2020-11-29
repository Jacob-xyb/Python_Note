# List 列表

## sort() 
### 描述
- sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。
### 语法
```python
list.sort(cmp=None, key=None, reverse=False)
```
### 参数
- cmp -- 可选参数, 如果指定了该参数会使用该参数的方法进行排序。
- key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
- reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。


```python
lista = [9,7,1,0,8,2,5,3]
list1 = lista.sort()
print(lista, list1)
# list.sort() 是对原列表进行排序，直接改变了原对象，而不会返回一个对象，所以list_1输出是None.
```

    [0, 1, 2, 3, 5, 7, 8, 9] None
    


```python
# 列表
vowels = ['e', 'a', 'u', 'o', 'i']
# 降序
vowels.sort(reverse=True)
# 输出结果
print(vowels)
# 可以反转排序，并且可以对字母进行排序
```

    ['u', 'o', 'i', 'e', 'a']
    


```python
# 获取列表的第二个元素
def takeSecond(elem):
    return elem[1] 
# 列表
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
# 指定第二个元素排序
random.sort(key=takeSecond)
# 输出类别
print(random)
```

    [(4, 1), (2, 2), (1, 3), (3, 4)]
    

## pop() 
### 描述
- pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。
### 语法
```python
list.pop([index=-1])
```
### 参数
- obj -- 可选参数，要移除列表元素的索引值，不能超过列表总长度，默认为 index=-1，删除最后一个列表值。


```python
list2 = ['Google', 'Runoob', 'Taobao']
list_pop=list2.pop(1)
print('被删除的对象：', list_pop)  # pop()还会返回被删除的对象 # 用于接收被删除的对象很有用，相当于弹出的过程
print('原列表变为了：', list2)
```

    被删除的对象： Runoob
    原列表变为了： ['Google', 'Taobao']
    
