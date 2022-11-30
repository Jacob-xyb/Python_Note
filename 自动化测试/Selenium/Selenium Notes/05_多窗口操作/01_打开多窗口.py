from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建 WebDriver 对象
wd = webdriver.Chrome()

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://www.baidu.com')
wd.execute_script("window.open('https://www.zhihu.com')")   # 会打开新窗口哦，并且切换到新窗口，但是 drive 并不会切过去

# switch切换
win1 = wd.window_handles[1]
wd.switch_to.window(win1)   # 网页切换的同时 drive 对象同时切换过去

# 根据id选择元素，返回的就是该元素对应的WebElement对象
element = wd.find_element(By.CSS_SELECTOR, 'input[type=number][name=digits]')

# 通过该 WebElement对象，就可以对页面元素进行操作了
# 比如输入字符串到 这个 输入框里
element.send_keys('888888')

win0 = wd.window_handles[0]
wd.switch_to.window(win0)

input()


