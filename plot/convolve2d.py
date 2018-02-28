
'''
Created on Jul 13, 2015
@author: kashefy
Original at https://gist.github.com/kashefy/00279f9edb3a56fd3d15
'''
import numpy as np
from scipy import signal

if __name__ == '__main__':

    x = np.array([[1, 1, 1, 0, 0],
                  [0, 1, 1, 1, 0],
                  [0, 0, 1, 1, 1],
                  [0, 0, 1, 1, 0],
                  [0, 1, 1, 0, 0]],
                 dtype='float')

    w_k = np.array([[1, 0, 1],
                    [0, -4, 0],
                    [1, 0, 1],],
                   dtype='float')

    # w_k = np.rot90(w_k, 2)

    print x.shape, w_k.shape
    f = signal.convolve2d(x, w_k, 'valid')

    print f

    weights = np.random.randn()
