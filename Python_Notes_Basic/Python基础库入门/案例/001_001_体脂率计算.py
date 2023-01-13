"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2023/1/13 17:23"
"""

import tkinter as tk

root = tk.Tk()
root.geometry('200x200+400+200')

label_height = tk.Label(root, text='身高:')
var_height = tk.StringVar()
entry_height = tk.Entry(root, textvariable=var_height)

label_weight = tk.Label(root, text='体重:')
var_weight = tk.StringVar()
entry_weight = tk.Entry(root, textvariable=var_weight)

label_age = tk.Label(root, text='年龄:')
var_age = tk.StringVar()
entry_age = tk.Entry(root, textvariable=var_age)

label_gender = tk.Label(root, text='性别:')
var_gender = tk.StringVar()
entry_gender = tk.Entry(root, textvariable=var_gender)


def calculate_result():
    pass


btn_calculate = tk.Button(text="计算", command=calculate_result)

var_result = tk.StringVar()
label_result = tk.Label(textvariable=var_result)


label_height.grid(row=0, column=0)
entry_height.grid(row=0, column=1)
label_weight.grid(row=1, column=0)
entry_weight.grid(row=1, column=1)
label_age.grid(row=2, column=0)
entry_age.grid(row=2, column=1)
label_gender.grid(row=3, column=0)
entry_gender.grid(row=3, column=1)
btn_calculate.grid(row=4, column=0, columnspan=2)
label_result.grid(row=5, column=0, columnspan=2)

root.mainloop()
