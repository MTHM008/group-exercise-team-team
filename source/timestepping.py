import numpy as np

def forward_euler(rhs, Y, dt, **kwargs):
    # applies the forward Euler method to the equation y' = f(y) where
    # the right hand side f(y) is returned by the function rhs
    return Y + dt*rhs(Y, **kwargs)

def timeloop(method, rhs, Y0, dt, tmax, **kwargs):

    t = 0
    Yn = Y0

    times = [t]
    soln = Y0.copy()

    while t < tmax:
        Ynp1 = method(rhs, Yn, dt, **kwargs)
        Yn = Ynp1
        t += dt
        soln = np.vstack((soln, Ynp1))
        times.append(t)

    return times, soln
