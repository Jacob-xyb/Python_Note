"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2023/1/13 16:38"
"""

# https://huaweicloud.csdn.net/63806abfdacf622b8df87704.html?q=Python%20tkinter

import tkinter as tk

window = tk.Tk()
window.geometry('300x240')
entry = tk.Entry(window)
# 目前这样是不会显示控件的

# region # 基础属性
# 控件自身返回的宽度单位是字符数，而不是px
print(entry['width'])  # 返回的字符数,默认20

# bd: 边框宽度
entry.config(bd=2)

# cursor: 设置鼠标样式
entry.config(cursor='mouse')
# endregion

# 插入光标的边框显示
entry.config(insertbackground='red', insertborderwidth=1)


entry.pack()

window.mainloop()
