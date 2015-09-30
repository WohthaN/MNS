import numpy as np
#import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
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