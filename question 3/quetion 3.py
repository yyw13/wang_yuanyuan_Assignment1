import numpy as np
import matplotlib.pyplot as plt




## problem 3 part a

## t is an array of the value of theta
## we cut [0, pi] interval into "n_interval" small intervals
start_t = 0
stop_t = np.pi
n_interval = 20
t = np.linspace(start_t, stop_t, num = n_interval, endpoint=False)

## calculate the integral
x = np.arange(0,20,0.1)
def J(t, m, x): ## m is m, and t is theta
    p = (np.cos(m*t - x*(np.sin(t))))/n_interval
    return sum(p)

## plot the figure when m=0, m=1, m=2 
plt.figure()
for m in range(3):
    u = []  ## set an array of different value of J(x), when m has different value
    for x_i in x:
        u.append(J(t,m,x_i)) 
    plt.plot(x,u)
    plt.ylabel('J(x)')  ## it's the plot of frequency vs chi
    plt.xlabel('x')
plt.show()



## problem 3 part b

## Assume intensity I0 is 5
I0 = 5.
## Assume lamda is 4
Lamda = 4.
## Assume distance from the aperture to the focal plane is R = 4
R = 4.
## Assume a is 1
a = 1.
## the range of q is q_range = 10
q_range = 10.

## q is the distance from the optical axis
## q^2 = m^2 + n^2

## we want to make a m by n matrix of the size of the image
m = np.arange(-q_range,q_range,0.1)
n = np.arange(-q_range,q_range,0.1)

## we make a empty n by m matrix first
q = np.zeros((len(n),len(m)))
for i in range(len(n)):
    for j in range(len(m)):
        q[i][j] = (n[i]**2 + m[j]**2)**0.5 ## q = (m**2 + n**2)**0.5

x=[]  ## make x a matrix
Ix=[] ## make Ix a matrix
## define f2 to be function to calculate x, which is an array of dimension 1*n
def f2(p_a,p_q,p_R,p_L):
    return ((((np.pi*2)*p_a)*p_q)/p_L)/p_R
x = (2.*np.pi*a*q)/(Lamda*R)


def j1(p_t, p_m, p_x):
    return (I0*(2*J(p_t,p_m,p_x)/p_x)**2)
Ix = np.zeros((len(n),len(m)))
for i in range(len(n)):
    for j in range(len(m)):
        Ix[i][j] = j1(t, 1, x[i][j])
## the center intensity of image is 4I0
## here is a coefficient of 4, because in the I(x) function, when both J(x)&x go to 0, I(x) = 4I0
Ix[len(Ix)/2,len(Ix)/2] = 4.*I0 

plt.figure()
plt.imshow(Ix, cmap='Greys')
plt.colorbar()
plt.title("Intensity")
plt.show()



## Part C
from PIL import Image
from scipy import signal
from scipy import misc
import matplotlib.image as mpimg
from scipy import ndimage

## please change the routine when you run this code, cause this image isn't in my laptop anymore now:)
img2 = misc.imread('/Users/yuanyuanwang/Desktop/CITA assignment 1/question 3/Galaxy.jpg') #read in image

## Img2 is now a 3d array, based on RGB system
Ix_test = []
Ix_test = Ix
Ix_test /= Ix_test.sum() ## the sum of intensity should add up to 1

## make the 3d array to three 2d arrays
## then convolve on the 2d arrays
r = signal.convolve2d(img2[:,:,0], Ix_test, mode='same') #convolve red
g = signal.convolve2d(img2[:,:,1], Ix_test, mode='same') #convolve green
b = signal.convolve2d(img2[:,:,2], Ix_test, mode='same') #convolve blue

## combine the three 2d arrays r & g & b to a 3d array
im_out = np.dstack([r, g, b])

import matplotlib.pyplot as plt
plt.subplot(2,1,1)
ax = plt.subplot("211")
ax.set_title('Original image')
plt.imshow(img2)

plt.subplot(2,1,2)
ax = plt.subplot("212")
ax.set_title('Convolved image')
plt.imshow(im_out)
plt.show()

