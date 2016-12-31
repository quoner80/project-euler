# Bouncy numbers
# Problem 112
#
# Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.
#
# Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
#
# We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
#
# Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.
#
# Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.
#
# Find the least number for which the proportion of bouncy numbers is exactly 99%.

import time;

start_time = time.time();

def print_execution_time():
    print 'Execution time = %f seconds.' % (time.time() - start_time);

def is_increasing(n):
    increasing = True;
    # Initialize to something that will always be >= any digit.
    previous_rightmost_digit = 9;
    while n > 0:
        rightmost_digit = n % 10;
        n /= 10;
        # print '%d <= %d?' % (rightmost_digit, previous_rightmost_digit);
        if rightmost_digit > previous_rightmost_digit:
            increasing = False;
            break;
        previous_rightmost_digit = rightmost_digit;
    return increasing;

def is_decreasing(n):
    decreasing = True;
    # Initialize to something that will always be <= any digit.
    previous_rightmost_digit = 0;
    while n > 0:
        rightmost_digit = n % 10;
        n /= 10;
        # print '%d >= %d?' % (rightmost_digit, previous_rightmost_digit);
        if rightmost_digit < previous_rightmost_digit:
            decreasing = False;
            break;
        previous_rightmost_digit = rightmost_digit;
    return decreasing;

def is_bouncy(n):
    return (not is_increasing(n)) and (not is_decreasing(n));

"""
print is_increasing(134468);
print is_increasing(66420);
print is_increasing(155349);

print is_decreasing(134468);
print is_decreasing(66420);
print is_decreasing(155349);

print is_bouncy(134468);
print is_bouncy(66420);
print is_bouncy(155349);
"""

target_percentage = 50;
target_percentage = 90;
target_percentage = 99;
bouncy_count = 0;
n = 0;
while True:
    n += 1;
    if is_bouncy(n):
        bouncy_count += 1;
    # print n, bouncy_count, float(bouncy_count) / n;
    if (bouncy_count * 100) == (n * target_percentage):
        print n;
        break;

print_execution_time();
