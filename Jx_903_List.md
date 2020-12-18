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
    

### pop()后不会改变列表id地址


```python
list2_1 = ['Google', 'Runoob', 'Taobao']
print(list2_1, id(list2_1))
list2_1.pop()
print(list2_1, id(list2_1))  # 利用pop()不会改变对象地址的改变。
list2_1 = ['Google', 'Runoob']
print(list2_1, id(list2_1)) #  = 是赋值语句，会创建一个新列表，就算内容不变，id也会改变，意思就是对象已经改变了。 
```

    ['Google', 'Runoob', 'Taobao'] 2493290164672
    ['Google', 'Runoob'] 2493290164672
    ['Google', 'Runoob'] 2493290437632
    

## del 删除列表元素 


```python
list3 = ['Google', 'Runoob', 'Taobao']
del list3[1]  # 输出列表的某个元素
print(list3)
```

    ['Google', 'Taobao']
    


```python
list3_1 = ['Google', 'Runoob', 'Taobao']
del list3_1[0:2]  # 发现一次性删除一个片段也是可行的
print(list3_1)
```

    ['Taobao']
    

## append() 和 extend() 
### 描述

- append() 方法用于在列表末尾添加新的对象。

- extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。

### 语法

- append()方法语法：

```python
list.append(obj)
```

- extend()方法语法：

```python
list.extend(seq)
```

### append()参数

- obj -- 添加到列表末尾的对象。

### extend()参数

- seq -- 元素列表，可以是列表、元组、集合、字典，若为字典,则仅会将键(key)作为元素依次添加至原列表的末尾。

### 返回值

- 该方法无返回值，但是会修改原来的列表。

### 如何在列表后面添加多个参数呢？？？


```python
# 首先 append() 只能添加一个参数
list4 = ['Google', 'Runoob', 'Taobao']
list4.append('hello', 'python')  # 这样添加是会报错的
print(list4)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-8-e98d147d396f> in <module>
          1 # 首先 append() 只能添加一个参数
          2 list4 = ['Google', 'Runoob', 'Taobao']
    ----> 3 list4.append('hello', 'python')  # 这样添加是会报错的
          4 print(list4)
    

    TypeError: append() takes exactly one argument (2 given)



```python
# 但是 extend() 是可以添加多个的
list4_1 = ['Google', 'Runoob', 'Taobao']
list4_1.extend('hello', 'python')  # 这样添加也是会报错的
print(list4_1)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-9-6ad66d8b0a6d> in <module>
          1 # 但是 extend() 是可以添加多个的
          2 list4_1 = ['Google', 'Runoob', 'Taobao']
    ----> 3 list4_1.extend('hello', 'python')  # 这样添加也是会报错的
          4 print(list4_1)
    

    TypeError: extend() takes exactly one argument (2 given)



```python
# 首先要了解 extend() 的原理 ；是用新列表扩展原来的列表，所以输入应该是一个可以迭代的序列才对！
list4_2 = ['Google', 'Runoob', 'Taobao']
list4_2.extend(['hello', 'python'])  # 这样就可以啦
print(list4_2)
list4_3 = ['Google', 'Runoob', 'Taobao']
list4_3.append(['hello', 'python'])  # 同样的参数，如果append会发生什么呢
print(list4_3)
# 这下区分了extend() 和 append() 的区别了吗？
```

    ['Google', 'Runoob', 'Taobao', 'hello', 'python']
    ['Google', 'Runoob', 'Taobao', ['hello', 'python']]
    

### append() 扩展

- append() 是浅拷贝，如果在 append 一个对象时，需要特别注意：

> append 的值其实是对象，拷贝的对象，会随着对象的变化而变化，让我们一起看看吧~

> 会在当前项目专门立一个文档讲解：浅复制和深复制。


```python
# 实例1
list4_4 = ['Google', 'Runoob', 'Taobao']
list_append = 'hello'
list4_4.append(list_append)
print(list4_4)  # 现在 'hello' 已经被添加到 list 中了
list_append = 'goodbye'  # 现在改变被添加的对象
print(list4_4)  # what?! 列表没有被改变
print(list_append)  # 对象的确是改变了，但是列表就是没有变化！
# 那我们看看前后list_append的地址有没有变化吧
```

    ['Google', 'Runoob', 'Taobao', 'hello']
    ['Google', 'Runoob', 'Taobao', 'hello']
    goodbye
    


```python
# 实例1+
list4_5 = ['Google', 'Runoob', 'Taobao']
list_append = 'hello'
list4_5.append(list_append)
print("被添加对象的地址:",list_append, id(list_append))
print(list4_4, id(list4_4[-1]))  # 现在 'hello' 已经被添加到 list 中了
list_append = 'goodbye'  # 现在改变被添加的对象
print("被添加对象的地址:",list_append, id(list_append))
print(list4_4, id(list4_4[-1]))  # what?! 列表没有被改变
print(list_append)  # 对象的确是改变了，但是列表就是没有变化！
# list_append的对象改变了，但是列表的地址是没有变化的。
```

    被添加对象的地址: hello 2493290681968
    ['Google', 'Runoob', 'Taobao', 'hello'] 2493290681968
    被添加对象的地址: goodbye 2493290607280
    ['Google', 'Runoob', 'Taobao', 'hello'] 2493290681968
    goodbye
    


```python
# 实例2
alist = []
num = [2]
alist.append(num)
print(id(num),id(alist[0]))
print(alist)
num.pop()
print(id(num),id(alist[0]))
print(alist)
# 被添加的对象有了变化但是地址没有变，所以列表就有了变化
```

    2493290416000 2493290416000
    [[2]]
    2493290416000 2493290416000
    [[]]
    


```python
# 实例2+
alist = []
num = [2]
alist.append(num)
print(id(num),id(alist[0]))
print(alist)
num = [0]
print(id(num),id(alist[0]))
print(alist)
# 被添加的对象被新建了，所以append还是记录原来的对象地址，所以没有变化。
```

    2493290437760 2493290437760
    [[2]]
    2493290416000 2493290437760
    [[2]]
    

### extend() 扩展

- extend()可以将所有类型的输入整合成列表的形式添加到原列表中：


```python
# 扩展列表
list4_6 = ['Google', 'Runoob', 'Taobao']
list4_7 =list(range(5)) # 创建 0-4 的列表
list4_6.extend(list4_7)  # 扩展列表
print ("扩展后的列表：", list4_6)  # 一个列表被整合到list中了
```

    扩展后的列表： ['Google', 'Runoob', 'Taobao', 0, 1, 2, 3, 4]
    


```python
# 扩展元祖
list4_6 = ['Google', 'Runoob', 'Taobao']
list4_7 = tuple(range(5)) # 创建 0-4 的元祖
list4_6.extend(list4_7)  # 扩展列表
print ("扩展后的列表：", list4_6)  # 一个列表被整合到list中了
```

    扩展后的列表： ['Google', 'Runoob', 'Taobao', 0, 1, 2, 3, 4]
    


```python
# 扩展字典
# 若为字典,则仅会将键(key)作为元素依次添加至原列表的末尾
list4_6 = ['Google', 'Runoob', 'Taobao']
list4_7 = {0,1,2,3,4} # 创建 键值为 0-4 的字典
list4_6.extend(list4_7)  # 扩展列表
print ("扩展后的列表：", list4_6)  # 一个列表被整合到list中了
```

    扩展后的列表： ['Google', 'Runoob', 'Taobao', 0, 1, 2, 3, 4]
    

## list 的加减乘除

### list的加法

- list的加法好像是直接将列表添加到后面，不，应该是扩展到后面。
- list的加法是深复制哦~


```python
list5 = [1, 2, 3]
list5_1 = [1, 2, 3]
list5_2 = list5 + list5_1 
print(list5_2, id(list5_2))
list5_1.pop()
print(list5_2, id(list5_2))
```

    [1, 2, 3, 1, 2, 3] 2202586639616
    [1, 2, 3, 1, 2, 3] 2202586639616
    

### 所以减乘除都没有咯


```python
print([1,2,3]-[1,1,1])  # 果然报错了~
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-14-0a6a8298db3f> in <module>
    ----> 1 print([1,2,3]-[1,1,1])  # 果然报错了~
    

    TypeError: unsupported operand type(s) for -: 'list' and 'list'

