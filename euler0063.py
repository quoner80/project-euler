# Powerful digit counts
#
# The 5-digit number, 16807 = 7^5, is also a fifth power. Similarly, the 9-digit number, 134217728 = 8^9, is a ninth power.
#
# How many n-digit positive integers exist which are also an nth power?

import time;

start_time = time.time();

total_count = 0;
power = 1;
while True:
    count = 0;
    upper_limit = 10 ** power;
    lower_limit = 10 ** (power - 1);
    base = 1;
    while True:
        result = base ** power;
        if result >= upper_limit:
            break;
        elif result >= lower_limit:
            count += 1;
            print base, power, result;
        base += 1;
    if count == 0:
        break;
    total_count += count;
    power += 1;
    print;
print "Total count = %d." % total_count;

print;
print "Execution time = %f seconds." % (time.time() - start_time);
