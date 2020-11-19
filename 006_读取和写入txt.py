import os


# f = open('py3.txt', 'wt', encoding='utf8')
# f.write('试一试')
# f.close()

# f = open('py3.txt', 'a', encoding='utf8')
# f.write('\n加一行')
# f.close()


# f = open('AD.txt', 'rt', encoding='utf8')
# 第一种读取方法
# f = open('py3.txt', 'rt', encoding='utf8')
# line = f.readline()
# while line:
#     print(line)
#     line = f.readline()
# f.close()
# 第二种读取方法
# for line in open('py3.txt', 'rt', encoding='utf8'):
#     print(line)
# 第三种读取方法
# f = open('py3.txt', 'rt', encoding='utf8')
# lines = f.readlines()  # 读取全部内容 ，并以列表方式返回
# list = []
# for line in lines:
#     list.append(line.encode('utf-8').decode('utf-8-sig'))
#     print(line, list)

# 文本转列表 去除编码前缀 但是还是有 \n
# lines = f.readlines()  # 读取全部内容 ，并以列表方式返回
# list = []
# for line in lines:
#     list.append(line.encode('utf-8').decode('utf-8-sig'))
#     print(line, list)
#
# f = open('AD1.txt', 'wt', encoding='utf8')
# f.write('溶解氧 化学需氧量 生化需氧量')
# f.close()
#
# f = open('AD1.txt', 'a', encoding='utf8')
# f.write('\n789 987 514 19 1.22')
# f.close()

f = open('AD1.txt', 'rt', encoding='utf-8-sig')
lines = f.readlines()  # 读取全部内容 ，并以列表方式返回
list = []
for line in lines:
    list.append(line.strip().split('\t'))
    # list = line.strip().split('\t')
    # print(list)
print(list[2][3])
f.close()

"""
split() 方法语法：
str.split(str="", num=string.count(str))
str -- 分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
num -- 分割次数。默认为 -1, 即分隔所有。
"""