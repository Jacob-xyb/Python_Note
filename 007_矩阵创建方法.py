w, h = 8, 5;
Matrix = [[0 for x in range(w)] for y in range(h)]
print(Matrix)

"""Python中矩阵创建和矩阵运算"""
# https://blog.csdn.net/qian_fighting/article/details/79080711
# 见云笔记
"""
1、from numpyimport *;
a1=array([1,2,3])
a2=mat(a1) 
矩阵与方块列表的区别如下：
2、data2=mat(ones((2,4)))
创建一个2*4的1矩阵，默认是浮点型的数据，如果需要时int类型，可以使用dtype=int
3、data5=mat(random.randint(2,8,size=(2,5))
产生一个2-8之间的随机整数矩阵
4、data3=mat(random.rand(2,2))
这里的random模块使用的是numpy中的random模块，random.rand(2,2)创建的是一个二维数组，需要将其转换成#matrix,并在数组中加入[0,1]之间均匀分布的随机样本
5、data4=mat(random.randn(2,2))numpy.random.randn() 
官方文档中给出的用法是：numpy.random.rand(d0,d1,…dn) ,以给定的形状创建一个数组，数组元素来符合标准正态分布N(0,1)若要获得一般正态分布则可用sigma * np.random.randn(…) + mu进行表示 
6、a1=random.random()  
random.random()用于生成一个0到1的随机浮点数

7、a1=random.rand()用于生成[0,1]之间均匀分布的随机浮点数
a=random.rand(2)
array([ 0.00760085,  0.91928957])
rand()与random()区别：
int rand(void); //返回一个随机数0 ~ pow(2, sizeof(int))-1
long int random(void); //返回一个随机数0 ~ pow(2, sizeof(long int))-1

总结：rand和random的区别就是返回类型不同,int和long int(虽然在普通的32位机上效果是一样的)
使用的rand或者random之前,一般使用time(0) getpid()设置随机种子.否则默认种子就是1,则每次产生的随机数都是一样的

补充：pow()用来计算以x 为底的 y 次方值，然后将结果返回。设返回值为 ret，则 ret = xy。
numpy矩阵运算
(1) 矩阵点乘：m=multiply(A,B)
(2) 矩阵乘法：m1=a*b  m2=a.dot(b)
(3) 矩阵求逆：a.I
(4) 矩阵转置：a.T
"""
