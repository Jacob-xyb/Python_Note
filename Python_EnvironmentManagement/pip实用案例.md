# pip install

## 镜像下载

国内镜像

```python
https://pypi.tuna.tsinghua.edu.cn/simple		# 清华大学
https://pypi.douban.com/simple					# 豆瓣(douban) 
https://pypi.mirrors.ustc.edu.cn/simple/		# 中国科技大学 
http://mirrors.aliyun.com/pypi/simple/			# 阿里云 
http://pypi.mirrors.ustc.edu.cn/simple/			# 中国科学技术大学
```

example：

```python
pip install PyQt5 -i https://pypi.douban.com/simple
```

## 导出当前环境包

```python
pip freeze >requirements.txt  # 会保存在你系统默认文件夹，例如：`C:\Users\Administrator\`
pip freeze >D:\requirements.txt
pip freeze >.\requirements.txt
```

## 导出当前项目环境

1. 安装 pipreqs

   `pip install pipreqs`

2. 进入当前项目根目录执行：

   `pipreqs . --encoding=utf8 --force`

   ```python
   # “.” 指的是将导出依赖包的文件放在当前目录下
   # “--encoding=utf8” 指的是存放文件的编码为utf-8,否则会报错
   # “--force” --force 强制执行，当生成目录下的requirements.txt存在时强子覆盖
   ```

3. 新环境安装即可

   `pip install -r requirements.txt`

