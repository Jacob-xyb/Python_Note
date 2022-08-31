# Python关键字

保留字即关键字，我们不能把它们用作任何标识符名称。Python 的标准库提供了一个 keyword 模块，可以输出当前版本的所有关键字：

```python
# Python 3.8
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))		# 35

['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

或者直接执行 `help("keywords")`:

```python
Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not      
```

## 简单的关键字

- **有关定义的关键字**

```python
def : 定义一个函数或方法；
class: 定义一个类对象；
lambda：定义一个匿名函数；
```

- **布尔关键字**

```python
False:代表真	# 与C++不同，只有bool(0)是False
True：代表假
```

- **控制流关键字**

```python
if...elif...else...:条件判断；
for...in...:对可迭代对象循环遍历
for...in...else...:遍历正常完成则执行else后的代码；
continue:终止本次循环，继续下一次循环；
break：跳出循环；
while：循环结构；
```

- **逻辑判断关键字**

```python
and:表示与
or：表示或；
not：表示非；
in：判断元素是否在容器内；
not in：判断元素是否不再容器内；
is:比较两个变量的内存地址；
```

- **异常**

```python
try:
代码1
except:
代码2
else：
代码3
finally：
代码4...
 
# 代码1发生异常就执行代码2，正常就执行代码3，无论正常与否都要执行代码4.
 
raise：主动触发异常；
```

- **其他**

```python
None:代表空，是python解释器的一个内置的关键字变量；本质是一个object()
from ... import ...:从模块导入对象
import ... :导入模块
import ... as ...:导入模块指定别名
with:触发上下文管理器；
assert：断言，True则通过，False则触发异常；
pass：表示跳过，用来防止报错；
return：函数返回值；
yield：生成器关键字；
del：从上下文堆栈中删除某个对象。
```

# 命令空间

`global` :将模块空间变量引入到局部空间修改；

`nonlocal` :将本局部空间的外层空间变量引入到本层局部空间修改，用来嵌套函数内；

