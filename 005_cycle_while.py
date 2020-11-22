"""while 基础用法"""
'''无限循环'''
def infinite_cycle():
    while True:  # while True 就是一个无限循环
        value = input("integer, [q to quite]")
        if value == "q":  # 停止循环
            break  # break 退出while循环
        number = int(value)
        if number % 2 == 0:  # 判断偶数
            continue  # continue 直接回到循环的初始位置
        print(number, "squared is", number * number)


"""if 基础用法"""
'''elif'''  # 从上往下依次判定，判定成果即跳过，so easy.

'''if 三元操作符'''
def min_num(x, y):
    # # 二元操作符写法
    # if x < y:
    #     small = x
    # else:
    #     small = y
    # #
    # 三元操作符写法
    small = x if x < y else y

    return small


'''assert 断言'''
# 当这个关键字后边的条件为假时，程序自动崩溃并抛出AssertionError的异常。
# 一般可以用来植入检查点，确保某个条件为真才能让程序正常工作。
assert 5 > 4  # assert没有返回值

