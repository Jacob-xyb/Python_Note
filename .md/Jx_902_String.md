# 字符串输出问题

1. 如果想输出: Let's go!


```python
print('let\'s go!')  # 采用 \' 转义符输出
print("let's go!")  # 采用 " ' " 来显示出 '
```

    let's go!
    let's go!
    

2. 如果想输出: C:\now


- `print(r'C:\now\')`  # 原始字符串的结尾加 \ ，是会报错的，是不行的


```python
print('C:\now')  # \n 是换行的意思 是无法输出正确结果的
```

    C:
    ow
    


```python
print(r'C:\now')  # r'' 前缀：原始字符串
# print(r'C:\now\')  # 原始字符串的结尾加 \ ，是会报错的，是不行的
print(r'C:\now'+'\\')  # 只有这样才能在结尾加上 \
```

    C:\now
    C:\now\
    

3. 三重引号字符串


```python
print('''一首小诗''')  # 三重引号可以输出很多段的内容
```

    一首小诗
    

# Python转义字符

**列举一些常用不好记的**

- ```\v``` 纵向制表符


```python
print("Hello \v World!")  # 纵向制表符（按道理说应该会换行...）
```

    Hello  World!
    

# strip()
- **str.strip([chars]);**
- **chars -- 移除字符串头尾指定的字符序列**


```python
str_300 = "*****this is **string** example....wow!!!*****"
print(str_300.strip('*'))  # 指定字符串 *
str_301 = "123abcrunoob321"
print(str_301.strip('12'))  # 字符序列为 12
# 只要头尾包含有指定字符序列中的字符就删除
```

    this is **string** example....wow!!!
    3abcrunoob3
    

# split()

- 描述

    - split() 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则分隔 num+1 个子字符串

- 语法

    - str.split(str="", num=string.count(str))

- 参数

    - str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
    - num -- 分割次数。默认为 -1, 即分隔所有。

- 返回值
    - 返回分割后的字符串列表。



```python
str_2 = "Line1-abcdef \nLine2-abc \nLine4-abcd"
print(str_2.split())        # 以空格为分隔符，包含 \n
print(str_2.split(' ', 1))  # 以空格为分隔符，分隔成两个
```

    ['Line1-abcdef', 'Line2-abc', 'Line4-abcd']
    ['Line1-abcdef', '\nLine2-abc \nLine4-abcd']
    

- 值得注意的是，对应单个字符串时会左右都生成两个空集。


```python
count = '0'
count = count.split()
print(count,len(count))

count = '0'
count = count.split('0')
print(count,len(count))

```

    ['0'] 1
    ['', ''] 2
    

# str.format() and f'{}'

## str.format()
- str.format()是对%-formatting的改进。它使用正常的函数调用语法，并且可以通过对要转换为字符串的对象的`__format __()`方法进行扩展。

- 使用str.format()，替换字段用大括号标记：


```python
"Hello, {}. I am {}.".format("everyone", "Jacob")
```




    'Hello, everyone. I am Jacob.'



- 您可以通过引用其索引来以任何顺序引用变量：


```python
"Hello, {1}. I am {0}.".format("everyone", "Jacob")
```




    'Hello, Jacob. I am everyone.'




```python
"Hello, {1}. I am {0}-{0}.".format("everyone", "Jacob")
```




    'Hello, Jacob. I am everyone-everyone.'



- 但是，如果插入变量名称，则会获得额外的能够传递对象的权限，然后在大括号之间引用参数和方法：


```python
person = {'name': 'Eric', 'age': 74}
"Hello, {name}. You are {age}.".format(name=person['name'], age=person['age'])
```




    'Hello, Eric. You are 74.'



> 你也可以使用**来用字典来完成这个巧妙的技巧：


```python
person = {'name': 'Eric', 'age': 74}
"Hello, {name}. You are {age}.".format(**person)
```




    'Hello, Eric. You are 74.'



> 你也可以使用列表来完成这个巧妙的技巧：


```python
"Hello, {info[0]}. You are {info[1]}.".format(info=['Eric', 74])
```




    'Hello, Eric. You are 74.'



- 敲黑板：


使用str.format()的代码比使用%-formatting的代码更易读，但当处理多个参数和更长的字符串时，str.format()仍然可能非常冗长。看看这个：


```python
first_name = "Eric"
last_name = "Idle"
age = 74
profession = "comedian"
affiliation = "Monty Python"

print(("Hello, {first_name} {last_name}. You are {age}. " +
       "You are a {profession}. You were a member of {affiliation}.").format(
           first_name=first_name,
           last_name=last_name,
           age=age,
           profession=profession,
           affiliation=affiliation))
```

    Hello, Eric Idle. You are 74. You are a comedian. You were a member of Monty Python.
    

## f-Strings

- 一种改进Python格式字符串的新方法

好消息是，F字符串在这里可以节省很多的时间。他们确实使格式化更容易。他们自Python 3.6开始加入标准库。您可以在PEP 498中阅读所有内容。

也称为“格式化字符串文字”，F字符串是开头有一个f的字符串文字，以及包含表达式的大括号将被其值替换。表达式在运行时进行渲染，然后使用__format__协议进行格式化。与往常一样，Python文档是您想要了解更多信息的最佳读物。

- 语法与str.format（）使用的语法类似，但较少细节啰嗦。看看这是多么容易可读：


```python
name = "Eric"
age = 74
f"Hello, {name}. You are {age}."
```




    'Hello, Eric. You are 74.'



使用大写字母F也是有效的：


```python
F"Hello, {name}. You are {age}."
```




    'Hello, Eric. You are 74.'



# 大小写


```python
s = "a duck goes into a bar..."
```

## capitalize()
- 字符串首字母大写


```python
print(s.capitalize())
```

    A duck goes into a bar...
    

## title()
- 所有字母首字母大写


```python
print(s.title())
```

    A Duck Goes Into A Bar...
    

## upper()
- 所有字母大写


```python
print(s.upper())
```

    A DUCK GOES INTO A BAR...
    

## lower() 和 casefold()
- 所有字母小写


```python
print(s.lower())
```

    a duck goes into a bar...
    


```python
print(s.casefold())
```

    a duck goes into a bar...
    

## swapcase()
- 所有字母大小写切换


```python
print(s.swapcase())
```

    A DUCK GOES INTO A BAR...
    

# 排版


```python
s = "a duck goes into a bar..."
```

## center()

- 居中

- 参数：

    - num: 在多少个字符内居中


```python
s.center(30)
```




    '  a duck goes into a bar...   '




```python
s.center(10)  # num小于字符串长度时，返回原字符串
```




    'a duck goes into a bar...'




```python
s.center(80)  
```




    '                           a duck goes into a bar...                            '



## ljust() and rjust()

- 左对齐和右对齐

- 参数：

    - num: 字符范围


```python
s.ljust(30)
```




    'a duck goes into a bar...     '




```python
s.rjust(30)
```




    '     a duck goes into a bar...'



# 相关函数

## 使用join()合并

- join()与split()正好相反。

- 语法：`string.join(list)`


```python
text = ["practice", "makes", "perfect"]
' '.join(text)
```




    'practice makes perfect'



## count()

- 描述

Python count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。

- 语法

count()方法语法：

str.count(sub, start= 0,end=len(string))

- 参数

sub -- 搜索的子字符串

start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。

end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。

- 返回值

该方法返回子字符串在字符串中出现的次数。


```python
s = "a duck goes into a bar..."
print(s.count("a", 1, -1))
```

    2
    

## replace()

- 描述

Python replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。

- 语法

replace()方法语法：

str.replace(old, new[, max])

- 参数

old -- 将被替换的子字符串。

new -- 新字符串，用于替换old子字符串。

max -- 可选字符串, 替换不超过 max 次

- 返回值

返回字符串中的 old（旧字符串） 替换成 new(新字符串)后生成的新字符串，如果指定第三个参数max，则替换不超过 __max__ 次。


```python
s = 'a famous duck goes into a famous bar...'
s = s.replace("duck", "marmoset")
print(s)
```

    a famous marmoset goes into a famous bar...
    

- 字符串是不能直接用索引进行赋值的


```python
s[9:13] = "marmoset"
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-14-0dbd7b4955d9> in <module>
    ----> 1 s[9:13] = "marmoset"
    

    TypeError: 'str' object does not support item assignment


## find()

- 描述

Python find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。

- 语法

find()方法语法：

str.find(str, beg=0, end=len(string))

- 参数

str -- 指定检索的字符串

beg -- 开始索引，默认为0。

end -- 结束索引，默认为字符串的长度。

- 返回值

如果包含子字符串返回开始的索引值，否则返回-1。


```python
exp = "this is string example....wow!!!"
temp = "exam"
print(exp.find(temp))
print(exp.find(temp,10))
print(exp.find(temp,20))
```

    15
    15
    -1
    

# 无函数实现部分功能

## 反转/逆序

- 例如`List`是有函数可以反转的。


```python
l = [1,2,3,4,5,6]
l.reverse()
l
```




    [6, 5, 4, 3, 2, 1]



- `Str`没有此函数，但是可以用通用方法。


```python
l = [1,2,3,4,5,6]
l = l[::-1]
print(l)
s = str(123456)
s = s[::-1]
print(s)
```

    [6, 5, 4, 3, 2, 1]
    654321
    
