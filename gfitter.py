from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
import sys

filename = str(sys.argv[1])
data = np.genfromtxt(filename)
x, y = data

def func(x, *params):
    y = np.zeros_like(x)
    for i in range(0, len(params), 3):
        ctr = params[i]
        amp = params[i+1]
        wid = params[i+2]
        y = y + amp * np.exp( -((x - ctr)/wid)**2)
    return y

guess = [0, 60000, 80, 1000, 60000, 80]
for i in range(12):
    guess += [60+80*i, 46000, 25]

popt, pcov = curve_fit(func, x, y, p0=guess)
print popt
fit = func(x, *popt)

plt.plot(x, y)
plt.plot(x, fit , 'r-')
plt.show()
