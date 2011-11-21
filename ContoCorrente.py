import sys
import argparse
import pylab
import matplotlib
import numpy

def main(operationsArray, interestRate, startValue):
    pass

def recorsiveMethod(opA, iR, sV):
    y = [sV]
    iR = 1 + iR

    for i in xrange(len(opA)):
        y.append(y[i] * iR + opA[i])

    plot = pylab.plot(range(len(opA) + 1), y)
    print y[len(y)-1]
    pylab.show()

def resolutiveMethod(opA, iR, sV):
    iR=1+iR
    y = sV*(iR**(len(opA)))
    for i in xrange(len(opA)):
        y+=opA[i]*(iR**(len(opA)-i-1))
    print y

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--start-value", action="store", dest="opA", required=True,
                        type=float)
    parser.add_argument("-i", "--interest-rate", action="store", dest="interests", required=True,
                        type=float)
    parser.add_argument("-o", "--deposits", action="store", dest="opl", default="[]")
    options = parser.parse_args()
    opA = options.opA
    interests = options.interests
    opl = eval(options.opl)

    recorsiveMethod(opl, interests, opA)
    resolutiveMethod(opl, interests, opA)

    print opA, interests, opl