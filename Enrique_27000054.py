#!/usr/bin/env python3
"""
Proyecto Polinomio de Lagrange.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""


def polinomio_lagrange(X, Y):
    """
    Implementa y retorna el Polinomio de Lagrange para las listas X e Y.

    Parámetros:
    X: lista de valores de la variable independiente.
    Y: lista de valores de la variable dependiente.
    """

    if len(X) != len(Y):
         raise ValueError("Dimensiones diferentes en X e Y.")

    # Ordena el par (x, y) en forma ascendente por x.
    pares = list(zip(X, Y))
    pares.sort(key = lambda x: x[0])
    X, Y  = zip(*pares)
    r= len(X)
 
    def polinomio(x):
        px=0
        j=[]
        for i in range (r):
            j= Y[i]
            for k in range (r):
                if (k!=i):
                    j=j*((x-X[k]) / (X[i]-X[k]))                   
            px= px+j
            
        return px
        
    return polinomio


if __name__ == '__main__':
    # Pruebe aquí su Polinomio de Lagrange ...
    X=[-4,-3,2,-6]
    Y=[-16,-5,-10,-50]
    polinomio=polinomio_lagrange(X,Y)
    p=polinomio(1)
    print(p)