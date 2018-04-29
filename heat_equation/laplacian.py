
import numpy as np
from scipy.ndimage import convolve

def laplacian(Z):
    return (                 Z[0:-2,1:-1] +
            Z[1:-1,0:-2] - 4*Z[1:-1,1:-1] + Z[1:-1,2:] +
                             Z[2:  ,1:-1] )


dL = 1

e2 = np.identity(10)

stencil= (1.0/(12.0*dL*dL))*np.array(
        [[0,0,-1,0,0],
         [0,0,16,0,0],
         [-1,16,-60,16,-1],
         [0,0,16,0,0],
         [0,0,-1,0,0]])

stencil2= (1.0/(2.0*dL*dL))*np.array(
        [[0,-1,0],
         [-1,4,-1],
         [0,-1,0]])


#        print convolve(e2, stencil2, mode='wrap')


print convolve(e2, stencil2)
