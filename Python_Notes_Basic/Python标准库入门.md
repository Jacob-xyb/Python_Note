# os

其实该语句就是在python环境下对文件，文件夹执行操作的一个模块

## os.

### 获取查看操作

- 查看当前系统

```python
import os
print(os.name)  # nt
# Windows NT（New Technology）是微软公司发布的桌面端操作系统，于1993年7月27日发布，该操作系统适用于一部分Windows电脑
```

- 获取当前文件所在路径

  `os.getcwd()`

### 系统文件操作

#### 删除文件

`os.remove(path)`

```python
import os 
os.remove([path])	# 删除指定路径文件

# 1.remove 不能删除文件夹
PermissionError: [WinError 5] 拒绝访问。
# 2.path 不存在时也会报错
FileNotFoundError: [WinError 2] 系统找不到指定的文件。
```

#### 删除空目录

`os.rmdir(dir)`

```python
import os
os.rmdir([dir])

# 如果删除的目录不是空的，会报错
OSError: [WinError 145] 目录不是空的。
```

#### 删除非空目录

**慎用！！！删除时不会有任何提示**

`shutil.rmtree(dir)`

```python
import shutil
shutil.rmtree([dir])
```

## os.path.

![](https://img-blog.csdnimg.cn/20210406141640898.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3FxXzQ1ODAyMDgx,size_16,color_FFFFFF,t_70)