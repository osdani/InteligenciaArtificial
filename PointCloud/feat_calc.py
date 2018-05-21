#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 22:38:39 2017

@author: haroldfmurcia
"""
import math, os, sys
import numpy as np
import pandas as pd
import re
import scipy as sc


eps = np.finfo(np.float32).eps

class get_Features(object):
    def __init__(self, vox_size):
        self.voxel_size = vox_size
        self.features   = []
        
    def get_echo_feat(self, df):
        N    = df.shape[0]
        echo = df.echo + 1
        NR   = df.NR
        ratio= np.array(echo) / np.array(NR) 
        r_1  = np.array( np.where(ratio==1) )
        r_2  = np.array( np.where(ratio==1.0/2.0) )
        r_3  = np.array( np.where(ratio==2.0/3.0) )
        r_4  = np.array( np.where(ratio==1.0/3.0) )
        r_p_1= r_1.size/(N*1.0)
        r_p_2= r_2.size/(N*1.0)
        r_p_3= r_3.size/(N*1.0)
        r_p_4= r_4.size/(N*1.0)
        n_single = 0
        n_first  = 0
        n_inter  = 0
        n_last   = 0
        echo = np.array(echo)
        NR = np.array(NR)
        for k in range(0,len(ratio)-1):
            if(echo[k]==1 and NR[k]==1):
                n_single = n_single+1
            elif(echo[k]==1 and NR[k]==2):
                n_first = n_first+1
            elif(echo[k]==1 and NR[k]==3):
                n_first = n_first+1
            elif(echo[k]==2 and NR[k]==2):
                n_last = n_last+1
            elif(echo[k]==2 and NR[k]==3):
                n_inter = n_inter+1
            elif(echo[k]==3 and NR[k]==3):
                n_last = n_last+1
        ERme = (n_first+n_inter)/(n_last+n_single+eps)
        ratio_proportion = [r_p_1, ERme]
        return np.array(ratio_proportion)

    def get_geom_feat(self, df):
        X = np.array(df.X)
        Y = np.array(df.Y)
        Z = np.array(df.Z)
        mean_x = np.mean(X)
        mean_y = np.mean(Y)
        mean_z = np.mean(Z)
        X = X.T #- mean_x
        Y = Y.T #- mean_y
        Z = Z.T #- mean_z
        cov_mat = np.cov([X,Y,Z])
        eig_val_cov, eig_vec_cov = np.linalg.eig(cov_mat)
        eig_val = np.sort(eig_val_cov)
        e1 = eig_val[2]
        e2 = eig_val[1]
        e3 = eig_val[0]
        # Anistropy, planarity, sphericity, Lniearity, curvature....
        # https://www.isprs-ann-photogramm-remote-sens-spatial-inf-sci.net/II-3/9/2014/isprsannals-II-3-9-2014.pdf
        if(e1>0 and e2>0 and e3>0):
            p0 = (e1-e2)/(e1 + eps)  # Linearity
            p1 = (e2-e3)/(e1 + eps)  # Planarity
            p2 =  e3/(e1 + eps)      # Sphericity
            p3 = pow(e1*e3*e3,1/3.0) # Omnivariance
            p4 = (e1-e3)/(e1 + eps)  # Anisotropy
            p5 = -( e3*np.log(e3) + e2*np.log(e2) + e1*np.log(e1) ) #Eigenentropy
            p6 = e1 +e3 + e3         # sumatory
            p7 = e3/(e1+e2+e3 + eps) #  change of curvature
        else:
            p0 = 0
            p1 = 0
            p2 = 0
            p3 = 0
            p4 = 0
            p5 = 0
            p6 = 0
            p7 = 0
            #print ("Algo pasa con los eing-values")
        # Calculate of angles
        mp = np.argmin(eig_val_cov)
        nx, ny, nz  = eig_vec_cov[:,mp] # https://mediatum.ub.tum.de/doc/800632/800632.pdf
        phi =abs(np.arctan(nz/ny))
        theta =abs(np.arctan((pow(nz,2)+pow(ny,2))/nx))
        return np.array([phi, p0, p1])

    def get_XYZ_feat(self, df,ground_classifier):
        xs = np.array(df.X)
        ys = np.array(df.Y)
        zs = np.array(df.Z)
        tmp_A = []
        tmp_b = []
        if len(xs)!= len(ys) or len(xs)!=len(zs):
            print "diferencia de longitudes"
        for i in range(len(xs)):
            tmp_A.append([xs[i], ys[i], 1])
            tmp_b.append(zs[i])
        b = np.matrix(tmp_b).T
        A = np.matrix(tmp_A)
        fit = (A.T * A).I * A.T * b
        errors = b - A * fit
        z_var  = np.var(errors)
        Ez = sc.stats.entropy(np.power(errors,2))
        tmp_A = []
        tmp_b = []
        for i in range(len(xs)):
            tmp_A.append([xs[i], 1, zs[i]])
            tmp_b.append(ys[i])
        b = np.matrix(tmp_b).T
        A = np.matrix(tmp_A)
        fit = (A.T * A).I * A.T * b
        errors = b - A * fit
        y_var  = np.var(errors)
        Ey = sc.stats.entropy(np.power(errors,2))
        tmp_A = []
        tmp_b = []
        for i in range(len(xs)):
            tmp_A.append([1, ys[i], zs[i]])
            tmp_b.append(xs[i])
        b = np.matrix(tmp_b).T
        A = np.matrix(tmp_A)
        fit = (A.T * A).I * A.T * b
        errors = b - A * fit
        x_var  = np.var(errors)
        Ex = sc.stats.entropy(np.power(errors,2))
        if ground_classifier==1:
            zu = max(zs)-min(zs)
        else:
            zu = np.mean(zs)
        Tvar = (x_var * y_var) / (z_var+eps)
        vz = np.var(zs)
        sz = sc.stats.skew(zs)
        kz = sc.stats.kurtosis(zs)
        vy = np.var(ys)
        sy = sc.stats.skew(ys)
        ky = sc.stats.kurtosis(ys)
        vx = np.var(xs)
        sx = sc.stats.skew(xs)
        kx = sc.stats.kurtosis(xs)
        xy_var = x_var +y_var
        xy_m_var = x_var*y_var
        xy_E = Ex + Ey
        return np.array([ z_var, Tvar])

    def norm_PW(self, df):
        # Normalization of pulse width
        h = 0.88
        div_y = 0.8*np.pi/180.0
        div_x = 0.08*np.pi/180.0
        tilt = np.array(df.tilt)
        z = abs(h - np.array(df.Z))
        r = np.array(df.r)
        alpha=[]
        for k in range(0,len(tilt)):
            if(tilt[k])>0:
                alpha.append(np.arcsin(z[k]/r[k]))
            elif(tilt[k])<0:
                alpha.append(np.arccos(z[k]/r[k]))
            else:
                alpha.append(0)
        alpha = np.array(alpha)
        dy = 0.5* z*abs( np.tan( alpha + div_y/2.0)  - np.tan( alpha - div_y/2.0) )
        dx = 0.5* z*abs( np.tan( alpha + div_x/2.0)  - np.tan( alpha - div_x/2.0) )
        bA = np.sqrt(dy*dx)*np.sin(alpha);
        pw_model = 0 + 1.7*bA
        pwn = np.array(df.wp) - pw_model
        for k in range(0,len(pwn)):
            if math.isnan(pwn[k]):
                print"pwn: " + str(pwn)
                print"alpha: " + str(alpha)
                print"dy: " + str(dy)
                print"dx: " + str(dx)
            elif pwn[k]<0:
                pwn[k] = 0
        return pwn

    def get_PW_feat(self, df, ground_classifier):
        xs  = np.array(df.X)
        ys  = np.array(df.Y)
        if ground_classifier == 3:
            zs  = norm_PW(df)
        else:
            zs  = np.array(df.wp)
        mPW = np.mean(zs)
        vPW = np.var(zs)
        sPW = sc.stats.skew(zs)
        kPW = sc.stats.kurtosis(zs)
        Epw = sc.stats.entropy(zs)
        tmp_A = []
        tmp_b = []
        for i in range(len(xs)):
            tmp_A.append([xs[i], ys[i], 1])
            tmp_b.append(zs[i])
        b = np.matrix(tmp_b).T
        A = np.matrix(tmp_A)
        if(np.linalg.det((A.T * A)) ==0):
            rows,cols =A.shape
            A = A + 0.0001*np.random.rand(rows,cols)
        fit = (A.T * A).I * A.T * b
        errors = b - A * fit
        z_var  = np.var(errors)
        Ez = sc.stats.entropy(np.power(errors,2))
        tmp_A = []
        tmp_b = []
        for i in range(len(xs)):
            tmp_A.append([xs[i], 1, zs[i]])
            tmp_b.append(ys[i])
        b = np.matrix(tmp_b).T
        A = np.matrix(tmp_A)
        if(np.linalg.det((A.T * A)) ==0):
            rows,cols =A.shape
            A = A + 0.0001*np.random.rand(rows,cols)
        fit = (A.T * A).I * A.T * b
        errors = b - A * fit
        y_var  = np.var(errors)
        Ey = sc.stats.entropy(np.power(errors,2))
        tmp_A = []
        tmp_b = []
        for i in range(len(xs)):
            tmp_A.append([1, ys[i], zs[i]])
            tmp_b.append(xs[i])
        b = np.matrix(tmp_b).T
        A = np.matrix(tmp_A)
        if(np.linalg.det((A.T * A)) ==0):
            rows,cols =A.shape
            A = A + 0.0001*np.random.rand(rows,cols)
        fit = (A.T * A).I * A.T * b
        errors = b - A * fit
        x_var  = np.var(errors)
        Ex = sc.stats.entropy(np.power(errors,2))
        #pw_feat = np.array([mPW, vPW, sPW, kPW, Epw, x_var, y_var, z_var, Ex, Ey, Ez])
        xy_var = x_var + y_var
        pw_feat = np.array([mPW, kPW, z_var])
        for k in range(0,len(pw_feat)):
            if math.isnan(pw_feat[k]):
                print "pw NAn" 
                pw_feat[k] = 0
            elif math.isinf(pw_feat[k]):
                print "pw inF" 
                print str(pw_feat)
                if pw_feat[k]>0:
                    pw_feat[k] = 1e3
                else:
                    pw_feat[k] = -1e3
        return pw_feat 