import numpy as np
import matplotlib.pyplot as plt
nps = (10+10)/100000
x1 = np.arange(-10,10,nps)
print(x1)
plt.plot(x1,x1**2)
plt.show()