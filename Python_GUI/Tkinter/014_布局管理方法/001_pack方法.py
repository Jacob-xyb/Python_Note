# pack() 是一种较为简单的布局方法，在不使用任何参数的情况下，它会将控件以添加时的先后顺序，
# ==> 自上而下，一行一行的进行排列，并且默认居中显示。

from tkinter import *

win = Tk()
win.title("C语言中文网")
win.geometry('450x300+300+300')
lb_red = Label(win, text="红色", bg="Red", fg='#ffffff', relief=GROOVE)
# 默认以top方式放置
lb_red.pack()
lb_blue = Label(win, text="蓝色", bg="blue", fg='#ffffff', relief=GROOVE)
# 沿着水平方向填充，使用 pady 控制蓝色标签与其他标签的上下距离为 5 个像素
lb_blue.pack(fill=X, pady='5px')
lb_green = Label(win, text="绿色", bg="green", fg='#ffffff', relief=RAISED)
# 将 黄色标签所在区域都填充为黄色，当使用 fill 参数时，必须设置 expand = 1，否则不能生效
lb_green.pack(side=LEFT, expand=1, fill=BOTH)
win.mainloop()
