import matplotlib.pyplot as plt
import numpy as np
N = 10
theta = np.arange(0.,2 * np.pi, 2 * np.pi / N)
radii = np.array([4,7,5,9,1,5,6,7, 8,3])
plt.axes([0.025, 0.025, 0.95, 0.95], polar=True)
colors = np.array(['#4bb2c5', '#c5b47f', '#EAA228', '#579575',
'#839557', '#958c12', '#953579', '#4b5de4', 'yellow', 'red'])
bars = plt.bar(theta, radii, width=(2*np.pi/N), bottom=0.0,
color=colors)
plt.show()