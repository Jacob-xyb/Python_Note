import itertools
"""
Infinite itertools，无限迭代器
生成一个无限序列
"""
x_1 = itertools.count(1, 3)  # count()会创建一个无限的迭代器
# def itertools_count(start, step):
#     """
#         执行到 yield时 函数就返回一个迭代值，
#         下次迭代时，代码从 yield b 的下一条语句继续执行，
#         而函数的本地变量看起来和上次中断执行前是完全一样的，
#         于是函数继续执行，直到再次遇到 yield。
#         :param start:
#         :param step:
#         :return:
#         """
#     rule = True
#     while rule:
#         yield start  # yield 的好处是显而易见的，把一个函数改写为一个 generator 就获得了迭代能力
#         start += step
# x_1 = itertools_count(1, 1)
# for i in x_1:
#     print(i)
#     if i >= 10:
#         break

x_2 = itertools.cycle('ABCD')  # cycle()会把传入的一个序列无限重复下去 字符串也是序列的一种
# def itertools_cycle(p):
#     while 1:
#         for i in p:
#             yield i
# x_2 = itertools_cycle((3,6,8,9))
# for i in x_2:
#     print(i)

x_3 = itertools.repeat(1, 10)  # elem [,n]  endlessly or up to n times
# def itertools_repeat(elem, counts:int=0):
#     if counts == 0:
#         while 1:
#             yield elem
#     else:
#         while counts > 0:
#             yield elem
#             counts -= 1
# x_3 = itertools_repeat([1,2,3], 3)
# for i in x_3:
#     print(i)


"""
有限迭代器：接收一个或多个序列（sequence）作为参数，进行组合、分组和过滤等；
"""
x_4 = itertools.chain([1, 2, 3], '123')  # 组合输出
# def itertools_chain(*item):
#     # print('length:', len(item))
#     for j in range(len(item)):
#         for k in item[j]:
#             yield k
# x_4 = itertools_chain([1, 2, 3], '123')
# for i in x_4:
#     print(i)

x_5 = itertools.compress('ABCDEF', [0, 1, 0, 1, 1, 1])  # 比较输出
# def itertools_compress(data, selectors):
#     """
#     length of data and selectors can be different
#     :param data: 可迭代的数组
#     :param selectors: 判断条件
#     :return: 判断后的结果
#     """
#     if len(data) >= len(selectors):
#         for i in range(len(selectors)):
#             if selectors[i]:
#                 yield data[i]
#     else:
#         for i in range(len(data)):
#             if selectors[i]:
#                 yield data[i]
# x_5 = itertools_compress('ABCDEF', [0,1,0,1,1,1])
# for i in x_5:
#     print(i)

x_6 = itertools.dropwhile(lambda x: x < 5, [1, 3, 4, 5, 7, 8])  # results:seq[n],seq[n+1],...starting when pred fails
# for i in x_6:
#     print(i)

x_7 = itertools.groupby('aabBccCDDdEfF', lambda x: x.upper())  # 把迭代器中相邻的重复元素挑出来放在一起：
"""
iterable[,keyfunc]
sub-iterators grouped by value of keyfunc(v)
"""
# for key, group in x_7:
#     print(key, list(group))

x_8 = itertools.combinations('ABC', 2)
"""
创建一个迭代器，返回iterable中所有长度为r的子序列，返回的子序列中的项按输入iterable中的顺序排序 (不带重复).
r 指定生成排列的元素的长度，如果不指定，函数会报错。
对应组合概念。
"""
# for i in x_8:
#     print(i)
# print(list(itertools.combinations('ABC', 2)))
