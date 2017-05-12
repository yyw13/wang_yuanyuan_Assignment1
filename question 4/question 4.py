#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

size = 1000 #determines the size and resolution of the plot in pixels-per-size

def isbounded(d): #this function inputs a possible complex C value, and returns the number of iterations it takes for it to go above a certain upper bound

	z = 0 + 0j #set z0 to be zero

	i = 0
	run = []
	stillUnder = np.zeros((size, size))

	while i < 70:
		z = z**2 + d #iterate the function
		i += 1
		zabs = z.real**2 + z.imag**2 #calculate the absolute value of the current z
		ifUnd = zabs < 100 #check if the absoulte value is bounded still, and puts a 1 in all the spots where it is
		stillUnder = stillUnder + ifUnd #add this matrix of 1s to the stillUnder matrix, so stillUnder keeps track of how many iterations each pixel has remained under the bound

	return stillUnder
	

cx = np.linspace(-1, 1, size)
cy = np.linspace(-1, 1, size)#set up the space from -1 to 1. these values can be modified

cxv, cyv = np.meshgrid(cx,cy)

c = cxv + cyv*(1j)

converge = isbounded(c) #converge is a matrix of values showing how many iterqations it took each pixel to diverge

plt.figure(figsize = (8,8))
plt.clf()
plt.imshow(converge)
plt.colorbar()

plt.show()#displays the image
#plt.savefig("QUestion4_output.png")

