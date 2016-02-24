clear all;
pkg load image;

img = imread('perfume.jpg');
%imgSize = size(img);
%sigma = 25;
%noise = randn(imgSize).*sigma;

%imgPlusNoise = img + noise;
%figure(1);
%imshow(imgPlusNoise);

%creating gaussian filter
%filterSize = 21;
%filterSigma = 3;
%filter = fspecial('gaussian', filterSize, filterSigma);
%smoothed = imfilter(imgPlusNoise, filter, 'symmetric');
%figure(2);
%imshow(smoothed);

imgPlusNoise = imnoise(img, 'salt & pepper', 0.02);
figure(1);
imshow(imgPlusNoise);

% apply median filter
medianFilteredImage = medfilt2(imgPlusNoise(:,:,1));
figure(2);
imshow(medianFilteredImage);
