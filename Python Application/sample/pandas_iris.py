import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#iris separate by ' '
iris=pd.read_csv("iris_all.txt",sep=" ")
print(iris)
print(iris.describe())
print("Mean of Sepal Length=",np.mean(iris['Sepal.Length']))
print(iris[iris["Spec.Pred"] =='virginica'])
print(iris.loc[(iris["Spec.Pred"] =='virginica') | (iris["Spec.Pred"] =='versicolor')])
print(iris.loc[(iris["Spec.Pred"] =='virginica') & (iris["Petal.Width"]>2.0)])
# graph
x=iris['Sepal.Length']
y=iris['Petal.Length']

plt.plot(x,y,"ro")
plt.show()

items, counts = np.unique(iris["Spec.Pred"], return_counts=True)
print(np.asarray((items, counts)))
plt.bar(items, counts)
plt.show()

plt.pie(counts,labels=items,autopct="%.1f%%")
plt.show()

