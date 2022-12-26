import tkinter as tk

window = tk.Tk()


def set_center(window, width, height):
    # window.update()
    # 窗口居中，获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    size_geo = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    window.geometry(size_geo)


set_center(window, 450, 400)

# 若内容是文字则以字符为单位，图像则以像素为单位
label = tk.Label(
    window,
    text="网址：c.biancheng.net",  # 用来指定 Lable 显示的文本，注意文本内可以包含换行符
    # 控制文本（或图像）在 Label 中显示的位置（方位），
    # 通过方位的英文字符串缩写（n、ne、e、se、s、sw、w、nw、center）实现定位，默认为居中（center）
    anchor="center",
    # 指定 Lable 中文本的 (字体,大小,样式）元组参数格式，一个 Lable 只能设置一种字体
    font=('宋体', 20, 'bold italic'),
    bg="#7CCD7C",  # 背景色
    # 设置标签内容区大小
    width=30, height=5,
    # 设置填充区距离、边框宽度
    padx=20, pady=15, borderwidth=10,
    # 指定边框样式，默认值是 "flat"，其他参数值有 "groove"、"raised"、"ridge"、"solid"或者"sunken"
    # relief="sunken",
)
label.pack()

window.mainloop()
