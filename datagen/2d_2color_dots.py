import numpy as np 
import matplotlib.pyplot as plt

### file data
path = "data/"
filename = "2d_2color_dots.txt"

### user-defined constants
m = 1000                     # amount of data
x_min = -200
x_max = 200
y_min = -200
y_max = 200
noise = 0.05                # chance of inverted color, =1 will results in almost total inversion
seed = 136


### generate seed
np.random.seed(seed)

### user-difined qualification function
def qualify(x, y):
    # this is a linear function
    r = 150
    Y = x*x + y*y <= r*r            # got an array of booleans here
    # add noise
    noiser = (np.random.random(Y.shape) >= noise)
    Y = (Y == noiser)                                                       # sounds weird but it actually equivalent to what we want
    # return
    Y = Y.astype(int)                                                       # better convert to to 0s and 1s
    return Y.reshape(1, Y.shape[0])                                         # from 1D to 2D for the ease of future operation


### main
## generate 2D coords (2 features)
X = np.zeros((2, m))
X[0] = np.random.random((1, m))*(x_max - x_min + 1) + x_min                 # generate properly scale the data           
X[1] = np.random.random((1, m))*(y_max - y_min + 1) + y_min

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