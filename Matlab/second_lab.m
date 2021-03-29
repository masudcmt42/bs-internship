clc;
clear all;
%read an Image
im=imread('cameraman.tif');
%% preprocessing
imR=imresize(im,[226,256]);
gus=fspecial('gaussian',3); %gsussian filter ('gaussian',hsize,sigma)
imf=imfilter(imR,gus,'conv','same');
figure(1),imagesc(imf);

%% Binary Segmantation
thr=0.4;
bw=im2bw(imf,thr);
figure(2),imagesc(bw),colormap(gray);
% thrasulding with mean
mu=mean(im(:))/256;
bw=im2bw(imf,mu);
figure(3),imagesc(bw),colormap(gray);
%% otsu thesholding segmentation
level = graythresh(imf); %Convert Intensity Image to Binary Image Using Level Threshold
bw=im2bw(imf,level);
figure(4),imagesc(bw),colormap(gray);

% Global histogram threshold using Otsu's method
counts = imhist(imf,16); % Calculate a 16-bin histogram for the image. 
T=otsuthresh(counts);
imOts=im2bw(imf,T);
figure(5),imagesc(bw),colormap(gray);
%% iteretive segmentation
I1=imf>.4;
I2=imf<.4;
mu=(mean(I1(:))+mean(I2(:)))/2;
for x=1:100
    I1=(imf>mu).*double(imf);
    I2=(imf<=mu).*double(imf);
    mu=(mean(I1(:))/256+mean(I2(:))/256)/2;
end
imit=im2bw(imf,mu);
figure(6),imagesc(imit),colormap(gray);