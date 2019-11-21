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
        try:
            j,px=0,0 
            while j < len(X):
                cx=1 
                i=0
                while i<len(X): 
                    if i!=j:
                        cx *= ((x-X[i])/(X[j]-X[i])) 
                    i += 1
                px+=(Y[j]*cx) 
                j += 1
            return px
        except e:
            raise ValueError("Error")
    return polinomio

if __name__ == '__main__':
    
   X,Y = [-4.5,-1.5,2,-3,-4], [5,-2,5,3,2]
   PL = polinomio_lagrange(X,Y)(-2)
   print("resultado: {}".format(PL)) 