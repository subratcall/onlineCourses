clear all;

function index = find_template_1D(t, s)
    % TODO: Locate template t in signal s and return index
    % NOTE: Turn off all output from inside the function before submitting!
	% zero padding
	zero_padding = 0;
	if (length(t) > 1)
		zero_padding = zeros(1,length(t) -1);
		
		disp('zero padding');
		disp(zero_padding);
		new_s = [s zero_padding];
	else
		new_s = [s];
	endif
	
	disp('new s');
	disp(new_s);
	
	correlation_result = zeros(size(s));
	%correlating
	for i=1:length(s)
		for j=1:length(t)
			correlation_result(i) += t(j) * new_s(i+j-1) ; 
		endfor
	endfor
	disp('correlation result');
	disp(correlation_result);
	[max max_index] = max(correlation_result);
	index = max_index;
endfunction

pkg load image; % AFTER function definition

% Test code:
s = [-1 0 0 1 1 1 0 -1 -1 0 1 0 0 -1];
t = [1 1 0];
disp('Signal:'), disp([1:size(s, 2); s]);
disp('Template:'), disp([1:size(t, 2); t]);

index = find_template_1D(t, s);
disp('Index:'), disp(index);
