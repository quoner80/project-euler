# Arithmetic expressions
# Problem 93
#
# By using each of the digits from the set, {1, 2, 3, 4}, exactly once, and making use of the four arithmetic operations (+, -, *, /) and brackets/parentheses, it is possible to form different positive integer targets.
#
# For example,
#
#    8 = (4 * (1 + 3)) / 2
#   14 = 4 * (3 + 1 / 2)
#   19 = 4 * (2 + 3) - 1
#   36 = 3 * 4 * (2 + 1)
#
# Note that concatenations of the digits, like 12 + 34, are not allowed.
#
# Using the set, {1, 2, 3, 4}, it is possible to obtain thirty-one different target numbers of which 36 is the maximum, and each of the numbers 1 to 28 can be obtained before encountering the first non-expressible number.
#
# Find the set of four distinct digits, a < b < c < d, for which the longest set of consecutive positive integers, 1 to n, can be obtained, giving your answer as a string: abcd.

import time;

start_time = time.time();

def print_execution_time():
    print "Execution time = %f seconds." % (time.time() - start_time);

# Tests float and integer comparison.
# print 4 * (3 + 1 / 2.0) == 14;

ADD      = '+';
SUBTRACT = '-';
MULTIPLY = '*';
DIVIDE   = '/';

operators = [ADD, SUBTRACT, MULTIPLY, DIVIDE];

def get_permutations(array):
    permutations = [];
    length = len(array);
    if length == 1:
        permutations.append(array);
    else:
        for i in range(length):
            subarray = list(array);
            element = subarray[i];
            del subarray[i];
            subpermutations = get_permutations(subarray);
            for subpermutation in subpermutations:
                permutations.append([element] + subpermutation);
    return permutations;

def evaluate(x, operation, y):
    value = None;
    if x != None and y != None:
        if operation == ADD:
            value = float(x) + y;
        elif operation == SUBTRACT:
            value = float(x) - y;
        elif operation == MULTIPLY:
            value = float(x) * y;
        elif operation == DIVIDE:
            if y == 0:
                value = None;
            else:
                value = float(x) / y;
    return value;

# Returns number as an integer if it is an integral number (fractional part == 0); otherwise returns None.
def get_value_if_integral(number):
    value = None;
    if number != None and number == int(number):
        value = int(number);
    return value;

def get_consecutive_natural_number_count(values):
    natural_number = 1;
    while natural_number in values:
        natural_number += 1;
    return (natural_number - 1);

# Predicted number of iterations:
# 210 x 6 x 4 x 4 x 4 x P(4, 4) = 210 x 6 x 4 x 4 x 4 x 4! = 1,935,360.
iteration_count = 0;
max_consecutive_natural_number_count = 0;
argmax_base_sequences = [];
'''
# Replace the below with the following to run only base sequence 1234.
for A in range(1, 2):
    for B in range(A + 1, 3):
        for C in range(B + 1, 4):
            for D in range(C + 1, 5):
'''
for A in range(7):
    for B in range(A + 1, 8):
        for C in range(B + 1, 9):
            for D in range(C + 1, 10):
                # print A, B, C, D;
                values = set();
                permutations = get_permutations([A, B, C, D]);
                for permutation in permutations:
                    (a, b, c, d) = permutation;
                    # print (a, b, c, d);
                    for X in operators:
                        for Y in operators:
                            for Z in operators:
                                # print a, X, b, Y, c, Z, d;
                                #
                                # All possible positions of parentheses:
                                #   a X b Y c Z d
                                #   (a X b) Y c Z d
                                #   a X (b Y c) Z d
                                #   a X b Y (c Z d)
                                #   (a X b Y c) Z d
                                #   a X (b Y c Z d)
                                #   (a X b) Y (c Z d)
                                #   ((a X b) Y c) Z d
                                #   (a X (b Y c)) Z d
                                #   a X ((b Y c) Z d)
                                #   a X (b Y (c Z d))
                                # Which is interesting, but less relevant than the possible order of operators X, Y and Z (3! = 6
                                # permutations):
                                #   X, Y, Z
                                #   X, Z, Y
                                #   Y, X, Z
                                #   Y, Z, X
                                #   Z, X, Y
                                #   Z, Y, X
                                #
                                #   X, Y, Z
                                value = get_value_if_integral(evaluate(evaluate(evaluate(a, X, b), Y, c), Z, d));
                                values.add(value);
                                #
                                #   X, Z, Y
                                value = get_value_if_integral(evaluate(evaluate(a, X, b), Y, evaluate(c, Z, d)));
                                values.add(value);
                                #
                                #   Y, X, Z
                                value = get_value_if_integral(evaluate(evaluate(a, X, evaluate(b, Y, c)), Z, d));
                                values.add(value);
                                #
                                #   Y, Z, X
                                value = get_value_if_integral(evaluate(a, X, evaluate(evaluate(b, Y, c), Z, d)));
                                values.add(value);
                                #
                                #   Z, X, Y
                                value = get_value_if_integral(evaluate(evaluate(a, X, b), Y, evaluate(c, Z, d)));
                                values.add(value);
                                #
                                #   Z, Y, X
                                value = get_value_if_integral(evaluate(a, X, evaluate(b, Y, evaluate(c, Z, d))));
                                values.add(value);
                                iteration_count += 6;
                base_sequence = (A * 1000) + (B * 100) + (C * 10) + D;
                consecutive_natural_number_count = get_consecutive_natural_number_count(values);
                # print; print sorted(values);
                print "%04d : %d" % (base_sequence, consecutive_natural_number_count);
                if consecutive_natural_number_count > max_consecutive_natural_number_count:
                    max_consecutive_natural_number_count = consecutive_natural_number_count;
                    argmax_base_sequences = [base_sequence];
                elif consecutive_natural_number_count == max_consecutive_natural_number_count:
                    argmax_base_sequences.append(base_sequence);

print;
print "iteration_count = %d." % iteration_count;
print "max_consecutive_natural_number_count = %d." % max_consecutive_natural_number_count;
print "argmax_base_sequences = %s." % argmax_base_sequences;
print;

print_execution_time();
