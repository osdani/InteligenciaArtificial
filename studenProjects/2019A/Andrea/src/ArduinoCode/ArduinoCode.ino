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
