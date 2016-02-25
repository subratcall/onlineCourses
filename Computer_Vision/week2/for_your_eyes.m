clear all;
% For Your Eyes Only
pkg load image;

frizzy = rgb2gray(imread('frizzy.png'));
froomer = rgb2gray(imread('froomer.png'));
imshow(frizzy);
imshow(froomer);

% TODO: Find edges in frizzy and froomer images

frizzy_edge = edge(frizzy,'canny');
froomer_edge = edge(froomer,'canny');
figure(1);
imshow(frizzy_edge);
figure(2);
imshow(froomer_edge);
% TODO: Display common edge pixels
common_edge = frizzy_edge & froomer_edge;

figure(3);
imshow(common_edge);
