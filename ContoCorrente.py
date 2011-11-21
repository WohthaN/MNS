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
    iR = 1 + iR

    for i in xrange(len(opA)):
        y.append(y[i] * iR + opA[i])

    return (opA+[0],y)

def resolutiveMethod(opA, iR, sV):
    iR=1+iR
    y = sV*(iR**(len(opA)))
    for i in xrange(len(opA)):
        y+=opA[i]*(iR**(len(opA)-i-1))
    return y


fig, axs = plt.subplots(2, 2, sharex=True, sharey=True)

opA = [random.random()*50 for i in xrange(12)]
opAc = [25 for i in xrange(12)]
iR = 0
sV = 100

(ix,iy) = recursiveMethod(opA, iR, sV)
axs[0][0].plot(xrange(len(ix)), ix, 'b-o')
axs[0][0].plot(xrange(len(iy)), iy, 'b-x')

(ix,iy) = recursiveMethod(opAc, iR, sV)
axs[0][1].plot(xrange(len(ix)), ix, 'g-s')
axs[0][1].plot(xrange(len(iy)), iy, 'g-*')

iR = 0.15
(ix,iy) = recursiveMethod(opA, iR, sV)
axs[1][0].plot(xrange(len(ix)), ix, 'b-o')
axs[1][0].plot(xrange(len(iy)), iy, 'b-x')

(ix,iy) = recursiveMethod(opAc, iR, sV)
axs[1][1].plot(xrange(len(ix)), ix, 'g-s')
axs[1][1].plot(xrange(len(iy)), iy, 'g-*')

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