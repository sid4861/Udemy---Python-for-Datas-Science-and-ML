import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,100)
y = x*2
z = x**2
##
##fig = plt.figure()
##axis = fig.add_axes([0.1,0.1,0.8,0.8])
##axis.plot(x, y)
##axis.set_xlabel('X')
##axis.set_ylabel('Y')
##axis.set_title('Title')
##plt.show()

##
##fig = plt.figure()
##ax1 = fig.add_axes([0,0,1,1])
##ax2 = fig.add_axes([0.2,0.2,0.5,0.2])
##ax1.plot(x, y)
##ax2.plot(x, y)
##plt.show()
##
##
##fig = plt.figure()
##ax1 = fig.add_axes([0,0,1,1])
##ax2 = fig.add_axes([0.2,0.5,0.4,0.4])
##
##ax1.plot(x, y)
##ax2.plot(x, z)
##ax2.set_xlim(20,22)
##ax2.set_ylim(30, 50)
##plt.show()


fig, axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(x, y, color='pink', lw='2', ls='-.')
axes[0].set_xlabel('x')
axes[0].set_ylabel('y')
axes[1].plot(x, z, color='violet', lw='2', ls='--')
axes[1].set_xlabel('x')
axes[1].set_ylabel('z')
plt.show()
