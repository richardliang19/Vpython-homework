from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np
X=np.array([[9],[4],[7],[3],[10],[7],[4],[3],[1],[9]])
Y=np.array([45,24,59,28,91,28,42,18,14,82])

plt.show()
plt.scatter(X,Y,linewidths=0.1)
plt.show()
model = LinearRegression()
model.fit(X,Y)
predict = model.predict(X)
plt.plot(X,predict,color="red")
plt.scatter(X,Y)
plt.show()