# 数组拼接
`竖直拼接`与`水平拼接`

- 竖直拼接Vertically为上下堆放，水平拼接Horizontally为左右堆放
- 分别使用vstack(())与hstack(())进行对二至多个的数组拼接
- NUMPY库
---
输入：
```python
import numpy as np
a = [1,2,3,4,5]
b = [6,7,8,9,10]
n_A = np.array(a)
n_B = np.array(b)
print(n_A,n_B)
n_AB = np.vstack((n_A,n_B))
print(n_AB)
n_AB_pro = n_AB *10
print(n_AB_pro)
n_AB_mix = np.hstack((n_AB,n_AB_pro))
print(n_AB_mix)
```
输出：
```python
[1 2 3 4 5] [ 6  7  8  9 10]
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]]
[[ 10  20  30  40  50]
 [ 60  70  80  90 100]]
[[  1   2   3   4   5  10  20  30  40  50] 
 [  6   7   8   9  10  60  70  80  90 100]]
```

