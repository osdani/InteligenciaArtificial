
# HeadMouse
MouseHead its a project that control the mouse with the facial gestures, these are Whistling, Eyesbrow ,open mouth, smile, Frowns and normal face. MouseHead implement a predictor algorithm with the tools how RandomForest. 
 * [see YouTube video](https://www.youtube.com/watch?v=UVUe5zhM2Mk)

##Requirements:
 - Source codes 
 - Data (Calibration, class report, shape_predictor_68_face_landmarks ,pictures)
### Hardware Elements
 -  Web Camera
### Software Requirements
  - [Python 2.7](https://www.python.org/download/releases/2.7/)
    - [cv2](https://pypi.org/project/opencv-python/)
    - [numpy](https://www.numpy.org/)
    - [dlib](https://pypi.org/project/dlib/) 
    - [time](https://docs.python.org/2/library/time.html)
    - [pandas](https://pandas.pydata.org/)
    - [sklearn](https://scikit-learn.org/stable/)
    - [imutils](https://pypi.org/project/imutils/)
    - [utils](https://pypi.org/project/utils/)
    - [pyautogui](https://pyautogui.readthedocs.io/en/latest/) 
  - [OS Linux](http://releases.ubuntu.com/16.04/)

### How to use:
 - To use the repository with the predeterminate data base (The algoritm can have fails, we suggest to calibrate with your own data).
 -- Execute mousehead by using: 
```sh
$ python final_bien.py 
```
 - To use with your own data base (first follow  "Create your own data base" instructions).
 -- To calibrate use:
```sh
$ python main.py 
```
### Create your own data base
 - Renamed the "file.txt" document on the data folder.
 - Create a new document called "file.txt" on the data folder.
 - Execute main.py code to create the data base whit your owns data and follow the calibration instructions.

### Calibration instructions
To calibrate the data base with your owns data, you have to execute the main.py after that you must to asigment a class to each gesture with the next steps:

REMEMBER: Is important do the gesture before assigment the class and stay doing the gesture all the calibration time, if you change your face expression in the calibration time this going to take miss data.

 - Gesture assigment on each class
 -- Whistling gesture, class    [0]
 -- Eyesbrow up gesture, class  [1]
 -- Open mouth gesture, class   [2]
 -- Smile gesture, class        [3]
 -- Frowns gesture, class       [4]
 -- Normal face, class          [6]

### Mouse instruction

Each action have an activation by gesture, have in mind if you want to do the mouse action you must to keep the gesture for a few seconds.

- Whistling gesture is the enable to scroll mouse.
 - Eyesbrow up gesture is the left click.
 - Open mouth gesture is the enable to move mouse.
 - Smile gesture is the activation or desactivation of the all sistem.
 - Frowns gestureis the rigth click.
 


***


### Authors:
**Universidad de Ibagué** - **Ingeniería Electrónica**
**Inteligencia Artificial - Curso:2019/A**

  - [Harold F Murcia](http://haroldmurcia.com) - *Tutor*
  - Juan Carlos Tique
  - Juan Sebastian Sierra
***
