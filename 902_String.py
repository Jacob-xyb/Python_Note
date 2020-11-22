"""字符串输出问题"""
# # 如果想输出: Let's go!
# print('let\'s go!')  # 采用 \' 转义符输出
# print("let's go!")  # 采用 " ' " 来显示出 '
# # 如果想输出: C:\now
# print('C:\now')  # \n 是换行的意思 是无法输出正确结果的
# print(r'C:\now')  # r'' 前缀：原始字符串
# # print(r'C:\now\')  # 原始字符串的结尾加 \ ，是会报错的，是不行的
# print(r'C:\now'+'\\')  # 只有这样才能在结尾加上 \
# # 三重引号字符串
# print('''一首小诗''')  # 三重引号可以输出很多段的内容
'''-----------------------------------------------------------------------------------'''
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
# str_2 = "Line1-abcdef \nLine2-abc \nLine4-abcd"
# print(str_2.split())        # 以空格为分隔符，包含 \n
# print(str_2.split(' ', 1))  # 以空格为分隔符，分隔成两个
"""
['Line1-abcdef', 'Line2-abc', 'Line4-abcd']
['Line1-abcdef', '\nLine2-abc \nLine4-abcd']
"""
# txt = "Google#Runoob#Taobao#Facebook"
# 第二个参数为 1，返回两个参数列表
# x = txt.split("#", 1)
# print(x)
"""
['Google', 'Runoob#Taobao#Facebook']
"""

"""strip()"""
'''
str.strip([chars]);
chars -- 移除字符串头尾指定的字符序列
'''
# str_300 = "*****this is **string** example....wow!!!*****"
# print(str_300.strip('*'))  # 指定字符串 *
# str_301 = "123abcrunoob321"
# print(str_301.strip('12'))  # 字符序列为 12
# 只要头尾包含有指定字符序列中的字符就删除
