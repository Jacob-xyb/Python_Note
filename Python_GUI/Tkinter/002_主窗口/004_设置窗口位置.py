import tkinter as tk

window = tk.Tk()


# 设置屏幕位置
# window.geometry('450x400+300+200')

# 屏幕居中的方式：
def set_center(window, width, height):
    # window.update()
    # 窗口居中，获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    window.geometry(size_geo)


set_center(window, 450, 400)
window.mainloop()
