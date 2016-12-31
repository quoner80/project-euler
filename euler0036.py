# Double-base palindromes
#
# The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)

import time;

start_time = time.time();

def is_binary_palindrome(n):
    binary = "{0:b}".format(n);
    binary_reverse = binary[ : : -1];
    if binary == binary_reverse:
        print "%d = %s (binary)" % (n, binary);
        return True;
    else:
        # print n, binary;
        return False;

double_palindrome_sum = 0;
for n in range(0, 10):
    if is_binary_palindrome(n):
        double_palindrome_sum += n;
for exponent in range(3):
    min_inclusive = 10 ** exponent;
    max_exclusive = 10 ** (exponent + 1);
    for h in range(min_inclusive, max_exclusive):
        half = str(h);
        half_reverse = half[ : : -1];
        n = int(half + half_reverse);
        if is_binary_palindrome(n):
            double_palindrome_sum += n;
    if exponent < 2:
        for h in range(min_inclusive, max_exclusive):
            half = str(h);
            half_reverse = half[ : : -1];
            for m in range(0, 10):
                n = int(half + str(m) + half_reverse);
                if is_binary_palindrome(n):
                    double_palindrome_sum += n;
print "Sum of double palindromes = %d." % double_palindrome_sum;

print "Execution time = %f seconds." % (time.time() - start_time);
