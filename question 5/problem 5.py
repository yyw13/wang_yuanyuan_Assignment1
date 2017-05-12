import numpy as np
import matplotlib.pyplot as plt

start = -14 ## the start number is 10^-14
stop = -4   ## the stop number is 10^-4

## cut the total interval to n small intervals
## k is the array of every start point of small intervals
d = np.logspace(start, stop, num=100, base=10, endpoint=True)

## computer the derivative of f(x), when x = 1
x = 1
def f(d):
    return (((x+d)*(x+d-1)) - (x*(x-1)))/d

plt.plot(d,f(d))
plt.ylabel('Derivative of f(x)')  ## it's the plot of frequency vs chi
plt.xlabel('Delta')
plt.show()

## We found that the plot is a straight line
## the smaller the k we choose, the closer the derivative of f(x) is close to the true value 