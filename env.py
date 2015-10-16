import numpy as np
#import scipy as sp
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.ticker as mpl_ticker


from math import *



mpl.rc('text', usetex='True')

def float_info():
    import sys
    print "Python built in: %s " % sys.float_info

    print "Numpy:"
    y = np.array([1.])
    print "\n".join(" - %s: %s " % (x,np.finfo(y[0].astype(x))) for x in ("float", "float16", "float32", "float64", "float128"))

def float_format(x):
    return "%.100g" % x

def plot_marker_generator():
    markers = [',','.','1','2','3','4','_','x','|','+']
    #filled markers , '8','>','<','^','v','o','d','D','h','H','*','p','s'  ]
    lmarkers = len(markers)
    c = 0
    while True:
        yield markers[c]
        c = (c+1)%lmarkers

def color_map_generator(N, repeat=1, cmap='spectral'):
    '''Returns a function that maps each index in 0, 1, ... N-1 to a distinct
    RGB color.'''
    # cmaps:
    # -spectral
    # -prism
    color_norm  = mpl.colors.Normalize(vmin=0, vmax=N-1)
    scalar_map = mpl.cm.ScalarMappable(norm=color_norm, cmap=cmap)
    index = 0
    while True:
        for _ in range(repeat):
            yield scalar_map.to_rgba(index)
        index = (index+1)%(N)

GRID_OPTIONS = {'b':True, 'which':'both', 'linestyle':':'}
GRID_OPTIONS_TWIN = {'b':True, 'which':'both', 'linestyle':'-.'}
