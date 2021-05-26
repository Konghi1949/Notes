import numpy as np
import pandas as pd
data = pd.read_csv("1.CSV")
print(a)
# print(data.isnull())
#空格算ONNULL
# print(data[2:6]["name"])
# print(data.loc[:,["sex","name"]])
# print(data.loc[[1,3,5],["id","name","age"]])
print(data.loc[1:5,["id","name","age"]])
