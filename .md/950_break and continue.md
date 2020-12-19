# break
- break语句用来终止循环语句，即循环条件没有False条件或者序列还没被完全递归完，也会停止执行循环语句。

- break语句用在while和for循环中。

- 如果您使用嵌套循环，break语句将停止执行最深层的循环，并开始执行下一行代码。

![示意图](https://www.runoob.com/wp-content/uploads/2014/09/E5A591EF-6515-4BCB-AEAA-A97ABEFC5D7D.jpg)


```python
for letter in 'Python':     # 第一个实例
   if letter == 'h':
      break
   print ('当前字母 :', letter)  # 遇到 'h' 的时候就会退出循环
```

    当前字母 : P
    当前字母 : y
    当前字母 : t
    

# continue
- Python continue 语句跳出本次循环，而break跳出整个循环。

- continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。

- continue语句用在while和for循环中

![示意图](https://www.runoob.com/wp-content/uploads/2014/09/8962A4F1-B78C-4877-B328-903366EA1470.jpg)


```python
for letter in 'Python':     # 第一个实例
   if letter == 'h':
      continue
   print ('当前字母 :', letter)  # 遇到 'h' 会直接进入下一轮循环
```

    当前字母 : P
    当前字母 : y
    当前字母 : t
    当前字母 : o
    当前字母 : n
    


```python
# continue 语句是一个删除的效果，他的存在是为了删除满足循环条件下的某些不需要的成分:
var = 10
while var > 0:
    var = var -1
    if var == 5 or var == 8:
        continue
    print ('当前值 :', var)
print ("Good bye!")
# 这里相当于删除了 5 和 8 的输出
```

    当前值 : 9
    当前值 : 7
    当前值 : 6
    当前值 : 4
    当前值 : 3
    当前值 : 2
    当前值 : 1
    当前值 : 0
    Good bye!
    


```python
# 我们想只打印0-10之间的奇数，可以用continue语句跳过某些循环：
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:      # 如果n是偶数，执行continue语句
        continue        # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
```

    1
    3
    5
    7
    9
    
