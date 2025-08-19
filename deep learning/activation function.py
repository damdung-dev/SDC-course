import numpy as np
import matplotlib.pyplot as plt
import math

def sigmoid(x):
    return 1/(1+math.e**-x)

x=np.arange(-10,10,0.003)
plt.plot(x,sigmoid(x))
plt.show()
