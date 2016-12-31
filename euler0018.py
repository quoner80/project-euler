# Maximum path sum I
#
# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.
#
#    3
#   7 4
#  2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
#
# Find the maximum total from top to bottom of the triangle below:
#
#               75
#              95 64
#             17 47 82
#            18 35 87 10
#           20 04 82 47 65
#          19 01 23 75 03 34
#         88 02 77 73 07 63 67
#        99 65 04 28 06 16 70 92
#       41 41 26 56 83 40 80 70 33
#      41 48 72 33 47 32 37 16 94 29
#     53 71 44 65 25 43 91 52 97 51 14
#    70 11 33 28 77 73 17 78 39 68 17 57
#   91 71 52 38 17 14 91 43 58 50 27 29 48
#  63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
#
# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

import math;

array = [
                             75,
                           95, 64,
                         17, 47, 82,
                       18, 35, 87, 10,
                     20,  4, 82, 47, 65,
                   19,  1, 23, 75,  3, 34,
                 88,  2, 77, 73,  7, 63, 67,
               99, 65,  4, 28,  6, 16, 70, 92,
             41, 41, 26, 56, 83, 40, 80, 70, 33,
           41, 48, 72, 33, 47, 32, 37, 16, 94, 29,
         53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14,
       70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57,
     91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48,
   63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31,
  4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23
];
'''
array = [
    3,
   7, 4,
  2, 4, 6,
 8, 5, 9, 3
];
'''

# Index i's left child index = i + 1 + triangular number of i's row = i + 1 + n.
# The formula for the n'th triangular number is:
#        n(n+1)
#    i = ------
#          2
# Solving for the positive n:
#    n^2 + n - 2i = 0
#        -1 + sqrt(1 - 4(* -2i))    sqrt(1 + 8i) - 1
#    n = ------------------------ = ----------------
#                   2                      2
# Plugging into the formula above:
#                                 sqrt(1 + 8i) - 1
#    i_left_child = i + 1 + floor[----------------]
#                                        2
def get_left_child_index(i):
    return int(i + 1 + math.floor(((math.sqrt(float(1 + (8 * i))) - 1) / 2)));

class Node:
    global array;
    global array_size;
    value = 0;
    left  = None;
    right = None;
    max_path_value = 0;
    def __init__(self, array_index):
        self.value = array[array_index];
        left_child_array_index = get_left_child_index(array_index);
        right_child_array_index = left_child_array_index + 1;
        left_path_value = 0;
        if left_child_array_index < array_size:
            self.left = Node(left_child_array_index);
            left_path_value = self.left.max_path_value;
        right_path_value = 0;
        if right_child_array_index < array_size:
            self.right = Node(right_child_array_index);
            right_path_value = self.right.max_path_value;
        self.max_path_value = self.value + max(left_path_value, right_path_value);

# print array;
array_size = len(array);
tree = Node(0);
'''
print tree;
node = tree;
while node != None:
    print node.value;
    node = node.left;
print tree;
node = tree;
while node != None:
    print node.value;
    node = node.right;
'''
print tree.max_path_value;
