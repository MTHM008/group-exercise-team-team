import numpy as np
from source.timestepping import *
from source.models import SIR


def run_SIR():
    S0 = 6e7
    I0 = 1000
    R0 = 0
    Y0 = np.array([S0, I0, R0])
    r = 3e-9
    a = 1/14
    t, y = timeloop(forward_euler, SIR, Y0, dt=1, tmax=200, r=r, a=a)
    return t, y


def test_Imax():

    t, y = run_SIR()
    Imax = y[:,1].max()
    assert Imax > 14e6 and Imax < 15e6
