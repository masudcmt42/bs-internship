clc;
clear all;

im=imread('cameraman.tif');

imR=imresize(im,[256,256]);
%imgry = im2gray(imR);
gus=fspecial('gaussian',[3 3],1.5);
imf=imfilter(imR,gus);

count=imhist(imf,16);
th=otsuthresh(count);
imt=im2bw(imf,th);
figure(1),imagesc(imt),colormap(gray);
im_seg=double(imt);

[A1,H1,V1,D1] = dwt2(im_seg,'db4');
[A2,H2,V2,D2] = dwt2(A1,'db4');
[A3,H3,V3,D3] = dwt2(A2,'db4');
feat=[A3,H3,V3,D3];
frat_red=pca(feat);
Mu=mean2(frat_red);
sd=std2(frat_red);
rm=mean2(rms(frat_red));
var=mean2(var(frat_red));
entr=entropy(frat_red);
