# -*- coding: utf-8 -*-
"""lab7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mKkcEdFETS-GT4GaAeTAIpkwFWEuAffS
"""

import matplotlib
import matplotlib.pyplot as plt
import time
import numpy as np
import random

casual_array = [random.randint(1, 10) for i in range(1 * 10**6)]
numpy_array = np.array([random.randint(1, 10) for i in range(1 * 10**6)])
time.perf_counter()

casual_mlt = 1
for i in casual_array:
    casual_mlt *= i
casual_time = time.perf_counter()
casual_type = type(casual_mlt)

numpy_mlt = np.prod(numpy_array)
numpy_time = time.perf_counter() - casual_time
numpy_type = type(np.prod(numpy_array))
print(casual_time, casual_type, numpy_time, numpy_type)

time = []
dros_pos = []
air_waste = []

with open('data1.csv', 'r') as f:
    for line in f:
        ind = line.split(sep=';')
        time.append(ind[0])
        x1.append(ind[3])
        x2.append(ind[4])
    f.close()

time_name = time[0]
time.pop(0)
time = np.array(time, float)
x1_name = x1[0]
x1.pop(0)
x1 = np.array(x1, float)
x2_name = x2[0]
x2.pop(0)
x2 = np.array(x2, float)

plt.title('Поворот дросселя и расход воздуха в течении времени')
plt.xlabel(time_name)
plt.ylabel(x2_name +' и '+ x1_name)
plt.plot(np.array(time), np.array(x1))
plt.plot(np.array(time), np.array(x2))
plt.show()

plt.title('График корреляции')
plt.xlabel(x1_name)
plt.ylabel(x2_name)
plt.plot(x1,x2,'o')
plt.show()

np.random.seed(40)
xs = np.linspace(-1*np.pi, 1*np.pi, 100)
ys = xs
zs = np.tan(xs)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(xs, ys, zs, marker='*', c='pink')
plt.title('3D  график')
plt.show()