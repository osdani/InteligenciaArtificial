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
* Remove sudo permissions: https://github.com/OpenKinect/libfreenect2/issues/79
* Create a ROS WS: http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment
* For RVIZ: roslaunch .... publish_tf:=true


## Save data
### Python
* Run: >> python capture_k1.py
* Data is saved in folder: ~/data/raw

### C++
* Install: my_pack (using catkin)
* After install run: rosrun my_pack k2_capture /{your_path}/{your_fileName}.txt

## view data in MATLAB
*  run files of "data_view" folder
