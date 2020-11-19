"""
Python split() 通过指定分隔符对字符串进行切片，
如果参数 num 有指定值，则分隔 num+1 个子字符串

str.split(str="", num=string.count(str))
参数
str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
num -- 分割次数。默认为 -1, 即分隔所有。
返回值
返回分割后的字符串列表。
"""
str = "Line1-abcdef \nLine2-abc \nLine4-abcd"
print(str.split())        # 以空格为分隔符，包含 \n
print(str.split(' ', 1))  # 以空格为分隔符，分隔成两个
"""
['Line1-abcdef', 'Line2-abc', 'Line4-abcd']
['Line1-abcdef', '\nLine2-abc \nLine4-abcd']
"""
txt = "Google#Runoob#Taobao#Facebook"
# 第二个参数为 1，返回两个参数列表
x = txt.split("#", 1)
print(x)
"""
['Google', 'Runoob#Taobao#Facebook']
"""
