#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 21:03:14 2017

@author: haroldfmurcia
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math, os, sys
import numpy as np
import pandas as pd
import re
import scipy as sc

from sklearn import svm
from sklearn.externals import joblib

import feat_calc



voxel_size = 0.5
eps = np.finfo(np.float32).eps


def prediction_calc(workfile, vrmlFile):
    print "Workfile: " + str(workfile)
    Xvox=[]
    Yvox=[]
    Zvox=[]
    try:
        data = pd.read_csv( workfile, sep=' ', names = ["tilt", "pan", "beta", "layer","r","echo","wp","flag","point","scan","rovX","rovY","rovZ","rovQw","rovQx","rovQy","rovQz","NR","X","Y","Z"], header=2)
        X = data.X
        Y = data.Y
        Z = data.Z
    except:
        data = pd.read_csv( workfile, sep='\t', names = ["tilt", "pan", "beta", "layer","r","echo","wp","flag","point","scan","rovX","rovY","rovZ","rovQw","rovQx","rovQy","rovQz","NR","X","Y","Z"], header=2)
        X = data.X
        Y = data.Y
        Z = data.Z
        print "Warning in text format"
    translation = re.findall(r'Transform { translation (.*)', vrmlFile.read())
    L = len(translation)
    for k in range(0,L-1):
        a = translation[k]
        x,y,z,s = a.split(' ')
        Xvox.append(float(x))
        Yvox.append(float(y))
        Zvox.append(float(z))
    XYZ=np.array([X,Y,Z])
    XYZ=XYZ.T
    s = voxel_size
    L = len(Xvox)
    samples_p = 0
    samples_n = 0
    Y_svm = []
    rows  = data.shape[0]
    data['prediction'] = -np.ones([rows,1])
    for k in range (0,L-1 ):
        xmin=Xvox[k]-s/2.0
        xmax=Xvox[k]+s/2.0
        ymin=Yvox[k]-s/2.0
        ymax=Yvox[k]+s/2.0
        zmin=Zvox[k]-s/2.0
        zmax=Zvox[k]+s/2.0
        bound_x = np.logical_and(XYZ[:,0]>=xmin, XYZ[:,0]<=xmax)
        bound_y = np.logical_and(XYZ[:,1]>=ymin, XYZ[:,1]<=ymax)
        bound_z = np.logical_and(XYZ[:,2]>=zmin, XYZ[:,2]<=zmax)
        bb_filter = np.logical_and(bound_x, bound_y, bound_z)
        pos = np.array(np.where(bb_filter))
        if pos.size >=3:
            df = data.iloc[pos[0,:]]
            df = data.iloc[pos[0,:]]
            FA    = Feat.get_echo_feat(df)
            FB    = Feat.get_geom_feat(df)
            FC    = Feat.get_XYZ_feat(df,0)
            FD    = Feat.get_PW_feat(df, 0)
            samples_p = samples_p + 1  
            if np.sum(FB[-2:])>0:
                features = np.concatenate((FA, FB, FC, FD), axis=0)
                features = np.array(features)
                features = features.reshape(1,-1)
                pred_0   = clf_0.predict(features)
            else:
                pred_0   = -1
            # NODE 1
            if pred_0 == 0: #Ground
                FC    = Feat.get_XYZ_feat(df,1)
                features = np.concatenate((FA, FB, FC, FD), axis=0)
                features = np.array(features)
                features = features.reshape(1,-1)
                # NODE 2
                pred = clf_g.predict(features)
                pred = 0
            elif pred_0 == 1: # object
                # NODE 3
                pred_o = clf_o.predict(features)
                if pred_o == 1:
                    # NODE 4
                    pred = clf_b.predict(features)
                else:
                    pred = 4
                pred = 1
            elif pred_0 == 2:#Transparent object
                # NODE 5
                pred = clf_v.predict(features)
                pred = 2
            elif pred_0 == 3:#Noise
                pred = 7
                pred = 3
            else:
                pred = -1
                #print "No prediction"
            data.loc[pos[0,:],'prediction'] = pred*np.ones([pos.size,1])
        sys.stdout.write('\r')
        j= int(10*(k -0)/((L-1)-0))
        sys.stdout.write("[%-10s] %d%%" % ('='*j, 10*j))
        sys.stdout.flush()
    print "samples +: " + str(samples_p)
    return data

if __name__ == "__main__":
    basic_path       = os.getcwd()
    path_classifiers = basic_path+'/classifiers/joblib/'
    path_data_xyz    = basic_path+'/validation/octomap/xyz/'
    path_data_pred   = basic_path+'/validation/prediction/'
    path_data_tree   = basic_path+'/validation/octomap/bt_wrl/'
    #
    Feat    = feat_calc.get_Features(vox_size=0.5)
    #load classifiers
    print "Loading classifiers"
    clf_0 = joblib.load(path_classifiers+'clf_0.pkl') 
    clf_g = joblib.load(path_classifiers+'clf_g.pkl') 
    clf_o = joblib.load(path_classifiers+'clf_o.pkl') 
    clf_b = joblib.load(path_classifiers+'clf_b.pkl') 
    clf_v = joblib.load(path_classifiers+'clf_v.pkl') 
    #load data
    print "Loading Data"
    txt_data_403  = 'outside_403_xyz'
    txt_data_503n = 'outside_503n_xyz'
    txt_data_402d = 'outside_402d_xyz'
    txt_data_502n = 'outside_502n_xyz'
    workfile_403  = os.path.join(path_data_xyz, txt_data_403 + ".txt")
    workfile_503n = os.path.join(path_data_xyz, txt_data_503n + ".txt")
    workfile_402d = os.path.join(path_data_xyz, txt_data_402d + ".txt")
    workfile_502n = os.path.join(path_data_xyz, txt_data_502n + ".txt")
    workfile_403_tree = os.path.join(path_data_tree, txt_data_403 + ".bt.wrl")
    workfile_503n_tree = os.path.join(path_data_tree, txt_data_503n + ".bt.wrl")
    workfile_402d_tree = os.path.join(path_data_tree, txt_data_402d + ".bt.wrl")
    workfile_502n_tree = os.path.join(path_data_tree, txt_data_502n + ".bt.wrl")
    vrml_403      = open(workfile_403_tree, "r")
    vrml_503n     = open(workfile_503n_tree, "r")
    vrml_402d     = open(workfile_402d_tree, "r")
    vrml_502n     = open(workfile_502n_tree, "r")
    # FIle 01
    print "Calculating Prediction 1"
    data     = prediction_calc(workfile_502n, vrml_502n)
    hLine= "% Tilt [rads], Pan [rads], Beta [rads], Layer, Radial Distance [m], Echo, Pulse width [cm], Flag, Point Number, Scan Number, rovX[m], rovY[m], rovZ[m], rovQw, rovQx, rovQy, rovQz,  Return Number, X [m], Y[m], Z[m]" 
    numFormat = "%2.12f %2.12f %2.12f %d %3.12f %d %2.12f %d %d %d %3.12f %3.12f %3.12f %3.12f %3.12f %3.12f %3.12f %d %3.12f %3.12f %3.12f"
    hLine = hLine + " prediction "
    numFormat = numFormat + " %d "
    completeName = os.path.join(path_data_pred, txt_data_502n + "_pred.txt")
    np.savetxt(completeName, data.values, fmt= numFormat ,delimiter='\t',header = hLine,  comments="")
    fig = plt.figure()
    ax = Axes3D(fig)
    X=np.array(data.X)
    Y=np.array(data.Y)
    Z=np.array(data.Z)
    colorMap = np.round(np.array(data.prediction))
    scf = ax.scatter(X, Y, Z, marker=',', cmap='jet',c=colorMap, s= 0.05)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.savefig(txt_data_502n+"_PRED"+'.png') 
    plt.close()
#    plt.show()
    print("(y)")
    ## FIle 01
    print "Calculating Prediction 2"
    data     = prediction_calc(workfile_403, vrml_403)
    hLine= "% Tilt [rads], Pan [rads], Beta [rads], Layer, Radial Distance [m], Echo, Pulse width [cm], Flag, Point Number, Scan Number, rovX[m], rovY[m], rovZ[m], rovQw, rovQx, rovQy, rovQz,  Return Number, X [m], Y[m], Z[m]" 
    numFormat = "%2.12f %2.12f %2.12f %d %3.12f %d %2.12f %d %d %d %3.12f %3.12f %3.12f %3.12f %3.12f %3.12f %3.12f %d %3.12f %3.12f %3.12f"
    hLine = hLine + " prediction "
    numFormat = numFormat + " %d "
    completeName = os.path.join(path_data_pred, txt_data_403 + "_pred.txt")
    np.savetxt(completeName, data.values, fmt= numFormat ,delimiter='\t',header = hLine,  comments="")
#    fig = plt.figure()
#    ax = Axes3D(fig)
#    X=np.array(data.X)
#    Y=np.array(data.Y)
#    Z=np.array(data.Z)
#    colorMap = np.round(np.array(data.prediction))
#    scf = ax.scatter(X, Y, Z, marker=',', cmap='jet',c=colorMap, s= 0.05)
#    ax.set_xlabel('X')
#    ax.set_ylabel('Y')
#    ax.set_zlabel('Z')
#    plt.show()
    print("(y)")
    ### FIle 03
    print "Calculating Prediction 3"
    data     = prediction_calc(workfile_503n, vrml_503n)
    hLine= "% Tilt [rads], Pan [rads], Beta [rads], Layer, Radial Distance [m], Echo, Pulse width [cm], Flag, Point Number, Scan Number, rovX[m], rovY[m], rovZ[m], rovQw, rovQx, rovQy, rovQz,  Return Number, X [m], Y[m], Z[m]" 
    numFormat = "%2.12f %2.12f %2.12f %d %3.12f %d %2.12f %d %d %d %3.12f %3.12f %3.12f %3.12f %3.12f %3.12f %3.12f %d %3.12f %3.12f %3.12f"
    hLine = hLine + " prediction "
    numFormat = numFormat + " %d "
    completeName = os.path.join(path_data_pred, txt_data_503n + "_pred.txt")
    np.savetxt(completeName, data.values, fmt= numFormat ,delimiter='\t',header = hLine,  comments="")
#    fig = plt.figure()
#    ax = Axes3D(fig)
#    X=np.array(data.X)
#    Y=np.array(data.Y)
#    Z=np.array(data.Z)
#    colorMap = np.round(np.array(data.prediction))
#    scf = ax.scatter(X, Y, Z, marker=',', cmap='jet',c=colorMap, s= 0.05)
#    ax.set_xlabel('X')
#    ax.set_ylabel('Y')
#    ax.set_zlabel('Z')
#    plt.show()
    print("(y)")
    #### FIle 04
    print "Calculating Prediction 4"
    data     = prediction_calc(workfile_402d, vrml_402d)
    hLine= "% Tilt [rads], Pan [rads], Beta [rads], Layer, Radial Distance [m], Echo, Pulse width [cm], Flag, Point Number, Scan Number, rovX[m], rovY[m], rovZ[m], rovQw, rovQx, rovQy, rovQz,  Return Number, X [m], Y[m], Z[m]" 
    numFormat = "%2.12f %2.12f %2.12f %d %3.12f %d %2.12f %d %d %d %3.12f %3.12f %3.12f %3.12f %3.12f %3.12f %3.12f %d %3.12f %3.12f %3.12f"
    hLine = hLine + " prediction "
    numFormat = numFormat + " %d "
    completeName = os.path.join(path_data_pred, txt_data_402d + "_pred.txt")
    np.savetxt(completeName, data.values, fmt= numFormat ,delimiter='\t',header = hLine,  comments="")
#    fig = plt.figure()
#    ax = Axes3D(fig)
#    X=np.array(data.X)
#    Y=np.array(data.Y)
#    Z=np.array(data.Z)
#    colorMap = np.round(np.array(data.prediction))
#    scf = ax.scatter(X, Y, Z, marker=',', cmap='jet',c=colorMap, s= 0.05)
#    ax.set_xlabel('X')
#    ax.set_ylabel('Y')
#    ax.set_zlabel('Z')
#    plt.show()
    print("(y)")
    
    
    
    