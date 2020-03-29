"""
K-Nearest neighbors classifier algorithm will search within the training set for the observation that most
closely approaches the new test sample .
Based on the Iris dataset.
"""

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

np.random.seed(1)
iris = datasets.load_iris()
data = iris.data
target = iris.target
i = np.random.permutation(len(data))
data_train=data[i[:-10]]
target_train=target[i[:-10]]
data_test=data[i[-10:]]
target_test=target[i[-10:]]
knc = KNeighborsClassifier()
knc.fit(data_train, target_train)
print(knc.predict(data_test))
print(target_test)

#mesh
cmap_light = ListedColormap(['#AAAAFF','#AAFFAA','#FFAAAA'])
h = .02
data = iris.data[:,:2]
target = iris.target
x_min, x_max = data[:,0].min() - .5, data[:,0].max() + .5
y_min, y_max = data[:,1].min() - .5, data[:,1].max() + .5
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
knn = KNeighborsClassifier()
knn.fit(data, target)
Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.figure()
plt.pcolormesh(xx,yy,Z,cmap=cmap_light)

#Plot the training points "The three decision boundaries"
plt.scatter(data[:,0],data[:,1],c=target)
plt.xlim(xx.min(),xx.max())
plt.ylim(yy.min(),yy.max())
plt.show()

#Petal size
data = iris.data[:,2:4]
target = iris.target
x_min, x_max = data[:,0].min() - .5, data[:,0].max() + .5
y_min, y_max = data[:,1].min() - .5, data[:,1].max() + .5
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
knn = KNeighborsClassifier()
knn.fit(data, target)
Z = knn.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.figure()
plt.pcolormesh(xx,yy,Z,cmap=cmap_light)

#Plot the training points "The three decision boundaries"
plt.scatter(data[:,0],data[:,1],c=target)
plt.xlim(xx.min(),xx.max())
plt.ylim(yy.min(),yy.max())
plt.show()