clc;
clear all;
%% image read
peppers=imread('peppers.png');

%% display image
figure(1),imagesc(peppers),title("Display image with scaled colors");
figure(2),imshow(peppers),title("Display image");
%%RGB to Gray
imGry=rgb2gray(peppers);
figure(3),imshow(imGry),title("Gray Image");
%% preprossing - resize
rice= imread("rice.png");
figure(4),imshow(rice),title("Main");
reRice=imresize(rice,[128, 128]);
figure(5),imshow(reRice),title("resized");

%% filtering - fspecial
I=imread("football.jpg")
avg=fspecial('average',3); %Averaging filter fspecial('average',hsize)
fltr=imfilter(I,avg);
figure(6),imshow([I fltr]);

dsk=fspecial('disk',3); %disk filter fspecial('disk',radius) 
fltr=imfilter(I,dsk);
figure(7),imshow([I fltr]);

gus=fspecial('gaussian',[3 3],1.5); %gsussian filter ('gaussian',hsize,sigma)
fltr=imfilter(I,gus);
figure(8),imshow([I fltr]);

gus=fspecial('laplacian',1); %laplacian filter fspecial('laplacian',alpha) 
fltr=imfilter(I,gus);
figure(9),imshow([I fltr]);

gus=fspecial('log',8,.2); %log filter fspecial('log',hsize,sigma) 
fltr=imfilter(I,gus);
figure(10),imshow([I fltr]);

gus=fspecial('motion',8.5,0.3); %motion filter fspecial('motion',len,theta)
fltr=imfilter(I,gus);
figure(11),imshow([I fltr]);

gus=fspecial('prewitt'); %prewitt filter
fltr=imfilter(I,gus);
figure(12),imshow([I fltr]);

gus=fspecial('sobel'); %sobel filter
fltr=imfilter(I,gus);
figure(13),imshow([I fltr]);