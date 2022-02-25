# help()

## 导出文档

```python
import sys
sys.stdout = open(r"d:\test.txt", "w")
help(sys)
sys.stdout.close()
```

