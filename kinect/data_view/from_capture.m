clear

%data = load('saves.txt');
data = load('save2.txt');
x = data(:,2);
y= data(:,3);
z= data(:,4);
r= data(:,5);
g=data(:,6);
b=data(:,7);

figure(1)
    plot3(x,y,z,'.')
    grid on
    grid on
    xlabel('x')
    ylabel('y')
    zlabel('z')

 figure(2)
    c=[r,g,b]/255; 
    scatter3(x,y,z,1,c) ;
    grid on
    grid on
    xlabel('x')
    ylabel('y')
    zlabel('z')
