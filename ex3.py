import numpy as np
import matplotlib.pyplot as plt
import scipy.special.cython_special
x=np.linspace(0.,20.,2000)
y0 = scipy.special.jn(0,x)
y1 = scipy.special.jn(1,x)
y2 = scipy.special.jn(2,x)
y3 = scipy.special.jn(3,x)
y4 = scipy.special.jn(4,x)
fig, ax = plt.subplots()
ax.plot(x,y0,color='black')
ax.plot(x,y1,color='red')
ax.plot(x,y2,color='blue')
ax.plot(x,y3,color='green')
ax.plot(x,y4,color='yellow')
plt.show()
