clear all;
% Project a point from 3D to 2D using a matrix operation

%% Given: Point p in 3-space [x y z], and focal length f
%% Return: Location of projected point on 2D image plane [u v]
function p_img = project_point(p, f)
    %% TODO: Define and apply projection matrix
    point_4 = [p 1];
    disp(point_4);
    
    projection_matrix = zeros(3,4);
    projection_matrix (1,1) = 1;
    projection_matrix (2,2) = 1;
    projection_matrix (3,3) = 1/f;
	disp(projection_matrix);
    p_img = projection_matrix*transpose(point_4);
    %p_img = 0;
endfunction

function p_img = orthographic_projection(p,f)
		 point_4 = [p 1];
    disp(point_4);
    
    projection_matrix = [1 0 0 0, 0 1 0 0, 0 0 0 1];		
			
	disp(projection_matrix);
    p_img = projection_matrix*transpose(point_4);
	
endfunction

function p_img = weak_prespective(p,f)
	
endfunction

%% Test: Given point and focal length (units: mm)
p = [200 100 120];
f = 50;

disp(project_point(p, f));
