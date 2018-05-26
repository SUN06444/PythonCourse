import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#wdbc separate by ','
wdbc=pd.read_csv("wdbc.txt")
print(wdbc[:10])
print("mean of c7=",np.mean(wdbc['c7']))
print(wdbc[['id','diagnosis']][:10])
df2=wdbc[['id','diagnosis']][:10]
df2.to_csv("wdbc1.txt")
print(wdbc.describe())
print(wdbc[wdbc["diagnosis"] =='B'][:10])


# graph
z=wdbc['c1']
plt.hist(z)
plt.show()

