import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-2.0,2.0,0.02)
y = np.arange(-2.0,2.0,0.02)
X,Y = np.meshgrid(x,y)
def f(x,y): return (1 - y**5 + x**5)*np.exp(-x**2-y**2)
C = plt.contour(X,Y,f(X,Y),8,colors='black')
plt.contourf(X,Y,f(X,Y),8,cmap=plt.cm.hot)
plt.clabel(C, inline=1, fontsize=10)
plt.colorbar()
plt.show()