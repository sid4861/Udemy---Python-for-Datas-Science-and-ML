import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


################## matplotlib concepts #####################

x = np.linspace(0, 5, 11)
y = x**2

##plt.plot(x,y)
##plt.xlabel('X label')
##plt.ylabel('Y label')
##plt.title('DEMO')
###plt.show()
##
##plt.subplot(1,2,1)
##plt.plot(x,y,'r')
##plt.subplot(1,2,2)
##plt.plot(x,y,'b')
###plt.show()

##fig = plt.figure()
##axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
##axes2 = fig.add_axes([0.2,0.5,0.4,0.4])
##axes1.plot(x,y,'r')
##axes1.set_xlabel('x')
##axes1.set_ylabel('y')
##axes1.set_title('LEFT FIGURE')
##
##axes2.plot(y,x,'b')
##axes2.set_xlabel('x')
##axes2.set_ylabel('y')
##axes2.set_title('RIGHT FIGURE')
##
##plt.show()


###############   part2 ####################

"""
    subplot function automatically creates axes depending on nrows and ncols
    no need to call add_axes method to create axes with fig object like above
"""

fig, axes = plt.subplots(nrows=1, ncols=2)
##axes[0].plot(x,y,'r')
##axes[1].plot(y,x,'b')
##axes[0].set_title('first plot')
##axes[1].set_title('second plot')
##plt.tight_layout()
##plt.show()

"""
axes is a list of axes, which can be looped over
"""

##for current_axis in axes:
##    current_axis.plot(x,y,'b')
##
##plt.tight_layout()
##plt.show()


# fig size and dpi
##
##fig = plt.figure(figsize=(8,2))
##ax = fig.add_axes([0,0,1,1])
##ax.plot(x,y,'r')
##plt.show()
##
##
##fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(5,2))
##axes[0].plot(x,y,'r')
##axes[0].set_title('top')
##axes[1].plot(y,x,'g')
##axes[1].set_title('bottom')
##
##fig.savefig('fig1.png', dpi=200)
##plt.tight_layout()
##plt.show()


### legends
##
##fig, axes = plt.subplots(nrows=1, ncols=2)
##axes[0].plot(x, x**2, 'r', label='X squared')
##axes[0].legend()
##axes[1].plot(x, x**3, 'g', label='X cube')
##axes[1].legend()
##plt.tight_layout()
##plt.show()
##


fig, axes = plt.subplots(nrows=1, ncols=2)
axes[0].plot(x, x**2,color='orange' ,lw=2, ls='--', marker='o', label='X square')
axes[0].set_title('LEFT')
axes[0].legend()

axes[1].plot(x, x**3,color='purple', lw=2,marker='X', label='x cube')
axes[1].set_title('RIGHT')
axes[1].legend()

plt.show()
