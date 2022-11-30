# 原理与安装

## Selenium 安装

```python
pip install selenium -i https://pypi.douban.com/simple/
```

## 浏览器驱动安装

[Chrome 浏览器驱动下载地址](https://chromedriver.storage.googleapis.com/index.html) 

## 简单案例

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome(service=Service(r'D:\PythonLib\ChromeDrive\chromedriver.exe'))

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://www.baidu.com')

input()
```

# 选择元素

简单案例：

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建 WebDriver 对象
wd = webdriver.Chrome()

# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://www.byhy.net/_files/stock1.html')

# 根据id选择元素，返回的就是该元素对应的WebElement对象
element = wd.find_element(By.ID, 'kw')

# 通过该 WebElement对象，就可以对页面元素进行操作了
# 比如输入字符串到 这个 输入框里
element.send_keys('通讯\n')
```

## find_elements



## 通过WebElement对象选择元素

不仅 WebDriver对象有 选择元素 的方法， WebElement对象 也有选择元素的方法。

WebElement对象 也可以调用 `find_elements`， `find_element` 之类的方法

WebDriver 对象 选择元素的范围是 整个 web页面， 而

WebElement 对象 选择元素的范围是 该元素的内部。

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

wd = webdriver.Chrome()

wd.get('https://cdn2.byhy.net/files/selenium/sample1.html')

element = wd.find_element(By.ID,'container')

# 限制 选择元素的范围是 id 为 container 元素的内部。
spans = element.find_elements(By.TAG_NAME, 'span')
for span in spans:
    print(span.text)
```

## 等待

```python
wd.implicitly_wait(10)
```

## 注意

特别注意：Selenium 升级到版本 4 以后， 下面这种 `find_element_by*` 方法都作为过期不赞成的写法

```python
# 初始化代码 ....

wd.find_element_by_id('username').send_keys('byhy')
wd.find_element_by_class_name('password').send_keys('sdfsdf')
wd.find_element_by_tag_name('input').send_keys('sdfsdf')
wd.find_element_by_css_selector('button[type=submit]').click()
```

运行会有告警，所以现在都要写成下面这种格式

```python
from selenium.webdriver.common.by import By

# 初始化代码 ....

wd.find_element(By.ID, 'username').send_keys('byhy')
wd.find_element(By.CLASS_NAME, 'password').send_keys('sdfsdf')
wd.find_element(By.TAG_NAME, 'input').send_keys('sdfsdf')
wd.find_element(By.CSS_SELECTOR,'button[type=submit]').click()
```

---

find_elements 返回的是找到的符合条件的 `所有` 元素 (这里有3个元素)， 放在一个 `列表` 中返回。

而如果我们使用 `wd.find_element` (注意少了一个s) 方法， 就只会返回 `第一个` 元素。

# 多窗口操作

## 打开多窗口

```python
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
```

# API

## By

`from selenium.webdriver.common.by import By`

```python
class By:
    """
    Set of supported locator strategies.
    """

    ID = "id"
    XPATH = "xpath"
    LINK_TEXT = "link text"
    PARTIAL_LINK_TEXT = "partial link text"
    NAME = "name"
    TAG_NAME = "tag name"
    CLASS_NAME = "class name"
    CSS_SELECTOR = "css selector"
```

## WebElement

[WebElement](https://www.selenium.dev/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.webelement.html?highlight=webelement#module-selenium.webdriver.remote.webelement)

```python
class WebElement:
    """
    Represents a DOM element.
    """
    clear()		# 如果是本文输入元素，则清除文本
    click()		# 点击
    id			# 注意这个id是selenium使用的
```

