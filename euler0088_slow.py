# Product-sum numbers
# Problem 88
#
# A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers, {a1, a2, ... , ak} is called a product-sum number: N = a_1 + a_2 + ... + a_k = a_1 x a_2 x ... x a_k.
#
# For example, 6 = 1 + 2 + 3 = 1 x 2 x 3.
#
# For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number. The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.
#   k = 2:  4 = 2 x 2 = 2 + 2
#   k = 3:  6 = 1 x 2 x 3 = 1 + 2 + 3
#   k = 4:  8 = 1 x 1 x 2 x 4 = 1 + 1 + 2 + 4
#   k = 5:  8 = 1 x 1 x 2 x 2 x 2 = 1 + 1 + 2 + 2 + 2
#   k = 6: 12 = 1 x 1 x 1 x 1 x 2 x 6 = 1 + 1 + 1 + 1 + 2 + 6
#
# Hence for 2 <= k <= 6, the sum of all the minimal product-sum numbers is 4 + 6 + 8 + 12 = 30; note that 8 is only counted once in the sum.
#
# In fact, as the complete set of minimal product-sum numbers for 2 <= k <= 12 is {4, 6, 8, 12, 15, 16}, the sum is 61.
#
# What is the sum of all the minimal product-sum numbers for 2 <= k <= 12000?

import numpy;
import math;
import time;
import sys;

start_time = time.time();

def print_execution_time():
    print "Execution time = %f seconds." % (time.time() - start_time);

def get_next_size_arrays(current_arrays, summation):
    arrays = list();
    for current_array in current_arrays:
        length = len(current_array);
        array = list(current_array);
        array[length - 1] += 1;
        if not (array in arrays):
            arrays.append(array);
            product = numpy.prod(array);
            print "%d %s %d" % (summation, array, product);
            if product == summation:
                print array;
                sys.exit("found it!");
        array = list(current_array);
        for i in range(length - 2, -1, -1):
            if array[i] < array[i + 1]:
                array[i] += 1;
                if not (array in arrays):
                    arrays.append(array);
                    product = numpy.prod(array);
                    print "%d %s %d" % (summation, array, product);
                    if product == summation:
                        print array;
                        sys.exit("found it!");
                array = list(current_array);
    return arrays;

N = 10000;
unknown_count = 1 + int(math.log(N, 2));
ones_count = N - unknown_count;
print("%d %d %d" % (N, unknown_count, ones_count));
current_arrays = [[1] * unknown_count];
print len(current_arrays), current_arrays;
summation = N;
while (True):
    summation += 1;
    current_arrays = get_next_size_arrays(current_arrays, summation);
    #print len(current_arrays), current_arrays;

'''
111 3

112 4

113 5
122 5

114 6
123 6
222 6

115 7
124 7
133 7
223 7

116 8
125 8
134 8
224 8
235 8

117 9
126 9
135 9
144 9
225 9
234 9
333 9

118 10
127 10
136 10
145 10
226 10
235 10
244 10
334 10

119 11
128 11
137 11
146 11
155 11

129 12
138 12
147 12
156 12
'''

print_execution_time();
