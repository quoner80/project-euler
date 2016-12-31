# Powerful digit sum
#
# A googol (10^100) is a massive number: one followed by one-hundred zeros; 100^100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
#
# Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?

import time;

start_time = time.time();

N = 100;

max_digital_sum = 0;
argmax_a = 0;
argmax_b = 0;
for a in range(1, N):
    for b in range(1, N):    
        p = str(a ** b);
        digital_sum = 0;
        for c in p:
            digital_sum += int(c);
        # print "%d^%d = %d produces the digital sum, %d." % (a, b, a ** b, digital_sum);
        if digital_sum > max_digital_sum:
            max_digital_sum = digital_sum;
            argmax_a = a;
            argmax_b = b;
print "%d^%d = %d produces the maximum digital sum, %d." % (argmax_a, argmax_b, argmax_a ** argmax_b, max_digital_sum);

print "Execution time = %f seconds." % (time.time() - start_time);
