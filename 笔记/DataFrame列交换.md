# DataFrame column交换
```python
import numpy as np
import pandas as pd
index = pd.Index(data=[1,2,3],name="NUM")
Data = {
    "dd":[776,555,444],
    "zz":[111,222,333]
}
a = pd.DataFrame(data=Data,index=index)
print(a)
cols = list(a)
print(cols)
cols.insert(0,cols.pop(cols.index('zz')))
print(cols)
a = a.loc[:,cols]
print(a)
```

输出为：
```python
      dd   zz
NUM
1    776  111
2    555  222
3    444  333
['dd', 'zz']
['zz', 'dd']
      zz   dd
NUM
1    111  776
2    222  555
3    333  444
```

### 核心函数
- `cols.insert(0,cols.pop(cols.index('zz')))`
- `a.loc[:,cols]`
  原理为获取所有的行，按照cols列表来依次取原data的列，得到新的DataFrame赋给新的变量data
