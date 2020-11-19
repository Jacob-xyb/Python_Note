"""数学函数"""
# python 的标准 math(https://docs.python.org/3/library/math.html)
# 库中汇集了大量的数学函数。

import math
print(math.pi)  # 3.141592653589793
print(math.e)  # 2.718281828459045

# fabs() 用于获得绝对值：
print(math.fabs(98.6))  # 98.6
print(math.fabs(-271.1))  # 271.1

# floor() 向下取整， ceil() 向上取整
print(math.floor(98.6))  # 98
print(math.floor(-271.1))  # -272
print(math.ceil(98.6))  # 99
print(math.ceil(-271.1))  # -271

# factorial() 计算阶乘（n!）
print(math.factorial(0))  # 1
print(math.factorial(1))  # 1
print(math.factorial(2))  # 2
print(math.factorial(3))  # 6
print(math.factorial(10))  # 3628800

# log() 计算自然对数（以e为底）：
print(math.log(1.0))  # 0.0
print(math.log(math.e))  # 1.0
# log(a, b) 以 b 为底，a 的对数
print(math.log(8, 2))  # 3.0
# pow() 做的工作与上面正好相反，它用于计算一个数的指数：
print(math.pow(2, 3))  # 8.0
#     python 内置的指数运算符 ** 也可以进行同样的计算，
#     只不过当底数和指数都是整数时，用 ** 计算得到的结果也是整数，不会被自动转化为浮点数
print(2 ** 3)  # 8
print(2.0 ** 3)  # 8.0

# 使用 sqrt() 得到平方根
print(math.sqrt(100.0))  # 10.0

# 常见的三角函数都可以使用，例如：sin()、 cos()、 tan()、 asin()、 acos()、 atan()、 atan2()。
# hypot() 函数计算两直角边对应斜边长（勾股定理）
print(math.hypot(3.0, 4.0))  # 5.0

# 角坐标转换：
print(math.radians(180.0))  # 3.141592653589793
print(math.degrees(math.pi))  # 180.0


