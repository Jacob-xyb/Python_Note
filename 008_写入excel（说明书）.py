import xlrd  # 读取Excel数据
import xlsxwriter  # 向Excel写入数据
import os.path  # 使用os中的方法，获取指定目录下的所有文件


"""使用python去新建一个Excel文件"""
workbook = xlsxwriter.Workbook('RES.xlsx')
# 创建一个工作表，所说的sheet表
# 默认创建sheet1
worksheet = workbook.add_worksheet()
# 设置格式
"""
add_format([properties])方法，用于在工作表中创建一个新的格式对象来格式化单元格。
properties：为dict类型，为指定一个格式属性的字典。
"""
bold = workbook.add_format({'bold': True})  # 加粗
# 等价语句
# bold = workbook.add_format()
# bold.set_bold()
# align 水平方向 valign 垂直方向 font_size 字体大小
bold_center = workbook.add_format({'align': 'center', 'valign': 'vcenter',
                                   'font_size': 18, 'border': 1})
# 创建图表对象
"""
add_chart(options)方法，用于在工作表中创建一个图表对象，
    内部是通过insert_chart()方法来实现的，参数为dict类型，是为图标指定一个字典属性。
"""
# 设置一个线条行的图表对象，代码如下：
# chart = workbook.add_chart({'type': 'line'})  # 没反应 bug..
"""------------------------------""""""------------------------------"""
# 向单元格写入数据
"""
write(row, col, *args)方法：是用来将普通数据写入单元格中。
*args：无名字参数为数据内容，可为数字，公式，字符串或格式对象。

  write.string()：写入字符串类型数据
  wirte_number()：写入数字型数据
  write_blank()：写入空类型数据
  write_formula()：写入公式型数据
  write_datetime()：写入日期型数据
  wirte_boolean()：写入逻辑型数据
  write_url()：写入超链接型数据
"""
worksheet.write(0, 0, 'hello')  # 行号和列标均是从0开始
# for n in range(10):
    # worksheet.write('A{}'.format(n), n, bold)
    # 等价写法
    # worksheet.write('A'+str(n), n, bold)

# # 合并单元格
# worksheet.merge_range('A1:H1', '合并单元格')
# 设置行高(行变化)
"""
set_row(row, height, cell_format, options)方法，用于设定行单元格的属性。
row：指定行位置，起始下标为0；
height：为float类型，设定行高，单位像素；
cell_format：format类型，指定对象格式；
options，字典类型，设置行hidden（隐藏）、
         level（组合分级）、collpsed（折叠）
"""
# worksheet.set_row(0, 70)
worksheet.write('B1', 'goodbye')
# 设定A1行高40，加粗
worksheet.set_row(0, 40, bold)
# 隐藏第二行
# worksheet.set_row(1, None, None, {'hidden': True})

# 列变化
"""
set_column(first_col, last_col, width, cell_format, options)方法，
        用于设置一列或多列单元格的属性。
first_col：整型，指定开始列位置，起始下标为0；
last_col：整型，指定结束列位置，起始下标为0；
width：float类型，设置列宽；
cell_format：format类型，指定格式对象；
options：dict类型，设置hidden（隐藏）、level（组合分级）、collpsed（折叠）；
"""
# 设定列A到B单元格宽度10像素，加粗
# worksheet.set_column(0, 1, 20, bold)
# 设置C到D单元格宽度20像素
# worksheet.set_column('C:D', 20)
# 隐藏E到G单元格
# worksheet.set_column('E:G', None, None, {'hidden': 1})
# 创建sheet2 '工作表名'
worksheet2 = workbook.add_worksheet('xyb')
"""------------------------------""""""------------------------------"""
"""
insert_image(row, col, image[, options])方法，
        用于插入图片到指定的单元格，支持PNG，JPEG，BMP等多种格式。
row：行坐标，起始索引值为0；
col：列坐标，起始索引值为0；
image：string类型，是图片路径；
options：dict类型，是可选参数，用于指定图片位置，如URL等信息；
"""
# 在B5单元格插入python-logo.png图片，超链接为http://python.org
# 此段代码不可行 ////////
# worksheet.insert_image('B5', 'img/python-logo.png', {'url': 'http://python.org'})


workbook.close()

# 整列写入
worksheet.write_column()
# write_column(row, col, data[, cell_format])
'''从（col, row）处开始写入列。
参数：
row(int) - 单元格所在的行（索引从0开始计数）。
col(int) - 单元格所在的列（索引从0开始计数）。
data - 写入单元格的数据。变量类型。
cell_format(Format) - 可选的格式化对象。'''

# 一些示例数据。
data = ('Foo', 'Bar', 'Baz')

# 将数据写入单元格序列。
worksheet.write_column('A1', data)

# 上面的例子等价于：
worksheet.write('A1', data[0])
worksheet.write('A2', data[1])
worksheet.write('A3', data[2])



# # 未整理
# import xlsxwriter
#
# workbook = xlsxwriter.Workbook('test.xlsx')
# worksheet = workbook.add_worksheet()
# worksheet.set_row(0, 70)
# worksheet.set_col('A:A', 10)
# workbook.close()
# #单元格样式设置
# import xlsxwriter
#
# header = '测试标题'
# workbook = xlsxwriter.Workbook('test.xlsx')
# worksheet = workbook.add_worksheet()
# worksheet.merge_range('A1:H1', '')
# f = workbook.add_format(({
#     'align': 'center',
#     'valign': 'top',
#     'font_size': 20,
#     'text_wrap': 1,  # 自动换行
# }))
# worksheet.write('A1', header, f)
# worksheet.set_row(0, 70)
# workbook.close()