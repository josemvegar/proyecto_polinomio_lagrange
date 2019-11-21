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

    if len(X) != len(Y): raise ValueError("Dimensiones diferentes en X e Y.")

    # Ordena el par (x, y) en forma ascendente por x.
    pares = list(zip(X, Y))
    pares.sort(key = lambda x: x[0])
    X, Y  = zip(*pares)

    def polinomio(x):     
         i=0
         j=0
         p=0
         size=len(X)
         while (i<size):
             result=1
             for j in range (size):
                if (j!=i):
                    result*=((x-X[j])/(X[i]-X[j]))
             p+=(Y[i]*result)
             i+=1
         return p
    return polinomio


if __name__ == '__main__':
    # Pruebe aquí su Polinomio de Lagrange ...
    X=[0,-2,4,2]
    Y=[-1,1,-2,3]
    p=polinomio_lagrange(X,Y)
    print(p(3))
    pass