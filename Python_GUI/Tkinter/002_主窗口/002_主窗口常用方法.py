import tkinter as tk

window = tk.Tk()

# 1.设置窗口title
window.title('C语言中文网')

# 2.是否允许用户拉伸主窗口大小，默认为可更改，当设置为 resizable(False,False)时不可更改
# window.resizable(False, False)

# 3.设定主窗口的大小以及位置，当参数值为 None 时表示获取窗口的大小和位置信息。
window.geometry('450x300')

# 4.获取电脑屏幕的大小
print("电脑的分辨率是%dx%d" % (window.winfo_screenwidth(), window.winfo_screenheight()))

# 5.要求窗口的大小，必须先刷新一下屏幕
# ==> 同样也适用于其他控件，但是使用前需要使用 window.update() 刷新屏幕，否则返回值为1
window.update()
print("窗口的分辨率是%dx%d" % (window.winfo_width(), window.winfo_height()))
print(window.geometry())

# 6.改变背景颜色
window.config(background="#6fb765")

# 7.设置窗口处于顶层
# window.attributes('-topmost', True)

# 8.设置窗口的透明度
# window.attributes('-alpha', 0.5)

# 9.设置窗口被允许最大最小调整的范围，与resizble()冲突
window.maxsize(600, 600)
window.minsize(50, 50)

# 10.更改左上角窗口的的icon图标
# window.iconbitmap('favicon.ico')

# 11.关闭当前窗口
# window.quit()

# 12.用来设置窗口的显示状态，参数值 normal（正常显示），icon（最小化），zoomed（最大化），
window.state("normal")

# 13.用来隐藏主窗口，但不会销毁窗口。
# window.withdraw()
# ==> window.deiconify() 将窗口从隐藏状态还原
# window.deiconify()

# 14.最小化窗口
window.iconify()

# 进入主循环，显示主窗口
window.mainloop()
