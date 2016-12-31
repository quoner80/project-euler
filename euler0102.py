# Triangle containment
# Problem 102
#
# Three distinct points are plotted at random on a Cartesian plane, for which -1000 <= x, y <= 1000, such that a triangle is formed.
#
# Consider the following two triangles:
#   A(-340, 495), B(-153, -910), C(835, -947)
#   X(-175,  41), Y(-421, -714), Z(574, -645)
#
# It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.
#
# Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of one thousand "random" triangles, find the number of triangles for which the interior contains the origin.
#
# NOTE: The first two examples in the file represent the triangles in the example given above.

import cmath;
import csv;
import math;
import time;
import sys;

start_time = time.time();

FILENAME = "p102_triangles.txt";
CHAR_THETA = unichr(0x03b8);

class Point:
    x = None;
    y = None;
    r = None;
    theta = None;
    def __init__(self, x, y):
        self.x = int(x);
        self.y = int(y);
        (self.r, self.theta) = cmath.polar(complex(self.x, self.y));
        # Convert range from [-pi, pi) to [0.0, 360.0), i.e. radians to degrees.
        if self.theta < 0.0:
            self.theta += (2 * math.pi);
        self.theta = math.degrees(self.theta);
    def __str__(self):
        return "(r = %f, %c = %f)" % (self.r, CHAR_THETA, self.theta);
    def __repr__(self):
        return  str(self);
    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y);
    def __ne__(self, other):
        return not __eq__(self, other);

class Rectangle:
    top_left = None;
    right_bottom = None;
    def __init__(self, top, left, right, bottom):
        self.top_left = Point(left, top);
        self.bottom_right = Point(right, bottom);
    def __str__(self):
        return "%s, %s" % (self.top_left, self.right_bottom);
    def __repr__(self):
        return  str(self);

# If the largest angle between any 2 points is less than 180 degrees, the origin is not encompassed by the triangle:
#
#                 p_0
#             |   .     . p_1
#             |  .   .
#             | . .
#             |.  
#   ----------+----------   p_0 to p_2 < 180
#             | .
#             |   .
#             |     .
#             |       . p_2
#
# If the largest angle between any 2 points is greater than or equal to 180 degrees, the origin is encompassed by the triangle:
#
#                 p_0
#             |   .     . p_1
#             |  .   .
#             | . .
#             |.  
#   ----------+----------   p_1 to p_2 > 180
#           . |
#         .   |
#       .     |
#     .       |
#    p_2
#
class Triangle:
    p_0 = None;
    p_1 = None;
    p_2 = None;
    #bounding_rectangle = None;
    contains_origin = None;
    def __init__(self, p_0, p_1, p_2):
        self.p_0 = p_0;
        self.p_1 = p_1;
        self.p_2 = p_2;
        #self.bounding_rectangle = Rectangle(self.get_left_point(), self.get_left_point(), self.get_left_point(), self.get_left_point());
        (angle_a_base_0, angle_b_base_0) = get_angles_from_to_and_to(p_0, p_1, p_2);
        (angle_a_base_1, angle_b_base_1) = get_angles_from_to_and_to(p_1, p_0, p_2);
        (angle_a_base_2, angle_b_base_2) = get_angles_from_to_and_to(p_2, p_0, p_1);
        minimal_angle_sum = min(angle_a_base_0 + angle_b_base_0, angle_a_base_1 + angle_b_base_1, angle_a_base_2 + angle_b_base_2);
        if minimal_angle_sum < 180.0:
            self.contains_origin = False;
        else:
            self.contains_origin = True;
    def __str__(self):
        return "%s, %s, %s" % (self.p_0, self.p_1, self.p_2);
    def __repr__(self):
        return  str(self);
    def left_point(self):
        return Point(0, 0);

def print_execution_time():
    print "Execution time = %f seconds." % (time.time() - start_time);

def get_angle_from_to(theta_start, theta_end):
    angle = theta_end - theta_start;
    if angle < 0.0:
        angle += 360.0;
    return angle;

def get_angles_from_to_and_to(p_base, p_0, p_1):
    angle_to_0 = None;
    angle_to_1 = None;
    theta_base = p_base.theta;
    theta_0 = p_0.theta;
    theta_1 = p_1.theta;
    angle_to_0_possibility_a = get_angle_from_to(theta_base, theta_0);
    angle_to_1_possibility_a = get_angle_from_to(theta_1, theta_base);
    angle_to_1_possibility_b = get_angle_from_to(theta_base, theta_1);
    angle_to_0_possibility_b = get_angle_from_to(theta_0, theta_base);
    if angle_to_0_possibility_a + angle_to_1_possibility_a < angle_to_0_possibility_b + angle_to_1_possibility_b:
        angle_to_0 = angle_to_0_possibility_a;
        angle_to_1 = angle_to_1_possibility_a;
    else:
        angle_to_0 = angle_to_0_possibility_b;
        angle_to_1 = angle_to_1_possibility_b;
    return (angle_to_0, angle_to_1);

def get_left_point(triangle):
    point = None;
    if triangle.p_0.x < triangle.p_1.x:
        if triangle.p_0.x < triangle.p_2.x:
            point = triangle.p_0;
        else:
            point = triangle.p_2;
    else:
        if triangle.p_1.x < triangle.p_2.x:
            point = triangle.p_1;
        else:
            point = triangle.p_2;
    return point;

def get_right_point(triangle):
    point = None;
    if triangle.p_0.x > triangle.p_1.x:
        if triangle.p_0.x > triangle.p_2.x:
            point = triangle.p_0;
        else:
            point = triangle.p_2;
    else:
        if triangle.p_1.x > triangle.p_2.x:
            point = triangle.p_1;
        else:
            point = triangle.p_2;
    return point;

def get_bottom_point(triangle):
    point = None;
    if triangle.p_0.y < triangle.p_1.y:
        if triangle.p_0.y < triangle.p_2.y:
            point = triangle.p_0;
        else:
            point = triangle.p_2;
    else:
        if triangle.p_1.y < triangle.p_2.y:
            point = triangle.p_1;
        else:
            point = triangle.p_2;
    return point;

def get_top_point(triangle):
    point = None;
    if triangle.p_0.y > triangle.p_1.y:
        if triangle.p_0.y > triangle.p_2.y:
            point = triangle.p_0;
        else:
            point = triangle.p_2;
    else:
        if triangle.p_1.y > triangle.p_2.y:
            point = triangle.p_1;
        else:
            point = triangle.p_2;
    return point;

origin_encompassing_triangle_count = 0;
triangles = [];

with open(FILENAME) as triangle_file:
    triangle_reader = csv.reader(triangle_file);
    for triangle_list in triangle_reader:
        p_0 = Point(triangle_list[0], triangle_list[1]);
        p_1 = Point(triangle_list[2], triangle_list[3]);
        p_2 = Point(triangle_list[4], triangle_list[5]);
        triangles.append(Triangle(p_0, p_1, p_2));
        '''
        if len(triangles) >= 8:
            break;
        '''

for triangle in triangles:
    slope_0_1 = None;
    slope_1_2 = None;
    slope_0_2 = None;
    if triangle.p_0.y != triangle.p_1.y:
        slope_0_1 = (float(triangle.p_0.x - triangle.p_1.x)) / float(triangle.p_0.y - triangle.p_1.y);
    if triangle.p_1.y != triangle.p_2.y:
        slope_1_2 = (float(triangle.p_1.x - triangle.p_2.x)) / float(triangle.p_1.y - triangle.p_2.y);
    if triangle.p_0.y != triangle.p_2.y:
        slope_0_2 = (float(triangle.p_0.x - triangle.p_2.x)) / float(triangle.p_0.y - triangle.p_2.y);
    '''
    # Checks whether there are any trianlges with two or more of the same point (there are none in FILENAME).
    if (triangle.p_0 == triangle.p_1) or (triangle.p_0 == triangle.p_2) or (triangle.p_1 == triangle.p_2):
        print triangle;
    # Checks whether there are any trianlges with a vertical side (there are three in FILENAME).
    if (triangle.p_0.x == triangle.p_1.x) or (triangle.p_0.x == triangle.p_2.x) or (triangle.p_1.x == triangle.p_2.x):
        print triangle;
    # Checks whether there are any trianlges with a horizontal side (there are two in FILENAME).
    if (triangle.p_0.y == triangle.p_1.y) or (triangle.p_0.y == triangle.p_2.y) or (triangle.p_1.y == triangle.p_2.y):
        print triangle;
    # Checks whether there are any sets of three collinear lines (there are none in FILENAME).
    if slope_0_1 == slope_0_2:
        print triangle;
    '''
    #print triangle, get_left_point(triangle), get_right_point(triangle);
    #print triangle, get_top_point(triangle), get_bottom_point(triangle);
    if not (int(triangle.p_0.theta) in range(0, 360) and int(triangle.p_1.theta) in range(0, 360) and int(triangle.p_2.theta) in range(0, 360)):
        sys.exit("malformed triangle: %s" % triangle);
    print "%c_0 = %03.6f, %c_1 = %03.6f, %c_2 = %03.6f -> %s" % (CHAR_THETA, triangle.p_0.theta, CHAR_THETA, triangle.p_1.theta, CHAR_THETA, triangle.p_2.theta, triangle.contains_origin);
    if triangle.contains_origin:
        origin_encompassing_triangle_count += 1;

print;
print "%d triangles encompass the origin." % origin_encompassing_triangle_count;
print;
print_execution_time();
