import tkinter as tk

# 创建窗口
window = tk.Tk()
window.geometry('450x300+300+300')


# 设置回调函数
def callback():
    print("click me!")


# 使用按钮控件调用函数
tk.Button(window, text="点击执行回调函数", command=callback).pack()

# 控件的 width 是字符数
tk.Button(window, text="hello", command=callback, width=4).pack()

# 显示窗口
tk.mainloop()
