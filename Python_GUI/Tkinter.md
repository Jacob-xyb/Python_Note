# 控件基本属性

在 Tkinter 中不同的控件受到各自参数的约束（即参数），所有控件既有相同属性，也有各自独有的属性。本节内容，先对这些控件的共用属性做简单介绍，如下表所示：

| 属性名称        | 说明                                                         |
| --------------- | ------------------------------------------------------------ |
| anchor          | 定义控件或者文字信息在窗口内的位置                           |
| background(bg)  | bg 是 background 的缩写，用来定义控件的背景颜色，参数值可以颜色的十六进制数，或者颜色英文单词 |
| bitmap          | 定义显示在控件内的位图文件                                   |
| borderwidth(bd) | 定于控件的边框宽度，单位是像素                               |
| command         | 该参数用于执行事件函数，比如单击按钮时执行特定的动作，可将执行用户自定义的函数 |
| cursor          | 当鼠标指针移动到控件上时，定义鼠标指针的类型，字符换格式，参数值有 crosshair（十字光标）watch（待加载圆圈）plus（加号）arrow（箭头）等 |
| font            | 若控件支持设置标题文字，就可以使用此属性来定义，它是一个数组格式的参数 (字体,大小，字体样式) |
| foreground(fg)  | fg 是 foreground 的缩写，用来定义控件的前景色，也就是字体的颜色 |
| height          | 该参数值用来设置控件的高度，文本控件以字符的数目为高度（px），其他控件则以像素为单位 |
| image           | 定义显示在控件内的图片文件                                   |
| justify         | 定义多行文字的排列方式，此属性可以是 LEFT/CENTER/RIGHT       |
| padx/pady       | 定义控件内的文字或者图片与控件边框之间的水平/垂直距离        |
| relief          | 定义控件的边框样式，参数值为FLAT（平的）/RAISED（凸起的）/SUNKEN（凹陷的）/GROOVE（沟槽桩边缘）/RIDGE（脊状边缘） |
| text            | 定义控件的标题文字                                           |
| state           | 控制控件是否处于可用状态，参数值默认为 NORMAL/DISABLED，默认为 NORMAL（正常的） |
| width           | 用于设置控件的宽度，使用方法与 height 相同                   |

# Label 标签

## 属性

| 属性名称            | 说明                                                         |
| ------------------- | ------------------------------------------------------------ |
| anchor              | 控制文本（或图像）在 Label 中显示的位置（方位），通过方位的英文字符串缩写（n、ne、e、se、s、sw、w、nw、center）实现定位，默认为居中（center） |
| bg                  | 用来设置背景色                                               |
| bd                  | 即 borderwidth 用来指定 Label 控件的边框宽度，单位为像素，默认为 2 个像素 |
| bitmap              | 指定显示在 Label 控件上的位图，若指定了 image 参数，则该参数会被忽略 |
| compound            | 控制 Lable 中文本和图像的混合模式，若选项设置为 CENTER，则文本显示在图像上，如果将选项设置为 BOTTOM、LEFT、RIGHT、TOP，则图像显示在文本旁边。 |
| cursor              | 指定当鼠标在 Label 上掠过的时候，鼠标的的显示样式，参数值为 arrow、circle、cross、plus |
| disableforeground   | 指定当 Label 设置为不可用状态的时候前景色的颜色              |
| font                | 指定 Lable 中文本的 (字体,大小,样式）元组参数格式，一个 Lable 只能设置一种字体 |
| fg                  | 设置 Label 的前景色                                          |
| **height/width**    | 设置 Lable 的高度/宽度，如果 Lable 显示的是文本，那么单位是文本单元，如果 Label 显示的是图像，那么单位就是像素，如果不设置，Label 会自动根据内容来计算出标签的高度 |
| highlightbackground | 当 Label 没有获得焦点的时候高亮边框的颜色，系统的默认是标准背景色 |
| highlightcolor      | 指定当 Lable 获得焦点的话时候高亮边框的颜色，系统默认为0，不带高亮边框 |
| image               | 指定 Label 显示的图片，一般是 PhotoImage、BitmapImage 的对象 |
| justify             | 表示多行文本的对齐方式，参数值为 left、right、center，注意文本的位置取决于 anchor 选项 |
| **padx/pady**       | padx 指定 Label 水平方向上的间距（即内容和边框间），pady 指定 Lable 水平方向上的间距（内容和边框间的距离） |
| relief              | 指定边框样式，默认值是 "flat"，其他参数值有 "groove"、"raised"、"ridge"、"solid"或者"sunken" |
| state               | 该参数用来指定 Lable 的状态，默认值为"normal"（正常状态），其他可选参数值有"active"和"disabled" |
| takefocus           | 默认值为False，如果是 True，表示该标签接受输入焦点           |
| text                | 用来指定 Lable 显示的文本，注意文本内可以包含换行符          |
| underline           | 给指定的字符添加下划线，默认值为 -1 表示不添加，当设置为 1 时，表示给第二个文本字符添加下划线。 |
| wraplength          | 将 Label 显示的文本分行，该参数指定了分行后每一行的长度，默认值为 0 |

**padx/pady**： 文字与边框的距离。

**height/width** : 文本控件以字符的数目为高度/宽度，其他控件则以像素为单位。

## Font 字体

```python
# 获取字体所有family
import tkinter.font as font
fontfamilylist = font.families(root=window)
print(fontfamilylist)
```

- style

  **weight：**

  设置字体厚度，粗体还是正常；

  NORMAL : 表示正常

  BOLD : 表示粗体

   **slant：**

  设置字体是否倾斜

  ROMAN : 不倾斜

  ITALIC : 倾斜

  **underline：**

  是否有下划线

  `1` 表示有下划线

  `0` 表示没有

  **overstrike：**

  是否有删除线

  1 表示有删除线

  0 表示没有删除线

  ```python
  # 方式1
  # ++ 方式1 style里面的设置顺序，可以随意，但family, size, style这三者的顺序不能乱；
  # ++ 另外下划线和删除线，要添加的话是直接style添加 underline和overstrike，0和1的表示用在方式2中。
  LB1 = tk.Label(root, text='第一种方法', font=('华文楷体', '18', 'bold italic underline overstrike '))
  
  # 方式2
  myfont = tkFont.Font(family='华文宋体', size=30, weight=tkFont.BOLD, slant=tkFont.ITALIC, underline=1, overstrike=1)
  LB1 = tk.Label(root, text='第二种方法', font=myfont)
  ```

# Entry

输入控件(Entry. 是用来输入或者显示单行字符串的控件。该控件允许用户输入或显示一行文字。 如果用户输入的文字长度大于Entry 控件的可显示范围时, 文字会向后滚动。 这种情况下所输入的字符串无法全部显示。可以通过移动光标，将不可见的文字部分移入可见区域。如果你想要输入多行文本, 就需要使用Text 控件。

## 特殊属性

| 属性名称                      | 说明                                                         |
| ----------------------------- | ------------------------------------------------------------ |
| exportselection               | 定义是否把选中的文本，自动拷贝到剪贴板。这个参数对输入控件不起作用 |
| selectbackground              | 选中文字时的背景颜色                                         |
| selectforeground              | 选中文字时的前景色                                           |
| selectborderwidth             | 选中区域的边框宽度                                           |
| show                          | 指定文本框内容以何种样式的字符显示，比如密码可以将值设为 show="*" |
| textvariable                  | 输入框内值，也称动态字符串，使用 **StringVar()** 对象来设置，而 text 为静态字符串对象 |
| xscrollcommand                | 设置输入框内容滚动条，当输入的内容大于输入框的宽度时使用户   |
| disabledbackground            | 定义输入控件被禁止使用时的背景颜色。                         |
| disabledforeground            | 定义输入控件被禁止时的前景（文本）颜色。                     |
| highlightbackground           | 定义输入控件没有获得输入焦点状态下的高亮背景颜色。就是输入框的亮边。 |
| highlightcolor                | 与highlightbackground属性类似。不过是输入控件获得输入焦点时的边框颜色。 |
| highlightthickness            | 定义边框的宽度                                               |
| insertbackground              | 输入控件中，插入光标的颜色                                   |
| insertwidth                   | 插入光标的宽度。                                             |
| insertborderwidth             | 插入光标的边框显示宽度。0是没有边框，1到其他正整数是只有一个像素的边框，如果是一个非0的数值，光标会使用RAISED效果的边框。 |
| insertofftime 、 insertontime | 这两个属性控制插入光标闪烁效果。就是插入光标的出现和消失的时间。单位是毫秒。 |
| invalidcommand / invcmd       | 验证输入合法性的回调函数，但不能独立使用。只有设置了validatecommand回调函数且该函数返回False的情况下，才会激活invalidcommand定义的回调函数。 |

# Treeview

Tkinter模块的Treeview组件类似于Dev中的treelist控件，但前者还可以当做树控件和表格控件使用，虽然功能可能没有dev和winform控件那么强大，但是在Tkinter中算是比较复杂、用处较多的了。

Treeview 组件左侧可以理解为一个树控件，右侧可以理解为一个表格，一个数据条目占据一行，横跨树控件和表格控件。Treeview 组件用show属性设置显示方式，值为tree则仅显示树控件，值为headings默认仅显示表格，值为tree headings则显示全部，默认为显示全部。Treeview 组件使用#0引用树控件所在列，而其它列则可以用#1~#No的数字引用，也可以用列名引用。而向Treeview 组件中插入一行值时，用Text属性赋予树控件所在列的值，用values数控赋予其它列的值。

![image.png](https://s2.loli.net/2022/12/27/TEkIJHosiSeapqw.png)

