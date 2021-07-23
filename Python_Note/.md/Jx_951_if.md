# if的基础应用

## 用列表判断

-输入的类型一定要与列表里的类型对应上


```python
def if_list(key):
    if key in ["hello", "world", 1]:
        print("yes,you are right.")
if_list(1)
```

    yes,you are right.
    

# if的语法进阶

## 简单案例-输出较大的数

### 最普通的写法


```python
a, b = 1, 2
if a>b:
    c = a
else:
    c = b
```

### 一行表达式, 为真时放if前


```python
a, b = 1, 2
c = a if a > b else b
```

### 二维列表，利用大小判断的0，1当作索引


```python
a, b = 1, 2
c = [b, a][a > b]
```

### 传说中的黑客，利用逻辑运算符进行操作，都是最简单的东西，却发挥无限能量


```python
a, b = 1, 2
c = a > b and a or b
```

#### 解释一下

- 利用and的特点，若and前位置为假则直接判断为假，利用or的特点，若or前位置为真则判断为真。

- 从前往后找：and找假，or找真

#### and：前真返后; 前假返前

- 个人理解：and找假：找到假的就返回，没找到就返回后面的


```python
# and：前真返后
print(111 and 222)
print(111 and 000)
# and：前假返前
print(000 and 111)
print(000 and '')
```

    222
    0
    0
    0
    

#### or：前真返前； 前假返后
- - 个人理解：or找假：找到真的就返回，没找到就返回后面的


```python
# or：前真返前
print(111 or 000)
print(111 or 111)
# or：前假返后
print(000 or 111)
print('' or 000)
```

    111
    111
    111
    0
    
