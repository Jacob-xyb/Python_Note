# -*- coding:utf-8 -*-
import tkinter as tk

root_window = tk.Tk()
# 设置窗口title
root_window.title('C语言中文网：c.biancheng.net')
# 设置窗口大小:宽x高,注,此处不能为 "*",必须使用 "x"
root_window.geometry('450x300')
# 更改左上角窗口的的icon图标,加载C语言中文网logo标
root_window.iconbitmap('favicon.ico')
# 设置主窗口的背景颜色,颜色值可以是英文单词，或者颜色值的16进制数,除此之外还可以使用Tk内置的颜色常量
root_window["background"] = "#C9C9C9"
# 添加文本内,设置字体的前景色和背景色，和字体类型、大小
text = tk.Label(root_window, text="C语言中文网，欢迎您", bg="yellow", fg="red", font=('Times', 20, 'bold italic'))
# 将文本内容放置在主窗口内
text.pack()
# 添加按钮，以及按钮的文本，并通过command 参数设置关闭窗口的功能
button = tk.Button(root_window, text="关闭", command=root_window.quit)
# 将按钮放置在主窗口内
button.pack(side="bottom")
# 进入主循环，显示主窗口
root_window.mainloop()
