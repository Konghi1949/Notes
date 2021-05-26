# pandas对CSV的读取
1.csv文件:
```python
id,name,sex,class,age
1,WxQ,boy,1,18
2,WxF,gril,2,34
3,XJX,boy,1,19
4,LY,boy,1,25
5,TT,gril,2,23
6,OP,gril,2,20
7,WO,gril,4,70
8,TYU,boy,,100
```

读取:`pd.read_csv("1.CSV")`
```python
data = pd.read_csv("1.CSV")
print(data)
```
```python
#输出
   id name   sex  class  age
0   1  WxQ   boy    1.0   18
1   2  WxF  gril    2.0   34
2   3  XJX   boy    1.0   19
3   4   LY   boy    1.0   25
4   5   TT  gril    2.0   23
5   6   OP  gril    2.0   20
6   7   WO  gril    4.0   70
7   8  TYU   boy    NaN  100
#空格也算是值
```
读行：`print(data[2:6]["name"])`
```python
#输出
2    XJX
3     LY
4     TT
5     OP
```
读列：`print(data.loc[:,["sex","name"]])`
```python
#输出
    sex name
0   boy  WxQ
1  gril  WxF
2   boy  XJX
3   boy   LY
4  gril   TT
5  gril   OP
6  gril   WO
7   boy  TYU
```
读特定行列：`print(data.loc[[1,3,5],["id","name","age"]])`
```python
#输出：
   id name  age
1   2  WxF   34
3   4   LY   25
5   6   OP   20
```
读连续的行列：`print(data.loc[1:5,["id","name","age"]])`
```python
#输出：
   id name  age
1   2  WxF   34
2   3  XJX   19
3   4   LY   25
4   5   TT   23
5   6   OP   20
```

