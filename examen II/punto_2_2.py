#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May  2 19:17:32 2018

@author: haroldfmurcia
"""

from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from mpl_toolkits.mplot3d import Axes3D

def graphData(cancer):
    [f,c]=cancer.data.shape
    # Separar por clases
    Pos_class_0=[] # Posiciones que corresponden  a la clase 0
    Pos_class_1=[] # Posiciones que corresponden  a la clase 1
    for k in range(0,f-1):
        if(cancer.target[k]==0):
            Pos_class_0.append(k)
        else:
            Pos_class_1.append(k)
    Pos_class_0 = np.array(Pos_class_0)
    Pos_class_1 = np.array(Pos_class_1)
    for k in range(0,c-1):
        plt.figure()
        plt.plot(cancer.data[Pos_class_0,k],'.',label='Clase 0')
        plt.plot(cancer.data[Pos_class_1,k],'.',label='Clase 1')
        plt.legend(loc='upper left')
        titulo = 'Decriptor No' + str(k+1)
        plt.title(titulo)
    # Ejemplo, seleccionamos 14,21,24
    d1 = 14 -1
    d2 = 21 -1
    d3 = 24 -1
    m_0_14 = np.mean(cancer.data[Pos_class_0,d1])  #media clase 0, descriptor 14
    m_0_21 = np.mean(cancer.data[Pos_class_0,d2])  #media clase 0, descriptor 21
    m_0_24 = np.mean(cancer.data[Pos_class_0,d3])  #media clase 0, descriptor 24
    s_0_14 = np.std(cancer.data[Pos_class_0,d1])  #std clase 0, descriptor 14
    s_0_21 = np.std(cancer.data[Pos_class_0,d2])  #std clase 0, descriptor 21
    s_0_24 = np.std(cancer.data[Pos_class_0,d3])  #std clase 0, descriptor 24
    m_1_14 = np.mean(cancer.data[Pos_class_1,d1])  #media clase 1, descriptor 14
    m_1_21 = np.mean(cancer.data[Pos_class_1,d2])  #media clase 1, descriptor 21
    m_1_24 = np.mean(cancer.data[Pos_class_1,d3])  #media clase 1, descriptor 24
    s_1_14 = np.std(cancer.data[Pos_class_1,d1])  #std clase 1, descriptor 14
    s_1_21 = np.std(cancer.data[Pos_class_1,d2])  #std clase 1, descriptor 21
    s_1_24 = np.std(cancer.data[Pos_class_1,d3])  #std clase 1, descriptor 24
    ## Calculo curvas de distribucion 
    D14_c0 = norm(loc = m_0_14, scale=s_0_14)       #Descriptor 14, clase 0
    D14_c1 = norm(loc = m_1_14, scale=s_1_14)       #Descriptor 14, clase 1
    D21_c0 = norm(loc = m_0_21, scale=s_0_21)       #Descriptor 14, clase 0
    D21_c1 = norm(loc = m_1_21, scale=s_1_21)       #Descriptor 14, clase 1
    D24_c0 = norm(loc = m_0_24, scale=s_0_24)       #Descriptor 14, clase 0
    D24_c1 = norm(loc = m_1_24, scale=s_1_24)       #Descriptor 14, clase 1
    x1 = np.arange(0, 500, .1)
    #plot the pdfs of these normal distributions
    plt.figure()
    plt.clf() 
    plt.plot(x1, D14_c0.pdf(x1), x1 , D14_c1.pdf(x1) )
    plt.title("Descriptor 14")
    #plot the pdfs of these normal distributions
    x1 = np.arange(0, 100, .1)
    plt.figure()
    plt.clf() 
    plt.plot(x1, D21_c0.pdf(x1), x1 , D21_c1.pdf(x1) )
    plt.title("Descriptor 21")
    #plot the pdfs of these normal distributions
    x1 = np.arange(0, 3000, .5)
    plt.figure()
    plt.clf() 
    plt.plot(x1, D24_c0.pdf(x1), x1 , D24_c1.pdf(x1) )
    plt.title("Descriptor 24")
    # nube de puntos 3D
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(cancer.data[Pos_class_0,d1],cancer.data[Pos_class_0,d2], cancer.data[Pos_class_0,d3])
    ax.scatter(cancer.data[Pos_class_1,d1],cancer.data[Pos_class_1,d2], cancer.data[Pos_class_1,d3])
    plt.xlabel('Descriptor 14')
    plt.ylabel('Descriptor 21')
    #plt.zlabel('Descriptor 24')
    plt.legend(loc='upper left')
    plt.show()
    # ejemplo nube de puntos 2d:  d1 vs. d2
    fig = plt.figure()
    plt.plot(cancer.data[Pos_class_0,d1],cancer.data[Pos_class_0,d2],'.',label='Clase 0')
    plt.plot(cancer.data[Pos_class_1,d1],cancer.data[Pos_class_1,d2],'.',label='Clase 1')
    plt.xlabel('Descriptor 14')
    plt.ylabel('Descriptor 21')
    plt.legend(loc='upper left')
    plt.show()
    # ejemplo nube de puntos 2d:  d2 vs. d3
    fig = plt.figure()
    plt.plot(cancer.data[Pos_class_0,d2],cancer.data[Pos_class_0,d3],'.',label='Clase 0')
    plt.plot(cancer.data[Pos_class_1,d2],cancer.data[Pos_class_1,d3],'.',label='Clase 1')
    plt.legend(loc='upper left')
    plt.xlabel('Descriptor 21')
    plt.ylabel('Descriptor 24')
    plt.show()
    
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
    iteraciones = 0
    while (abs(dJ))>10e-6:
        iteraciones +=1
        # Calculo de predicción
        pred = np.dot(X,W)
        # Función de activación
        pred = sigmoid(pred)
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
        if iteraciones>1000e3:
            break
    plt.figure()
    plt.plot(J,'o')
    plt.xlabel("Iteraciones")
    plt.ylabel("Costo")
    return W

def validation(W,X,Y):
    pred = np.dot(X,W)
    pred = sigmoid(pred)
    for k in range(0,len(pred)-1):
        if pred[k]>0.5:
            pred[k]=1
        else:
            pred[k]=0
    error = Y - pred
    aciertos = 0.0
    for k in range(0,len(error)-1):
        if error[k]==0:
            aciertos +=1.0
    print "El porcentaje de efectividad etimado es de: " + str(aciertos/len(error)*100.0) + " %"

if __name__ == "__main__":
    cancer = datasets.load_breast_cancer()
    graphData(cancer)
    L = len(cancer.data)
    # inicializacion de matrices para y = ax^2 +bx +c
    X = np.ones([L,4])
    Y = np.zeros([L,1])
    X[:,1] = cancer.data[:,13]
    X[:,2] = cancer.data[:,20]
    X[:,3] = cancer.data[:,23]
    Y[:,0] = cancer.target
    W = SGD(X,Y,1e-9)
    validation(W,X,Y)
    
    
    