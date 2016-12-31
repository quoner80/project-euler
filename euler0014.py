# Longest Collatz sequence
#
# The following iterative sequence is defined for the set of positive integers:
#
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

def get_collatz_chain_length(n):
    length = 1
    while not n == 1:
        length += 1;
        if n % 2 == 0:
            n = n / 2;
        else:
            n = (3 * n) + 1;
    return length;

N = 1000000;
collatz_max = 0;
arg_max = [];
for arg in range(1, N):
    collatz = get_collatz_chain_length(arg);
    if collatz > collatz_max:
        collatz_max = collatz;
        arg_max = [arg];
    elif collatz == collatz_max:
        arg_max.append(arg);
print "collatz_max = %d" % collatz_max;
print "arg_max = %s" % arg_max;
