# Draw a line in a diagram frpm postion (0,0) to position (6, 250) 
import matplotlib.pyplot as plt
import numpy as np

xpoints= np.array([0, 6])
ypoints= np.array([6, 250])
plt.plot(xpoints , ypoints)
plt.show()
#--------------------------------------------
#Draw a line in a diagram from position (1, 3) to position (8, 10):

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()
#-----------------------------------------
#Plotting Without Line
#Draw two points in the diagram, one at position (1, 3) and one in position (8, 10):

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()

#Multiple Points

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 8, 1, 10, 5])
plt.plot(x, y, 'o')  # 'o'   
plt.show()
#Draw a line in a diagram from position (1, 3) to (2, 8) then to (6, 1) and finally to position (8, 10):
xpoints= np.array([1,2,6,8])
ypoints= np.array([3,8,1,10])
plt.plot(xpoints, ypoints)
plt.show()
#Default X-Points ,they will get defult values 0,1,2,3 depends on y values
ypoints= np.array([3,8,1,10,5,7])
plt.plot(ypoints)
plt.show()

#marker to emphasize each point with a specified marker
plt.plot(ypoints)
plt.show()
ypoints= np.array([3,8,1,10,5,7])
plt.plot(ypoints, marker='*') # mark each point with *
plt.show()
#fmt
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o-.m')
plt.show()