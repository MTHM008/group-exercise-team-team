import numpy as np

def SIR(Y, r, a):
    S, I, R = Y
    return [-r*I*S,r*I*S - a*I, aI]

def Brusselator(Y, a, b):
    x, y = Y
return np.array([a + x**2*y - b*x +x, b*x - x**2*y])
