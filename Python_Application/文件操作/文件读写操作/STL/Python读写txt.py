def test_write00(filePath, context, mode):
    f = open(filePath, mode)
    f.write(context)
    f.close()


if __name__ == "__main__":
    filePath = "test.txt"
    context = "try try try"
    mode = 'w'
    test_write00(filePath, context, mode)
