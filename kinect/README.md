# Kinect
This repository includes some files to connect and acquire data from Microsoft Kinect sensors.

## Kinect V1
### Use:
* sudo apt-get install libfreenect-dev
* sudo apt-get install ros-kinetic-freenect-launch
* roslaunch freenect_launch freenect.launch
* ROStopic: /camera/depth/registered_points

## Kinect V2
### Use:
* Install: https://github.com/code-iai/iai_kinect2


## Save data
* Run: >> python capture_k1.py
* Data is saved in folder: ~/data/raw 
