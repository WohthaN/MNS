import random
import sys
import argparse
import pylab
import matplotlib
import matplotlib.pyplot as plt
import numpy
from ContoCorrente import recursiveMethod, resolutiveMethod

fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)

steps = 12

opA = [random.gauss(1,2)*25 for i in xrange(steps)]
opAc = [25 for i in xrange(steps)]
iR = 1
iR1 = 1.1
sV = 10

(ix,iy) = recursiveMethod(opA, iR, sV)
riy = [resolutiveMethod(opA[0:x],iR,sV) for x in xrange(steps+1)]
axs[0][0].plot(xrange(len(ix)), ix, 'b-o')
axs[0][0].plot(xrange(len(iy)), iy, 'b-')
axs[0][0].plot(xrange(len(riy)), riy, 'bx')
axs[0][0].grid()
axs[0][0].legend(('depositi','m. ricorsivo','m. risolutivo'))
axs[0][0].title.set_text('Conto senza interessi')

(ix,iy) = recursiveMethod(opAc, iR, sV)
riy = [resolutiveMethod(opAc[0:x],iR,sV) for x in xrange(steps+1)]
axs[0][1].plot(xrange(len(ix)), ix, 'g-o')
axs[0][1].plot(xrange(len(iy)), iy, 'g-')
axs[0][1].plot(xrange(len(riy)), riy, 'gx')
axs[0][1].grid()
axs[0][1].legend(('depositi','m. ricorsivo','m. risolutivo'))
axs[0][1].title.set_text('Conto senza interessi')

(ix,iy) = recursiveMethod(opA, iR1, sV)
riy = [resolutiveMethod(opA[0:x],iR1,sV) for x in xrange(steps+1)]
axs[1][0].plot(xrange(len(ix)), ix, 'b-o')
axs[1][0].plot(xrange(len(iy)), iy, 'b-')
axs[1][0].plot(xrange(len(riy)), riy, 'bx')
axs[1][0].grid()
axs[1][0].title.set_text('Conto con interessi')

(ix,iy) = recursiveMethod(opAc, iR1, sV)
riy = [resolutiveMethod(opAc[0:x],iR1,sV) for x in xrange(steps+1)]
axs[1][1].plot(xrange(len(ix)), ix, 'g-o')
axs[1][1].plot(xrange(len(iy)), iy, 'g-')
axs[1][1].plot(xrange(len(riy)), riy, 'gx')
axs[1][1].grid()
axs[1][1].title.set_text('Conto con interessi')

pylab.show()
