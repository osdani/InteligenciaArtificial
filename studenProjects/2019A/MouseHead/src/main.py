import cv2
import numpy as np
import dlib
import time
import os

dirA = os.getcwd()
dir = dirA[:-3]
Fdir = dir + "data/"


cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(Fdir+"shape_predictor_68_face_landmarks.dat")
contador=0
print('ingrese target')
target=input("indique el target del gesto: ")

while contador<500:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

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
        #
        v_desc = "silvar = {}".format(descriptor_SILBAR)
        cv2.putText(frame, v_desc, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

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

        v_desc1 = "cejas = {}".format(descriptor_full)
        cv2.putText(frame, v_desc1, (10,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)
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

        v_desc2 = "boca = {}".format(descriptor_BOCA)
        cv2.putText(frame, v_desc2, (10,60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

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
        #
        v_desc3 = "sonrisa = {}".format(descriptor_SONRISA)
        cv2.putText(frame, v_desc3, (10,80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)
        cv2.waitKey
#===============================================================================
#                            CEJAS-NARIZ
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
        v_desc1 = "cejas-nariz = {}".format(descriptor_cejanariz)
        cv2.putText(frame, v_desc1, (10,100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

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

        v_desc1 = "ojos = {}".format(descriptor_ojos)
        cv2.putText(frame, v_desc1, (10,120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

#===============================================================================
#                            FIN
#===============================================================================

        gestos = np.array([descriptor_SILBAR, descriptor_full, descriptor_BOCA, descriptor_SONRISA,descriptor_cejanariz,descriptor_ojos])

        for n in range(0, 68):
               x = landmarks.part(n).x
               y = landmarks.part(n).y
               cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

        for i in range(0,2):
            cv2.imshow("Foto", frame)
            cv2.waitKey(1)
            f = open(Fdir + 'file.txt','a')
            f.write(format(gestos[0])+'\t'+format(gestos[1])+'\t'+format(gestos[2])+'\t'+format(gestos[3])+'\t'+format(gestos[4])+'\t'+format(gestos[5])+'\t'+format(target)+'\n')
            f.close()

        contador += 1

    cv2.imshow("Fram", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()

print('ingrese target')
target=input("indique el target del gesto: ")
contador=0

#====================================================================================================================================================================
#                            DESCRIPTOR 0
#====================================================================================================================================================================

while contador<500:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

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
        #
        v_desc = "silvar = {}".format(descriptor_SILBAR)
        cv2.putText(frame, v_desc, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

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

        v_desc1 = "cejas = {}".format(descriptor_full)
        cv2.putText(frame, v_desc1, (10,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)
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

        v_desc2 = "boca = {}".format(descriptor_BOCA)
        cv2.putText(frame, v_desc2, (10,60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

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
        #
        v_desc3 = "sonrisa = {}".format(descriptor_SONRISA)
        cv2.putText(frame, v_desc3, (10,80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)
        cv2.waitKey
#===============================================================================
#                            CEJAS-NARIZ
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
        v_desc1 = "cejas-nariz = {}".format(descriptor_cejanariz)
        cv2.putText(frame, v_desc1, (10,100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

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

        v_desc1 = "ojos = {}".format(descriptor_ojos)
        cv2.putText(frame, v_desc1, (10,120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

#===============================================================================
#                            FIN
#===============================================================================

        gestos = np.array([descriptor_SILBAR, descriptor_full, descriptor_BOCA, descriptor_SONRISA,descriptor_cejanariz,descriptor_ojos])

        for n in range(0, 68):
               x = landmarks.part(n).x
               y = landmarks.part(n).y
               cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

        for i in range(0,2):
            cv2.imshow("Foto", frame)
            cv2.waitKey(1)
            f = open(Fdir + 'file.txt','a')

            f.write(format(gestos[0])+'\t'+format(gestos[1])+'\t'+format(gestos[2])+'\t'+format(gestos[3])+'\t'+format(gestos[4])+'\t'+format(gestos[5])+'\t'+format(target)+'\n')
            f.close()

        contador += 1

    cv2.imshow("Fram", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()
target=input("indique el target del gesto: ")
contador=0

#====================================================================================================================================================================
#                            DESCRIPTOR 1
#====================================================================================================================================================================

while contador<500:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

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

        v_desc = "silvar = {}".format(descriptor_SILBAR)
        cv2.putText(frame, v_desc, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

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

        v_desc1 = "cejas = {}".format(descriptor_full)
        cv2.putText(frame, v_desc1, (10,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)
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

        v_desc2 = "boca = {}".format(descriptor_BOCA)
        cv2.putText(frame, v_desc2, (10,60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

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
        #
        v_desc3 = "sonrisa = {}".format(descriptor_SONRISA)
        cv2.putText(frame, v_desc3, (10,80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)
        cv2.waitKey
#===============================================================================
#                            CEJAS-NARIZ
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
        v_desc1 = "cejas-nariz = {}".format(descriptor_cejanariz)
        cv2.putText(frame, v_desc1, (10,100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

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

        v_desc1 = "ojos = {}".format(descriptor_ojos)
        cv2.putText(frame, v_desc1, (10,120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

#===============================================================================
#                            FIN
#===============================================================================

        gestos = np.array([descriptor_SILBAR, descriptor_full, descriptor_BOCA, descriptor_SONRISA,descriptor_cejanariz,descriptor_ojos])

        for n in range(0, 68):
               x = landmarks.part(n).x
               y = landmarks.part(n).y
               cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

        for i in range(0,2):
            cv2.imshow("Foto", frame)
            cv2.waitKey(1)
            f = open(Fdir + 'file.txt','a')
            f.write(format(gestos[0])+'\t'+format(gestos[1])+'\t'+format(gestos[2])+'\t'+format(gestos[3])+'\t'+format(gestos[4])+'\t'+format(gestos[5])+'\t'+format(target)+'\n')
            f.close()

        contador += 1

    cv2.imshow("Fram", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()
target=input("indique el target del gesto: ")
contador=0


#====================================================================================================================================================================
#                            DESCRIPTOR 2
#====================================================================================================================================================================

while contador<500:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

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

        v_desc = "silvar = {}".format(descriptor_SILBAR)
        cv2.putText(frame, v_desc, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

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

        v_desc1 = "cejas = {}".format(descriptor_full)
        cv2.putText(frame, v_desc1, (10,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)
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

        v_desc2 = "boca = {}".format(descriptor_BOCA)
        cv2.putText(frame, v_desc2, (10,60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

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
        #
        v_desc3 = "sonrisa = {}".format(descriptor_SONRISA)
        cv2.putText(frame, v_desc3, (10,80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)
        cv2.waitKey
#===============================================================================
#                            CEJAS-NARIZ
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
        v_desc1 = "cejas-nariz = {}".format(descriptor_cejanariz)
        cv2.putText(frame, v_desc1, (10,100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

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

        v_desc1 = "ojos = {}".format(descriptor_ojos)
        cv2.putText(frame, v_desc1, (10,120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

#===============================================================================
#                            FIN
#===============================================================================

        gestos = np.array([descriptor_SILBAR, descriptor_full, descriptor_BOCA, descriptor_SONRISA,descriptor_cejanariz,descriptor_ojos])

        for n in range(0, 68):
               x = landmarks.part(n).x
               y = landmarks.part(n).y
               cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

        for i in range(0,2):
            cv2.imshow("Foto", frame)
            cv2.waitKey(1)
            f = open(Fdir + 'file.txt','a')
            f.write(format(gestos[0])+'\t'+format(gestos[1])+'\t'+format(gestos[2])+'\t'+format(gestos[3])+'\t'+format(gestos[4])+'\t'+format(gestos[5])+'\t'+format(target)+'\n')
            f.close()

        contador += 1

    cv2.imshow("Fram", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()
target=input("indique el target del gesto: ")
contador=0


#====================================================================================================================================================================
#                            DESCRIPTOR 3
#====================================================================================================================================================================

while contador<500:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

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

        v_desc = "silvar = {}".format(descriptor_SILBAR)
        cv2.putText(frame, v_desc, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

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

        v_desc1 = "cejas = {}".format(descriptor_full)
        cv2.putText(frame, v_desc1, (10,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)
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

        v_desc2 = "boca = {}".format(descriptor_BOCA)
        cv2.putText(frame, v_desc2, (10,60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

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
        #
        v_desc3 = "sonrisa = {}".format(descriptor_SONRISA)
        cv2.putText(frame, v_desc3, (10,80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)
        cv2.waitKey
#===============================================================================
#                            CEJAS-NARIZ
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
        v_desc1 = "cejas-nariz = {}".format(descriptor_cejanariz)
        cv2.putText(frame, v_desc1, (10,100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

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

        v_desc1 = "ojos = {}".format(descriptor_ojos)
        cv2.putText(frame, v_desc1, (10,120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

#===============================================================================
#                            FIN
#===============================================================================

        gestos = np.array([descriptor_SILBAR, descriptor_full, descriptor_BOCA, descriptor_SONRISA,descriptor_cejanariz,descriptor_ojos])

        for n in range(0, 68):
               x = landmarks.part(n).x
               y = landmarks.part(n).y
               cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

        for i in range(0,2):
            cv2.imshow("Foto", frame)
            cv2.waitKey(1)
            f = open(Fdir + 'file.txt','a')
            f.write(format(gestos[0])+'\t'+format(gestos[1])+'\t'+format(gestos[2])+'\t'+format(gestos[3])+'\t'+format(gestos[4])+'\t'+format(gestos[5])+'\t'+format(target)+'\n')
            f.close()

        contador += 1

    cv2.imshow("Fram", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()
target=input("indique el target del gesto: ")
contador=0

#====================================================================================================================================================================
#                            DESCRIPTOR 4
#====================================================================================================================================================================

while contador<500:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

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

        v_desc = "silvar = {}".format(descriptor_SILBAR)
        cv2.putText(frame, v_desc, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

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

        v_desc1 = "cejas = {}".format(descriptor_full)
        cv2.putText(frame, v_desc1, (10,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)
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

        v_desc2 = "boca = {}".format(descriptor_BOCA)
        cv2.putText(frame, v_desc2, (10,60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

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
        #
        v_desc3 = "sonrisa = {}".format(descriptor_SONRISA)
        cv2.putText(frame, v_desc3, (10,80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)
        cv2.waitKey
#===============================================================================
#                            CEJAS-NARIZ
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
        v_desc1 = "cejas-nariz = {}".format(descriptor_cejanariz)
        cv2.putText(frame, v_desc1, (10,100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

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

        v_desc1 = "ojos = {}".format(descriptor_ojos)
        cv2.putText(frame, v_desc1, (10,120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

#===============================================================================
#                            FIN
#===============================================================================

        gestos = np.array([descriptor_SILBAR, descriptor_full, descriptor_BOCA, descriptor_SONRISA,descriptor_cejanariz,descriptor_ojos])

        for n in range(0, 68):
               x = landmarks.part(n).x
               y = landmarks.part(n).y
               cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

        for i in range(0,2):
            cv2.imshow("Foto", frame)
            cv2.waitKey(1)
            f = open(Fdir + 'file.txt','a')
            f.write(format(gestos[0])+'\t'+format(gestos[1])+'\t'+format(gestos[2])+'\t'+format(gestos[3])+'\t'+format(gestos[4])+'\t'+format(gestos[5])+'\t'+format(target)+'\n')
            f.close()

        contador += 1

    cv2.imshow("Fram", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()
target=input("indique el target del gesto: ")
contador=0

#====================================================================================================================================================================
#                              DESCRIPTOR 5
#====================================================================================================================================================================

while contador<500:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)


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

        v_desc = "silvar = {}".format(descriptor_SILBAR)
        cv2.putText(frame, v_desc, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

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

        v_desc1 = "cejas = {}".format(descriptor_full)
        cv2.putText(frame, v_desc1, (10,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)
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

        v_desc2 = "boca = {}".format(descriptor_BOCA)
        cv2.putText(frame, v_desc2, (10,60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

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
        #
        v_desc3 = "sonrisa = {}".format(descriptor_SONRISA)
        cv2.putText(frame, v_desc3, (10,80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)
        cv2.waitKey
#===============================================================================
#                            CEJAS-NARIZ
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
        v_desc1 = "cejas-nariz = {}".format(descriptor_cejanariz)
        cv2.putText(frame, v_desc1, (10,100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

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

        v_desc1 = "ojos = {}".format(descriptor_ojos)
        cv2.putText(frame, v_desc1, (10,120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

#===============================================================================
#                            FIN
#===============================================================================

        gestos = np.array([descriptor_SILBAR, descriptor_full, descriptor_BOCA, descriptor_SONRISA,descriptor_cejanariz,descriptor_ojos])

        for n in range(0, 68):
               x = landmarks.part(n).x
               y = landmarks.part(n).y
               cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

        for i in range(0,2):
            cv2.imshow("Foto", frame)
            cv2.waitKey(1)
            f = open(Fdir + 'file.txt','a')
            f.write(format(gestos[0])+'\t'+format(gestos[1])+'\t'+format(gestos[2])+'\t'+format(gestos[3])+'\t'+format(gestos[4])+'\t'+format(gestos[5])+'\t'+format(target)+'\n')
            f.close()

        contador += 1

    cv2.imshow("Fram", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()
target=input("indique el target del gesto: ")
contador=0

#====================================================================================================================================================================
#                              DESCRIPTOR 5
#====================================================================================================================================================================

while contador<500:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray)

    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)


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

        v_desc = "silvar = {}".format(descriptor_SILBAR)
        cv2.putText(frame, v_desc, (10,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

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

        v_desc1 = "cejas = {}".format(descriptor_full)
        cv2.putText(frame, v_desc1, (10,40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)
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

        v_desc2 = "boca = {}".format(descriptor_BOCA)
        cv2.putText(frame, v_desc2, (10,60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

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
        #
        v_desc3 = "sonrisa = {}".format(descriptor_SONRISA)
        cv2.putText(frame, v_desc3, (10,80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)
        cv2.waitKey
#===============================================================================
#                            CEJAS-NARIZ
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
        v_desc1 = "cejas-nariz = {}".format(descriptor_cejanariz)
        cv2.putText(frame, v_desc1, (10,100), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

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

        v_desc1 = "ojos = {}".format(descriptor_ojos)
        cv2.putText(frame, v_desc1, (10,120), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255),2)

#===============================================================================
#                            FIN
#===============================================================================

        gestos = np.array([descriptor_SILBAR, descriptor_full, descriptor_BOCA, descriptor_SONRISA,descriptor_cejanariz,descriptor_ojos])

        for n in range(0, 68):
               x = landmarks.part(n).x
               y = landmarks.part(n).y
               cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

        for i in range(0,2):
            cv2.imshow("Foto", frame)
            cv2.waitKey(1)
            f = open(Fdir + 'file.txt','a')
            f.write(format(gestos[0])+'\t'+format(gestos[1])+'\t'+format(gestos[2])+'\t'+format(gestos[3])+'\t'+format(gestos[4])+'\t'+format(gestos[5])+'\t'+format(target)+'\n')
            f.close()

        contador += 1

    cv2.imshow("Fram", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()
target=input("indique el target del gesto: ")
contador=0
