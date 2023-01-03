import tkinter as tk

root = tk.Tk()

root.geometry('500x300+100+100')
root.title('辞职信')

frame1 = tk.Frame(root)
frame1.pack()

label1 = tk.Label(frame1, text="尊敬的各位领导:", font=24, padx=30, pady=30)
label1.pack()
label1.pack(side=tk.LEFT, anchor=tk.N)
# tk.Label(frame1, text="", font=24, padx=30, pady=30, width=10).pack(side=tk.RIGHT, anchor=tk.N)

frame2 = tk.Frame()

root.mainloop()
