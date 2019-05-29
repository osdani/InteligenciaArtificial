#OpenCV module
import cv2
#Modulo para leer directorios y rutas de archivos
import os
#OpenCV trabaja con arreglos de numpy
import numpy
# Parte 1: Creando el entrenamiento del modelo
import dlib
print('Iniciando Programa de Reconocimiento Facial...')
print ""
detector = dlib.get_frontal_face_detector() # DETECTAR CARA DE FRENTE
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat_2") # Puntos de la cara
imgpoints = []
objpoints = []
#Directorio donde se encuentran las carpetas con las caras de entrenamiento
#dir_faces = 'D:\Universidad\IA\OpenCV\Reconocimiento Facial\Multipurpose Facial Recognition System\Data'

RutaActual = os.getcwd()
Carpeta = RutaActual[:-3]
# Data es la carpeta base donde se encuentra los datos de los autores
# Si desea puede crear su propia carpeta, solo debe cambiar el Data
# por el nombre de la carpeta que usted creo previamente
dir_faces = Carpeta +'Data'
print 'Ruta ' + dir_faces
#Tamao para reducir a miniaturas las fotografias
size = 4

# Crear una lista de imagenes y una lista de nombres correspondientes
(images, lables, names, id) = ([], [], {}, 0)
for (subdirs, dirs, files) in os.walk(dir_faces):
    for subdir in dirs:
        names[id] = subdir
        subjectpath = os.path.join(dir_faces, subdir)
        for filename in os.listdir(subjectpath):
            path = subjectpath + '/' + filename
            lable = id
            images.append(cv2.imread(path, 0))
            lables.append(int(lable))
        id += 1
(im_width, im_height) = (112, 92)

# Crear una matriz Numpy de las dos listas anteriores
(images, lables) = [numpy.array(lis) for lis in [images, lables]]
# OpenCV entrena un modelo a partir de las imagenes
model = cv2.face.LBPHFaceRecognizer_create()
model.train(images, lables)


# Parte 2: Utilizar el modelo entrenado en funcionamiento con la camara
face_cascade = cv2.CascadeClassifier( 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:
    #leemos un frame y lo guardamos
    rval, frame = cap.read()
    frame=cv2.flip(frame,1,0)
    rval, video = cap.read()
    video=cv2.flip(video,1,0)
    #convertimos la imagen a blanco y negro    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #redimensionar la imagen
    mini = cv2.resize(gray, (int(gray.shape[1] / size), int(gray.shape[0] / size)))

    """buscamos las coordenadas de los rostros (si los hay) y
   guardamos su posicion"""
    faces = face_cascade.detectMultiScale(mini)
    
    for i in range(len(faces)):
        face_i = faces[i]
        (x, y, w, h) = [v * size for v in face_i]
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (im_width, im_height))

        # Intentado reconocer la cara
        prediction = model.predict(face_resize)
        
         #Dibujamos un rectangulo en las coordenadas del rostro
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        
        # Escribiendo el nombre de la cara reconocida
        # La variable cara tendra el nombre de la persona reconocida
        cara = '%s' % (names[prediction[0]])
        estado=''
        #Si la prediccion tiene una exactitud menor a 100 se toma como prediccion valida
        if prediction[1]<100 :
          #Ponemos el nombre de la persona que se reconoció
          cv2.putText(frame,'%s - %.0f' % (cara,prediction[1]),(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 0),2)
          #En caso de que la cara sea de algun conocido se realizara determinadas accione          
          #Busca si los nombres de las personas reconocidas estan dentro de los que tienen acceso          
          #flabs.TuSiTuNo(cara)
        #Si la prediccion es mayor a 100 no es un reconomiento con la exactitud suficiente
        elif prediction[1]>101 and prediction[1]<500:           
            #Si la cara es desconocida, poner desconocido
            estado='Desconocido'
            cv2.putText(frame, estado,(x-10, y-10), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 0),2)
            if estado=='Desconocido':
                cv2.putText(frame, 'Bienvenido',(x-10, y-30), cv2.FONT_HERSHEY_PLAIN,1.5,(0, 255, 0),2)
################################ Etiquetas #################################################################
        Lider=''
        Cod=''
        Edad=''
        Profesion=''
        if cara=='Santiago' and estado==''and Lider=='' and Cod=='' :
            Lider="Nombre: {} Reyes".format(cara)
            Cod='Id: 123456789'
            Edad='Edad: 21'
            Profesion='Profesion: Estudiante'
            cv2.putText(frame, 'Lider',(x-10, y-50), cv2.FONT_HERSHEY_PLAIN,1.5,(0, 0, 255),2)
            cv2.putText(frame, Cod,(x-10, y-30), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 255),2)
            cv2.putText(frame, Edad,(x-10, y+h+20), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 255),2)
            cv2.putText(frame, Profesion,(x-10, y+h+40), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 255),2)
        if cara=='Judith' and estado=='' and Lider=='' and Cod=='' :
            cv2.putText(frame, 'Cliente',(x-10, y-30), cv2.FONT_HERSHEY_PLAIN,1.5,(0, 255, 0),2)
            Cod='Id: 123456789'
            Edad='Edad: 55'
            Profesion='Profesion: Pensionado'
            cv2.putText(frame, 'Lider',(x-10, y-50), cv2.FONT_HERSHEY_PLAIN,1.5,(0, 0, 255),2)
            cv2.putText(frame, Cod,(x-10, y-30), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 255),2)
            cv2.putText(frame, Edad,(x-10, y+h+20), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 255),2)
            cv2.putText(frame, Profesion,(x-10, y+h+40), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 255),2)
        if cara=='Cesar' and estado=='' and Lider=='' and Cod=='' :
            Lider="Nombre: {} Reyes H.".format(cara)
            Cod='Id: 123456789'
            Edad='Edad: 55'
            Profesion='Profesion: Pensionado'
            cv2.putText(frame, 'Lider',(x-10, y-50), cv2.FONT_HERSHEY_PLAIN,1.5,(0, 0, 255),2)
            cv2.putText(frame, Cod,(x-10, y-30), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 255),2)
            cv2.putText(frame, Edad,(x-10, y+h+20), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 255),2)
            cv2.putText(frame, Profesion,(x-10, y+h+40), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 255),2)
        if cara=='rene' and estado=='' and Lider=='' and Cod=='':
            cv2.putText(frame, 'Cuidado un Rene',(x-10, y-30), cv2.FONT_HERSHEY_PLAIN,1.5,(0, 0, 255),2)
        if cara=='Rene' and estado=='' and Lider=='' and Cod=='' :
            Lider="Nombre: Cristian {}".format(cara)
            Cod='Id: 123456789'
            Edad='Edad: 22'
            Profesion='Profesion: Estudiante'
            cv2.putText(frame, 'Lider',(x-10, y-50), cv2.FONT_HERSHEY_PLAIN,1.5,(0, 0, 255),2)
            cv2.putText(frame, Cod,(x-10, y-30), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 255),2)
            cv2.putText(frame, Edad,(x-10, y+h+20), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 255),2)
            cv2.putText(frame, Profesion,(x-10, y+h+40), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 255),2)
        if cara=='Duvan' and estado=='' and Lider=='' and Cod=='' :
            Lider="Nombre: {} Joven".format(cara)
            Cod='Id: 123456789'
            Edad='Edad: 22'
            Profesion='Profesion: Estudiante'
            cv2.putText(frame, 'Lider',(x-10, y-50), cv2.FONT_HERSHEY_PLAIN,1.5,(0, 0, 255),2)
            cv2.putText(frame, Cod,(x-10, y-30), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 255),2)
            cv2.putText(frame, Edad,(x-10, y+h+20), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 255),2)
            cv2.putText(frame, Profesion,(x-10, y+h+40), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 255),2)
        if cara=='Ing harold' and estado=='' and Lider=='' and Cod=='':
            cv2.putText(frame, 'Gracias Ing 5.0?',(x-10, y-50), cv2.FONT_HERSHEY_PLAIN,1.5,(0, 255, 0),2)
        if cara=='Ing Harold' and estado=='' and Lider=='' and Cod=='':
            Lider="Nombre: {} Murcia".format(cara)
            Cod='Id: 123456789'
            Edad='Edad: --'
            Profesion='Profesion: Ingeniero'
            cv2.putText(frame, 'Ing Harold',(x-10, y-50), cv2.FONT_HERSHEY_PLAIN,1.5,(0, 255, 0),2)
            cv2.putText(frame, Cod,(x-10, y-30), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 255),2)
            cv2.putText(frame, Edad,(x-10, y+h+20), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 255),2)
            cv2.putText(frame, Profesion,(x-10, y+h+40), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 255),2)
        if cara=='tique' and estado=='' and Lider=='' and Cod=='':
            cv2.putText(frame, 'Culo  Gordo',(x-10, y-50), cv2.FONT_HERSHEY_PLAIN,1.5,(0, 0, 255),2)
        if cara=='Tique' and estado=='' and Lider=='' and Cod=='':
            Lider="Nombre: Juan Carlos {}".format(cara)
            Cod='Id: 123456789'
            Edad='Edad: 23'
            Profesion='Profesion: Estudiante'
            cv2.putText(frame, 'Cliente',(x-10, y-50), cv2.FONT_HERSHEY_PLAIN,1.5,(0, 0, 255),2)
            cv2.putText(frame, Cod,(x-10, y-30), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 255),2)
            cv2.putText(frame, Edad,(x-10, y+h+20), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 255),2)
            cv2.putText(frame, Profesion,(x-10, y+h+40), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 255),2)
        if cara=='Andres' and estado=='' and Lider=='' and Cod=='':
            Lider="Nombre: {} Salasar".format(cara)
            Cod='Id: 123456789'
            Edad='Edad: 22'
            Profesion='Profesion: Estudiante'
            cv2.putText(frame, 'Cliente',(x-10, y-50), cv2.FONT_HERSHEY_PLAIN,1.5,(0, 255, 0),2)
            cv2.putText(frame, Cod,(x-10, y-30), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 255),2)
            cv2.putText(frame, Edad,(x-10, y+h+20), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 255),2)
            cv2.putText(frame, Profesion,(x-10, y+h+40), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 255),2)
        if cara=='Brahian' and estado=='' and Lider=='' and Cod=='':
            Lider="Nombre: {} Espinosa".format(cara)
            Cod='Id: 123456789'
            Edad='Edad: 23'
            Profesion='Profesion: Estudiante'
            cv2.putText(frame, 'Cliente',(x-10, y-50), cv2.FONT_HERSHEY_PLAIN,1.5,(0, 255, 0),2)
            cv2.putText(frame, Cod,(x-10, y-30), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 255),2)
            cv2.putText(frame, Edad,(x-10, y+h+20), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 255),2)
            cv2.putText(frame, Profesion,(x-10, y+h+40), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 255),2)
        if cara=='Sierra' and estado=='' and Lider=='' and Cod=='':
            Lider="Nombre: Sebastian {}".format(cara)
            Cod='Id: 123456789'
            Edad='Edad: 23'
            Profesion='Profesion: Estudiante'
            cv2.putText(frame, 'Cliente',(x-10, y-50), cv2.FONT_HERSHEY_PLAIN,1.5,(0, 0, 255),2)
        if cara=='sierra' and estado=='' and Lider=='' and Cod=='':
            cv2.putText(frame, 'My Bless',(x-10, y-50), cv2.FONT_HERSHEY_PLAIN,1.5,(0, 0, 255),2)
        if cara=='Angel' and estado=='' and Lider=='' and Cod=='':
            Lider="Nombre: {} Calderon".format(cara)
            Cod='Id: 123456789'
            Edad='Edad: 20'
            Profesion='Profesion: Estudiante'
            cv2.putText(frame, 'Cliente',(x-10, y-50), cv2.FONT_HERSHEY_PLAIN,1.5,(0, 255, 0),2)
            cv2.putText(frame, Cod,(x-10, y-30), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 255),2)
            cv2.putText(frame, Edad,(x-10, y+h+20), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 255),2)
            cv2.putText(frame, Profesion,(x-10, y+h+40), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 255),2)
        if cara=='Daniel' and estado=='' and Lider=='' and Cod=='':
            Lider="Nombre: {} Rodriguez".format(cara)
            Cod='Id: 123456789'
            Edad='Edad: 20'
            Profesion='Profesion: Estudiante'
            cv2.putText(frame, 'Peligroso',(x-10, y-50), cv2.FONT_HERSHEY_PLAIN,1.5,(0, 0, 255),2)
            cv2.putText(frame, Cod,(x-10, y-30), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 255),2)
            cv2.putText(frame, Edad,(x-10, y+h+20), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 255),2)
            cv2.putText(frame, Profesion,(x-10, y+h+40), cv2.FONT_HERSHEY_PLAIN,1.5,(255, 255, 255),2)

##################################################################################################################
    cv2.imshow('OpenCV Reconocimiento facial', frame)
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 2. Detecto cara y puntos dlib
    faces = detector(gray)
    if len(faces) > 0:  # mirar lo del not none
        for face in faces:
            # Dibujo rectangulo cara
            x1, y1 = face.left(), face.top()
            x2, y2 = face.right(), face.bottom()
            #cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            # Obtengo puntos de estudio
            landmarks = predictor(gray, face)
            for n in range(0, 68): 
               x = landmarks.part(n).x 
               y = landmarks.part(n).y 
               cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)
            # Definimos los puntos del rostro
            p0=(landmarks.part(0).x , landmarks.part(0).y)
            p1=(landmarks.part(1).x , landmarks.part(1).y)
            p2=(landmarks.part(2).x , landmarks.part(2).y)
            p3=(landmarks.part(3).x , landmarks.part(3).y)
            p4=(landmarks.part(4).x , landmarks.part(4).y)
            p5=(landmarks.part(5).x , landmarks.part(5).y)
            p6=(landmarks.part(6).x , landmarks.part(6).y)
            p7=(landmarks.part(7).x , landmarks.part(7).y)
            p8=(landmarks.part(8).x , landmarks.part(8).y)
            p9=(landmarks.part(9).x , landmarks.part(9).y)
            
            p10=(landmarks.part(10).x , landmarks.part(10).y)
            p11=(landmarks.part(11).x , landmarks.part(11).y)
            p12=(landmarks.part(12).x , landmarks.part(12).y)
            p13=(landmarks.part(13).x , landmarks.part(13).y)
            p14=(landmarks.part(14).x , landmarks.part(14).y)
            p15=(landmarks.part(15).x , landmarks.part(15).y)
            p16=(landmarks.part(16).x , landmarks.part(16).y)
            p17=(landmarks.part(17).x , landmarks.part(17).y)
            p18=(landmarks.part(18).x , landmarks.part(18).y)
            p19=(landmarks.part(19).x , landmarks.part(19).y)
            
            p20=(landmarks.part(20).x , landmarks.part(20).y)
            p21=(landmarks.part(21).x , landmarks.part(21).y)
            p22=(landmarks.part(22).x , landmarks.part(22).y)
            p23=(landmarks.part(23).x , landmarks.part(23).y)
            p24=(landmarks.part(24).x , landmarks.part(24).y)
            p25=(landmarks.part(25).x , landmarks.part(25).y)
            p26=(landmarks.part(26).x , landmarks.part(26).y)
            p27=(landmarks.part(27).x , landmarks.part(27).y)
            p28=(landmarks.part(28).x , landmarks.part(28).y)
            p29=(landmarks.part(29).x , landmarks.part(29).y)
            
            p30=(landmarks.part(30).x , landmarks.part(30).y)
            p31=(landmarks.part(31).x , landmarks.part(31).y)
            p32=(landmarks.part(32).x , landmarks.part(32).y)
            p33=(landmarks.part(33).x , landmarks.part(33).y)
            p34=(landmarks.part(34).x , landmarks.part(34).y)
            p35=(landmarks.part(35).x , landmarks.part(35).y)
            p36=(landmarks.part(36).x , landmarks.part(36).y)
            p37=(landmarks.part(37).x , landmarks.part(37).y)
            p38=(landmarks.part(38).x , landmarks.part(38).y)
            p39=(landmarks.part(39).x , landmarks.part(39).y)

            p40=(landmarks.part(40).x , landmarks.part(40).y)
            p41=(landmarks.part(41).x , landmarks.part(41).y)
            p42=(landmarks.part(42).x , landmarks.part(42).y)
            p43=(landmarks.part(43).x , landmarks.part(43).y)
            p44=(landmarks.part(44).x , landmarks.part(44).y)
            p45=(landmarks.part(45).x , landmarks.part(45).y)
            p46=(landmarks.part(46).x , landmarks.part(46).y)
            p47=(landmarks.part(47).x , landmarks.part(47).y)
            p48=(landmarks.part(48).x , landmarks.part(48).y)
            p49=(landmarks.part(49).x , landmarks.part(49).y)

            p50=(landmarks.part(50).x , landmarks.part(50).y)
            p51=(landmarks.part(51).x , landmarks.part(51).y)
            p52=(landmarks.part(52).x , landmarks.part(52).y)
            p53=(landmarks.part(53).x , landmarks.part(53).y)
            p54=(landmarks.part(54).x , landmarks.part(54).y)
            p55=(landmarks.part(55).x , landmarks.part(55).y)
            p56=(landmarks.part(56).x , landmarks.part(56).y)
            p57=(landmarks.part(57).x , landmarks.part(57).y)
            p58=(landmarks.part(58).x , landmarks.part(58).y)
            p59=(landmarks.part(59).x , landmarks.part(59).y)

            p60=(landmarks.part(60).x , landmarks.part(60).y)
            p61=(landmarks.part(61).x , landmarks.part(61).y)
            p62=(landmarks.part(62).x , landmarks.part(62).y)
            p63=(landmarks.part(63).x , landmarks.part(63).y)
            p64=(landmarks.part(64).x , landmarks.part(64).y)
            p65=(landmarks.part(65).x , landmarks.part(65).y)
            p66=(landmarks.part(66).x , landmarks.part(66).y)
            p67=(landmarks.part(67).x , landmarks.part(67).y)
            #Creamos un punto en la frente
            wfrente = (landmarks.part(19).x + landmarks.part(24).x)/2
            zfrente = (landmarks.part(19).y + landmarks.part(24).y)/2
            pFrente = (wfrente,zfrente)
            # Unimos los puntos necesarios para crear una especie de mascara
            cv2.line (frame, p0, p1, (255,255,255), 1)
            cv2.line (frame, p1, p2, (255,255,255), 1)
            cv2.line (frame, p2, p3, (255,255,255), 1)
            cv2.line (frame, p3, p4, (255,255,255), 1)
            cv2.line (frame, p4, p5, (255,255,255), 1)
            cv2.line (frame, p5, p6, (255,255,255), 1)
            cv2.line (frame, p6, p7, (255,255,255), 1)
            cv2.line (frame, p7, p8, (255,255,255), 1)
            cv2.line (frame, p8, p9, (255,255,255), 1)
            cv2.line (frame, p9, p10, (255,255,255), 1)
            cv2.line (frame, p10, p11, (255,255,255), 1)
            cv2.line (frame, p11, p12 , (255,255,255), 1)
            cv2.line (frame, p12, p13, (255,255,255), 1)
            cv2.line (frame, p13, p14, (255,255,255), 1)
            cv2.line (frame, p14, p15, (255,255,255), 1)
            cv2.line (frame, p15, p16, (255,255,255), 1)
            
            cv2.line (frame, p17, p18, (255,255,255), 1)
            cv2.line (frame, p18, p19, (255,255,255), 1)
            cv2.line (frame, p19, p20, (255,255,255), 1)
            cv2.line (frame, p20, p21, (255,255,255), 1)

            cv2.line (frame, p22, p23, (255,255,255), 1)
            cv2.line (frame, p23, p24, (255,255,255), 1)
            cv2.line (frame, p24, p25, (255,255,255), 1)
            cv2.line (frame, p25, p26, (255,255,255), 1)

            cv2.line (frame, p27, p28, (255,255,255), 1)
            cv2.line (frame, p28, p29, (255,255,255), 1)
            cv2.line (frame, p29, p30, (255,255,255), 1)
            cv2.line (frame, p30, p31, (255,255,255), 1)
            cv2.line (frame, p31, p32, (255,255,255), 1)
            cv2.line (frame, p32, p33, (255,255,255), 1)
            cv2.line (frame, p33, p34, (255,255,255), 1)
            cv2.line (frame, p34, p35, (255,255,255), 1)
            cv2.line (frame, p35, p30, (255,255,255), 1)

            cv2.line (frame, p48, p49, (255,255,255), 1)
            cv2.line (frame, p49, p50, (255,255,255), 1)
            cv2.line (frame, p50, p51, (255,255,255), 1)
            cv2.line (frame, p51, p52, (255,255,255), 1)
            cv2.line (frame, p52, p53, (255,255,255), 1)
            cv2.line (frame, p53, p54, (255,255,255), 1)
            cv2.line (frame, p54, p55, (255,255,255), 1)
            cv2.line (frame, p55, p56, (255,255,255), 1)
            cv2.line (frame, p56, p57, (255,255,255), 1)
            cv2.line (frame, p57, p58, (255,255,255), 1)
            cv2.line (frame, p58, p59, (255,255,255), 1)
            cv2.line (frame, p59, p48, (255,255,255), 1)
            cv2.line (frame, p48, p60, (255,255,255), 1)
            cv2.line (frame, p60, p59, (255,255,255), 1)
            cv2.line (frame, p60, p49, (255,255,255), 1)
            cv2.line (frame, p54, p64, (255,255,255), 1)
            cv2.line (frame, p64, p55, (255,255,255), 1)
            cv2.line (frame, p64, p53, (255,255,255), 1)
            cv2.line (frame, p61, p62, (255,255,255), 1)

            cv2.line (frame, p36, p37, (255,255,255), 1)
            cv2.line (frame, p37, p38, (255,255,255), 1)
            cv2.line (frame, p38, p39, (255,255,255), 1)
            cv2.line (frame, p39, p40, (255,255,255), 1)
            cv2.line (frame, p40, p41, (255,255,255), 1)
            cv2.line (frame, p41, p36, (255,255,255), 1)
            
            cv2.line (frame, p42, p43, (255,255,255), 1)
            cv2.line (frame, p43, p44, (255,255,255), 1)
            cv2.line (frame, p44, p45, (255,255,255), 1)
            cv2.line (frame, p45, p46, (255,255,255), 1)
            cv2.line (frame, p46, p47, (255,255,255), 1)
            cv2.line (frame, p47, p42, (255,255,255), 1)

            cv2.line (frame, p0, p17, (255,255,255), 1)
            cv2.line (frame, p21, p22, (255,255,255), 1)
            cv2.line (frame, p16, p26, (255,255,255), 1)
            
            cv2.line (frame, p0, p36, (255,255,255), 1)
            cv2.line (frame, p17, p36, (255,255,255), 1)
            cv2.line (frame, p17, p37, (255,255,255), 1)
            cv2.line (frame, p18, p37, (255,255,255), 1)
            cv2.line (frame, p19, p37, (255,255,255), 1)
            cv2.line (frame, p19, p38, (255,255,255), 1)
            cv2.line (frame, p20, p38, (255,255,255), 1)
            cv2.line (frame, p21, p38, (255,255,255), 1)
            cv2.line (frame, p21, p39, (255,255,255), 1)
            cv2.line (frame, p21, p27, (255,255,255), 1)
            cv2.line (frame, p27, p39, (255,255,255), 1)
            cv2.line (frame, p27, p22, (255,255,255), 1)
            cv2.line (frame, p22, p42, (255,255,255), 1)
            cv2.line (frame, p27, p42, (255,255,255), 1)
            cv2.line (frame, p22, p43, (255,255,255), 1)
            cv2.line (frame, p23, p43, (255,255,255), 1)
            cv2.line (frame, p24, p43, (255,255,255), 1)
            cv2.line (frame, p24, p44, (255,255,255), 1)
            cv2.line (frame, p25, p44, (255,255,255), 1)
            cv2.line (frame, p26, p44, (255,255,255), 1)
            cv2.line (frame, p26, p45, (255,255,255), 1)

            cv2.line (frame, p39, p28, (255,255,255), 1)
            cv2.line (frame, p42, p28, (255,255,255), 1)
            cv2.line (frame, p39, p28, (255,255,255), 1)
            cv2.line (frame, p16, p45, (255,255,255), 1)
            cv2.line (frame, p39, p29, (255,255,255), 1)
            cv2.line (frame, p42, p29, (255,255,255), 1)
            cv2.line (frame, p39, p30, (255,255,255), 1)
            cv2.line (frame, p42, p30, (255,255,255), 1)
            cv2.line (frame, p40, p30, (255,255,255), 1)
            cv2.line (frame, p41, p30, (255,255,255), 1)
            cv2.line (frame, p47, p30, (255,255,255), 1)
            cv2.line (frame, p46, p30, (255,255,255), 1)

            cv2.line (frame, p40, p31, (255,255,255), 1)
            cv2.line (frame, p41, p31, (255,255,255), 1)
            cv2.line (frame, p42, p35, (255,255,255), 1)
            cv2.line (frame, p47, p35, (255,255,255), 1)
            cv2.line (frame, p46, p35, (255,255,255), 1)
            cv2.line (frame, p41, p48, (255,255,255), 1)
            cv2.line (frame, p36, p48, (255,255,255), 1)
            cv2.line (frame, p46, p54, (255,255,255), 1)
            cv2.line (frame, p45, p54, (255,255,255), 1)
            cv2.line (frame, p31, p48, (255,255,255), 1)
            cv2.line (frame, p35, p54, (255,255,255), 1)

            cv2.line (frame, p31, p49, (255,255,255), 1)
            cv2.line (frame, p31, p50, (255,255,255), 1)
            cv2.line (frame, p32, p50, (255,255,255), 1)
            cv2.line (frame, p33, p50, (255,255,255), 1)
            cv2.line (frame, p33, p51, (255,255,255), 1)
            cv2.line (frame, p33, p52, (255,255,255), 1)
            cv2.line (frame, p34, p52, (255,255,255), 1)
            cv2.line (frame, p35, p52, (255,255,255), 1)
            cv2.line (frame, p35, p53, (255,255,255), 1)
            
            cv2.line (frame, p62, p63, (255,255,255), 1)
            cv2.line (frame, p63, p65, (255,255,255), 1)
            cv2.line (frame, p65, p66, (255,255,255), 1)
            cv2.line (frame, p66, p67, (255,255,255), 1)
            cv2.line (frame, p67, p61, (255,255,255), 1)

            cv2.line (frame, p57, p8, (255,255,255), 1)
            cv2.line (frame, p57, p7, (255,255,255), 1)
            cv2.line (frame, p57, p9, (255,255,255), 1)
            cv2.line (frame, p58, p7, (255,255,255), 1)
            cv2.line (frame, p58, p6, (255,255,255), 1)
            cv2.line (frame, p56, p9, (255,255,255), 1)
            cv2.line (frame, p56, p10, (255,255,255), 1)
            cv2.line (frame, p6, p59, (255,255,255), 1)
            cv2.line (frame, p6, p48, (255,255,255), 1)
            cv2.line (frame, p10, p55, (255,255,255), 1)
            cv2.line (frame, p10, p54, (255,255,255), 1)
            cv2.line (frame, p5, p48, (255,255,255), 1)
            cv2.line (frame, p4, p48, (255,255,255), 1)
            cv2.line (frame, p3, p48, (255,255,255), 1)
            cv2.line (frame, p11, p54, (255,255,255), 1)
            cv2.line (frame, p12, p54, (255,255,255), 1)
            cv2.line (frame, p13, p54, (255,255,255), 1)
            cv2.line (frame, p2, p48, (255,255,255), 1)
            cv2.line (frame, p1, p48, (255,255,255), 1)
            cv2.line (frame, p0, p48, (255,255,255), 1)
            cv2.line (frame, p16, p54, (255,255,255), 1)
            cv2.line (frame, p15, p54, (255,255,255), 1)
            cv2.line (frame, p14, p54, (255,255,255), 1)
            cv2.line (frame, p17, p48, (255,255,255), 1)
            cv2.line (frame, p26, p54, (255,255,255), 1)

            cv2.line (frame, p49, p61, (255,255,255), 1)
            cv2.line (frame, p59, p67, (255,255,255), 1)
            cv2.line (frame, p53, p63, (255,255,255), 1)
            cv2.line (frame, p55, p65, (255,255,255), 1)
            cv2.line (frame, pFrente, p21, (255,255,255), 1)
            cv2.line (frame, pFrente, p22, (255,255,255), 1)
            cv2.line (frame, pFrente, p20, (255,255,255), 1)
            cv2.line (frame, pFrente, p23, (255,255,255), 1)

            cv2.circle(frame, pFrente, 2, (0, 255, 0), -1)
    #Mostramos la imagen
    cv2.imshow('Caracteristicas', frame)

    #Si se presiona la tecla ESC se cierra el programa
    key = cv2.waitKey(10)
    if key == 27:
        cv2.destroyAllWindows()
        break
