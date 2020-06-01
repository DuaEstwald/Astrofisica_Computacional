# Este .py sirve para introducir desde fuera los parametros de la lente

ltype = 'TwoPoints' 
sour = 'fitsim'
filename = 'medusa0.png'
jpg = True
# Definimos el numero de pixeles de cada plano
n_y = 401
nx = 401
#if sour == 'gcirc':
#ny = 388
#if sour == 'fitsim':
#    ny = a[0].size
# Definimos el tamanio de los planos, medida en radio de Einstein
xl = 3. # plano imagen
yl = 3. # plano fuente
# Definimos los parametros de la fuente
xpos = 0.05
ypos = 0.4
rad = 0.1

def param(name):
    x01 = -0.15
    x02 = 0.1
    ml = 1.0
    k = 0.1
    g = 0.4
    th = 1.
    if name == 'Point':
        return x01,x02,ml
    elif name == 'TwoPoints':
        x01l1 = 0.0
        x02l1 = -0.5
        ml1 = 0.5
        x01l2 = 0.0
        x02l2 = 0.5
        ml2 = 0.5
        return x01l1,x02l1,x01l2,x02l2,ml1,ml2
    elif name == 'ChangRefsdal':
        return x01,x02,ml,k,g
    elif name == 'SIS':
        return x01,x02,th
    elif name == 'SISChangRefsdal':
        return x01,x02,th,k,g


