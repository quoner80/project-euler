# Magic 5-gon ring
#
# Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.
#
#     4
#      \
#       3
#      / \
#     1---2---6
#    /
#   5
#
# Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example), each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.
#
# It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.
#
#   Total       Solution Set
#     9     4,2,3; 5,3,1; 6,1,2
#     9     4,3,2; 6,2,1; 5,1,3
#     10    2,3,5; 4,5,1; 6,1,3
#     10    2,5,3; 6,3,1; 4,1,5
#     11    1,4,6; 3,6,2; 5,2,4
#     11    1,6,4; 5,4,2; 3,2,6
#     12    1,5,6; 2,6,4; 3,4,5
#     12    1,6,5; 3,5,4; 2,4,6
#
# By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.
#
# Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings. What is the maximum 16-digit string for a "magic" 5-gon ring?
#
#       O
#         +
#           O     O
#         +   +  /
#       O       O
#     +  \     /
#   O     O---O----O
#          \
#           O

import time;

start_time = time.time();

# Returns a copy of "array" with the elements left-rotated by "count" positions.
# For example left_rotate([a, b, c, d, e], 2) returns [c, d, e, a, b].
def left_rotate(array, count):
    length = len(array);
    left_rotated_array = [None] * length;
    for i in range(length):
        left_rotated_array[(i - count) % length] = array[i];
    return left_rotated_array;

# Returns the permutations of the "count" chars in each string in "strings".
def get_permutations(strings, count):
    permutations = [];
    for string in strings:
        if count <= 1:
            for char in string:
                permutations.append(char);
        else:
            for c in range(len(string)):
                char = string[c];
                stringlet = string[:c] + string[(c + 1):];
                stringlet_permutations = get_permutations([stringlet], count - 1);
                for p in range(len(stringlet_permutations)):
                    permutations.append(char + stringlet_permutations[p]);
    return permutations;

# Index the positions in the 5-gon structure in array p[] as follows:
#
#      [0]
#         +
#          [5]   [1]
#         +   +  /
#      [9]     [6]
#     +  \     /
#  [4]   [8]-[7]--[2]
#          \
#          [3]
#
# p[0] + p[5] + p[6] must equal
# p[1] + p[6] + p[7] must equal
# p[2] + p[7] + p[8] must equal
# p[3] + p[8] + p[9] must equal
# p[4] + p[9] + p[5]
N = 1234567890;
S = str(N);
length = len(S);
permutations = get_permutations([S], length);
concatenations = [];
for permutation in permutations:
    # Set N to 1356789 and uncomment the following to run a toy subset of the possible permutations.
    # permutation = "024" + permutation;
    p = [0] * 10;
    indexOf0 = -1;
    for i in range(10):
        p[i] = int(permutation[i]);
        if p[i] == 0:
            indexOf0 = i;
            p[i] = 10;
    # If the 10 is internal (indices 5 through 9), skip it since this algorithm should consider only 16-digit magic strings.
    if indexOf0 >= 5:
        continue;
    s = p[0] + p[5] + p[6];
    if s == p[1] + p[6] + p[7] and s == p[2] + p[7] + p[8] and s == p[3] + p[8] + p[9] and s == p[4] + p[9] + p[5]:
        print "%d,%d,%d; %d,%d,%d; %d,%d,%d; %d,%d,%d; %d,%d,%d [%d]" % (p[0],p[5],p[6], p[1],p[6], p[7],p[2],p[7], p[8],p[3],p[8], p[9],p[4],p[9],p[5], s);
        c0 = int(str(p[0]) + str(p[5]) + str(p[6]));
        c1 = int(str(p[1]) + str(p[6]) + str(p[7]));
        c2 = int(str(p[2]) + str(p[7]) + str(p[8]));
        c3 = int(str(p[3]) + str(p[8]) + str(p[9]));
        c4 = int(str(p[4]) + str(p[9]) + str(p[5]));
        solution_unrotated = ([c0, c1, c2, c3, c4]);
        solution = left_rotate(solution_unrotated, solution_unrotated.index(min(solution_unrotated)));
        concatenation = "";
        for s in solution:
            concatenation += str(s);
        if not concatenation in concatenations:
            concatenations.append(concatenation);
concatenations = sorted(concatenations);
print concatenations;
print;
print "maximum concatenation = %d." % int(concatenations[-1]);
print;
print "Execution time = %f seconds." % (time.time() - start_time);
