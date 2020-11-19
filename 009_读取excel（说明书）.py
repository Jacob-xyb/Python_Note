import os
import xlrd
import xlsxwriter


"""获取指定目录下的所有文件"""
files = os.listdir()
for item in files:
    if item.endswith('.xlsx'):  # 过滤掉非excel文件
        # 打开excel文件
        file = xlrd.open_workbook(item)  # open_workbook(path)
        # 使用指定的sheet页
        info = file.sheet_by_index(0)  # 0代表的是第一个sheet页
        # 获取指定的单元格的值
        # name = info.cell(4, 1).value  # 行和列的获取
        # leave_beijing = info.cell(4, 2).value
        # in_beijing_time = info.cell(4, 3).value
        # province = info.cell(4, 4).value
        # city = info.cell(4, 5).value
        # work_time = info.cell(4, 6).value
        # remark = info.cell(4, 7).value
        # date_time = info.cell(1, 0).value
        # day_time = info.cell(1, 1).value
        # inflow = info.cell(1, 2).value
        # level = info.cell(1, 3).value
        # print(item)
        # print(date_time, day_time, inflow, level)
        """把获取到的数据写到新的Excel文件中"""
'''1.使用xlrd模块读取Excel文件'''
Workbook = xlrd.open_workbook('RES.xlsx')
'''2.获取表名单'''
book_names = Workbook.sheet_names()  # 以列表的形式返回
print(book_names)
'''3.打开表单'''
# mySheet = Workbook.sheet_by_index(0)    # 通过索引打开
mySheet = Workbook.sheet_by_name('Sheet1')  # 通过表单名打开
'''4.获取表单行数和列数'''
n_rows = mySheet.nrows  # 获取总行数
n_cols = mySheet.ncols  # 获取总列数
'''5.获取一行和一列数据'''
my_Row_Values = mySheet.row_values(0)   # (i) i是行数，从0开始，返回list对象
my_Col_Values = mySheet.col_values(0)[1:]   # (i) i是列数，从0开始，返回list对象
print(my_Row_Values, my_Col_Values)
'''6.读取单元格数据'''
# my_Cell_Value = mySheet.cell(i, j).value    # 获取单元格，i是行数，j是列数
# my_Cell_Value = mySheet.cell_value(i, j)    # 等价写法


