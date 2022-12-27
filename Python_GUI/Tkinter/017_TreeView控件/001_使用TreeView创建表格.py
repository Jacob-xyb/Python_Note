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

# treeview.heading('#0', text='', anchor=tk.CENTER)
# treeview.heading('Rank', text='Id', anchor=tk.CENTER)
# treeview.heading('Name', text='rank', anchor=tk.CENTER)
# treeview.heading('Badge', text='Badge', anchor=tk.CENTER)
#
# treeview.insert(parent='', index=0, iid=0, text='', values=('1', 'Vineet', 'Alpha'))
# treeview.insert(parent='', index=1, iid=1, text='', values=('2', 'Anil', 'Bravo'))
# treeview.insert(parent='', index=2, iid=2, text='', values=('3', 'Vinod', 'Charlie'))
# treeview.insert(parent='', index=3, iid=3, text='', values=('4', 'Vimal', 'Delta'))
# treeview.insert(parent='', index=4, iid=4, text='', values=('5', 'Manjeet', 'Echo'))

window.mainloop()
