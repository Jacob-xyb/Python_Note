# import dis



```python
import dis
dis.dis("[]")
```

      1           0 BUILD_LIST               0
                  2 RETURN_VALUE
    


```python
dis.dis("list()")
```

      1           0 LOAD_NAME                0 (list)
                  2 CALL_FUNCTION            0
                  4 RETURN_VALUE
    
