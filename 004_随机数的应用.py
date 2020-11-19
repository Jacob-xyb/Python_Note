# 随机数功能
from random import *
# 1.choice(seq)
# seq -- 可以是一个列表，元组或字符串，
# 返回其中的一个随机项。
c1_1 = choice([1, 2, 3, 4, 5])
c1_2 = choice([1, 2, 3, 4, 5])
c1_3 = choice(range(1, 11))
c1_4 = choice("string")
print(c1_1, c1_2, c1_3, c1_4)

# 2.randint(start, end)
# 返回 [start, end] 之间的一个随机整数。包头又包尾。
c2_1 = randint(-1, 5)
print(c2_1)

# 3. random()
# 返回一个 [0, 1) 的随机浮点数
c3_1 = random()
print(c3_1, round(c3_1, 2))
# round() 方法返回浮点数x的四舍五入值。
# round(x, n)
# print(round(c3_1, 2))

# 4.uniform(a, b)
# 返回 [a, b] 之间的一个随机浮点数。
# 注：a和b接受的数据大小随意
print(uniform(10, 20), uniform(20, 10), uniform(30, 30))
# print(uniform(20, 10))
# print(uniform(30, 30))

# 5.randrange(start, end, step)
# 返回[start,end)之间的一个随机整数。包头不包尾。
print(randrange(0, 10, 2))

# 6.sample(seq, number)
# 从 seq 中随机取出 number 个元素，以列表的形式返回。
# 取出的元素不会重复
print(sample({1, 2, 3, 4, 5}, 3))

# 7.shuffle(lt)
# 将 lt (列表对象) 中的元素打乱。
lt = ['a', 'b', 'c', 'd', 'e', 'f']
shuffle(lt)  # 类似洗牌
print(lt)

# 主要来源：https://urlify.cn/IFB3aq
