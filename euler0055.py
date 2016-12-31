# Lychrel numbers
#
# If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
#
# Not all numbers produce palindromes so quickly. For example,
#    349 +  943 = 1292,
#   1292 + 2921 = 4213
#   4213 + 3124 = 7337
#
# That is, 349 took three iterations to arrive at a palindrome.
#
# Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).
#
# Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.
#
# How many Lychrel numbers are there below ten-thousand?
#
# NOTE: Wording was modified slightly on 24 April 2007 to emphasise the theoretical nature of Lychrel numbers.

import time;

start_time = time.time();

MAX_ITERATIONS = 49;
MAX_CANDIDATE = 9999;

def is_palindrome(n):
    forward = str(n);
    reverse = forward[::-1];
    return forward == reverse;

lychrel_number_count = 0;
for n in range(1, MAX_CANDIDATE + 1):
    iterations = 1;
    forward = n;
    while iterations <= MAX_ITERATIONS:
        reverse = int(str(forward)[::-1]);
        forward = forward + reverse;
        if is_palindrome(forward):
            # print "%d arrives at palindrome %d after %d iterations." % (n, forward, iterations);
            break;
        iterations += 1;
    if iterations > MAX_ITERATIONS:
        print "%d is a lychrel number." % n;
        lychrel_number_count += 1;
print "There are %d lychrel numbers below %d." % (lychrel_number_count, MAX_CANDIDATE + 1);

print "Execution time = %f seconds." % (time.time() - start_time);
