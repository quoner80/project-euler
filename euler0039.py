# Integer right triangles
#
# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
#
# {20,48,52}, {24,45,51}, {30,40,50}
#
# For which value of p <= 1000, is the number of solutions maximised?

import time;

start_time = time.time();

N = 1000;

count_max = 0;
p_argmax = 0;
for p in range(1, N + 1):
    count = 0;
    for a in range(1, (p / 3)):
        for b in range (a + 1, (((p - a - 1) / 2)) + 1):
            c = p - a - b;
            if a ** 2 + b ** 2 == c ** 2:
                count += 1;
    if count > count_max:
        count_max = count;
        p_argmax = p;
print "count_max = %d; p_argmax = %d." % (count_max, p_argmax);

print "Execution time = %f seconds." % (time.time() - start_time);
