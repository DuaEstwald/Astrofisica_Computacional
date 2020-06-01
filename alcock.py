# Aqui vienen dado un fichero de parametros caracteristicos para la microlente LMC-9


def microlensing(name):
    if name == 'LMC9':
        M1M2 = 1.627
        a = 1.657
        u0 = -0.054
        theta = 0.086
        eps1 = 1./(1.+(1./M1M2))
        eps2 = 1./(1.+M1M2)
        x1l1 = -eps2*a
        x2l1 = 0.
        x1l2 = eps1*a
        x2l2 = 0.
    return eps1,eps2,x1l1,x2l1,x1l2,x2l2,theta,u0
