#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May  2 18:50:35 2018

@author: haroldfmurcia
"""

# examen 2.1
# Coeficientes ideales: a = 7.5; b = 1.5; c = -100;

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = "/Users/haroldfmurcia/repositories/InteligenciaArtificial/examen II/"
filename = "data_set_2.txt"

def dataRead():
    data= pd.read_csv(path+filename,sep="\t", header=None)
    data.columns=["x","y"]
    x = np.array(data.x)
    y = np.array(data.y)
    plt.figure(1)
    plt.plot(x,y,'.')
    plt.xlabel('x')
    plt.ylabel('y')
    return x,y

def regresion(X,Y,eta):
    [f,c] = X.shape
    W = np.zeros([c,1])
    # Inicializacion de costo y precosto
    cost    = 1e3
    precost = 0
    dJ      = cost-precost
    # Cost vector
    J=[]
    while (abs(dJ))>10e-6:
        # Calculo de predicción
        pred = np.dot(X,W)
        # Calculo de error
        error= (Y - pred)
        # Calculo de gradiente
        gt   = -X.T.dot(error)
        delta= eta*gt
        W    = W - delta
        cost = np.sum(np.power(error,2))
        dJ   = cost-precost
        precost = cost
        J.append(cost)
    plt.figure(2)
    plt.plot(J,'o')
    plt.xlabel("Iteraciones")
    plt.ylabel("Costo")
    return W


if __name__ == "__main__":
    x,y = dataRead()
    # tamaño de x
    L = len(x)
    # inicializacion de matrices para y = ax^2 +bx +c
    X = np.ones([L,3])
    Y = np.zeros([L,1])
    X[:,1] = x
    X[:,2] = np.power(x,2)
    Y[:,0] = y
    W = regresion(X,Y,1e-6)
    pred = np.dot(X,W)
    # Superponer graficas
    plt.figure(3)
    plt.plot(x,y,'.')
    plt.plot(x,pred)
    plt.xlabel('x')
    plt.ylabel('y')
    print "Los coeficientes que mejor se adaptan a la curva y =ax^2+bx+c son: " + "a:" +str(W[2])+", b:"+str(W[1])+", c:"+str(W[0])
    
    
    
    
    