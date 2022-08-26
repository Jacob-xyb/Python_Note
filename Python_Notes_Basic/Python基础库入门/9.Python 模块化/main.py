from utils import get_sum
from utils import *     # 还是只导入一次包， import * 优先级最高
from class_utils import *

print(get_sum(1, 2))
encoder = Encoder()
decoder = Decoder()
print(encoder.encode('abcde'))
print(encoder.encode('edcba'))
