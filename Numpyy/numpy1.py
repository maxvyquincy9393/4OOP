import numpy as np
import matplotlib.pyplot as plt

# persamaan garis

x = np.arange(0, 10,1)
y = 2 * x + 3

print(x)
print(y)

#plt.plot(x, y)
#plt.show()

# circle

jari2 = 5

sudut = np.linspace(0,2*np.pi,100)
x2 = jari2 * np.cos(sudut)
y2 = jari2 * np.sin(sudut)

plt.plot(x2, y2)
