"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2023/1/16 11:24"
"""

import tkinter as tk

root = tk.Tk()
root.geometry('204x180+400+200')

label_height = tk.Label(root, text='身高(m):')
var_height = tk.StringVar()
entry_height = tk.Entry(root, textvariable=var_height)

label_weight = tk.Label(root, text='体重(kg):')
var_weight = tk.StringVar()
entry_weight = tk.Entry(root, textvariable=var_weight)

label_age = tk.Label(root, text='年龄:')
var_age = tk.StringVar()
entry_age = tk.Entry(root, textvariable=var_age)

label_gender = tk.Label(root, text='性别:')
var_gender = tk.StringVar()
entry_gender = tk.Entry(root, textvariable=var_gender)


def calculate_result():
    # BMI = 体重(kg) / (身高 * 身高)(米)
    # 体脂率 = 1.2 * BMI + 0.23 * 年龄 - 5.4 - 10.8*性别（男：1 女：0）
    # 正常成年人的体脂率分别是男性15%~18%和女性25%~28%
    weight = float(var_weight.get())
    height = float(var_height.get())
    age = int(var_age.get())
    gender = 1 if var_gender.get() == "男" or "male" else 0

    BMI = weight / height ** 2
    body_fat_rate = 1.2 * BMI + 0.23 * age - 5.4 - 10.8 * gender

    flag = [True, "正常"]

    if gender == 1:
        if body_fat_rate < 15:
            flag = [False, "偏瘦"]
        elif body_fat_rate > 18:
            flag = [False, "偏胖"]
    else:
        if body_fat_rate < 25:
            flag = [False, "偏瘦"]
        elif body_fat_rate > 28:
            flag = [False, "偏胖"]
    var_result.set(f"体脂率：{body_fat_rate:.6f} {flag[1]}")


btn_calculate = tk.Button(text="计算", command=calculate_result)

var_result = tk.StringVar()
label_result = tk.Label(root, textvariable=var_result)

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
