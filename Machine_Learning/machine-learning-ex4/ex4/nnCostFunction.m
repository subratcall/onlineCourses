function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%neural network which performs classification
%   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) computes the cost and gradient of the neural network. The
%   parameters for the neural network are "unrolled" into the vector
%   nn_params and need to be converted back into the weight matrices. 
% 
%   The returned parameter grad should be a "unrolled" vector of the
%   partial derivatives of the neural network.
%

% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

% Setup some useful variables
m = size(X, 1);
         
% You need to return the following variables correctly 
J = 0;
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));

% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the code by working through the
%               following parts.
%
% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m
%
% Part 2: Implement the backpropagation algorithm to compute the gradients
%         Theta1_grad and Theta2_grad. You should return the partial derivatives of
%         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
%         Theta2_grad, respectively. After implementing Part 2, you can check
%         that your implementation is correct by running checkNNGradients
%
%         Note: The vector y passed into the function is a vector of labels
%               containing values from 1..K. You need to map this vector into a 
%               binary vector of 1's and 0's to be used with the neural network
%               cost function.
%
%         Hint: We recommend implementing backpropagation using a for-loop
%               over the training examples if you are implementing it for the 
%               first time.
%
% Part 3: Implement regularization with the cost function and gradients.
%
%         Hint: You can implement this around the code for
%               backpropagation. That is, you can compute the gradients for
%               the regularization separately and then add them to Theta1_grad
%               and Theta2_grad from Part 2.
%

a1 = [ones(m,1),X];
z2 = a1*transpose(Theta1);
a2 = [ones(size(z2,1),1),sigmoid(z2)];
z3 = a2*transpose(Theta2);
hTheta = sigmoid(z3);

extY = zeros(size(hTheta));

for i = 1:size(y,1)
  index = y(i);
  extY(i, index) = 1;
endfor

insideBracket = -extY.*log(hTheta) - (1-extY).*log(1-hTheta);
J = sum(sum(insideBracket))/m;

theta1Sqr = Theta1(:,2:end).*Theta1(:,2:end);
theta2Sqr = Theta2(:,2:end).*Theta2(:,2:end);

J += lambda*(sum(sum(theta1Sqr))+sum(sum(theta2Sqr)))/(2*m);


% -------------------------------------------------------------

delta3 = transpose(hTheta - extY);

delta2 = (transpose(Theta2)*delta3) .* transpose(a2 .* (1-a2));
delta2 = delta2(2:end,:);

bigD2 = delta3*a2;
bigD1 = delta2*a1;

Theta2_grad = bigD2/m;
Theta1_grad = bigD1/m;

regTheta1 = lambda * Theta1 / m;
regTheta2 = lambda * Theta2 / m;

regTheta1(:,1) = zeros(size(regTheta1(1),1));
regTheta2(:,1) = zeros(size(regTheta2(1),1));

Theta1_grad += regTheta1;
Theta2_grad += regTheta2;

% =========================================================================

% Unroll gradients
grad = [Theta1_grad(:) ; Theta2_grad(:)];


end
