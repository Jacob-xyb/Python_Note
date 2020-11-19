from timeit import Timer


def test1():
    l = []
    for i in range(1000):
        l = l + [i]
def test2():
    l = []
    for i in range(1000):
        l.append(i)
def test3():
    l = [i for i in range(1000)]
def test4():
    l = list(range(1000))



# print([i for i in range(100)])
t1 = Timer('test1()', 'from __main__ import test1')
print('concat %f seconds\n' % t1.timeit(1000))
t2 = Timer('test2()', 'from __main__ import test2')
print('append %f seconds\n' % t2.timeit(1000))
t3 = Timer('test3()', 'from __main__ import test3')
print('comprehension %f seconds\n' % t3.timeit(1000))
t4 = Timer('test4()', 'from __main__ import test4')
print('list range %f seconds\n' % t4.timeit(1000))
