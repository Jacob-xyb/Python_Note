from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建 WebDriver 对象
wd = webdriver.Chrome()

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://www.baidu.com')
wd.execute_script("window.open('https://www.zhihu.com')")   # 会打开新窗口哦，并且切换到新窗口，但是 drive 并不会切过去
wd.execute_script("window.open('https://www.lagou.com/')")
wd.execute_script("window.open('https://www.jianshu.com/')")


handles = wd.window_handles

for handle in handles:
    wd.switch_to.window(handle)
    print(wd.current_url)

# 第二个元素往后是与我们代码写入的顺序是相反的
"""
https://www.baidu.com/
https://www.jianshu.com/
https://www.lagou.com/
https://www.zhihu.com/signin?next=%2F
"""

input()


