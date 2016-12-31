# Digit power sum
# Problem 119
#
# The number 512 is interesting because it is equal to the sum of its digits raised to some power: 5 + 1 + 2 = 8, and 8^3 = 512. Another example of a number with this property is 614656 = 28^4.
#
# We shall define a_n to be the nth term of this sequence and insist that a number must contain at least two digits to have a sum.
#
# You are given that a_2 = 512 and a_10 = 614656.
# 
# Find a_30.

import time;

start_time = time.time();

def print_execution_time():
    print 'Execution time = %f seconds.' % (time.time() - start_time);

# power is the base raised to the exponent.
def is_power_interesting(power, base):
    digit_sum = 0;
    while power != 0:
        digit_sum += (power % 10);
        power /= 10;
    return (digit_sum == base);

"""
print is_power_interesting(512, 8);
print is_power_interesting(32342, 5);
print is_power_interesting(614656, 28);
"""
# Start with 0 in the first array position in order to use 1-based indexing. This will still be in the first position after the
# sort because the other entries will be positive integers.
a = [0];
for base in range(2, 1000):
    for exponent in range(2, 101):
        power = base ** exponent;
        if is_power_interesting(power, base):
            a.append(power);
            print '%d = %d ^ %d' % (power, base, exponent);
a.sort();
print;
print a[2];
print a[10];
print a[30];

print_execution_time();
