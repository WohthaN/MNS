import random
import sys
import argparse
import pylab
import matplotlib
import matplotlib.pyplot as plt
import numpy

def main(operationsArray, interestRate, startValue):
    pass

def recursiveMethod(opA, iR, sV):
    y = [sV]
    for i in xrange(len(opA)):
        y.append(y[i] * iR + opA[i])
    return (opA,y)

def resolutiveMethod(opA, iR, sV):
    y = sV*(iR**(len(opA)))
    for i in xrange(len(opA)):
        y+=opA[i]*(iR**(len(opA)-i-1))
    return y


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


(ix,iy) = recursiveMethod(opAc, iR, sV)
riy = [resolutiveMethod(opAc[0:x],iR,sV) for x in xrange(steps+1)]
axs[0][1].plot(xrange(len(ix)), ix, 'g-o')
axs[0][1].plot(xrange(len(iy)), iy, 'g-')
axs[0][1].plot(xrange(len(riy)), riy, 'gx')
axs[0][1].grid()
axs[0][1].legend(('depositi','m. ricorsivo','m. risolutivo'))

(ix,iy) = recursiveMethod(opA, iR1, sV)
riy = [resolutiveMethod(opA[0:x],iR1,sV) for x in xrange(steps+1)]
axs[1][0].plot(xrange(len(ix)), ix, 'b-o')
axs[1][0].plot(xrange(len(iy)), iy, 'b-')
axs[1][0].plot(xrange(len(riy)), riy, 'bx')
axs[1][0].grid()

(ix,iy) = recursiveMethod(opAc, iR1, sV)
riy = [resolutiveMethod(opAc[0:x],iR1,sV) for x in xrange(steps+1)]
axs[1][1].plot(xrange(len(ix)), ix, 'g-o')
axs[1][1].plot(xrange(len(iy)), iy, 'g-')
axs[1][1].plot(xrange(len(riy)), riy, 'gx')
axs[1][1].grid()

pylab.show()
#
#if __name__ == "__main__":
#
#    parser = argparse.ArgumentParser()
#    parser.add_argument("-s", "--start-value", action="store", dest="opA", required=True,
#                        type=float)
#    parser.add_argument("-i", "--interest-rate", action="store", dest="interests", required=True,
#                        type=float)
#    parser.add_argument("-o", "--deposits", action="store", dest="opl", default="[]")
#    options = parser.parse_args()
#    opA = options.opA
#    interests = options.interests
#    opl = eval(options.opl)
#
#    recorsiveMethod(opl, interests, opA)
#    resolutiveMethod(opl, interests, opA)
#
#    print opA, interests, opl