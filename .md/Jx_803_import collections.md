# collection

- collections是Python内建的一个集合模块，提供了许多有用的集合类。

## Counter

- ```Counter```是一个简单的计数器，例如，统计字符出现的个数:


```python
from collections import Counter
```

- ```Counter```实际上也是```dict```的一个子类


```python
s = "hello world"
count = Counter(s)
print(count)
```

    Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
    

- ```Counter```还可以进行加减，但是```dict```不行


```python
s = "hello world"
count = Counter(s)
print(count)
s_1 = "hello"
count_1 = Counter(s_1)
print(count_1)
print(count + count_1)
print(count - count_1)
print(count_1 - count)  # 小集合 - 大集合 %save，结果就是空的啦
```

    Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
    Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
    Counter({'l': 5, 'o': 3, 'h': 2, 'e': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
    Counter({'l': 1, 'o': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
    Counter()
    


```python
s = "hello world"
s = list(s)
count = Counter(s)
print(count)
s_1 = "hello"
count_1 = Counter(s_1)
print(count_1)
print(count + count_1)
print(count - count_1)
```

    Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
    Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
    Counter({'l': 5, 'o': 3, 'h': 2, 'e': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
    Counter({'l': 1, 'o': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
    

- ```Counter```可以转换为```list```，是```key```的列表
- ```Counter```可以转换为```dict```
    - 有趣的是```Counter```的key顺序是按value大小排列的，```dict```的key顺序是按数据源顺序排列的


```python
s = "hello world"
count = Counter(s)
print(count)
res_list = list(count)
res_dict = dict(count)
print(res_list, res_dict)
```

    Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
    ['h', 'e', 'l', 'o', ' ', 'w', 'r', 'd'] {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
    

### 案例

**1.找不同**
- 字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。


```python
s = "ymbgaraibkfmvocpizdydugvalagaivdbfsfbepeyccqfepzvtpyxtbadkhmwmoswrcxnargtlswqemafandgkmydtimuzvjwxvlfwlhvkrgcsithaqlcvrihrwqkpjdhgfgreqoxzfvhjzojhghfwbvpfzectwwhexthbsndovxejsntmjihchaotbgcysfdaojkjldprwyrnischrgmtvjcorypvopfmegizfkvudubnejzfqffvgdoxohuinkyygbdzmshvyqyhsozwvlhevfepdvafgkqpkmcsikfyxczcovrmwqxxbnhfzcjjcpgzjjfateajnnvlbwhyppdleahgaypxidkpwmfqwqyofwdqgxhjaxvyrzupfwesmxbjszolgwqvfiozofncbohduqgiswuiyddmwlwubetyaummenkdfptjczxemryuotrrymrfdxtrebpbjtpnuhsbnovhectpjhfhahbqrfbyxggobsweefcwxpqsspyssrmdhuelkkvyjxswjwofngpwfxvknkjviiavorwyfzlnktmfwxkvwkrwdcxjfzikdyswsuxegmhtnxjraqrdchaauazfhtklxsksbhwgjphgbasfnlwqwukprgvihntsyymdrfovaszjywuqygpvjtvlsvvqbvzsmgweiayhlubnbsitvfxawhfmfiatxvqrcwjshvovxknnxnyyfexqycrlyksderlqarqhkxyaqwlwoqcribumrqjtelhwdvaiysgjlvksrfvjlcaiwrirtkkxbwgicyhvakxgdjwnwmubkiazdjkfmotglclqndqjxethoutvjchjbkoasnnfbgrnycucfpeovruguzumgmgddqwjgdvaujhyqsqtoexmnfuluaqbxoofvotvfoiexbnprrxptchmlctzgqtkivsilwgwgvpidpvasurraqfkcmxhdapjrlrnkbklwkrvoaziznlpor"
t = "qhxepbshlrhoecdaodgpousbzfcqjxulatciapuftffahhlmxbufgjuxstfjvljybfxnenlacmjqoymvamphpxnolwijwcecgwbcjhgdybfffwoygikvoecdggplfohemfypxfsvdrseyhmvkoovxhdvoavsqqbrsqrkqhbtmgwaurgisloqjixfwfvwtszcxwktkwesaxsmhsvlitegrlzkvfqoiiwxbzskzoewbkxtphapavbyvhzvgrrfriddnsrftfowhdanvhjvurhljmpxvpddxmzfgwwpkjrfgqptrmumoemhfpojnxzwlrxkcafvbhlwrapubhveattfifsmiounhqusvhywnxhwrgamgnesxmzliyzisqrwvkiyderyotxhwspqrrkeczjysfujvovsfcfouykcqyjoobfdgnlswfzjmyucaxuaslzwfnetekymrwbvponiaojdqnbmboldvvitamntwnyaeppjaohwkrisrlrgwcjqqgxeqerjrbapfzurcwxhcwzugcgnirkkrxdthtbmdqgvqxilllrsbwjhwqszrjtzyetwubdrlyakzxcveufvhqugyawvkivwonvmrgnchkzdysngqdibhkyboyftxcvvjoggecjsajbuqkjjxfvynrjsnvtfvgpgveycxidhhfauvjovmnbqgoxsafknluyimkczykwdgvqwlvvgdmufxdypwnajkncoynqticfetcdafvtqszuwfmrdggifokwmkgzuxnhncmnsstffqpqbplypapctctfhqpihavligbrutxmmygiyaklqtakdidvnvrjfteazeqmbgklrgrorudayokxptswwkcircwuhcavhdparjfkjypkyxhbgwxbkvpvrtzjaetahmxevmkhdfyidhrdeejapfbafwmdqjqszwnwzgclitdhlnkaiyldwkwwzvhyorgbysyjbxsspnjdewjxbhpsvj"
print(list(Counter(t)-Counter(s))[0])
```

    t
    

## defaultdict

- Python中通过Key访问字典，当Key不存在时，会引发‘KeyError’异常。为了避免这种情况的发生，可以使用collections类中的defaultdict()方法来为字典提供默认值。

- 语法
```
collections.defaultdict([default_factory[, …]])
```

该函数返回一个类似字典的对象。defaultdict是Python内建字典类（dict）的一个子类，它重写了方法_missing_(key)，增加了一个可写的实例变量default_factory,实例变量default_factory被missing()方法使用，如果该变量存在，则用以初始化构造器，如果没有，则为None。其它的功能和dict一样。

第一个参数为default_factory属性提供初始值，默认为None；其余参数包括关键字参数（keyword arguments）的用法，和dict构造器用法一样。


```python
from collections import defaultdict
```

当字典中没有的键第一次出现时，default_factory自动为其返回一个空列表，list.append()会将值添加进新列表；再次遇到相同的键时，list.append()将其它值再添加进该列表。

这种方法比使用dict.setdefault()更为便捷，dict.setdefault()也可以实现相同的功能。 


```python
from collections import defaultdict
s=[('yellow',1),('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d=defaultdict(list)
for k, v in s:
    d[k].append(v)
a=sorted(d.items())
print(a)
```

    [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
    

dict.setdefault()实现


```python
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d={}
for k, v in s:
    d.setdefault(k,[]).append(v)
print('\n',d)
a=sorted(d.items())
print('\n',a)
```

    
     {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
    
     [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]
    

- 这个factory_function可以是list、set、str等等，作用是当key不存在时，返回的是工厂函数的默认值，比如list对应[ ]，str对应的是空字符串，set对应set( )，int对应0，如下举例：


```python
from collections import defaultdict

dict1 = defaultdict(int)
dict2 = defaultdict(set)
dict3 = defaultdict(str)
dict4 = defaultdict(list)
dict1[2] ='two'

print(dict1[1])
print(dict2[1])
print(dict3[1])
print(dict4[1])
```

    0
    set()
    
    []
    

### 案例

1. 计数


- 字符串中的字母第一次出现时，字典中没有该字母，default_factory函数调用int()为其提供一个默认值0,加法操作将计算出每个字母出现的次数。

函数int()是常值函数的一种特例，总是返回0。使用匿名函数（lambda function）可以更快、更灵活的创建常值函数，返回包括0在内的任意常数值。


```python
from collections import defaultdict
s = 'mississippi'
d = defaultdict(int)
for k in s:
    d[k] += 1
print('\n',d)
a=sorted(d.items())
print('\n',a)
```

    
     defaultdict(<class 'int'>, {'m': 1, 'i': 4, 's': 4, 'p': 2})
    
     [('i', 4), ('m', 1), ('p', 2), ('s', 4)]
    
