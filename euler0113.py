# Non-bouncy numbers
# Problem 113
#
# Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.
#
# Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
#
# We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
#
# As n increases, the proportion of bouncy numbers below n increases such that there are only 12951 numbers below one-million that are not bouncy and only 277032 non-bouncy numbers below 10^10.
#
# How many numbers below a googol (10^100) are not bouncy?

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

def is_non_bouncy(n):
    return is_increasing(n) or is_decreasing(n);

"""
print is_non_bouncy(134468);
print is_non_bouncy(66420);
print is_non_bouncy(155349);
"""

"""
cumulative_non_bouncy_count = 0;
for exponent in range(6):
    start = 10 ** exponent;
    non_bouncy_count = 0;
    for n in range(start, 10 * start):
        if is_non_bouncy(n):
            non_bouncy_count += 1;
    cumulative_non_bouncy_count += non_bouncy_count;
    print start, non_bouncy_count, cumulative_non_bouncy_count;
"""

"""
exponent = 2;
start = 10 ** exponent;
count = 0;
for n in range(start, 10 * start):
    if is_decreasing(n):
        if n % 10 == 9 and (n / 10) % 10 == 9:
            count += 1;
            print n;
print;
print count;
"""

"""
exponent = 2;
start = 10 ** exponent;
count = 0;
for n in range(start, 10 * start):
    if is_increasing(n):
        if n % 10 == 9 and (n / 10) % 10 == 9:
            count += 1;
            print n;
print;
print count;
"""

digit_count_maximum = 100;
cumulative_non_bouncy_count = 0;

# Initialize to the list [1 .. 9] which contain no last digit 0, and 1 last digit of 1 through 9 each:
increasing_last_digits = [1] * 10;
increasing_last_digits[0] = 0;
decreasing_last_digits = list(increasing_last_digits);
digit_count = 0;

while True:
    digit_count += 1;
    increasing_count = sum(increasing_last_digits);
    decreasing_count = sum(decreasing_last_digits);
    non_bouncy_count = increasing_count + decreasing_count - 9;
    cumulative_non_bouncy_count += non_bouncy_count;
    print '%d-digit, increasing: %d, %s' % (digit_count, increasing_count, increasing_last_digits);
    print '%d-digit, decreasing: %d, %s' % (digit_count, decreasing_count, decreasing_last_digits);
    print '%d-digit, both      : 9, [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]' % (digit_count);
    print '%d-digit, non-bouncy: %d + %d - %d = %d' % (digit_count, increasing_count, decreasing_count, 9, non_bouncy_count);
    print '%d-digit, cumulative non-bouncy: %d' % (digit_count, cumulative_non_bouncy_count);
    print;
    if digit_count >= digit_count_maximum:
        break;

    # Increasing numbers:
    #
    # For every trailing 0, one can append digits 0 through 9:
    #   next_increasing_last_digits[0] += increasing_last_digits[0];
    #   next_increasing_last_digits[1] += increasing_last_digits[0];
    #   ...
    #   next_increasing_last_digits[9] += increasing_last_digits[0];
    # For every trailing 1, one can append digits 1 through 9:
    #   next_increasing_last_digits[1] += increasing_last_digits[1];
    #   next_increasing_last_digits[2] += increasing_last_digits[1];
    #   ...
    #   next_increasing_last_digits[9] += increasing_last_digits[1];
    # ...
    # For every trailing 9, one can append digits 9 through 9.
    #   next_increasing_last_digits[9] += increasing_last_digits[9];
    # 
    # In general, for every trailing d, one can append digits d through 9.
    next_increasing_last_digits = [0] * 10;
    for d in range(10):
        for i in range(d, 10):
            #print i, d;
            next_increasing_last_digits[i] += increasing_last_digits[d];
    increasing_last_digits = list(next_increasing_last_digits);

    # Decreasing numbers:
    #
    # For every trailing 0, one can append digits 0 through 0:
    #   next_decreasing_last_digits[0] += decreasing_last_digits[0];
    # For every trailing 1, one can append digits 0 through 1:
    #   next_decreasing_last_digits[0] += decreasing_last_digits[1];
    #   next_decreasing_last_digits[1] += decreasing_last_digits[1];
    # ...
    # For every trailing 9, one can append digits 0 through 9.
    #   next_decreasing_last_digits[0] += decreasing_last_digits[9];
    #   next_decreasing_last_digits[1] += decreasing_last_digits[9];
    #   ...
    #   next_decreasing_last_digits[9] += decreasing_last_digits[9];
    # 
    # In general, for every trailing d, one can append digits 0 through d.
    #   next_decreasing_last_digits[0] += decreasing_last_digits[d];
    #   next_decreasing_last_digits[1] += decreasing_last_digits[d];
    #   ...
    #   next_decreasing_last_digits[d] += decreasing_last_digits[d];
    next_decreasing_last_digits = [0] * 10;
    for d in range(10):
        for i in range(d + 1):
            next_decreasing_last_digits[i] += decreasing_last_digits[d];
    decreasing_last_digits = list(next_decreasing_last_digits);

print 'Non-bouncy numbers below 10^%d = %d.' % (digit_count_maximum, cumulative_non_bouncy_count);
print;
print_execution_time();
