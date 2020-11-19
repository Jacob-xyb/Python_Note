"""python 和 typhon 就是变位词"""
"""
解法1：逐字检查
将词1的字符逐个在词2中寻找，找到就“打勾”标记
实现“打勾”标记：将词2对应字符设为None,
    但是字符串是不可变类型，需要先复制到列表中
复杂度：O(n^2)
"""
def anagramSolution1(s1, s2):
    alist = list(s2)
    pos1 = 0
    still_OK = True
    while pos1 < len(s1) and still_OK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 += 1
        if found:
            alist[pos2] = None
        else:
            still_OK = False
        pos1 += 1
    return still_OK


"""
解法2：排序比较
先排序，再比较
复杂度：O(nlogn)
"""
def anagramSolution2(s1, s2):
    alist1 = lisr(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()
    pos = 0
    matches = True
    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos += 1
        else:
            matches = False
    return matches


"""
解法3：暴力法
穷尽所有可能组合
将s1全排列，再查看s2是否出现在全排列列表中

根据组合数学的结论，如果n个字符进行全排列，其所有可能的字符串个数为n！
复杂度：O(n!)
非常差的算法
"""

"""
解法4：计数比较
解决思路：对比两个词中每个字母出现的次数
"""
def anagramSolution4(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1
    j = 0
    stillOK = True
    while j < 26 and stillOK:
        if c1[j] == c2[j]:
            j += 1
        else:
            stillOK = False
    return stillOK


print(anagramSolution1('abcd', 'dcba'))
