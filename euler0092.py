# Square digit chains
# Problem 92
#
# A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.
# 
# For example,
#   44 -> 32 -> 13 -> 10 -> 1 -> 1
#   85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89
#
# Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
#
# How many starting numbers below ten million will arrive at 89?

import time;

start_time = time.time();

N = 100;
N = 10000000;

def print_execution_time():
    print "Execution time = %f seconds." % (time.time() - start_time);

end_values = [0] * N;

count_1 = 0;
count_89 = 0;

for n in range(1, N):
    x = n;
    while x != 1 and x != 89:
        n_string = str(x);
        x = 0;
        for digit in n_string:
            x += int(digit) ** 2;
        if (x < N) and (end_values[x] != 0):
            x = end_values[x];
    end_values[n] = x;
    # Print one of every hundred thousand results as a progress indicator.
    if (n % 100000) == 0:
        print n, x;
    if x == 1:
        count_1 += 1;
    else:
        count_89 += 1;
print "count_1  = %d." % count_1;
print "count_89 = %d." % count_89;

print_execution_time();
