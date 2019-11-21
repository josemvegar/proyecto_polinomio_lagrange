#!/usr/bin/env python3
"""
Proyecto Polinomio de Lagrange.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""


def polinomio_lagrange(X,Y):
    """
    Implementa y retorna el Polinomio de Lagrange para las listas X e Y.

    Parámetros:
    X: lista de valores de la variable independiente.
    Y: lista de valores de la variable dependiente.
    """
    if len(X) != len(Y): raise ValueError("Dimensiones diferentes en X e Y.")
   
    # Ordena el par (x, y) en forma ascendente por x.
    z = list(zip(X,Y))
    z.sort(key = lambda x: x[0])
    print (z)
    X, Y  = zip(*z)

    def p(x):
        r=[]  
        result=0
        n=len(X)
        for i in range(n):
            result1=1
            r2=1
            xk=X[i]
            for j in range(n):  
                if j!=i:
                    xi=X[j]
                    result1*=(x-xi)/float(xk-xi)
            r.append(result1)
        for k in range(n):
            result = result+(Y[k]*r[k])
        return result
    return p


if __name__ == '__main__':
    X=[-1.5,-0.5,1,-2,-4]
    Y=[9,-2,5,33,0]
    p=polinomio_lagrange(X,Y)
    R=p(-4)
    print (R)