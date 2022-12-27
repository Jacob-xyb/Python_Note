# Treeview

Tkinter模块的Treeview组件类似于Dev中的treelist控件，但前者还可以当做树控件和表格控件使用，虽然功能可能没有dev和winform控件那么强大，但是在Tkinter中算是比较复杂、用处较多的了。

Treeview 组件左侧可以理解为一个树控件，右侧可以理解为一个表格，一个数据条目占据一行，横跨树控件和表格控件。Treeview 组件用show属性设置显示方式，值为tree则仅显示树控件，值为headings默认仅显示表格，值为tree headings则显示全部，默认为显示全部。Treeview 组件使用#0引用树控件所在列，而其它列则可以用#1~#No的数字引用，也可以用列名引用。而向Treeview 组件中插入一行值时，用Text属性赋予树控件所在列的值，用values数控赋予其它列的值。

![](https://img.jbzj.com/file_images/article/202209/2022092716205653.png)