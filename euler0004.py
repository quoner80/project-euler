# Largest palindrome product
#
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

import math

def is_palindrome(n):
    forward = str(n);
    reverse = forward[::-1];
    return forward == reverse;

MAX = 999;
MIN = 100;
max_palindrome = 1;
max_palindrome_x = 1;
max_palindrome_y = 1;
max_x = MAX;
min_x = MIN;
for x in range(max_x, min_x - 1, -1):
    max_y = MAX;
    # Testing all the way down to MAX is not necessary if there is already a max_palindrome.
    # Test only down to y such that x * y > max_palindrome.
    min_y = max(MIN, int(math.floor(float(max_palindrome) / x)));
    for y in range(max_y, min_y - 1, -1):
        xy = x * y;
        if is_palindrome(xy):
            if xy > max_palindrome:
                max_palindrome = xy;
                max_palindrome_x = x;
                max_palindrome_y = y;
                print "%d * %d = %d" % (max_palindrome_x, max_palindrome_y, max_palindrome);
            break;
print "\n%d * %d = %d" % (max_palindrome_x, max_palindrome_y, max_palindrome);
