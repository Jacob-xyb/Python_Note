# https://www.bilibili.com/read/cv15914394
import time
import tkinter as tk
import tkinter.ttk as ttk
import threading


def thread_it(func, *args):
    '''将函数打包进线程'''
    # 创建
    t = threading.Thread(target=func, args=args)
    # 守护 !!!
    t.setDaemon(True)
    # 启动
    t.start()
    # 阻塞--卡死界面！
    # t.join()


def cycle_insert():
    items = [('1', 'Vineet', 'Alpha'),
             ('2', 'Anil', 'Bravo'),
             ('3', 'Vinod', 'Charlie'),
             ('4', 'Vimal', 'Delta'),
             ('5', 'Manjeet', 'Echo')]

    for i in range(len(items)):
        treeview.insert(parent='', index=i, iid=str(i), text='', values=items[i])
        time.sleep(1)
        window.update()     # 有效解决 假死状态


window = tk.Tk()

treeview = ttk.Treeview(master=window)
tk.Button(text="click", command=cycle_insert).pack()
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
