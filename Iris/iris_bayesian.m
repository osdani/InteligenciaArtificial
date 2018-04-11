
clear,clc,close all
load fisheriris.mat

sepalL=meas(:,1);
sepalW=meas(:,2);
petalL=meas(:,3);
petalW=meas(:,4);

plot(sepalL)
grid on
hold on
plot(sepalW,'r')
plot(petalL,'g')
plot(petalW,'k')
legend('sepalL','sepalW','petalL','petalW')

figure(2)
subplot(411)
mu_1=mean(sepalL(1:50));
mu_2=mean(sepalL(51:100));
mu_3=mean(sepalL(101:end));
sigma1=std(sepalL(1:50));
sigma2=std(sepalL(51:100));
sigma3=std(sepalL(101:end));
Y1 = normpdf(sepalL(1:50),mu_1,sigma1);
Y2 = normpdf(sepalL(51:100),mu_2,sigma2);
Y3 = normpdf(sepalL(101:end),mu_3,sigma3);
stem(sepalL(1:50),Y1)
hold on
stem(sepalL(51:100),Y2)
stem(sepalL(101:end),Y3)
ylabel('Sepal Lenght')
legend('Setosa','VersiColor','Virginica')
grid on

disp('Matriz de Covarianza 1: ')
M1=[sepalL(1:50),sepalL(51:100),sepalL(101:end)];
cov(M1)

subplot(412)
mu_1=mean(sepalW(1:50));
mu_2=mean(sepalW(51:100));
mu_3=mean(sepalW(101:end));
sigma1=std(sepalW(1:50));
sigma2=std(sepalW(51:100));
sigma3=std(sepalW(101:end));
Y1 = normpdf(sepalW(1:50),mu_1,sigma1);
Y2 = normpdf(sepalW(51:100),mu_2,sigma2);
Y3 = normpdf(sepalW(101:end),mu_3,sigma3);
stem(sepalW(1:50),Y1)
hold on
stem(sepalW(51:100),Y2)
stem(sepalW(101:end),Y3)
ylabel('Sepal W')
legend('Setosa','VersiColor','Virginica')
grid on
disp('Matriz de Covarianza 2: ')
M2=[sepalW(1:50),sepalW(51:100),sepalW(101:end)];
cov(M2)

subplot(413)
mu_pLSet=mean(petalL(1:50));
mu_pLVer=mean(petalL(51:100));
mu_pLVir=mean(petalL(101:end));
sigma_pLSet=std(petalL(1:50));
sigma_pLVer=std(petalL(51:100));
sigma_pLVir=std(petalL(101:end));
Y1 = normpdf(petalL(1:50),mu_pLSet,sigma_pLSet);
Y2 = normpdf(petalL(51:100),mu_pLVer,sigma_pLVer);
Y3 = normpdf(petalL(101:end),mu_pLVir,sigma_pLVir);
stem(petalL(1:50),Y1)
hold on
stem(petalL(51:100),Y2)
stem(petalL(101:end),Y3)
ylabel('Petal Lenght')
legend('Setosa','VersiColor','Virginica')
grid on

disp('Matriz de Covarianza 3: ')
M3=[petalL(1:50),petalL(51:100),petalL(101:end)];
cov(M3)

subplot(414)

mu_pWSet=mean(petalW(1:50));
mu_pWVer=mean(petalW(51:100));
mu_pWVir=mean(petalW(101:end));
sigma_pWSet=std(petalW(1:50));
sigma_pWVer=std(petalW(51:100));
sigma_pWVir=std(petalW(101:end));
Y1 = normpdf(petalW(1:50),mu_pWSet,sigma_pWSet);
Y2 = normpdf(petalW(51:100),mu_pWVer,sigma_pWVer);
Y3 = normpdf(petalW(101:end),mu_pWVir,sigma_pWVir);
stem(petalW(1:50),Y1)
hold on
stem(petalW(51:100),Y2)
stem(petalW(101:end),Y3)
ylabel('Petal W')
legend('Setosa','VersiColor','Virginica')
grid on
disp('Matriz de Covarianza 4: ')
M4=[petalW(1:50),petalW(51:100),petalW(101:end)];
cov(M4)


figure(3)
plot3(sepalL(1:50),petalL(1:50),petalW(1:50),'ro')
hold on
plot3(sepalL(51:100),petalL(51:100),petalW(51:100),'g*')
plot3(sepalL(101:end),petalL(101:end),petalW(101:end),'bo')
grid on
xlabel('sepalL')
ylabel('petalL')
zlabel('petalW')
legend('Setosa','Versicolor','Virginica')


%% Clasificador Bayesiano
% https://es.wikipedia.org/wiki/Clasificador_bayesiano_ingenuo

PSetosa=50/150;
PVersicolor=50/150;
PVirginica=50/150;

PL=meas(:,3);
PW=meas(:,4);


for(k=1:length(PL)) % 100 of data
    
    lTest=PL(k);
    wTest=PW(k);

    PpetalLSetosa=    1/sqrt(2*pi*sigma_pLSet^2)*exp(-(lTest-mu_pLSet)^2/(2*sigma_pLSet^2));
    PpetalLVersicolor=1/sqrt(2*pi*sigma_pLVer^2)*exp(-(lTest-mu_pLVer)^2/(2*sigma_pLVer^2));
    PpetalLVirginica= 1/sqrt(2*pi*sigma_pLVir^2)*exp(-(lTest-mu_pLVir)^2/(2*sigma_pLVir^2));

    PpetalWSetosa=    1/sqrt(2*pi*sigma_pWSet^2)*exp(-(wTest-mu_pWSet)^2/(2*sigma_pWSet^2));
    PpetalWVersicolor=1/sqrt(2*pi*sigma_pWVer^2)*exp(-(wTest-mu_pWVer)^2/(2*sigma_pWVer^2));
    PpetalWVirginica= 1/sqrt(2*pi*sigma_pWVir^2)*exp(-(wTest-mu_pWVir)^2/(2*sigma_pWVir^2));

    evidencia=PSetosa*PpetalLSetosa*PpetalWSetosa + ...
        PVersicolor*PpetalLVersicolor*PpetalWVersicolor + ...
        PVirginica*PpetalLVirginica*PpetalWVirginica;

    postSetosa=    PSetosa*PpetalLSetosa*PpetalWSetosa/evidencia
    postVersicolor=PVersicolor*PpetalLVersicolor*PpetalWVersicolor/evidencia
    postVirginica= PVirginica*PpetalLVirginica*PpetalWVirginica/evidencia
    
    % Predicci?n
    POS=[postSetosa,postVersicolor,postVirginica];
    if(max(POS)==postSetosa)
        pred(k)=1;
    elseif(max(POS)==postVersicolor)
        pred(k)=2;
    else
        pred(k)=3;
    end
end
