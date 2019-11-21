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
        poli=0
        lal=0
        for i in range(len(X)):
            lalaux=1
            for a in range(len(X)):
                if (a!=i):
                    lal=(x-X[a])/(X[i]-X[a])
                    lalaux=lalaux*lal
            poliaux=Y[i]*lalaux
            poli=poli+poliaux
        return poli

    return polinomio


if __name__ == '__main__':
    x=[2,1,-1]
    y=[3,-2,1]
    polres=polinomio_lagrange(x,y)
    for i in range(len(x)):
        print ("el valor para= ", x[i]," es igual a= ", polres(x[i]))
    bye=input()
    pass