import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0.5, 2, 100)
y = -np.log(x) + x * x / 2 - 0.5
plt.plot(x, y)
plt.show()