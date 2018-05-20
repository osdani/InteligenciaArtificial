clear
bag = rosbag('your_file.bag');
bagselect1 = select(bag, 'Topic', '/kinect2/sd/points ')
msgs = readMessages(bagselect1, [1:14])

pcloud = msgs{1,1};
XYZ = readXYZ(pcloud) ;
X=XYZ(:,1);
Y=XYZ(:,2);
Z=XYZ(:,3);
rgb = readRGB(pcloud);
R=rgb(:,1);
G=rgb(:,2);
B=rgb(:,3);


L=length(X);
for k=1:L
    P=rotx(-90)*[X(k);Y(k);Z(k)];
    X(k) = P(1);
    Y(k) = P(2);
    Z(k) = P(3);
end

c=[R,G,B]; scatter3(X,Y,Z,1,c);
axis([-4 5 2 8 -6 2])
xlabel('X') ;
ylabel('Y') ;
zlabel('Z');