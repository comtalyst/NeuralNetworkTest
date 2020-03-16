import numpy as np 
import matplotlib.pyplot as plt
import math

### file data
path = "data/"
filename = "2d_2color_dots.txt"

### user-defined constants
m = 1000                     # amount of data
x_min = 0
x_max = 1
y_min = 0
y_max = 1
noise = 0.00                # chance of inverted color, =1 will results in almost total inversion
seed = 136


### generate seed
np.random.seed(seed)

### user-difined qualification function
def qualify(x, y):
    # this is a sin function
    r1 = 0.09
    r2 = 0.5
    r3 = 0.4
    Y = y <= np.sin(x/r1)*r2 + r3           # got an array of booleans here
    # add noise
    noiser = (np.random.random(Y.shape) >= noise)
    Y = (Y == noiser)                                                       # sounds weird but it actually equivalent to what we want
    # return
    Y = Y.astype(int)                                                       # better convert to to 0s and 1s
    return Y.reshape(1, Y.shape[0])                                         # from 1D to 2D for the ease of future operation


### main
## generate 2D coords (2 features)
X = np.zeros((2, m))
X[0] = np.random.random((1, m))*(x_max - x_min ) + x_min                 # generate properly scale the data           
X[1] = np.random.random((1, m))*(y_max - y_min ) + y_min

## generate outputs
Y = qualify(X[0], X[1])

## ready the data for extraction
s = ' '.join(map(str, X[0])) + '\n' + ' '.join(map(str, X[1])) + '\n' + ' '.join(map(str, Y[0])) + '\n'

## write generated data into a file
f = open(path + filename, "w")
f.write(s)
f.close()

## plot the data
plt.scatter(X[0, :], X[1, :], c=Y, s=40, cmap=plt.cm.Spectral)
plt.show()