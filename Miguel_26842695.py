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
        #Funcion que calcula el polinomio de Lagrange
        try:
            """k: Variable que determina que L(x) se esta calculando, tambien se
            utiliza para iterar"""
            
            k=0 

            polinomio=0 #Variable donde se almacena el polinomio

            while k<len(X):#Ciclo iterativo para calcular el polinomio

                Lx=1 #Variable donde se almacena la L(x) que se este calculando

                """i: Variable iterable que se utiliza en el calculo de L(x) para 
                determinar Xi"""
                
                i=0 

                while i<len(X): #Ciclo iterativo para calcular la L(x)
                    
                    if i!=k:
                        Lx=Lx*((x-X[i])/(X[k]-X[i])) #Se calcula la L(x)

                    i=i+1
                
                polinomio=polinomio+(Y[k]*Lx) #Se calcula el polinomio
                k=k+1

            return polinomio
        except:
            print ("Error en la ejecucion")
            return 0
            
    return polinomio


if __name__ == '__main__':
    # Pruebe aquí su Polinomio de Lagrange ...

    X=[-1.5,-0.5,1,-2,-4]
    Y=[9,-2,5,33,0]


    pol=polinomio_lagrange(X,Y)

    print("Este es el resultado", pol(-4))