# https://www.bilibili.com/read/cv15914394

import tkinter as tk
import tkinter.ttk as ttk

window = tk.Tk()

treeview = ttk.Treeview(master=window)
treeview.pack()

treeview['columns'] = ('Rank', 'Name', 'Badge')
treeview.column('#0', width=0, stretch=tk.NO)
treeview.column('Rank', anchor=tk.CENTER, width=80)
treeview.column('Name', anchor=tk.CENTER, width=80)
treeview.column('Badge', anchor=tk.CENTER, width=80)

treeview.heading('#0', text='', anchor=tk.CENTER)
treeview.heading('Rank', text='Id', anchor=tk.CENTER)
treeview.heading('Name', text='rank', anchor=tk.CENTER)
treeview.heading('Badge', text='Badge', anchor=tk.CENTER)

treeview.insert(parent='', index=0, iid=0, text='', values=('1', 'Vineet', 'Alpha'))
treeview.insert(parent='', index=1, iid=1, text='', values=('2', 'Anil', 'Bravo'))
treeview.insert(parent='', index=2, iid=2, text='', values=('3', 'Vinod', 'Charlie'))
treeview.insert(parent='', index=3, iid=3, text='', values=('4', 'Vimal', 'Delta'))
treeview.insert(parent='', index=4, iid=4, text='', values=('5', 'Manjeet', 'Echo'))


def selectjob(event):
    print('----------')
    print('iid=', treeview.selection())  # 输入选中的行的iid值
    print(treeview.item(treeview.selection()))  # 输出选中行的各参数值的键值对字典
    print('text=', treeview.item(treeview.selection(), option='text'))  # 输出某个参数的值
    pop_window()


def pop_window():
    child_window = tk.Toplevel(window)
    child_window.title('')
    child_window.geometry("600x400")
    window.attributes('-disabled', True)
    window.wait_window(child_window)
    window.attributes('-disabled', False)
    # window.state("normal")
    window.deiconify()


treeview.bind("<<TreeviewSelect>>", selectjob)  # 某行被选中事件

window.mainloop()
