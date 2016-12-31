# Convergents of e
#
# The square root of 2 can be written as an infinite continued fraction.
#
#                          1
#   sqrt(2) = 1 + -------------------
#                            1
#                 2 + ---------------
#                              1
#                     2 + -----------
#                                1
#                         2 + -------
#                             2 + ...
#
# The infinite continued fraction can be written, sqrt(2) = [1;(2)], (2) indicates that 2 repeats ad infinitum. In a similar way, sqrt(23) = [4;(1,3,1,8)].
#
# It turns out that the sequence of partial values of continued fractions for square roots provide the best rational approximations. Let us consider the convergents for sqrt(2).
#
#       1   3
#   1 + - = -
#       2   2
#
#         1     7
#   1 + ----- = -
#           1   5
#       2 + -
#           2
#
#           1       17
#   1 + --------- = --
#             1     12
#       2 + -----
#               1
#           2 + -
#               2
#
#             1         41
#   1 + ------------- = --
#               1       29
#       2 + ---------
#                 1
#           2 + -----
#                   1
#               2 + -
#                   2
#
# Hence the sequence of the first ten convergents for sqrt(2) are:
#   1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...
#
# What is most surprising is that the important mathematical constant,
#   e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].
#
# The first ten terms in the sequence of convergents for e are:
#   2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
#
# The sum of digits in the numerator of the 10th convergent is 1 + 4 + 5 + 7 = 17.
#
# Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.

import time;

start_time = time.time();

# e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...]:
def get_term(index):
    term = 1;
    if index == 0:
        term = 2;
    elif (index - 1) % 3 == 1:
        term = 2 * (1 + ((index - 1) / 3));
    return term;

#   2
#
#       1
#   2 + - = 3
#       1
#
#         1          1        2   8
#   2 + ----- = 2 + --- = 2 + - = -
#           1        3        3   3
#       1 + -        -
#           2        2
#
#           1              1            1          1        3   11
#   2 + --------- = 2 + ------- = 2 + ----- = 2 + --- = 2 + - = --
#             1              1            1        4        4   4
#       1 + -----       1 + ---       1 + -        -
#               1            3            3        3
#           2 + -            -
#               1            1
#
#             1                  1                1              1            1          1        5   19
#   2 + ------------- = 2 + ----------- = 2 + --------- = 2 + ------- = 2 + ----- = 2 + --- = 2 + - = --
#               1                  1                1              1            2        7        7   7
#       1 + ---------       1 + -------       1 + -----       1 + ---       1 + -        -
#                 1                  1                1            5            5        5
#           2 + -----           2 + ---           2 + -            -
#                   1                2                2            2
#               1 + -                -
#                   1                1

for convergent in range(2, 101):
    d = get_term(convergent - 1);
    w = get_term(convergent - 2);
    n = 1;
    n = n + (w * d);
    for index in range(convergent - 3, -1, -1):
        temp = d;
        d = n;
        n = temp;
        w = get_term(index);
        n = n + (w * d);
    numerator_sum = 0;
    for c in str(n):
        numerator_sum += int(c);
    # print convergent, n, d, float(n) / d;
    print "%03d: %d / %d %d" % (convergent, n, d, numerator_sum);

print;
print "Execution time = %f seconds." % (time.time() - start_time);
