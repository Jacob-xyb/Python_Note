# 资源汇总

  可以直接从包和模块的基本操作开始看，模块详解将的比较杂乱，晦涩。

- b站链接

 [b站模块详解学习视频](https://www.bilibili.com/video/BV194411r7a8?p=1)

# 基本概念

## 模块 module

一般情况下，module 是一个以`.py`为后缀的文件。

其他可作为module的文件类型还有".pyo"、".pyc"、".pyd"、".so"、".dll"，但Python初学者几乎用不到。

module 可看作一个工具类，可共用或者隐藏代码细节，将相关代码放置在一个module以便让代码更好用、易懂，让coder重点放在高层逻辑上。 

module能定义函数、类、变量，也能包含可执行的代码。

## 包 package

为避免模块名冲突，Python引入了按目录组织模块的方法，称之为 包（package）。

包 是含有Python模块的文件夹。

  ![](https://i.loli.net/2021/07/14/8bgEYVNSHlPwBvr.png)  

​    当一个文件夹下有 `__init__.py` 时，意为该文件夹是一个包（package），其下的多个模块（module）构成一个整体，而这些模块（module）都可通过同一个包（package)导入其他代码中。  

## 包和模块来源

**包和模块来源有3种：**

- **标准库**

就是python安装环境中自带的库。

其中**内置库**不需要导入，意思就是在我们编码的过程中，python自动帮我们导入的模块，比如`print`函数。

既然有函数，就一定封装在一个模块里面，这个模块就是`__builtin__`；

```py
# py2.7
import __builtin__
print(dir(__builtin__))

# 在python3.x中，内置的模块名有所改变 在某些IDE中，并不支持以上兼容，所以python3有自己的特有写法
import builtins
print(dir(builtins))
```

- **第三方模块**
- **自定义模块**

# 包和模块的创建

## 创建模块

**直接创建一个 .py 文件即可**

## 创建包

**创建一个文件夹，文件夹内务必创建一个 \__init__.py 的文件**

> py3.3+ 可以不用创建了，但是为了兼容以及一些其他包处理，还是建议默认创建

### \__init__.py 的作用

`__init__.py` 文件 用于组织包（package），方便管理各个模块之间的引用、控制着包的导入行为。 


该文件可以什么内容都不写，即为空文件（为空时，仅仅用import [该包]形式 是什么也做不了的），存在即可，相当于一个标记。  

 不建议在 `__init__.py` 中写模块，以保证该文件简单。不过可在 `__init__.py` 导入我们需要的模块，以便避免一个个导入、方便使用。

但若想使用 `from pacakge_1 import *` 这种形式的写法，需在 `__init__.py` 中加上：

```py
__all__ = [‘file_a’, ‘file_b’] #package_1下有file_a.py和file_b.py
```

这样就导入了 `file_a` 和 `file_b` 两个变量

### \__all__ 变量

使用`__all__`定义模块访问白名单

其中，`__all__` 是一个重要的变量，用来指定此包（package）被 `import *` 时，那些模块（module）会被import进【当前作用域中】。不在`__all__` 列表中的模块不会被其他程序引用。  

1. 只对“from package import *”导入产生影响，对“import package.module”或“from package import module”不产生影响；
2. 在`__all__`列表中的元素不论是否带下划线开头，“from 模块名 import *”都会导入，不受模块的缺省封装机制影响，可以说这是另一种方式的封装；
3. 在模块定义`__all__`变量后，可以使用 `模块.__all__` 查看模块建议使用的模块成员。

### \__path__ 变量

`__path__`也是一个常用变量，是个列表，默认情况下只有一个元素，即当前包（package）的路径。修改 `__path__` 可改变包（package）内的搜索路径。

当我们在导入一个包（package）时（会先加载  `__init__.py` 定义的引入模块，然后再运行其他代码），实际上是导入的它的 `__init__.py` 文件（导入时，该文件自动运行，助我们一下导入该包中的多个模块）。我们可以在 `__init__.py` 中再导入其他的包（package）或 模块 或 自定义类。

# 包和模块的基本信息

## 包和模块的名称

`包`的名称即是`文件夹`的名称。

`模块`的名称即是`module.py`的名称，导入时不需要加`.py`后缀。  

## 一些常用操作

- **package.\__file__**

  获取 package 所在路径

  ```py
  import os
  print(os.__file__)
  # D:\ProgramData\Miniconda3\lib\os.py
  ```

- **dir(package)**

  获取 package 所有的API
  
  ```py
  import os
  print(dir(os))
  ```
  
# 包和模块的导入方式

## 常规导入

- 形如 `import M`

  导入单个模块
  
- 形如  `import M1, M2`

  导入多个模块
  
- 形如 `import M1 as Jx`

  对导入的包和模块起一个别名，调用时输入别名即可。使用别名后，M1就无法调用了。
  
- 形如 `import P`

  **如果导入的是一个包名，而没有模块时，代码是不会报错的，但是并不会自动导入这个包里面的任何模块。**
  
  ```py
  # P 包中有 p1.py p2.py p3.py
  import P 
  P.p1 # 会报错，且不会执行 p1,p2,p3模块内的内容。
  ```
  
  但是导入任何一个包时，都会自动的去运行当前包的`__init__.py`文件，这个文件里面可以自由导入所需模块，需要使用绝对路径来导入，涉及到 `包和模块的检索路径问题`，后续再详细讲解。

## from语句导入

- 想要导入一个模块或包中的某个部分。`from A import B [as C]`

  from语句导入只能是`from package import module`或者`from module import function`，形如`from package import module.function`或者`from package import package.module`都是不可以的；

  因为 import 后面必须是最简化的内容，不允许出现 `xx.xx` 。

  **例如：**

  ```py
  from P import sub_P.sp1	# SyntaxError: invalid syntax
  ```

- 特殊的`from module import *`或者`from package import *`。

  对于`from module import *`，没有`__all__`变量时，在运用此方法时会导入模块中的全部对象。
  
  > `_`开头的除外，因为`_`开头的为私有对象，无法导入；但是 from module import _name 显式导入私有变量是可以的。
  
  如果只想引用时导入部分有用的变量，可以使用 `__all__ = ["name1","name2"]` 来自定义，`__all__`的位置对模块的导入没有影响，但是放在最前面是比较合理的方式。
  
  > 注意，`__all__`变量内记录的是字符串。
  
  对于`from package import *`，此时如果你的`__init__.py`内没有指定导入的模块或包时，就会什么都不导入。但是，都会将`__init__.py`执行一遍。

# import 运行机制

**最重要的几点机制：**

1. import 多次包和模块时，永远只会导入**一次**文件，不同的是命名空间不同而已。

## import package

1. import package 时，必定会执行 package 的 \__init__ .py  文件。

![image.png](https://s2.loli.net/2022/10/20/fqvRP9VWKFB6rcg.png)

```py
# **mian.py**
# 无论怎样导入，均会执行 tool 的 __init__.py 文件内的所有语句

import tool
import tool.t1
from tool import *
```

2. 以任何方式 import package 时，均可获取 \__init__.py 文件内的对象

```py
# **mian.py**
# 假设 tool 的 __init__.py 文件内有一个变量为 init_num = 10

# 方式1
def import1():
    import tool
    print(tool.init_num)
   
# 方式2
def import2():
    import tool.t1
    print(tool.init_num)
   
# 方式3
from tool import *
print(init_num)
```

3. **注意：** `from tool import *` 语句只能在 **模块**（也就是.py文件）中执行，函数内无法执行。

   ```py
   SyntaxError: import * only allowed at module level
   ```
