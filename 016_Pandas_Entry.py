import pandas as pd       # 导入pandas模块


'''解决数据输出时列名不对齐的问题'''
pd.set_option('display.unicode.east_asian_width', True)  # 列名对齐
# pd.set_option('display.unicode.ambiguous_as_wide', True)  # 列名对齐
# # 行列显示不全
# pd.set_option('display.max_columns', None)  # 显示所有列
# pd.set_option('display.max_rows', None)  # 显示所有行
# pd.set_option('display.max_rows', 1000)  # 修改默认输出最大行数
# pd.set_option('display.max_columns', 1000)  # 修改默认输出最大列数

'''读取excel'''  # 后面有详细介绍
df = pd.read_excel('016_Pandas_Entry')  # 读取Excel文件
print(df.head())  # 显示前5条数据
# print(df)
'''--------------------------------------------------------------------------------'''
"""Series"""
'''创建一个Series对象'''
'''
创建Series时，主要使用Pandas的Series方法，语法如下：
s = pd.Series(data, index=index)
参数说明：
data: 表示数据，支持python字典、多维数组、标量值（即只有大小没有方向的量）。
index: 表示行标签（索引）
返回值：Series对象
说明：
当data参数是多维数组时，index长度必须与data长度一致。
如果没有指定index参数，将自动创建数值型索引（从0~data的数据长度减1）
'''
s1 = pd.Series([88, 60, 75])
s2 = pd.Series(5)
print(s2)

'''通过pandas引入Series对象'''
from pandas import Series
s3 = Series([88, 60, 75])
print(s3)

s4 = pd.Series([88, 60, 75], name='语文')  # Series也是可以有列名的
print(s4)
'''设置Series索引'''
s1 = pd.Series([88, 60, 75], index=[1, 2, 3])
s2 = pd.Series([88, 60, 75], index=['明日同学', '高同学', '七月流火'])
print(s1)
print(s2)
print(s1[0])  # 通过一个标签索引获取索引值
print(s2[['明日同学', '七月流火']])  # 通过多个标签索引获取索引值
# 注意：Series对象不能使用[-1]定位索引。
print(s1[0:2])  # 用位置索引做切片，包头不包尾 ！！位置索引而不是标签
print(s2['明日同学':'七月流火'])  # 通过切片获取索引 包头包尾
# 获取索引和值
print(s1.index)  # 输出为：Int64Index([1, 2, 3], dtype='int64')
print(s1.values)
'''--------------------------------------------------------------------------------'''
"""DataFrame"""
# 遍历DataFrame
data = [[110, 105, 99], [105, 88, 115], [109, 120, 130]]
index = [0, 1, 2]
columns = ['语文', '数学', '英语']
df1 = pd.DataFrame(data=data, index=index, columns=columns)
# df = pd.DataFrame(data=data, index=index)  # 列名不设置时，默认为RangeIndex
print(df1)
# 遍历DataFrame表格数据的每一列
for col in df1.columns:  # df1.columns : ['语文', '数学', '英语']
    # print(col)  # col为一个个列名
    series = df1[col]
    print(series)
# 创建DataFrame by 字典
df2 = pd.DataFrame({
    '语文': [110, 105, 99],
    '数学': [105, 88, 115],
    '英语': [109, 120, 130],
    '班级': '高一7班'},
    index=[0, 1, 2])
print(df2)
'''
注意：
通过字典创建时，字典中的value值只能是一维数组或单个的简单数据类型，
如果是数组，则要求所有的数组长度一致；
如果是单个数据，则每行都需要添加相同数据。
'''
# 读取excel
# 解决数据输出时列名不对齐的问题
pd.set_option('display.unicode.east_asian_width', True)
df3 = pd.read_excel('016_Pandas_Entry.xlsx')
print(df3.head(), '\n')  # 输出前5条数据
'''
pd.read_excel(io,sheet_name=0,header=0,names=None,index_col=None)
Args:
    io: 字符串，xls或xlsx文件路径或类文件对象.
    sheet_name: 获取工作表，默认值为0.
        sheet_name=[0,1,'Sheet3'] 第一个，第二个和名为'Sheet3'的Sheet页.
    header: 指定作为列名的行，默认值为0.数据为除列名以外的数据，设置header=None(此时列索引为数字).
    names: 默认值为None,要使用的列名列表.
    index_col: 指定列为索引列，默认值为None
'''
# df = pd.read_excel('016_Pandas_Entry.xlsx', sheet_name='莫寒')  # 单独标签页
# df = pd.read_excel('016_Pandas_Entry.xlsx', sheet_name=[0, 2])  # 输出是一个字典



