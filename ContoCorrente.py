def recursiveMethod(opA, iR, sV):
    y = [sV]
    for i in xrange(len(opA)):
        y.append(y[i] * (1+iR) + opA[i])
    return (opA,y)

def resolutiveMethod(opA, iR, sV):
    y = sV*(iR**(len(opA)))
    for i in xrange(len(opA)):
        y+=opA[i]*((1+iR)**(len(opA)-i-1))
    return y
