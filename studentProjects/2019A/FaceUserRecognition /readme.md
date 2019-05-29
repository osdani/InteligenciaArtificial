# Facial Recognition System


Here we present a system that automatically identifies a person, through an analysis of the subject's facial characteristics, extracted from an image or a key frame of a video source, and comparing them with an already trained database by using a Random Forest predictor. 
 * [see YouTube video](https://www.youtube.com/watch?v=EuuAR7Xf568)

For the development of this program, the following requirements are needed:
***
·# Hardware requirements:
- Webcam
***
#· Software requirements:
- Python 2.7
- OpenCV
***

## Python Libraries:

The libraries used in the development of the code are the following:
- [cv2](https://pypi.org/project/opencv-python/) 
- [dlib](http://dlib.net/)
- [os](https://docs.python.org/3/library/os.html)
- [numpy](https://www.numpy.org/)
- [sys](https://docs.python.org/2/library/sys.html)
- [smtplib](https://docs.python.org/3/library/smtplib.html)
- [pathlib](https://docs.python.org/3/library/pathlib.html)
- [sklearn](https://scikit-learn.org/stable/)
***

### Tech:
Multipurpose Facial Recognition System uses different open source projects to work properly:
* dlib.net - Excellent tool for detecting objects in images
* [Database of Faces AT&T Laboratories Cambridge](https://www.cl.cam.ac.uk/research/dtg/attarchive/facedatabase.html) - Database for better training
***

### Installation:

To begin, we must install OpenCV with all its dependencies:

```sh
$ pip install opencv-contrib-python
$ pip install numpy
$ pip install dlib
$ pip install os
$ pip install sys
$ pip install smtplib
$ pip install pathlib
```
***
### How to Use: 
**Step 1 : Training**
Go to the *src* folder, open and execute the file Entrenamiento by using:
```sh
$ python Entrenamiento.py
```
Enter the name of the person you want to recognize and press ENTER.
The training will be running taking around 300 photos, which will be stored in the *data* folder, for each photo, information about the descriptors is stored.
The descriptors are relationships of different parts of the face such as: the width and length of the eyes, the thickness of the lips, the dimensions of the nose among others.

**Step 2: Database check**

To make sure that the training was a success, we go to the *data* folder and open the name of the person you previously trained as a label.

To keep in mind:
- If in the captured images the person is clearly appreciated, the training will be a success.
- If not, delete the person's folder and do again the training.

**Important!!!**

Why should this step be done?
For different reasons:

- At the time of the training there were more than two people in front of the camera.
- The person at the time of the training could cover some place of the face "damaging" the taking of the descriptors already mentioned.
- At the beginning of the training the angle of the camera was not adequately accommodated and could have taken an image that is not of the face but of the throat, which sometimes its shape or structure resembles the face of a person.

**Step 3 Facial Recognition:**

In the src folder open and run the file Reconocimiento and enjoy the experience of this program by using:
```sh
$ python Reconocimiento.py
```
***
### Authors:
**Universidad de Ibagué** - **Ingeniería Electrónica**
**Inteligencia Artificial - Curso:2019/A**

 - [Harold F Murcia](http://haroldmurcia.com) - *Tutor*
 - Duvan Diaz Joven
 - Cristian Rene Gongora Torres
 - Santiago Reyes Barragan
***
