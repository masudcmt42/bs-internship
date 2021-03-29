clc;
clear all;
%% read Image
im=imread('peppers.png');
%% preprocess
imR=imresize(im,[256,256]);
h=fspecial('gaussian',3);
imf=imfilter(imR,h);

%% ouso thresholding 
count=imhist(imf,16);
th=otsuthresh(count);
imt=im2bw(imf,th);
figure(1),imagesc(imt),colormap(gray);

%% Feture Extruction
im_seg=double(imt);
% cA = Approximation Coefficients
% cH = Horizontal Coefficients
% cV = vertical detail coefficients
% cD
[cA1,cH1,cV1,cD1] = dwt2(im_seg,'db4'); %Single-level discrete 2-D wavelet transform
[cA2,cH2,cV2,cD2] = dwt2(cA1,'db4');
[cA3,cH3,cV3,cD3] = dwt2(cA2,'db4');

dw_feat=[cA3,cH3,cV3,cD3];

%% principal component analysis - Fature Reduction
g=pca(dw_feat);
Mu=mean2(g);
sd=std2(g);
rm=mean2(rms(g));
var=mean2(var(g));
entr=entropy(g);



