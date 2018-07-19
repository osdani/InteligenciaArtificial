#include <iostream>
#include <fstream>
#include <string>
#include <vector>

#include <ros/ros.h>
// PCL specific includes
#include <sensor_msgs/PointCloud2.h>
#include <pcl_conversions/pcl_conversions.h>
#include <pcl/point_cloud.h>
#include <pcl/point_types.h>
#include <pcl/filters/voxel_grid.h>
#include <pcl/visualization/cloud_viewer.h>


//Opencv Image

#include <opencv2/opencv.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <sensor_msgs/image_encodings.h>
#include <sensor_msgs/CameraInfo.h>
#include <sensor_msgs/Image.h>
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>


using namespace std;
ofstream myfile;

std::string first_arg;
std::string fileName;
ros::Publisher pub;


void cloud_cb (const sensor_msgs::PointCloud2ConstPtr& input){
  myfile.open(fileName.c_str());
  myfile << "%NODE\t" << "X\t" << "Y\t" << "Z\t" << "R\t" << "G\t" << "B\n";
  float x = 0, y = 0, z=0; // set x and y
  int R=0, G=0, B=0;
  pcl::PointCloud<pcl::PointXYZRGB> depth;
  pcl::fromROSMsg( *input, depth);
  int width = depth.width;
  int height = depth.height;
  int L = depth.points.size();

  for (size_t i =0; i < L; i++){
    x = depth.points[i].x;
    z = -depth.points[i].y;
    y = depth.points[i].z;
    R = depth.points[i].r;
    G = depth.points[i].g;
    B = depth.points[i].b;
    if (x==x){
      myfile << x << "\t" << y << "\t" << z << "\t" << R << "\t" << G << "\t" << B << "\n";
    }
    /*
    printf ( "x: %f\t",x );
    printf ( "y: %f\t",y );
    printf ( "z: %f\t",z );
    printf ( "R: %d\t",R );
    printf ( "G: %d\t",G );
    printf ( "B: %d\n",B );
    */
  }
  myfile.close();
  ros::shutdown();



  //sensor_msgs::PointCloud2 output;
  // Publish the map
  //output = *input;
  //pub.publish(output);
   // ---------------------------------
  // Perform the actual filtering
  //pcl::VoxelGrid<pcl::PCLPointCloud2> sor;
  //sor.setInputCloud (cloudPtr);
  //sor.setLeafSize (0.1, 0.1, 0.1);
  //sor.filter (cloud_filtered);

  // Convert to ROS data type
  //sensor_msgs::PointCloud2 output;
  //pcl_conversions::moveFromPCL(cloud_filtered, output);

  // Publish the data
  //pub.publish (output);
}

void imageCb(const sensor_msgs::ImageConstPtr& msg){
  cv_bridge::CvImagePtr cv_ptr;
  try{
    cv_ptr = cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::BGR8);

    stringstream ss;
    string name = fileName;
    string type = ".jpg";
    ss<<name<<type;
    string filename = ss.str();
    ss.str("");

    cv::imwrite(filename, cv_ptr->image);
  }
  catch (cv_bridge::Exception& e){
    ROS_ERROR("cv_bridge exception: %s", e.what());
    return;
  }
}

int main (int argc, char* argv[])
{
  // Initialize ROS
  ros::init (argc, argv, "k2_capture");

  if(!ros::ok())
  {
    return 0;
  }

  ros::NodeHandle nh;

  first_arg= argv[1];
  fileName = first_arg;
  printf("%s\n", fileName.c_str() );

  // Create a ROS subscriber for the input point cloud
  uint32_t queue_size = 1;
  image_transport::ImageTransport it(nh);
  image_transport::Subscriber sub = it.subscribe("/kinect2/qhd/image_color", queue_size, imageCb);
  //image_sub_ = it_.subscribe("/kinect2/qhd/image_color", 1, imageCb);
  ros::Subscriber sub1 = nh.subscribe<sensor_msgs::PointCloud2> ("/kinect2/qhd/points", queue_size, cloud_cb);
  //ros::Subscriber sub = nh.subscribe<sensor_msgs::PointCloud2> ("/camera/depth/points", queue_size, cloud_cb);

  // Create a ROS publisher for the output point cloud
  pub = nh.advertise<sensor_msgs::PointCloud2> ("output", 1);

  // Spin
  ros::spin();
  return 0;
}
