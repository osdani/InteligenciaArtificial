import cv2
import numpy as np
import dlib
import time
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
from imutils import face_utils
from utils import *
import pyscreeze
import pyautogui as pag
import pyautogui
import imutils
import speech_recognition as sr
import webbrowser as wb
import os

dirA = os.getcwd()
dir = dirA[:-3]
Fdir = dir + "data/"

C = 0
A = 0
B = 0
D = 0
E = 0
S = 0

ALL_MODE = False
ALL_COUNTER = 0
INPUT_MODE = False
SCROLL_MODE = False
MOUTH_COUNTER = 0
EYE_COUNTER = 0
SMILE_COUNTER = 0
NITRO_MODE = False
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(Fdir+"shape_predictor_68_face_landmarks.dat")
ANCHOR_POINT = (0, 0)
WHITE_COLOR = (255, 255, 255)
YELLOW_COLOR = (0, 255, 255)
RED_COLOR = (0, 0, 255)
GREEN_COLOR = (0, 255, 0)
BLUE_COLOR = (255, 0, 0)
BLACK_COLOR = (0, 0, 0)
(nStart, nEnd) = face_utils.FACIAL_LANDMARKS_IDXS["nose"]

vid = cv2.VideoCapture(0)

resolution_w = 1366
resolution_h = 768
cam_w = 640
cam_h = 480
unit_w = resolution_w / cam_w
unit_h = resolution_h / cam_h

data = pd.read_csv(Fdir+'file.txt', sep='\t', names = ["DESCRIPTOR1", "DESCRIPTOR2", "DESCRIPTOR3", "DESCRIPTOR4","DESCRIPTOR5","DESCRIPTOR6","TARGET"], header=None)
clf = RandomForestClassifier(max_depth=10, random_state=0)
X=data[["DESCRIPTOR1", "DESCRIPTOR2", "DESCRIPTOR3", "DESCRIPTOR4","DESCRIPTOR5","DESCRIPTOR6"]]
X=np.array(X)
Y=data[['TARGET']]
Y=np.array(Y)

X1=X[0:6000]
Y1=Y[0:6000]

clf.fit(X1, Y1)

while True:
    _, frame = vid.read()
    frame = cv2.flip(frame, 1)
    frame = imutils.resize(frame, width=cam_w, height=cam_h)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray, 0)
    if len(faces) > 0:
        rect = faces[0]
    else:
        #cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF
        continue
    shape = predictor(gray, rect)
    shape = face_utils.shape_to_np(shape)

    nose = shape[nStart:nEnd]
    nose_point = (nose[3, 0], nose[3, 1])

    drag = 3
    drag2 = 40

    for face in faces:

        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()

        landmarks = predictor(gray, face)

        pos1 = (landmarks.part(1).x,landmarks.part(1).y)
        pos2 = (landmarks.part(2).x,landmarks.part(2).y)
        pos3 = (landmarks.part(3).x,landmarks.part(3).y)
        pos4 = (landmarks.part(4).x,landmarks.part(4).y)
        pos5 = (landmarks.part(5).x,landmarks.part(5).y)
        pos6 = (landmarks.part(6).x,landmarks.part(6).y)
        pos7 = (landmarks.part(7).x,landmarks.part(7).y)
        pos8 = (landmarks.part(8).x,landmarks.part(8).y)
        pos9 = (landmarks.part(9).x,landmarks.part(9).y)
        pos10 = (landmarks.part(10).x,landmarks.part(10).y)
        pos11 = (landmarks.part(11).x,landmarks.part(11).y)
        pos12 = (landmarks.part(12).x,landmarks.part(12).y)
        pos13 = (landmarks.part(13).x,landmarks.part(13).y)
        pos14 = (landmarks.part(14).x,landmarks.part(14).y)
        pos15 = (landmarks.part(15).x,landmarks.part(15).y)
        pos16 = (landmarks.part(16).x,landmarks.part(16).y)
        pos17 = (landmarks.part(17).x,landmarks.part(17).y)
        pos18 = (landmarks.part(18).x,landmarks.part(18).y)
        pos19 = (landmarks.part(19).x,landmarks.part(19).y)
        pos20 = (landmarks.part(20).x,landmarks.part(20).y)
        pos21 = (landmarks.part(21).x,landmarks.part(21).y)
        pos22 = (landmarks.part(22).x,landmarks.part(22).y)
        pos23 = (landmarks.part(23).x,landmarks.part(23).y)
        pos24 = (landmarks.part(24).x,landmarks.part(24).y)
        pos25 = (landmarks.part(25).x,landmarks.part(25).y)
        pos26 = (landmarks.part(26).x,landmarks.part(26).y)
        pos27 = (landmarks.part(27).x,landmarks.part(27).y)
        pos28 = (landmarks.part(28).x,landmarks.part(28).y)
        pos29 = (landmarks.part(29).x,landmarks.part(29).y)
        pos30 = (landmarks.part(30).x,landmarks.part(30).y)
        pos31 = (landmarks.part(31).x,landmarks.part(31).y)
        pos32 = (landmarks.part(32).x,landmarks.part(32).y)
        pos33 = (landmarks.part(33).x,landmarks.part(33).y)
        pos34 = (landmarks.part(34).x,landmarks.part(34).y)
        pos35 = (landmarks.part(35).x,landmarks.part(35).y)
        pos36 = (landmarks.part(36).x,landmarks.part(36).y)
        pos37 = (landmarks.part(37).x,landmarks.part(37).y)
        pos38 = (landmarks.part(38).x,landmarks.part(38).y)
        pos39 = (landmarks.part(39).x,landmarks.part(39).y)
        pos40 = (landmarks.part(40).x,landmarks.part(40).y)
        pos41 = (landmarks.part(41).x,landmarks.part(41).y)
        pos42 = (landmarks.part(42).x,landmarks.part(42).y)
        pos43 = (landmarks.part(43).x,landmarks.part(43).y)
        pos44 = (landmarks.part(44).x,landmarks.part(44).y)
        pos45 = (landmarks.part(45).x,landmarks.part(45).y)
        pos46 = (landmarks.part(46).x,landmarks.part(46).y)
        pos47 = (landmarks.part(47).x,landmarks.part(47).y)
        pos48 = (landmarks.part(48).x,landmarks.part(48).y)
        pos49 = (landmarks.part(49).x,landmarks.part(49).y)
        pos50 = (landmarks.part(50).x,landmarks.part(50).y)
        pos51 = (landmarks.part(51).x,landmarks.part(51).y)
        pos52 = (landmarks.part(52).x,landmarks.part(52).y)
        pos53 = (landmarks.part(53).x,landmarks.part(53).y)
        pos54 = (landmarks.part(54).x,landmarks.part(54).y)
        pos55 = (landmarks.part(55).x,landmarks.part(55).y)
        pos56 = (landmarks.part(56).x,landmarks.part(56).y)
        pos57 = (landmarks.part(57).x,landmarks.part(57).y)
        pos58 = (landmarks.part(58).x,landmarks.part(58).y)
        pos59 = (landmarks.part(59).x,landmarks.part(59).y)
        pos60 = (landmarks.part(60).x,landmarks.part(60).y)
        pos61 = (landmarks.part(61).x,landmarks.part(61).y)
        pos62 = (landmarks.part(62).x,landmarks.part(62).y)
        pos63 = (landmarks.part(63).x,landmarks.part(63).y)
        pos64 = (landmarks.part(64).x,landmarks.part(64).y)
        pos65 = (landmarks.part(65).x,landmarks.part(65).y)
        pos66 = (landmarks.part(66).x,landmarks.part(66).y)
        pos67 = (landmarks.part(67).x,landmarks.part(67).y)

#===============================================================================
#                            SILBAR
#===============================================================================

        cv2.line(frame, pos60,pos64, (0,0,255),1)
        cv2.line(frame, pos64,pos55, (0,0,255),1)
        cv2.line(frame, pos55,pos59, (0,0,255),1)
        cv2.line(frame, pos59,pos60, (0,0,255),1)

        difS1 = np.sqrt((landmarks.part(60).x-landmarks.part(64).x)**2 + (landmarks.part(60).y-landmarks.part(64).y)**2)
        difS2 = np.sqrt((landmarks.part(51).x-landmarks.part(57).x)**2 + (landmarks.part(51).y-landmarks.part(57).y)**2)

        descriptor_SILBAR = difS1/difS2

#===============================================================================
#                            SUBIR CEJAS
#===============================================================================

        cv2.line(frame, pos36,pos39, (0,0,255),1)
        cv2.line(frame, pos39,pos19, (0,0,255),1)
        cv2.line(frame, pos19,pos39, (0,0,255),1)
        cv2.line(frame, pos19,pos36, (0,0,255),1)

        cv2.line(frame, pos42,pos45, (0,0,255),1)
        cv2.line(frame, pos45,pos24, (0,0,255),1)
        cv2.line(frame, pos24,pos42, (0,0,255),1)
        cv2.line(frame, pos24,pos45, (0,0,255),1)

        X1 = (landmarks.part(39).x + landmarks.part(36).x)/2
        X2 = (landmarks.part(39).y + landmarks.part(36).y)/2
        X3 = (landmarks.part(42).x + landmarks.part(45).x)/2
        X6 = (landmarks.part(42).y + landmarks.part(45).y)/2

        dif1 = np.sqrt((X1-landmarks.part(19).x)**2 + (X2-landmarks.part(19).y)**2)
        dif2 = np.sqrt((landmarks.part(36).x-landmarks.part(39).x)**2 + (landmarks.part(36).y-landmarks.part(39).y)**2)

        dif4 = np.sqrt((X3-landmarks.part(24).x)**2 + (X6-landmarks.part(24).y)**2)
        dif5 = np.sqrt((landmarks.part(45).x-landmarks.part(42).x)**2 + (landmarks.part(45).y-landmarks.part(42).y)**2)

        descriptor_ceja1 =  dif2/dif1
        descriptor_ceja2 =  dif5/dif4

        descriptor_full = (descriptor_ceja1+descriptor_ceja2)
#===============================================================================
#                            ABRIR BOCA
#===============================================================================
        cv2.line(frame, pos50,pos52, (0,0,255),1)
        cv2.line(frame, pos52,pos56, (0,0,255),1)
        cv2.line(frame, pos56,pos58, (0,0,255),1)
        cv2.line(frame, pos58,pos50, (0,0,255),1)

        difB1 = np.sqrt((landmarks.part(51).x-landmarks.part(57).x)**2 + (landmarks.part(51).y-landmarks.part(57).y)**2)
        difB2 = np.sqrt((landmarks.part(61).x-landmarks.part(63).x)**2 + (landmarks.part(61).y-landmarks.part(63).y)**2)

        descriptor_BOCA = difB1/difB2

#===============================================================================
#                            SONRISA
#===============================================================================

        cv2.line(frame, pos60,pos64, (0,0,255),1)
        cv2.line(frame, pos64,pos55, (0,0,255),1)
        cv2.line(frame, pos55,pos59, (0,0,255),1)
        cv2.line(frame, pos59,pos60, (0,0,255),1)

        difC1 = np.sqrt((landmarks.part(60).x-landmarks.part(64).x)**2 + (landmarks.part(60).y-landmarks.part(64).y)**2)
        difC2 = np.sqrt((landmarks.part(51).x-landmarks.part(57).x)**2 + (landmarks.part(51).y-landmarks.part(57).y)**2)

        descriptor_SONRISA = difC1/difC2
#===============================================================================
#                           Fruncir cejas
#===============================================================================
        cv2.line(frame, pos21,pos22, (0,0,255),1)
        cv2.line(frame, pos22,pos27, (0,0,255),1)
        cv2.line(frame, pos21,pos27, (0,0,255),1)
        cv2.line(frame, pos22,pos21, (0,0,255),1)

        x1 = (landmarks.part(21).x + landmarks.part(22).x)/2
        y1 = (landmarks.part(22).x + landmarks.part(27).x)/2
        z1 = (landmarks.part(21).x + landmarks.part(27).x)/2

        x2 = (landmarks.part(21).y + landmarks.part(22).y)/2
        y2 = (landmarks.part(22).y + landmarks.part(27).y)/2
        z2 = (landmarks.part(21).y + landmarks.part(27).y)/2

        dif11 = np.sqrt((x1-landmarks.part(27).x)**2 + (x2-landmarks.part(27).y)**2)
        dif22 = np.sqrt((landmarks.part(21).x-landmarks.part(22).x)**2 + (landmarks.part(21).y-landmarks.part(22).y)**2)

        descriptor_cejanariz =  (dif22/dif11)

#===============================================================================
#                            CERRAR LOS OJOS
#===============================================================================

        cv2.line(frame, pos36,pos37, (0,0,255),1)
        cv2.line(frame, pos37,pos38, (0,0,255),1)
        cv2.line(frame, pos38,pos39, (0,0,255),1)
        cv2.line(frame, pos39,pos40, (0,0,255),1)
        cv2.line(frame, pos40,pos41, (0,0,255),1)
        cv2.line(frame, pos41,pos36, (0,0,255),1)

        cv2.line(frame, pos42,pos43, (0,0,255),1)
        cv2.line(frame, pos43,pos44, (0,0,255),1)
        cv2.line(frame, pos44,pos45, (0,0,255),1)
        cv2.line(frame, pos45,pos46, (0,0,255),1)
        cv2.line(frame, pos46,pos47, (0,0,255),1)
        cv2.line(frame, pos47,pos42, (0,0,255),1)

        diE1 = np.sqrt((landmarks.part(37).x-landmarks.part(41).x)**2 + (landmarks.part(37).y-landmarks.part(41).y)**2)
        diE2 = np.sqrt((landmarks.part(38).x-landmarks.part(40).x)**2 + (landmarks.part(38).y-landmarks.part(40).y)**2)

        diE3 = np.sqrt((landmarks.part(36).x-landmarks.part(39).x)**2 + (landmarks.part(36).y-landmarks.part(39).y)**2)

        descriptor_ojos=  (diE1+diE2)/(diE3)

#===============================================================================
#                            FIN Calculo descriptores
#===============================================================================
        for n in range(0, 68):
               x = landmarks.part(n).x
               y = landmarks.part(n).y
               cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

        matri=[descriptor_SILBAR, descriptor_full, descriptor_BOCA, descriptor_SONRISA,descriptor_cejanariz,descriptor_ojos]
        pred=clf.predict([matri])
##---------------------Enable Nitro (Sonrisa)
        cv2.putText(frame, format(pred), (10,300), cv2.FONT_HERSHEY_SIMPLEX, 0.7, RED_COLOR, 2)

        if pred == 3:
            S += 1
            ALL_COUNTER += 1

            if S == 15 and pred == 3:
                ALL_MODE = not ALL_MODE
                ALL_COUNTER = 0
                #B = 0

        if pred != 3:
            S = 0

        if ALL_MODE:

            cv2.putText(frame, "SISTEMA ACTIVO", (400,90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, RED_COLOR, 2)

            if pred == 2: #indique el target del gesto: 1
                B += 1
                MOUTH_COUNTER += 1
                if B == 5 and pred == 2:
                    INPUT_MODE = not INPUT_MODE
                    # SCROLL_MODE = not SCROLL_MODE
                    MOUTH_COUNTER = 0
                    ANCHOR_POINT = nose_point
            if pred != 2:
                B =0
    ##---------------------Click Derecho (Fruncir cejas)-----------------------
            if pred == 4:
                C += 1
                #print C
                if C == 5 and pred == 4:
                    pag.click(button='right')
                    cv2.putText(frame, "Click Derecho", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, RED_COLOR, 2)
            if pred != 4:
                C =0
    ##----------------------------------Click Izquierdo (Levantar cejas)--------------------------------

            if pred == 1:
                A += 1

                if A == 5 and pred == 1:
                    pag.click(clicks=1, button='left')
                    cv2.putText(frame, "Click Izquierdo", (10, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, RED_COLOR, 2)
            if pred != 1:
                A =0

##-------------------------Enable Movimiento nariz (Abrir Boca)----------------------------

            if INPUT_MODE:
                cv2.putText(frame, "Lectura Del Movimiento Activada", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, RED_COLOR, 2)
                x, y = ANCHOR_POINT
                nx, ny = nose_point
                w, h = 30, 15
                m,n = 50,25
                v,b = 70,35
                u,i = 90,45
                multiple = 1

                cv2.rectangle(frame, (x - w, y - h), (x + w, y + h), GREEN_COLOR, 1)
                cv2.line(frame, ANCHOR_POINT, nose_point, BLUE_COLOR, 1)
                cv2.rectangle(frame, (x - m, y - n), (x + m, y + n), RED_COLOR, 1)


                dir = direction(nose_point, ANCHOR_POINT, w, h)
                dir2 = direction(nose_point, ANCHOR_POINT, m, n)
                #print dir

                if dir == 'right':
                    pag.moveRel(drag, 0)
                    cv2.putText(frame, "Derecha", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, RED_COLOR, 2)
                elif dir == 'left':
                    pag.moveRel(-drag, 0)
                    cv2.putText(frame, "Izquierda", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, RED_COLOR, 2)
                elif dir == 'up':
                    if SCROLL_MODE:
                        pag.scroll(1)
                        cv2.putText(frame, "Arriba", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, RED_COLOR, 2)
                    else:
                        pag.moveRel(0, -drag)
                        cv2.putText(frame, "Arriba", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, RED_COLOR, 2)
                elif dir == 'down':
                    if SCROLL_MODE:
                        pag.scroll(-1)
                        cv2.putText(frame, "Abajo", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, RED_COLOR, 2)
                    else:
                        pag.moveRel(0, drag)
                        cv2.putText(frame, "Abajo", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, RED_COLOR, 2)
                        ##-------------------------------------Drag2-----------------------------------------
                if dir2 == 'right':
                    pag.moveRel(drag2, 0)
                    cv2.putText(frame, "Derecha", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, RED_COLOR, 2)
                elif dir2 == 'left':
                    pag.moveRel(-drag2, 0)
                    cv2.putText(frame, "Izquierda", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, RED_COLOR, 2)
                elif dir2 == 'up':
                    if SCROLL_MODE:
                        pag.scroll(1)
                        cv2.putText(frame, "Arriba", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, RED_COLOR, 2)
                    else:
                        pag.moveRel(0, -drag2)
                        cv2.putText(frame, "Arriba", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, RED_COLOR, 2)
                elif dir2 == 'down':
                    if SCROLL_MODE:
                        pag.scroll(-1)
                        cv2.putText(frame, "Abajo", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, RED_COLOR, 2)
                    else:
                        pag.moveRel(0, drag2)
                        cv2.putText(frame, "Abajo", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, RED_COLOR, 2)

        ##--------------------Enable scroll (Cerrar OJos)----------------------------------------
            if pred == 0:
                D += 1
                EYE_COUNTER += 1
                if D == 10 and pred == 0:
                    SCROLL_MODE = not SCROLL_MODE
                    # INPUT_MODE = not INPUT_MODE
                    EYE_COUNTER = 0
            if pred != 0:
                D =0

            if SCROLL_MODE:
                cv2.putText(frame, 'Scroll Activado', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, RED_COLOR, 2)
    print pred
    cv2.imshow("Fram", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
