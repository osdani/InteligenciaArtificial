# -*- coding: utf-8 -*-
"""
Created on Sun May 12 16:52:29 2019

@author: brahian
"""

import speech_recognition as sr
import matplotlib.pyplot as plt
from sklearn import datasets
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
from playsound import playsound
#import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from pandas import ExcelWriter
from pandas import ExcelFile
from threading import Timer
import serial, time
import sys
import os

arduino = serial.Serial("/dev/ttyUSB1", 9600)


def entrenamiento(a):
    
    xls=pd.read_excel(a+'datos2.xls',header=None)
    xls2=pd.read_excel(a+'target2.xls',header=None)
    #print xls
    n,m=xls.shape
    excel=np.zeros((n,m))
    Y=np.array(xls2)
    
    excel=np.array(xls)
    X=np.zeros((n,m))
    for i in range(n):
        for j in range(m):
            s = excel[i,j]
#            print(s)
            if s==0 or s=='0':
                X[i,j]=0
            else:
                t=[ord(c) for c in s]
                q=''
                for k in range(len(t)):
                    q=(q+str(t[k]))
                qx=int(q)
                X[i,j]=qx
    #print X
    clf = RandomForestClassifier(max_depth=20, random_state=0)
    f=clf.fit(X, Y[:,0])
    pred=f.predict(X)
    f1=f1_score(Y[:,0], pred, average=None)
    print(f1)
    return f

def microfono(a):

    r = sr.Recognizer()
    while(True):
        with sr.Microphone() as source:
            print("Espera. Calibrando microfono...")  
            # listen for 5 seconds and create the ambient noise energy level  
            r.adjust_for_ambient_noise(source, duration=1) 
            playsound(a+'Escuchar.mp3')
            print("Te Escucho :")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language = 'es-CO')
                print("Dijiste : {}".format(text))
                break
            except:
                print("Perdon no te entendí")
                playsound(a+'NoEntender.mp3')
                text = '0'
    return text
    
def prediccion(text):
    articles=['El ',' el','Los ',' los','Lo ',' lo','Las ',' las','La ',' la','Unos ',' unos','Unas ',' unas','Un ',' un','Una ',' una','Del ',' del','Al ',' al ','De ',' de']
    T=str(text)
    T1=T
    for i in range(len(articles)):
        T1 = T1.replace(articles[i], '')
    
    T2=np.array(T1.split())
    
    #xtest=np.array(['luz','Carlos',0,0,0,0])
    m=len(T2)
    Xtest=np.zeros((1,6))
    for j in range(m):
        s = T2[j]
        if s==0 or s=='0':
            Xtest[0,j]=0
        else:
            t=[ord(c) for c in s]
            q=''
            for k in range(len(t)):
                q=(q+str(t[k]))
            qx=int(q)
            Xtest[0,j]=qx
    print(Xtest)
    pred=f.predict(Xtest)
    #pred=f.predict(Xtest.T)
    return pred

def correo(a):
    print('A quien lo envias?')
    playsound(a+'ElegirContacto.wav')
    enviado=0
    quien=microfono(a)
    contacto=lista()
    for i in range(len(contacto)):
        number=str(contacto[i,1])
        if str(quien)==str(contacto[i,0]):
            To = str(number+"@********.com")
            print('Agregue Asunto')
            playsound(a+'Asunto.wav')
            text=microfono(a)
            Asunto = str(text)
            print('Mensaje a enviar')
            playsound(a+'Mensaje.wav')
            text=microfono(a)
            Mensaje = str(text)
            # create message object instance
            msg = MIMEMultipart()
            message = Mensaje
            # setup the parameters of the message
            password = "*******"
            msg['From'] = "******@******.com"
            msg['To'] = To
            msg['Subject'] = Asunto
            # add in the message body
            msg.attach(MIMEText(message, 'plain'))
            #create server
            server = smtplib.SMTP('smtp.gmail.com: 587')
            server.starttls()
            # Login Credentials for sending the mail
            server.login(msg['From'], password)
            # send the message via the server.
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            server.quit()
            enviado=1
            print("successfully sent email to %s:" % (msg['To']))
            playsound(a+'MensajeEnviado.wav')


    if enviado==0:
#        To = str("2420151009@estudiantesunibague.edu.co")
        print('No hay contacto con ese nombre')
        playsound(a+'SinContactos.wav')

    
def escribir(tx,nx,a):

    t=str(microfono(a))
    if t != '0':
        t=t.replace(' ','')
        tx=tx+' '+t
        text=tx.split()
        playsound(a+'InserteEmail.wav')
        n=str(microfono(a))
        if t != '0':
            n=n.replace(' ','')
            nx=nx+' '+n
            number=nx.split()
            df = pd.DataFrame({'a':text,
                               'b':number})
            
            writer = ExcelWriter(a+'Contactos.xlsx')
            df.to_excel(writer,'Sheet1',header=False,index=False)
            writer.save()
            playsound(a+'Okey.mp3')

    return tx, nx
    
def lista(a):
        
    lista=pd.read_excel(a+'Contactos.xlsx',header=None)
    contacto=np.array(lista)
    return contacto

def mercado(txt,a):
    print('Que quieres hacer con tu mercado')
    playsound(a+'Mercado.wav')
    funcion=str(microfono(a))
    if funcion !='0':
        if funcion=='Agregar' or funcion=='agregar':
            while(True):
                print('Que quieres agregar')
                playsound(a+'Agregando.wav')
                t=str(microfono(a))
                if t =='Nada más' or t=='nada más':
                    break
                    playsound(a+'Okey.mp3')
                if t !='0':
                    t=t.replace(' ','')
                    txt=txt+' '+t
                    text=txt.split()
                    df = pd.DataFrame({'a':[text]})
                    
                    writer = ExcelWriter(a+'Mercado.xlsx')
                    df.to_excel(writer,'Sheet1',header=False,index=False)
                    writer.save()
                
        elif funcion=='Mirar' or funcion=='mirar':
            playsound(a+'MirarLista.wav')
            lista=pd.read_excel(a+'Mercado.xlsx',header=None)
            print(lista)
            txt=txt
            playsound(a+'Okey.mp3')

#        else:
#            txt=txt
#    else:
#        txt=txt
#            
    return txt
        
def alarma(a):
    print('cuanto tiempo')
    text=str(microfono(a))
    if text !='0':
        
        tiempo=text.split()
        if tiempo[0]=='un' or tiempo[0]=='uno':
            numero=1
        else:
            numero=float(tiempo[0])
        unidad=tiempo[1]
        if unidad=='segundo' or unidad=='Segundo' or unidad=='segundos' or unidad=='Segundos':
            mult=1
            
        elif unidad=='minuto' or unidad=='Minuto' or unidad=='minutos' or unidad=='Minutos':
            mult=60
        espera=numero*mult
        t = Timer(espera, timeout)
        t.start()

def timeout(a):
    print("A levantarse!!!")
    playsound(a+'Despertador.wav')

if __name__ == "__main__":
    txt=''
    tx=''
    nx=''
    c=os.path.dirname(__file__)
    a=c[:-3]+'data/'
    f = entrenamiento(a)


    while(True):
        if input()==' ':
            text = microfono(a)
            if text != '0':
                 
                pred=prediccion(text)
                print(pred)
                
                if pred[0]==1:
                    playsound(a+'Okey.mp3')
                    playsound(a+'EncenderLuz.wav')
                    arduino.write(b'1')  
                elif pred[0]==2:
                    playsound(a+'Okey.mp3')
                    playsound(a+'ApagarLuz.wav')
                    arduino.write(b'2') 
                if pred[0]==3:
                    txt=mercado(txt,a)
                elif pred[0]==4:
                    playsound(a+'Alarma.wav')
                    alarma(a)
                    playsound(a+'Okey.mp3')
                elif pred[0]==6:
                    playsound(a+'AgregarContacto.wav')
                    tx,nx=escribir(tx,nx,a)
                elif pred[0]==7:
                    playsound(a+'Okey.mp3')
                    playsound(a+'AbriendoPuerta.wav')
                    arduino.write(b'7') 
                elif pred[0]==8:
                    playsound(a+'Okey.mp3')
                    playsound(a+'CerrandoPuerta.wav')
                    arduino.write(b'8') 
                elif pred[0]==9:
                    playsound(a+'Okey.mp3')
                    playsound(a+'Temazo.wav')
                    playsound(a+'MortalKombat.mp3')
                elif pred[0]==10:
                    playsound(a+'Okey.mp3')
                    correo(a)
                elif pred[0]==0:
                    playsound(a+'Saludar.wav')
                elif pred[0]==5:
                    playsound(a+'Chiste.wav')
                    playsound(a+'Chiste2.wav')
                                    
    arduino.close()


