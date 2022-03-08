# import timeit


```python
import timeit
timeit.timeit('[]', number=10**7)
```




    0.22924450000000007




```python
timeit.timeit('list()', number=10**7)
```




    0.7119108999999995


