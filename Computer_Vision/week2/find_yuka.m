clear all;
pkg load image; % AFTER function definition

function [yIndex xIndex] = find_template_2D(template, img)
    % TODO: Find template in img and return [y x] location
    % NOTE: Turn off all output from inside the function before submitting!
	c = normxcorr2(template,img);
	[maxValueY yMaxIndex]= max(c);
	[maxValueX xMaxIndex] = max(maxValueY);
	rawYIndex = yMaxIndex(xMaxIndex);
	rawXIndex = xMaxIndex;
	yIndex = rawYIndex - size(template,1) +1;
	xIndex = rawXIndex - size(template,2) +1;
endfunction

% Test code:
img = imread('perfume.jpg');
grey_img = rgb2gray(img);
imshow(img);

glyph = img(21:(21+70), 80:(80+86));
imshow(glyph);

[y x] = find_template_2D(glyph, grey_img);
disp([y x]); % should be the top-left corner of template in tablet
