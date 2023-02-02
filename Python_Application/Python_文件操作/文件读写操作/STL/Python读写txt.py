def test_write00(filePath, context, mode):
    f = open(filePath, mode)
    for i in range(5):
        f.write(context)
        f.write("\n")
    f.close()


# 第一种读法
def test_read00(filePath, mdoe):
    context = ""
    f = open(filePath, mode)
    line = f.readline()
    while line:
        context += line
        line = f.readline()
    f.close()
    return context


# 第二种读法
def test_read01(filePath, mdoe):
    context = ""
    f = open(filePath, mode)
    for line in f:
        context += line
    f.close()
    return context


# 第三种读法
def test_read02(filePath, mode):
    context = ""
    f = open(filePath, mode)
    lines = f.readlines()
    for line in lines:
        context += line
    f.close()
    return context


if __name__ == "__main__":
    # write
    # filePath = "test.txt"
    # context = "try try try"
    # mode = 'w'
    # test_write00(filePath, context, mode)

    # read
    filePath = "test.txt"
    context = ""
    mode = 'r'
    # context = test_read02(filePath, mode)
    # print(context)

