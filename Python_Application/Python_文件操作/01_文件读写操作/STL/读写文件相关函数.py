"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2023/2/3 10:30"
"""


def func_flush(f):
    f.write("123")
    f.flush()
    f.write("456")
    f.close()


if __name__ == '__main__':
    f = open('test.txt', 'w')
    func_flush(f)
    f.close()

"""
__author__ = "Jacob-xyb"
__web__ = "https://github.com/Jacob-xyb"
__time__ = "2023/2/3 10:38"
"""
