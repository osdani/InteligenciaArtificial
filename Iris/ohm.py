#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 20:42:06 2018

@author: haroldfmurcia
"""

import numpy as np
import matplotlib.pyplot as plt

def SGD(y,x,eta,Epoch):
    N = len(y)
    y = np.array([y]).T # Target
    inputs = 2
    X = np.zeros([N,inputs])
    x0 = np.ones(N) # input 0
    x1 = np.array(x) # input 1...
    X[:,0]=x0
    X[:,1]=x1
    W = np.zeros([inputs,1])
    J = [0] * Epoch
    for iteration in range(0,Epoch):
        prediction = X.dot(W)
        errors = y - prediction
        gradient = -X.T.dot(errors)
        W = W - eta*gradient
        J[iteration]=np.sum(0.5*pow(errors[0],2))
    print "W: " + str(W) 
    plt.plot(J)  
    plt.show() 
    return W


if __name__ == "__main__":
    # Gradiente DEscendente
    # Ejemplo Ley de Ohm.
    
    # Generar base de datos a partir de ley de ohm para luego devolverse y validar la estimación
    # de la resistencia Ω.
    
    N  = 100
    Ruido = 0.0025*np.random.randn(N)
    Vi = np.linspace(0.0, 12.0, num=N)
    R  = 333
    I  = Vi/R + Ruido
    
    
    plt.plot(I,Vi,'o')
    plt.title("I vs. V")
    plt.show()
    
    
    ## Estimación de parámetro R a partir de datos de voltaje y corriente
    # Vector de parámetros W, inicializado en cero o un valor al azar
    W = SGD(Vi,I,10e-3,90000)
    plt.title("Real data and Estimation")
    plt.plot(I,W[1]*I+W[0],I,Vi,'o')