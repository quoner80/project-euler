# Digit factorial chains
#
# The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:
#
#   1! + 4! + 5! = 1 + 24 + 120 = 145
#
# Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:
#
#   169 -> 363601 -> 1454 -> 169
#   871 -> 45361 -> 871
#   872 -> 45362 -> 872
#
# It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,
#
#   69 -> 363600 -> 1454 -> 169 -> 363601 (-> 1454)
#   78 -> 45360 -> 871 -> 45361 (-> 871)
#   540 -> 145 (-> 145)
#
# Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.
#
# How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?

import time;

start_time = time.time();

N = 1000000;
T = 60;

factorials = [1];
for i in range(1, 10):
    factorials.append(i * factorials[i - 1]);

def get_factorial_sum(n):
    factorial_sum = 0;
    if (n == 0):
        factorial_sum = 1;
    while n != 0:
        factorial_sum += factorials[n % 10];
        n = n / 10;
    return factorial_sum;

# This approach does not work, at least in this simple form. Take n = 69, for example. Because it finds 169 (but not 1454) in
# the repeaters dictionary, giving an incorrect result of 6 (should be 5).
#
# repeaters[n] = repeating length of n
"""
repeaters = {};
for n in range(70):
    x = n;
    non_repeating_length = None;
    chain = [];
    while (not x in repeaters) and (not x in chain):
        chain.append(x);
        x = get_factorial_sum(x);
    if x in repeaters:
        non_repeating_length = len(chain) + repeaters[x];
    else: # if x in chain:
        non_repeating_length = len(chain);
        repeaters[x] = non_repeating_length - chain.index(x);
    print n, non_repeating_length, chain, x;
print repeaters;
"""

count = 0;
for n in range(N):
    x = n;
    chain = [];
    while not x in chain:
        chain.append(x);
        x = get_factorial_sum(x);
    non_repeating_length = len(chain);    
    if non_repeating_length >= T:
        count += 1;
        print n, non_repeating_length, x;
print "count = %d." % count;

print;
print "Execution time = %f seconds." % (time.time() - start_time);
