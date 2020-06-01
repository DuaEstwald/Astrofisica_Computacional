
# En este codigo estan presentadas las distintas lentes

# NOTAS: POR ALGUNA RAZON NO FUNCIONA SI UTILIZAMOS NUMPY


# xl1,xl2 son los puntos correspondientes a x01,x02 en el programa de evencio

def Point(x1,x2,x1l,x2l,ml): # Point lens of mass ml at x1l,x2l
    x1ml = (x1-x1l) # distancia a traves del eje x desde el rayo a la posicion de la lente
    x2ml = (x2-x2l)
    d = x1ml**2+x2ml**2+ 1.0e-12 #Este ultimo termino es solo para evitar que d sea exactamente 0 y no pete cuando salga dividiento
    y1 = x1-ml*(x1-x1l)/d
    y2 = x2-ml*(x2-x2l)/d
    return y1,y2


def TwoPoints(x1,x2,x1l1,x2l1,x1l2,x2l2,ml1,ml2): # Two point lens of mass ml1 at x1l1,x2l1 and ml2 at x1l2,x2l2
    x1ml1 = (x1-x1l1)
    x2ml1 = (x2-x2l1)
    d1 = x1ml1**2+x2ml1**2 + 1.0e-12
    x1ml2 = (x1-x1l2)
    x2ml2 = (x2-x2l2)
    d2 = x1ml2**2+x2ml2**2 + 1.0e-12
    y1 = x1 - ml1*x1ml1/d1 - ml2*x1ml2/d2 # lens equations
    y2 = x2 - ml1*x2ml1/d1 - ml2*x2ml2/d2
    return y1,y2


def ChangRefsdal(x1,x2,x1l,x2l,ml,k,g):
    x1ml = (x1-x1l)
    x2ml = (x2-x2l)
    d = x1ml**2.+x2ml**2.+1.0e-12
    y1 = x1*(1.0-(k+g))-ml*x1ml/d
    y2 = x2*(1.0-(k-g))-ml*x2ml/d
    return y1,y2

def SIS(x1,x2,x1l,x2l,th):
    x1ml = (x1-x1l)
    x2ml = (x2-x2l)
    d = (x1ml**2+x2ml**2+1.0e-12)**(0.5)
    y1 = x1-th*x1ml/d
    y2 = x2-th*x2ml/d
    return y1,y2

def SISChangRefsdal(x1,x2,x1l,x2l,th,k,g):
    x1ml = (x1-x1l)
    x2ml = (x2-x2l)
    d = (x1ml**2+x2ml**2+1.0e-12)**(0.5)
    y1 = x1*(1-(k+g))-th*x1ml/d
    y2 = x2*(1-(k-g))-th*x2ml/d
    return y1,y2


