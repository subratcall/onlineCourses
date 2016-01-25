import math

def polyArea(n,s):
	return n * s * s / (4 * math.tan(math.pi / n))

print polyArea(5,7)

print polyArea(7,3)

def project_to_distance(point_x, point_y, distance):
	dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)    
	scale = distance / dist_to_origin
	print point_x * scale, point_y * scale
    
project_to_distance(2, 7, 4)
