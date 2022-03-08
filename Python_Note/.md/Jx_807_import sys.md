# import sys

我们在写shell脚本时，经常会通过接受执行脚本时传入的变量来做相应的操作，来保证脚本的灵活性。比如我们要写一个脚本来调用ping命令对指定的域名进行ping测试，这时候显然将域名当做参数传递给脚本要比把域名写死在脚本中灵活的多。shell中可以只用$1,$2这样的特殊变量来获取传入的参数，而python中需要用sys模块下的argv变量来获取。

> sys.argv是一个列表，与shell相同，其第一个元素是当前脚本的名称，之后才是传入的参数。

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import os

print(type(sys.argv))
print(sys.argv)
```

![](https://images2015.cnblogs.com/blog/1063221/201611/1063221-20161122230829518-389711267.png)
