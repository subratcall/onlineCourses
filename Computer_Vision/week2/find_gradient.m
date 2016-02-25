
clear all;
pkg load image;

% Gradient Direction
function result = select_gdir(gmag, gdir, mag_min, angle_low, angle_high)
    % TODO Find and return pixels that fall within the desired mag, angle range
	% gdir = (gdir + 180)/360.0;
	result = gmag >= mag_min & gdir >= angle_low & gdir <= angle_high;
endfunction

%% Load and convert image to double type, range [0, 1] for convenience
img = double(imread('octagon.png')) / 255.; 
figure(1);
imshow(img); % assumes [0, 1] range for double images

%% Compute x, y gradients
[gx gy] = imgradientxy(img, 'sobel'); % Note: gx, gy are not normalized

%% Obtain gradient magnitude and direction
[gmag gdir] = imgradient(gx, gy);
figure(2);
imshow(gmag / (4 * sqrt(2))); % mag = sqrt(gx^2 + gy^2), so [0, (4 * sqrt(2))]
figure(3);

imshow((gdir + 180.0) / 360.0); % angle in degrees [-180, 180]

%% Find pixels with desired gradient direction
my_grad = select_gdir(gmag, gdir, 1, 30, 60); % 45 +/- 15
figure(4);
imshow(my_grad);  
% NOTE: enable after you've implemented select_gdir

