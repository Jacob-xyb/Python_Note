def import1():
    import tool
    print(tool.init_num)


def import2():
    import tool.t1
    from tool import *
    print(tool.init_num)


if __name__ == '__main__':
    # import1()
    # import2()
    from tool import *
    print(init_num)

