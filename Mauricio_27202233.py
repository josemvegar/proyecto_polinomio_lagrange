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
        Pn = 0.0
        for i in range(len(X)):
            Lx = 1.0
            for k in range(len(X)):
                if i == k: continue
                Lx *= (x - X[k])/(X[i] - X[k])
            Pn += (Lx * Y[k])
        return Pn
    return polinomio


if __name__ == '__main__':
    X=[2,1,-1]
    Y=[3,-2,1]
    Pn=polinomio_lagrange(X,Y)
    print(Pn(2))