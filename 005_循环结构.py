while True:
    value = input("integer, [q to quite]")
    if value == "q":  # 停止循环
        break
    number = int(value)
    if number % 2 == 0:  # 判断偶数
        continue
    print(number, "squared is", number * number)


