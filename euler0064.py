# Odd period square roots
#
# All square roots are periodic when written as continued fractions and can be written in the form:
#                          1
#   sqrt(N) = a0 + ------------------
#                             1
#                  a1 + -------------
#                               1
#                       a2 + --------
#                            a3 + ...
# Or:
#   sqrt(N) = a0 + 1 / (a1 + 1 / (a2 + 1 / (a3 + ...) ) )
#
# For example, let us consider sqrt(23):
#                                          1                            1                           1                  1
#   sqrt(23) = 4 + sqrt(23) - 4 = 4 + ------------ = 4 + ------------------------------- = 4 + ------------ = 4 + ------------
#                                          1                      sqrt(23) + 4                 sqrt(23) + 4       sqrt(23) + 4
#                                     ------------       -------------------------------       ------------       ------------
#                                     sqrt(23) - 4       (sqrt(23) - 4) * (sqrt(23) + 4)         23 - 4^2              7
#
#                           1                        1
#            = 4 + -------------------- = 4 + ----------------
#                  7 + sqrt(23) + 4 - 7           sqrt(23) - 3
#                  --------------------       1 + ------------
#                           7                         7
# Or:
#   sqrt(23) = 4 + sqrt(23) - 4 = 4 + (1 / (1 / sqrt(23) ) ) - 4 = ... = 4 + 1 / (1 + ( (sqrt(23) - 3) / 7 ) )
#
# If we continue we would get the following expansion:
#
#                         1
#   sqrt(23) = 4 + -------------------
#                               1
#                    1 + ---------------
#                                 1
#                        3 + -----------
#                                   1
#                            1 + -------
#                                8 + ...
#
# The process can be summarised as follows:
#
#                1         sqrt(23) + 4       sqrt(23) - 3
#   a0 = 4, ------------ = ------------ = 1 + ------------ (1 is the whole number part because 1 < (sqrt(23) + 4) / 7 < 2)
#           sqrt(23) - 4        7                  7
#
#                7         7 * (sqrt(23) + 3)   sqrt(23) + 3       sqrt(23) - 3
#   a1 = 1, ------------ = ------------------ = ------------ = 3 + ------------ (3 is the whole number part because 3 < (sqrt(23) + 3) / 2 < 4)
#           sqrt(23) - 3           14                2                  2
#
#                2         2 * (sqrt(23) + 3)   sqrt(23) + 3       sqrt(23) - 4
#   a2 = 3, ------------ = ------------------ = ------------ = 1 + ------------ (1 is the whole number part because 1 < (sqrt(23) + 3) / 7 < 2)
#           sqrt(23) - 3           14                7                  7
#
#                7         7 * (sqrt(23) + 4)   sqrt(23) + 4       sqrt(23) - 4
#   a3 = 1, ------------ = ------------------ = ------------ = 8 + ------------ (8 is the whole number part because 8 < sqrt(23) + 4 < 9)
#           sqrt(23) - 4           7                 1                  1
#
#                1             sqrt(23) - 3
#   a4 = 8, ------------ = 1 + ------------ (from a0)
#           sqrt(23) - 4            7
#
#                7             sqrt(23) - 3
#   a5 = 1, ------------ = 3 + ------------ (from a1)
#           sqrt(23) - 3            2
#
#                2             sqrt(23) - 4
#   a6 = 3, ------------ = 1 + ------------ (from a2)
#           sqrt(23) - 3            7
#
#                7             sqrt(23) - 4
#   a7 = 1, ------------ = 8 + ------------ (from a3)
#           sqrt(23) - 4            1
#
#                1             sqrt(23) - 3
#   a8 = 8, ------------ = 1 + ------------ (from a0/a4)
#           sqrt(23) - 4            7
#
# It can be seen that the sequence is repeating. For conciseness, we use the notation sqrt(23) = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats indefinitely.
#
# The first ten continued fraction representations of (irrational) square roots are:
#   sqrt(2)  = [1;(2)],         period=1
#   sqrt(3)  = [1;(1,2)],       period=2
#   sqrt(5)  = [2;(4)],         period=1
#   sqrt(6)  = [2;(2,4)],       period=2
#   sqrt(7)  = [2;(1,1,1,4)],   period=4
#   sqrt(8)  = [2;(1,4)],       period=2
#   sqrt(10) = [3;(6)],         period=1
#   sqrt(11) = [3;(3,6)],       period=2
#   sqrt(12) = [3;(2,6)],       period=2
#   sqrt(13) = [3;(1,1,1,1,6)], period=5
#
# Exactly four continued fractions, for N <= 13, have an odd period.
#
# How many continued fractions for N <= 10000 have an odd period?

import math;
import time;
import sys;

start_time = time.time();

N = 10000;

class Iteration:
    a = None;
    n1 = None;
    d1 = None;
    w = None;
    n2 = None;
    d2 = None;
    def __eq__(self, other):
        return (self.a == other.a) and (self.n1 == other.n1) and (self.d1 == other.d1) and (self.w == other.w) and (self.n2 == other.n2) and (self.d2 == other.d2);
    def __ne__(self, other):
        return (self.a != other.a) or (self.n1 != other.n1) or (self.d1 != other.d1) or (self.w != other.w) or (self.n2 != other.n2) or (self.d2 != other.d2);
    def __str__(self):
        return str(self.a) + ' ' + str(self.n1) + ' ' + str(self.d1) + ' ' + str(self.w) + ' ' + str(self.n2) + ' ' + str(self.d2);

odd_period_count = 0;
for n in range(N + 1):
    # Exclude perfect squares.
    if (int(math.sqrt(n)) ** 2) != n:
        iterations = [];
        # Note that this first iteration is a pseudo-iteration and is not added to the iterations list.
        iteration = Iteration();
        iteration.w = int(math.sqrt(n));
        iteration.n2 = iteration.w;
        iteration.d2 = 1;
        while True:
            #                   n1_i+1             sqrt(n) + d1_i+1                 sqrt(n) - n2_i+1
            # a_i+1 = w_i, ---------------- = --------------------------- = w_i+1 + ----------------
            #              sqrt(n) - d1_i+1   (n - (d1_i+1 ^ 2)) / n1_i+1                d2_i+1
            previous_iteration = iteration;
            iteration = Iteration();
            iteration.a = previous_iteration.w;
            iteration.n1 = previous_iteration.d2;
            iteration.d1 = previous_iteration.n2;
            iteration.d2 = (n - (iteration.d1 ** 2)) / iteration.n1;
            if (iteration.n1 * iteration.d2) != (n - (iteration.d1 ** 2)):
                print "Error in algorithm assumption!";
                sys.exit(-1);
            iteration.w = int((math.sqrt(n) + iteration.d1) / iteration.d2);
            iteration.n2 = (iteration.w * iteration.d2) - iteration.d1;
            # print n, iteration.a, iteration.n1, iteration.d1, iteration.w, iteration.n2, iteration.d2;
            matching_index = None;
            index = 0;
            for existing_iteration in iterations:
                if existing_iteration == iteration:
                    matching_index = index;
                    break;
                index += 1;
            if matching_index != None:
                period = len(iterations) - matching_index;
                parity = "even";
                if period % 2 == 1:
                    parity = "odd";
                    odd_period_count += 1;
                # print "n = %04d, matching_index = %d, period = %d (%s)." % (n, matching_index, period, parity);
                print "n = %04d, period = %d (%s)." % (n, period, parity);
                break;
            else:
                iterations.append(iteration);
print;
print "odd_period_count = %d." % odd_period_count;

print;
print "Execution time = %f seconds." % (time.time() - start_time);
