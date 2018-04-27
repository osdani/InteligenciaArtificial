#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 23:23:58 2018

PERCEPTRON FOR CLASSIFICATION

@author: haroldfmurcia
"""


import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np



def dataGEN():
    # import some data to play with
    iris = datasets.load_iris()
    X = iris.data[:, :4]  # we only take the first two features.
    Y = iris.target
    groups = ("Setosa","Versicolour","Virginica")
    plt.title("Descriptores y clases")
    plt.plot(X[0:49,2],X[0:49,3],'.')
    plt.plot(X[50:100,2],X[50:100,3],'.')
    plt.plot(X[101:150,2],X[101:150,3],'.')
    plt.xlabel("Descriptor 3")
    plt.xlabel("Descriptor 4")
    plt.legend(groups)
    # Evaluación del 70% de dos clases
    target = np.concatenate( [np.array(Y[0:35]),np.array(Y[50:85])] )
    x1 = np.concatenate([X[0:35,2], X[50:85,2]])
    x2 = np.concatenate([X[0:35,3], X[50:85,3]])
    return x1, x2, target.T

def sigmoid(pred):
    output = 1.0 / (1.0 + np.exp(-pred) )
    return output

def SGD(X,Y,eta):
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
        # Función de activación
        pred = sigmoid(pred)
        # Calculo de error
        error= (Y - pred.T).T
        # Calculo de gradiente
        gt   = -X.T.dot(error)
        delta= eta*gt
        W    = W - delta
        cost = np.sum(np.power(error,2))
        dJ   = cost-precost
        precost = cost
        J.append(cost)
    plt.figure()
    plt.plot(J,'o')
    plt.xlabel("Iteraciones")
    plt.ylabel("Costo")
    return W

def validacion(W):  
    # import some data to play with
    iris = datasets.load_iris()
    X = iris.data[:, :4]  # we only take the first two features.
    Y = iris.target
    groups = ("Setosa","Versicolour","Virginica")
    target = np.concatenate( [np.array(Y[35:50]),np.array(Y[85:100])] )
    x1 = np.concatenate([X[35:50,2], X[85:100,2]])
    x2 = np.concatenate([X[35:50,3], X[85:100,3]])
    X = np.ones([len(x1),3])
    X[:,1] = x1
    X[:,2] = x2
    pred   = sigmoid(np.dot(X,W))
    # cuantización
    for k in range(0,len(pred)-1):
        if(pred[k])>0.5:
            pred[k] = 1
        else:
            pred[k] = 0
    # Graficas
    plt.figure()
    plt.plot(target[0:15],'k.')
    plt.plot(target[16:30],'k.')
    plt.plot(pred[0:15],'r+')
    plt.plot(pred[16:30],'rx')
    plt.show()
    return pred

if __name__ == "__main__":
    x1,x2, Y = dataGEN()
    X = np.ones([len(x1),3])
    X[:,1] = x1
    X[:,2] = x2
    eta = 1e-3
    W = SGD(X,Y,eta)
    prediccion = validacion(W)
    