"""基础用法"""
'''用列表判断'''  # 输入的类型一定要与列表里的类型对应上
def if_list(key):
    if key in ["hello", "world", 1]:
        print("yes,you are right")
if_list(1)
