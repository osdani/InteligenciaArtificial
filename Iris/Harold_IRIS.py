#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 23:42:23 2018

@author: haroldfmurcia
"""

import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np
# import some data to play with
iris = datasets.load_iris()
X = iris.data[:, :4]  # we only take the first two features.
Y = iris.target
groups = ("Setosa","Versicolour","Virginica")

# Datos Sepal L
SL=X[:, 0]
#clase 0_ Setosa:
SL_0=SL[0:49]
#clase 1_ Versicolour:
SL_1=SL[50:99]    
#clase 2_ Virginica:
SL_2=SL[100:149]       
         
# Datos Sepal W
SW=X[:, 1]
#clase 0_ Setosa:
SW_0=SW[0:49]
#clase 1_ Versicolour:
SW_1=SW[50:99]    
#clase 2_ Virginica:
SW_2=SW[100:149]       
         
# Datos Petal L
PL=X[:, 2]
#clase 0_ Setosa:
PL_0=PL[0:49]
#clase 1_ Versicolour:
PL_1=PL[50:99]    
#clase 2_ Virginica:
PL_2=PL[100:149]       
         

# Datos Petal W
PW=X[:, 3]
#clase 0_ Setosa:
PW_0=PW[0:49]
#clase 1_ Versicolour:
PW_1=PW[50:99]    
#clase 2_ Virginica:
PW_2=PW[100:149]   



#************************************Gaussian distribution:*********************************************

from scipy.stats import norm

#Sepalo Length:
#Means:
SL_0mean=np.mean(SL_0);          SL_1mean=np.mean(SL_1);          SL_2mean=np.mean(SL_2)      
#Std:
SL_0std=np.std(SL_0);          SL_1std=np.std(SL_1);          SL_2std=np.std(SL_2)               

SL_d0 = norm(loc = SL_0mean, scale=SL_0std)
SL_d1 = norm(loc = SL_1mean, scale=SL_1std)
SL_d2 = norm(loc = SL_2mean, scale=SL_2std)
x1 = np.arange(0, 10, .1)

#plot the pdfs of these normal distributions
plt.figure(1, figsize=(8, 6))
plt.clf() 
plt.plot(x1, SL_d0.pdf(x1), x1 , SL_d1.pdf(x1), x1 , SL_d2.pdf(x1) )
plt.title("Sepalo Length")

#Sepalo Width:
#Means:
SW_0mean=np.mean(SW_0);          SW_1mean=np.mean(SW_1);          SW_2mean=np.mean(SW_2)      
#Std:
SW_0std=np.std(SW_0);          SW_1std=np.std(SW_1);          SW_2std=np.std(SW_2)               

SW_d0 = norm(loc = SW_0mean, scale=SW_0std)
SW_d1 = norm(loc = SW_1mean, scale=SW_1std)
SW_d2 = norm(loc = SW_2mean, scale=SW_2std)
x1 = np.arange(0, 10, .1)

#plot the pdfs of these normal distributions
plt.figure(2, figsize=(8, 6))
plt.clf() 
plt.plot(x1, SW_d0.pdf(x1), x1 , SW_d1.pdf(x1), x1 , SW_d2.pdf(x1) )
plt.title("Sepalo Width")

#Petal length:
#Means:
PL_0mean=np.mean(PL_0);        PL_1mean=np.mean(PL_1);        PL_2mean=np.mean(PL_2)      
#Std:
PL_0std=np.std(PL_0);          PL_1std=np.std(PL_1);          PL_2std=np.std(PL_2)               

PL_d0 = norm(loc = PL_0mean, scale=PL_0std)
PL_d1 = norm(loc = PL_1mean, scale=PL_1std)
PL_d2 = norm(loc = PL_2mean, scale=PL_2std)
x1 = np.arange(0, 10, .1)

#plot the pdfs of these normal distributions
plt.figure(3, figsize=(8, 6))
plt.clf() 
plt.plot(x1, PL_d0.pdf(x1), x1 , PL_d1.pdf(x1), x1, PL_d2.pdf(x1) )
plt.title("Petal length")

#Petal Width:
#Means:
PW_0mean=np.mean(PW_0);        PW_1mean=np.mean(PW_1);        PW_2mean=np.mean(PW_2)      
#Std:
PW_0std=np.std(PW_0);          PW_1std=np.std(PW_1);          PW_2std=np.std(PW_2)               

PW_d0 = norm(loc = PW_0mean, scale=PW_0std)
PW_d1 = norm(loc = PW_1mean, scale=PW_1std)
PW_d2 = norm(loc = PW_2mean, scale=PW_2std)
x1 = np.arange(-0.1, 10, .1)

#plot the pdfs of these normal distributions
plt.figure(4, figsize=(8, 6))
plt.clf() 
plt.plot(x1, PW_d0.pdf(x1), x1 , PW_d1.pdf(x1), x1, PW_d2.pdf(x1) )
plt.title("Petal Width")