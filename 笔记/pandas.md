# Pandas

### Series（系列）
  Series 是一个带有`名称`和`索引`的一维数组
```python
import pandas as pd
import numpy as np
# 引入
money = [4.5,7.3,11.2,100.0,43.1]
name = ["西瓜","苹果","菠萝","香蕉","圣女果"]
S_thing = pd.Series(money)
S_thing.index = name
S_thing.index.name = "商品"
S_thing.name = "订单"
N_thing = S_thing.value
print(S_thing)
print(S_thing["西瓜"] > 3.0)
print(N_thing,type(N_thing))
```
print结果为：
```python
商品
西瓜       4.5
苹果       7.3
菠萝      11.2
香蕉     100.0
圣女果     43.1
Name: 订单, dtype: float64
True
[  4.5   7.3  11.2 100.   43.1] <class 'numpy.ndarray'>
```

注意点：
  - Series对象有`字典`功能,也可以直接转换字典
  - 通过Series的俩个属性`values`和`index`获取内容和索引
  - Series获取的内容输出为一个`numpy.ndarray`类型
  - `pd.isnull`和`pd.nonull`可检测缺失数据
  - 主要特点为：同质数据、大小不可变、数据值可变

---

### Dataframe（数据帧）
  DataFrame 是一个带有索引的（异构数据）二维数据结构，每列可以有自己的名字，并且可以有不同的数据类型。你可以把它想象成一个 excel 表格或者数据库中的一张表，DataFrame 是最常用的 Pandas 对象

```python
import pandas as pd
import numpy as np

air_name = pd.Index(data =["北京-深圳" ,"东京-名古屋" ,"3元-2元"] ,name ="航班")
air_data ={
    "售价" :[1800,18000,999999],
    "区域" :["国内" ,"跨国" ,"跨世"],
    "序号" :[1,2,3]
}

air =pd.DataFrame(data =air_data, index =air_name)
print(air)
# print(air[1:])
# print(air.loc["3元-2元"])
# print(air.iloc[2])
# print(air["售价"])
# print(air[["售价","区域"]])
air["是否在售"] = "在售"
# 添加列
print(air)
air.pop("是否在售")
# 删除列
print(air)
air["是否在售"] = ["在售","在售","断票"]
print(air)
print(air.assign(air_new = air["售价"] + 1))
# 添加新列，不在原变量上添加，可以另存为
```
print结果:
```python
            售价  区域  序号 
航班                         
北京-深圳     1800  国内   1 
东京-名古屋   18000  跨国   2
3元-2元   999999  跨世   3   
            售价  区域  序号 是否在售
航班
北京-深圳     1800  国内   1   在售
东京-名古屋   18000  跨国   2   在售
3元-2元   999999  跨世   3   在售
            售价  区域  序号
航班
北京-深圳     1800  国内   1
东京-名古屋   18000  跨国   2
3元-2元   999999  跨世   3
            售价  区域  序号 是否在售
航班
北京-深圳     1800  国内   1   在售
东京-名古屋   18000  跨国   2   在售
3元-2元   999999  跨世   3   断票
            售价  区域  序号 是否在售  air_new
航班
北京-深圳     1800  国内   1   在售     1801
东京-名古屋   18000  跨国   2   在售    18001
3元-2元   999999  跨世   3   断票  1000000
```
注意点：
  - 列可以无限扩展
  - 主要特点为：异构数据、大小可变、数据可变
---
