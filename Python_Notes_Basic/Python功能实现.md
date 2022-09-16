# Windows

## 识别系统语言

- **系统语言：**

  ```python
  import ctypes
  dll_handle = ctypes.windll.kernel32
  sys_lang = hex(dll_handle.GetSystemDefaultUILanguage())
  print(sys_lang)		# '0x804'
  ```

  系统语言用代号表式:

  中文是：0x804
  英语是：0x409

- **区域语言：**

  ```python
  import locale
  loc_lang = locale.getdefaultlocale()
  print(loc_lang)		# ('zh_CN', 'cp936')
  ```

  中文是：('zh_CN', 'cp936')

  英文是：('en_US', 'cp936')