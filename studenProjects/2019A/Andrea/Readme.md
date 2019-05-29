
# ANDREA ASISTENTE PERSONAL

Andrea is a personal assistant, that works with everyones voice. It was programmed in python language and is able to work in every linux device by using a trained Learning model with a Random Forest classifier-
 * [see YouTube video](https://www.youtube.com/watch?v=sMY6JamrtIM).

This repository contents:
  - Source codes
  - data :
    - dev scripts(Arduino)
    - Andrea´s voice files
    - data base
## Hardware requirements:
  - Device with linux
  - Microphone
  - Arduino board (Mega, Uno, Nano)

## Software Requirements:
  - Python 3.2
      - SpeechRecognition
      - PyAudio
      - Pandas
      - numpy
      - [sklearn](www.fgdfgd)
      - threading
 

### Install PyAudio
Installing the dependencies in python3, executed in terminal:
```sh
$ sudo apt-get install python-pyaudio python3-pyaudio
```
It is necessary to install lastest PyAudio version, hence download PyAudio-0.2.11.tar.gz from the link https://pypi.python.org/pypi/PyAudio#downloads and execute in file direction:

```sh
$ sudo python setup.py install
```

### Install SpeechRecongnition

First, make sure you have Python3, then execute the command:

```sh
$ pip install SpeechRecognition
```

## Repository Folders:

    /your_root        - path
    |--data           / Data base
    Andrea.py         / Main script
    
In folder where was download the file, execute Andrea.py in terminal.

## How To Config:

To send messages from your own e-mail, write your e-mail address and password:

```sh
def correo():
    print('A quien lo envias?')
    playsound('ElegirContacto.wav')
    enviado=0
    quien=microfono()
    contacto=lista()
    for i in range(len(contacto)):
        number=str(contacto[i,1])
        if str(quien)==str(contacto[i,0]):
            To = str(number+"@**********.com")
            print('Agregue Asunto')
            playsound('Asunto.wav')
            text=microfono()
            Asunto = str(text)
            print('Mensaje a enviar')
            playsound('Mensaje.wav')
            text=microfono()
            Mensaje = str(text)
            # create message object instance
            msg = MIMEMultipart()
            message = Mensaje
            # setup the parameters of the message
            password = "*******"
            msg['From'] = "*******@*******.com"
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
            playsound('MensajeEnviado.wav')
```

It is neccesary to use an arduino device as slave, and config arduino's port with code above

```sh
arduino = serial.Serial("/dev/tty***", 9600)
```

A simple code example:

```sh
#include <Servo.h>

const int pinLED = 8;

// Declaramos la variable para controlar el servo
Servo servoMotor;

void setup() 
{
  Serial.begin(9600);
  pinMode(pinLED, OUTPUT);
  // Iniciamos el servo para que empiece a trabajar con el pin 9
  servoMotor.attach(9);
}

void loop()
{
  if (Serial.available()>0) 
  {
    char option = Serial.read();
    if (option == '1')
    {
        digitalWrite(pinLED, HIGH);
        delay(100);
    }

    if (option == '2')
    {
        digitalWrite(pinLED, LOW);
        delay(100);
    }

    if(option =='7'){

      // Desplazamos a la posición 90º
      servoMotor.write(80);
      // Esperamos 1 segundo
      delay(1000);
     
    }
    if(option =='8'){
      servoMotor.write(170);
      // Esperamos 1 segundo
      delay(1000);
    }
    
  }
}
```


***


### Authors:
**Universidad de Ibagué** - **Ingeniería Electrónica**
**Inteligencia Artificial - Curso:2019/A**

  - [Harold F Murcia](http://haroldmurcia.com) - *Tutor*
  - [Brahian Steven Espisonsa Ruiz](mailto:2420151009@estudiantesunibague.edu.co)
  - [Andres Sebastian Salazar Alturo](mailto:2420151021@estudiantesunibague.edu.co)
***
