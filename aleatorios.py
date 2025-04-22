"""
Pau Dresaire

"""

class Aleat:
    """
    Clase que implementa un generador de números aleatorios usando LCG.
    Atributos: m, a, c, x0, que son los parametros para aplicar la formula de LCG
    Pruebas:
    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    16
    29
    18
    15
    
    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    18
    15
    20
    1
    """
    def __init__(self, m=2**48, a=25214903917, c=11, x0=1212121):
        self.m, self.a, self.c, self.x0 = m, a, c, x0
        self.xn = x0
        #self.xn = (self.a * self.x0 + self.c) % self.m

    def __next__(self):
        self.xn = (self.a * self.xn + self.c) % self.m
        return self.xn

    def __call__(self, seed):
        self.xn = seed   


def aleat(m=2**48, a=25214903917, c=11, x0=1212121):
    """
    Función generadora que implementa un generador de números aleatorios usando LCG.
    Argumentos: m, a, c, x0, que son los parametros para aplicar la formula de LCG
    Pruebas:
    >>> rand = aleat(m=64, a=5, c=46, x0=36)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    34
    24
    38
    44
    
    >>> rand.send(24)
    38
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    44
    10
    32
    14
    """
    xn = (a * x0 + c) % m

    while True:
        seed = yield xn
        if seed:
            xn = (a * seed + c) % m
        else:
        	xn = (a * xn + c) % m