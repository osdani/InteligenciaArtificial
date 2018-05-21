#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 22:38:39 2017

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
from sklearn.metrics import f1_score
from sklearn.externals import joblib

import feat_calc

voxel_size = 0.5
eps = np.finfo(np.float32).eps



#####################################################################################
#####################################################################################
def features_calc(workfile, vrmlFile, ground_classifier_flag):
    print "Workfile: " + str(workfile)
    X_svm = []
    Xvox=[]
    Yvox=[]
    Zvox=[]
    try:
        data = pd.read_csv( workfile, sep='  ', names = ["tilt", "pan", "beta", "layer","r","echo","wp","flag","point","scan","rovX","rovY","rovZ","rovQw","rovQx","rovQy","rovQz","NR","X","Y","Z"], header=2)
        #moving_mode = 1
        X = data.X
        Y = data.Y
        Z = data.Z
    except:
        data = pd.read_csv( workfile, sep='  ', names = ["tilt", "pan", "beta", "layer","r","echo","wp","flag","point","scan","NR","X","Y","Z"], header=2)
        X = data.X
        Y = data.Y
        Z = data.Z
        #moving_mode = 0
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
    samples = 0
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
            FA    = Feat.get_echo_feat(df)
            FB    = Feat.get_geom_feat(df)
            FC    = Feat.get_XYZ_feat(df,ground_classifier_flag)
            FD    = Feat.get_PW_feat(df, ground_classifier_flag)
            if np.sum(FB[-2:])>0:
                features = np.concatenate((FA, FB, FC, FD), axis=0)
                X_svm.append(features)
                samples = samples + 1  
    print "Evaluated Voxels: " + str(samples)
    return np.array(X_svm), samples

if __name__ == "__main__":
    # main folders
    basic_path       = os.getcwd()
    path_ground      = basic_path+'/dataBase/ground/'
    path_buidings    = basic_path+'/dataBase/buildings/'
    path_vegetation  = basic_path+'/dataBase/vegetation/'
    path_others      = basic_path+'/dataBase/others/'
    path_noise       = basic_path+'/dataBase/noise/'
    # GROUND
    txt_aphalt_02  = 'asphalt_10'
    txt_aphalt_03  = 'asphalt_03'
    txt_aphalt_04  = 'asphalt_08'
    txt_cement_01  = 'cement_01a'
    txt_cement_02  = 'cement_01b'
    txt_cement_03  = 'cement_03'
    txt_cement_04  = 'cement_06'
    txt_grass_01   = 'grass_04'
    txt_grass_02   = 'grass_06n'
    txt_grass_03   = 'grass_07'
    txt_gravs_01   = 'gravs_08a'
    txt_gravs_02   = 'gravs_08b'
    txt_border_01  = 'street_border_01a'
    txt_border_02  = 'street_border_01b'
    txt_border_03  = 'street_border_02'
    workfile_asphalt_02      = os.path.join(path_ground, txt_aphalt_02 + ".txt")
    workfile_asphalt_03      = os.path.join(path_ground, txt_aphalt_03 + ".txt")
    workfile_asphalt_04      = os.path.join(path_ground, txt_aphalt_04 + ".txt")
    workfile_cement_01       = os.path.join(path_ground, txt_cement_01 + ".txt")
    workfile_cement_02       = os.path.join(path_ground, txt_cement_02 + ".txt")
    workfile_cement_03       = os.path.join(path_ground, txt_cement_03 + ".txt")
    workfile_cement_04       = os.path.join(path_ground, txt_cement_04 + ".txt")
    workfile_grass_01        = os.path.join(path_ground, txt_grass_01 + ".txt")
    workfile_grass_02        = os.path.join(path_ground, txt_grass_02 + ".txt")
    workfile_grass_03        = os.path.join(path_ground, txt_grass_03 + ".txt")
    workfile_gravs_01        = os.path.join(path_ground, txt_gravs_01 + ".txt")
    workfile_gravs_02        = os.path.join(path_ground, txt_gravs_02 + ".txt")
    workfile_border_01       = os.path.join(path_ground, txt_border_01 + ".txt")
    workfile_border_02       = os.path.join(path_ground, txt_border_02 + ".txt")
    workfile_border_03       = os.path.join(path_ground, txt_border_03 + ".txt")
    workfile_asphalt_02_tree = os.path.join(path_ground + "octomap/bt_wrl/", txt_aphalt_02 + ".bt.wrl")
    workfile_asphalt_03_tree = os.path.join(path_ground + "octomap/bt_wrl/", txt_aphalt_03 + ".bt.wrl")
    workfile_asphalt_04_tree = os.path.join(path_ground + "octomap/bt_wrl/", txt_aphalt_04 + ".bt.wrl")
    workfile_cement_01_tree  = os.path.join(path_ground + "octomap/bt_wrl/", txt_cement_01 + ".bt.wrl")
    workfile_cement_02_tree  = os.path.join(path_ground + "octomap/bt_wrl/", txt_cement_02 + ".bt.wrl")
    workfile_cement_03_tree  = os.path.join(path_ground + "octomap/bt_wrl/", txt_cement_03 + ".bt.wrl")
    workfile_cement_04_tree  = os.path.join(path_ground + "octomap/bt_wrl/", txt_cement_04 + ".bt.wrl")
    workfile_grass_01_tree   = os.path.join(path_ground + "octomap/bt_wrl/", txt_grass_01 + ".bt.wrl")
    workfile_grass_02_tree   = os.path.join(path_ground + "octomap/bt_wrl/", txt_grass_02 + ".bt.wrl")
    workfile_grass_03_tree   = os.path.join(path_ground + "octomap/bt_wrl/", txt_grass_03 + ".bt.wrl")
    workfile_gravs_01_tree   = os.path.join(path_ground + "octomap/bt_wrl/", txt_gravs_01 + ".bt.wrl")
    workfile_gravs_02_tree   = os.path.join(path_ground + "octomap/bt_wrl/", txt_gravs_02 + ".bt.wrl")
    workfile_border_01_tree  = os.path.join(path_ground + "octomap/bt_wrl/", txt_border_01 + ".bt.wrl")
    workfile_border_02_tree  = os.path.join(path_ground + "octomap/bt_wrl/", txt_border_02 + ".bt.wrl")
    workfile_border_03_tree  = os.path.join(path_ground + "octomap/bt_wrl/", txt_border_03 + ".bt.wrl")
    vrml_asphalt_02 = open(workfile_asphalt_02_tree,"r")
    vrml_asphalt_03 = open(workfile_asphalt_03_tree,"r")
    vrml_asphalt_04 = open(workfile_asphalt_04_tree,"r")
    vrml_cement_01  = open(workfile_cement_01_tree, "r")
    vrml_cement_02  = open(workfile_cement_02_tree, "r")
    vrml_cement_03  = open(workfile_cement_03_tree, "r")
    vrml_cement_04  = open(workfile_cement_04_tree, "r")
    vrml_grass_01   = open(workfile_grass_01_tree,  "r")
    vrml_grass_02   = open(workfile_grass_02_tree,  "r")
    vrml_grass_03   = open(workfile_grass_03_tree,  "r")
    vrml_gravs_01   = open(workfile_gravs_01_tree,  "r")
    vrml_gravs_02   = open(workfile_gravs_02_tree,  "r")
    vrml_border_01  = open(workfile_border_01_tree, "r")
    vrml_border_02  = open(workfile_border_02_tree, "r")
    vrml_border_03  = open(workfile_border_03_tree, "r")
    # BUILDINGS
    txt_a_build_01           = 'a-build_01'
    txt_b_build_02           = 'b-build_02'
    txt_buildings_06         = 'buildings_06'
    txt_buildings_04         = 'building_04'
    txt_buildings_03         = 'buildings_03'
    txt_fence_04             = 'fence_06n'
    txt_fence_06             = 'fence_04'
    txt_metal_build_07       = 'metal_build_07'
    txt_metal_glass          = 'metal_glass_building_08'
    txt_a_build_columns_03   = 'build_columns_01'
    txt_steel_stairs_06      = 'steel_stairs_06'
    workfile_steel_stairs_06 = os.path.join(path_buidings, txt_steel_stairs_06 + ".txt")
    workfile_metal_build_07  = os.path.join(path_buidings, txt_metal_build_07 + ".txt")
    workfile_metal_glass     = os.path.join(path_buidings, txt_metal_glass + ".txt")
    workfile_a_build_columns_03= os.path.join(path_buidings, txt_a_build_columns_03 + ".txt")
    workfile_a_build_01        = os.path.join(path_buidings, txt_a_build_01 + ".txt")
    workfile_b_build_02        = os.path.join(path_buidings, txt_b_build_02 + ".txt")
    workfile_buildings_06      = os.path.join(path_buidings, txt_buildings_06 + ".txt")
    workfile_buildings_04      = os.path.join(path_buidings, txt_buildings_04 + ".txt")
    workfile_buildings_03      = os.path.join(path_buidings, txt_buildings_03 + ".txt")
    workfile_fence_04          = os.path.join(path_buidings, txt_fence_04 + ".txt")
    workfile_fence_04_tree     = os.path.join(path_buidings + "octomap/bt_wrl/", txt_fence_04 + ".bt.wrl")
    workfile_fence_06          = os.path.join(path_buidings, txt_fence_06 + ".txt")
    workfile_fence_06_tree     = os.path.join(path_buidings + "octomap/bt_wrl/", txt_fence_06 + ".bt.wrl")
    workfile_metal_build_07_tree   = os.path.join(path_buidings + "octomap/bt_wrl/", txt_metal_build_07 + ".bt.wrl")
    workfile_metal_glass_tree  = os.path.join(path_buidings + "octomap/bt_wrl/", txt_metal_glass + ".bt.wrl")
    workfile_a_build_01_tree   = os.path.join(path_buidings + "octomap/bt_wrl/", txt_a_build_01 + ".bt.wrl")
    workfile_buildings_06_tree = os.path.join(path_buidings + "octomap/bt_wrl/", txt_buildings_06  + ".bt.wrl")
    workfile_buildings_04_tree = os.path.join(path_buidings + "octomap/bt_wrl/", txt_buildings_04  + ".bt.wrl")
    workfile_buildings_03_tree = os.path.join(path_buidings + "octomap/bt_wrl/", txt_buildings_03  + ".bt.wrl")
    workfile_b_build_02_tree   = os.path.join(path_buidings + "octomap/bt_wrl/", txt_b_build_02 + ".bt.wrl")
    workfile_a_build_columns_03_tree = os.path.join(path_buidings + "octomap/bt_wrl/", txt_a_build_columns_03 + ".bt.wrl")
    workfile_steel_stairs_06_tree    = os.path.join(path_buidings + "octomap/bt_wrl/", txt_steel_stairs_06 + ".bt.wrl")
    vrml_a_build_01          = open(workfile_a_build_01_tree, "r")
    vrml_buildings_06        = open(workfile_buildings_06_tree, "r")
    vrml_buildings_04        = open(workfile_buildings_04_tree, "r")
    vrml_buildings_03        = open(workfile_buildings_03_tree, "r")
    vrml_b_build_02          = open(workfile_b_build_02_tree, "r")
    vrml_fence_04            = open(workfile_fence_04_tree, "r")
    vrml_fence_06            = open(workfile_fence_06_tree, "r")
    vrml_a_build_columns_03  = open(workfile_a_build_columns_03_tree, "r")
    vrml_metal_build_07      = open(workfile_metal_build_07_tree, "r")
    vrml_metal_glass         = open(workfile_metal_glass_tree, "r")
    vrml_steel_stairs_06     = open(workfile_steel_stairs_06_tree, "r")
    # Vegetation
    txt_vegetation_02        = 'vegetation_02'
    workfile_vegetation_02   = os.path.join(path_vegetation, txt_vegetation_02 + ".txt")
    workfile_vegetation_02_tree = os.path.join(path_vegetation + "octomap/bt_wrl/", txt_vegetation_02 + ".bt.wrl")
    vrml_vegetation_02       = open(workfile_vegetation_02_tree, "r")
    #
    txt_tree_foliage_06       = 'tree_foliage_06'
    workfile_tree_foliage_06  = os.path.join(path_vegetation, txt_tree_foliage_06 + ".txt")
    workfile_tree_foliage_06_tree = os.path.join(path_vegetation + "octomap/bt_wrl/", txt_tree_foliage_06 + ".bt.wrl")
    vrml_tree_foliage_06      = open(workfile_tree_foliage_06_tree, "r")
    # OTHERS
    txt_cars_10             = 'cars_10'
    workfile_cars_10        = os.path.join(path_others, txt_cars_10 + ".txt")
    workfile_cars_10_tree   = os.path.join(path_others + "octomap/bt_wrl/", txt_cars_10 + ".bt.wrl")
    vrml_cars_10            = open(workfile_cars_10_tree, "r")
    txt_steel_chair_06n     = 'steel_chair_06n'
    workfile_steel_chair_06n= os.path.join(path_others, txt_steel_chair_06n + ".txt")
    workfile_steel_chair_06n_tree= os.path.join(path_others + "octomap/bt_wrl/", txt_steel_chair_06n + ".bt.wrl")
    vrml_steel_chair_06n    = open(workfile_steel_chair_06n_tree, "r")
    # NOISE
    txt_noise_06n           = 'noise_06n'
    workfile_noise_06n      = os.path.join(path_noise, txt_noise_06n + ".txt")
    workfile_noise_06n_tree = os.path.join(path_noise + "octomap/bt_wrl/", txt_noise_06n + ".bt.wrl")
    vrml_noise_06n          = open(workfile_noise_06n_tree, "r")
    #################################################################################
    #################################################################################
    Targets = [  0,1,2,3,4,5,6,7,8,9,10   ];
    # FEATURES
    Feat    = feat_calc.get_Features(vox_size=0.5)
    # CALCULATING FEATURES
    X_gravs_021, samples        = features_calc(workfile_gravs_01, vrml_gravs_01 ,0)
    Y_gravs_021                 = Targets[0]*np.ones([samples,1])
    X_gravs_022, samples        = features_calc(workfile_gravs_02, vrml_gravs_02 ,0)
    Y_gravs_022                 = Targets[0]*np.ones([samples,1])
    X_grass_06n, samples        = features_calc(workfile_grass_02, vrml_grass_02 ,0)
    Y_grass_06n                 = Targets[0]*np.ones([samples,1])
    X_asphalt_02, samples       = features_calc(workfile_asphalt_02, vrml_asphalt_02 ,0)
    Y_asphalt_02                = Targets[0]*np.ones([samples,1])
    X_cement_03, samples        = features_calc(workfile_cement_03, vrml_cement_03 ,0)
    Y_cement_03                 = Targets[0]*np.ones([samples,1])
    X_border_03, samples        = features_calc(workfile_border_03, vrml_border_03 ,0)
    Y_border_03                 = Targets[0]*np.ones([samples,1])
    #
    X_building_a01, samples     = features_calc(workfile_a_build_01, vrml_a_build_01 ,0)
    Y_building_a01              = Targets[1]*np.ones([samples,1])
    X_buildings_06 , samples    = features_calc(workfile_buildings_06 , vrml_buildings_06  ,0)
    Y_buildings_06              = Targets[1]*np.ones([samples,1])
    X_buildings_04 , samples    = features_calc(workfile_buildings_04 , vrml_buildings_04  ,0)
    Y_buildings_04              = Targets[1]*np.ones([samples,1])
    X_buildings_03 , samples    = features_calc(workfile_buildings_03 , vrml_buildings_03  ,0)
    Y_buildings_03              = Targets[1]*np.ones([samples,1])
    X_building_b02, samples     = features_calc(workfile_b_build_02, vrml_b_build_02 ,0) 
    Y_building_b02              = Targets[1]*np.ones([samples,1])
    X_fence_04, samples         = features_calc(workfile_fence_04, vrml_fence_04 ,0)
    Y_fence_04                  = Targets[1]*np.ones([samples,1])
    X_fence_06, samples         = features_calc(workfile_fence_06, vrml_fence_06 ,0)
    Y_fence_06                  = Targets[1]*np.ones([samples,1])
    X_a_build_column_03, samples= features_calc(workfile_a_build_columns_03, vrml_a_build_columns_03 ,0)
    Y_a_build_column_03         = Targets[1]*np.ones([samples,1])
    X_metal_build_07, samples   = features_calc(workfile_metal_build_07, vrml_metal_build_07 ,0)
    Y_metal_build_07            = Targets[1]*np.ones([samples,1])
    X_metal_glass, samples      = features_calc(workfile_metal_glass, vrml_metal_glass ,0)
    Y_metal_glass               = Targets[1]*np.ones([samples,1])
    #
    X_cars_10 , samples         = features_calc(workfile_cars_10 , vrml_cars_10 ,0)
    Y_cars_10                   = Targets[1]*np.ones([samples,1])
    X_steel_chair_06n, samples  = features_calc(workfile_steel_chair_06n , vrml_steel_chair_06n ,0)
    Y_steel_chair_06n           = Targets[1]*np.ones([samples,1])
    #
    X_vegetation_02, samples    = features_calc(workfile_vegetation_02, vrml_vegetation_02 ,0)
    Y_vegetation_02             = Targets[2]*np.ones([samples,1])
    X_tree_foliage_06 , samples = features_calc(workfile_tree_foliage_06 , vrml_tree_foliage_06 ,0)
    Y_tree_foliage_06           = Targets[2]*np.ones([samples,1])
    #
    #X_noise_06n , samples       = features_calc(workfile_noise_06n , vrml_noise_06n ,0)
    #Y_noise_06n                 = Targets[3]*np.ones([samples,1])
    #
    #
    X = np.concatenate(( X_gravs_021, X_gravs_022, X_grass_06n, X_asphalt_02, X_cement_03, X_border_03, X_building_a01, X_buildings_06, X_buildings_04, X_buildings_03, X_metal_glass,  X_fence_04, X_fence_06, X_a_build_column_03, X_metal_build_07, X_vegetation_02, X_tree_foliage_06, X_cars_10, X_steel_chair_06n    ), axis=0)
    Y = np.concatenate(( Y_gravs_021, Y_gravs_022, Y_grass_06n, Y_asphalt_02, Y_cement_03, Y_border_03, Y_building_a01, Y_buildings_06, Y_buildings_04, Y_buildings_03, Y_metal_glass,  Y_fence_04, Y_fence_06, Y_a_build_column_03, Y_metal_build_07, Y_vegetation_02, Y_tree_foliage_06, Y_cars_10, Y_steel_chair_06n  ), axis=0)
    clf_0 = svm.SVC()
    clf_0.fit(X, Y)
    pred_0 = clf_0.predict(X)
    print "CLASIFIER 0: Main Node  ----------------------------------------" #NODE 1
    print "Ground, object, transparent object, noise"
    f1_0 = f1_score(Y, pred_0, average=None)
    np.set_printoptions(precision=4)
    print f1_0
    print "----------------------------------------------------------------"
    #[ERme,ERme2, ERme3, r_p_1, r_p_2, r_p_3, r_p_4] 0-4
    #[p0, p1, p2, p3, p4, p5, p6, p7, phi, theta ] 5-14
    #([ xy_var, xy_m_var, z_var, Tvar, zu, vz, kz, xy_E, Ez]) 15-23 
    #[mPW, vPW, kPW, Epw, xy_var, z_var] 24-31
    # ploting TESTING
#    F=0
#    plt.plot(X_asphalt_02[:,F],'.',label="asph",markersize=1)
#    plt.plot(X_building_a01[:,F],'.',label="build-a",markersize=1)
#    plt.plot(X_building_b02[:,F],'.',label="build-b",markersize=1)
#    plt.plot(X_fence_04[:,F],'.',label="fence",markersize=1)
#    plt.plot(X_vegetation_02[:,F],'.',label="veg",markersize=1)
#    plt.plot(X_tree_foliage_06[:,F],'.',label="tree",markersize=1)
#    plt.plot(X_cars_10[:,F],'.',label="cars",markersize=1)
#    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#    axes = plt.gca()
#    axes.set_ylim([0,3])
    #
    # CALCULATING FEATURES clasf 2
    vrml_gravs_01.close()
    vrml_gravs_02.close()
    vrml_asphalt_02.close()
    vrml_grass_02.close()
    vrml_cement_03.close()
    vrml_border_03.close()
    vrml_gravs_01   = open(workfile_gravs_01_tree, "r")
    vrml_gravs_02   = open(workfile_gravs_02_tree, "r")
    vrml_asphalt_02 = open(workfile_asphalt_02_tree, "r")
    vrml_grass_02   = open(workfile_grass_02_tree, "r")
    vrml_cement_03   = open(workfile_cement_03_tree, "r")
    vrml_border_03   = open(workfile_border_03_tree, "r")
    X_gravs_021, samples        = features_calc(workfile_gravs_01, vrml_gravs_01, 1)
    Y_gravs_021                 = Targets[1]*np.ones([samples,1])
    X_gravs_022, samples        = features_calc(workfile_gravs_02, vrml_gravs_02, 1)
    Y_gravs_022                 = Targets[1]*np.ones([samples,1])
    X_asphalt_02, samples        = features_calc(workfile_asphalt_02, vrml_asphalt_02, 1)
    Y_asphalt_02                 = Targets[0]*np.ones([samples,1])
    X_grass_06n, samples        = features_calc(workfile_grass_02, vrml_grass_02, 1)
    Y_grass_06n                 = Targets[1]*np.ones([samples,1])
    X_cement_03, samples        = features_calc(workfile_cement_03, vrml_cement_03 ,1)
    Y_cement_03                 = Targets[0]*np.ones([samples,1])
    X_border_03, samples        = features_calc(workfile_border_03, vrml_border_03 ,1)
    Y_border_03                 = Targets[1]*np.ones([samples,1])
    X = np.concatenate(( X_cement_03, X_asphalt_02, X_gravs_021, X_gravs_022,  X_grass_06n, X_border_03  ), axis=0)
    Y = np.concatenate(( Y_cement_03, Y_asphalt_02, Y_gravs_021, Y_gravs_022, Y_grass_06n, Y_border_03  ), axis=0)
    clf_g = svm.SVC()
    clf_g.fit(X, Y)
    pred_g = clf_g.predict(X)
    print "Ground CLASIFIER------------------------------------------------"  #NODE 2
    print "(cement, asphalt), (gravs, grass, border)"
    f1_g = f1_score(Y, pred_g, average=None)
    np.set_printoptions(precision=3)
    print f1_g
    print "----------------------------------------------------------------"
    #
    # CALCULATING FEATURES clasf 3
    vrml_a_build_01.close()
    vrml_b_build_02.close()
    vrml_a_build_columns_03.close()
    vrml_metal_build_07.close()
    vrml_fence_04.close()
    vrml_fence_06.close()
    vrml_steel_stairs_06.close()
    vrml_metal_glass.close()
    vrml_metal_glass            = open(workfile_metal_glass_tree, "r")
    vrml_a_build_01             = open(workfile_a_build_01_tree, "r")
    vrml_b_build_02             = open(workfile_b_build_02_tree, "r")
    vrml_a_build_columns_03     = open(workfile_a_build_columns_03_tree, "r")
    vrml_metal_build_07         = open(workfile_metal_build_07_tree, "r")
    vrml_fence_04               = open(workfile_fence_04_tree, "r")
    vrml_fence_06               = open(workfile_fence_06_tree, "r")
    vrml_steel_stairs_06        = open(workfile_steel_stairs_06_tree, "r")
    vrml_steel_chair_06n.close()
    vrml_cars_10.close()
    vrml_steel_chair_06n        = open(workfile_steel_chair_06n_tree, "r")
    vrml_cars_10                = open(workfile_cars_10_tree, "r")
    X_building_a01, samples     = features_calc(workfile_a_build_01, vrml_a_build_01 ,0)
    Y_building_a01              = Targets[1]*np.ones([samples,1])
    X_building_b02, samples     = features_calc(workfile_b_build_02, vrml_b_build_02 ,0) 
    Y_building_b02              = Targets[1]*np.ones([samples,1])
    X_a_build_column_03, samples= features_calc(workfile_a_build_columns_03, vrml_a_build_columns_03 ,0)
    Y_a_build_column_03         = Targets[1]*np.ones([samples,1])
    X_metal_build_07, samples   = features_calc(workfile_metal_build_07, vrml_metal_build_07 ,0)
    Y_metal_build_07            = Targets[1]*np.ones([samples,1])
    X_fence_04, samples         = features_calc(workfile_fence_04, vrml_fence_04 ,0)
    Y_fence_04                  = Targets[1]*np.ones([samples,1])
    X_fence_06, samples         = features_calc(workfile_fence_06, vrml_fence_06 ,0)
    Y_fence_06                  = Targets[1]*np.ones([samples,1])
    X_metal_glass, samples      = features_calc(workfile_metal_glass, vrml_metal_glass ,0)
    Y_metal_glass               = Targets[1]*np.ones([samples,1])
    X_cars_10 , samples         = features_calc(workfile_cars_10 , vrml_cars_10 ,0)
    Y_cars_10                   = Targets[0]*np.ones([samples,1])
    X_steel_chair_06n, samples  = features_calc(workfile_steel_chair_06n , vrml_steel_chair_06n ,0)
    Y_steel_chair_06n           = Targets[0]*np.ones([samples,1])
    X = np.concatenate(( X_building_a01, X_building_b02, X_a_build_column_03, X_metal_build_07, X_fence_04, X_fence_06, X_metal_glass, X_cars_10, X_steel_chair_06n  ), axis=0)
    Y = np.concatenate(( Y_building_a01, Y_building_b02, Y_a_build_column_03, Y_metal_build_07, Y_fence_04, Y_fence_06, Y_metal_glass, Y_cars_10, Y_steel_chair_06n  ), axis=0)
    clf_o = svm.SVC()
    clf_o.fit(X, Y)
    pred_o = clf_o.predict(X)
    print "Object CLASIFIER 3----------------------------------------------" #NODE 3
    print "Building, obstacle"
    f1_o = f1_score(Y, pred_o, average=None)
    np.set_printoptions(precision=3)
    print f1_o
    print "----------------------------------------------------------------"
    #
    #
    # CALCULATING FEATURES clasf 4
    vrml_a_build_01.close()
    vrml_b_build_02.close()
    vrml_a_build_columns_03.close()
    vrml_metal_build_07.close()
    vrml_fence_04.close()
    vrml_fence_06.close()
    vrml_steel_stairs_06.close()
    vrml_metal_glass.close()
    vrml_metal_glass            = open(workfile_metal_glass_tree, "r")
    vrml_a_build_01             = open(workfile_a_build_01_tree, "r")
    vrml_b_build_02             = open(workfile_b_build_02_tree, "r")
    vrml_a_build_columns_03     = open(workfile_a_build_columns_03_tree, "r")
    vrml_metal_build_07         = open(workfile_metal_build_07_tree, "r")
    vrml_fence_04               = open(workfile_fence_04_tree, "r")
    vrml_fence_06               = open(workfile_fence_06_tree, "r")
    vrml_steel_stairs_06        = open(workfile_steel_stairs_06_tree, "r")
    X_building_a01, samples     = features_calc(workfile_a_build_01, vrml_a_build_01 ,0)
    Y_building_a01              = Targets[2]*np.ones([samples,1])
    X_building_b02, samples     = features_calc(workfile_b_build_02, vrml_b_build_02 ,0) 
    Y_building_b02              = Targets[2]*np.ones([samples,1])
    X_a_build_column_03, samples= features_calc(workfile_a_build_columns_03, vrml_a_build_columns_03 ,0)
    Y_a_build_column_03         = Targets[2]*np.ones([samples,1])
    X_metal_build_07, samples   = features_calc(workfile_metal_build_07, vrml_metal_build_07 ,0)
    Y_metal_build_07            = Targets[2]*np.ones([samples,1])
    X_fence_04, samples         = features_calc(workfile_fence_04, vrml_fence_04 ,0)
    Y_fence_04                  = Targets[3]*np.ones([samples,1])
    X_fence_06, samples         = features_calc(workfile_fence_06, vrml_fence_06 ,0)
    Y_fence_06                  = Targets[3]*np.ones([samples,1])
    X_metal_glass, samples      = features_calc(workfile_metal_glass, vrml_metal_glass ,0)
    Y_metal_glass               = Targets[2]*np.ones([samples,1])
    #X_steel_stairs_06, samples  = features_calc(workfile_steel_stairs_06 , vrml_steel_stairs_06  ,0)
    #Y_steel_stairs_06           = Targets[8]*np.ones([samples,1])
    X = np.concatenate(( X_building_a01, X_building_b02, X_a_build_column_03, X_metal_build_07, X_metal_glass, X_fence_04, X_fence_06  ), axis=0)
    Y = np.concatenate(( Y_building_a01, Y_building_b02, Y_a_build_column_03, Y_metal_build_07, Y_metal_glass, Y_fence_04, Y_fence_06  ), axis=0)
    clf_b = svm.SVC()
    clf_b.fit(X, Y)
    pred_b = clf_b.predict(X)
    print "Building CLASIFIER 4------------------------------------------"  #NODE 4
    print "Wall, column, metal-building, metal-stairs, fence"
    f1_b = f1_score(Y, pred_b, average=None)
    np.set_printoptions(precision=3)
    print f1_b
    #
    #
    # CALCULATING FEATURES clasf 5
    vrml_vegetation_02.close()
    vrml_tree_foliage_06.close()
    vrml_vegetation_02       = open(workfile_vegetation_02_tree, "r")
    vrml_tree_foliage_06      = open(workfile_tree_foliage_06_tree, "r")
    X_vegetation_02, samples    = features_calc(workfile_vegetation_02, vrml_vegetation_02, 0)
    Y_vegetation_02             = Targets[5]*np.ones([samples,1])
    X_tree_foliage_06 , samples = features_calc(workfile_tree_foliage_06 , vrml_tree_foliage_06,0)
    Y_tree_foliage_06           = Targets[6]*np.ones([samples,1])
    X = np.concatenate(( X_vegetation_02, X_tree_foliage_06  ), axis=0)
    Y = np.concatenate(( Y_vegetation_02, Y_tree_foliage_06  ), axis=0)
    clf_v = svm.SVC()
    clf_v.fit(X, Y)
    pred_v = clf_v.predict(X)
    print "Vegetation CLASIFIER 5------------------------------------------"  #NODE 5
    print "vegetation, tree-foliage"
    f1_v = f1_score(Y, pred_v, average=None)
    np.set_printoptions(precision=3)
    print f1_v
    print "----------------------------------------------------------------"
    print "----------------------------------------------------------------"
    print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - "
    path = '/Users/haroldfmurcia/Desktop/classification/classifiers/joblib/'
    print "SAVING CLASSIFIERS IN FOLDER: " + path
    fileName = 'clf_0'
    completeName = os.path.join(path, fileName + '.pkl')
    joblib.dump(clf_0, completeName) 
    fileName = 'clf_g'
    completeName = os.path.join(path, fileName + '.pkl')
    joblib.dump(clf_g, completeName)
    fileName = 'clf_o'
    completeName = os.path.join(path, fileName + '.pkl')
    joblib.dump(clf_o, completeName)
    fileName = 'clf_b'
    completeName = os.path.join(path, fileName + '.pkl')
    joblib.dump(clf_b, completeName)
    fileName = 'clf_v'
    completeName = os.path.join(path, fileName + '.pkl')
    joblib.dump(clf_v, completeName)
    print "- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - END"
