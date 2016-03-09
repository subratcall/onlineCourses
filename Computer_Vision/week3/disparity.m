% TODO: Match two strips to compute disparity values
clear all;
pkg load image;
% Find best match for a patch in a given strip (SSD)
% Note: You may use this or roll your own
function best_x = find_best_match(patch, strip)
    min_diff = Inf;
    best_x = 0; % column index (x value) of topleft corner; haven't found it yet
    for x = 1:(size(strip)(2) - size(patch)(2))
        other_patch = strip(:, x:(x + size(patch)(2) - 1));
        diff = sumsq((patch - other_patch)(:));
        if diff < min_diff
            min_diff = diff;
            best_x = x;
        endif
    endfor
endfunction


function disparity = match_strips(strip_left, strip_right, b)

	strip_left_width = size(strip_left)(1);
    strip_left_length = size(strip_left)(2);
    
    strip_right_width = size(strip_right)(1);
    strip_right_length = size(strip_right)(2);
    
    num_of_patch = floor(strip_right_length / b);
    %disp(num_of_patch);
    x = 1;
    for i=1:num_of_patch
		%disp(x);
		temp_patch = strip_left(:, x:x + (b -1));
		disparity(i) = x - find_best_match(temp_patch, strip_right);
		x += b;
    endfor
    
    % For each non-overlapping patch/block of width b in the left strip,
    %   find the best matching position (along X-axis) in the right strip.
    % Return a vector of disparities (left X-position - right X-position).
    % Note: Only consider whole blocks that fit within image bounds.
endfunction


% Test code:

%% Load images
left = imread('flowers-left.png');
right = imread('flowers-right.png');
figure, imshow(left);
figure, imshow(right);

%% Convert to grayscale, double, [0, 1] range for easier computation
left_gray = double(rgb2gray(left)) / 255.0;
right_gray = double(rgb2gray(right)) / 255.0;

%% Define strip row (y) and square block size (b)
y = 120;
b = 100;

%% Extract strip from left image
strip_left = left_gray(y:(y + b - 1), :);
figure, imshow(strip_left);

%% Extract strip from right image
strip_right = right_gray(y:(y + b - 1), :);
figure, imshow(strip_right);

%% Now match these two strips to compute disparity values
disparity = match_strips(strip_left, strip_right, b);
disp(disparity);
figure, plot(disparity);
