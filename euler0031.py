# Coin sums
#
# In England the currency is made up of pound, P, and pence, p, and there are eight coins in general circulation:
#    1p, 2p, 5p, 10p, 20p, 50p, 1P (100p) and 2P (200p).
#
# It is possible to make P2 in the following way:
#    1x1P + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
#
# How many different ways can P2 be made using any number of coins?

import time;

start_time = time.time();

SUM = 200;
ways = 0;
for x1p in range(0, SUM + 1):
    sum_1p = 1 * x1p;
    for x2p in range(0, ((SUM - sum_1p) / 2) + 1):
        sum_2p = 2 * x2p;
        sum_1p_2p = sum_1p + sum_2p;
        for x5p in range(0, ((SUM - sum_1p_2p) / 5) + 1):
            sum_5p = 5 * x5p;
            sum_1p_2p_5p = sum_1p_2p + sum_5p;
            for x10p in range(0, ((SUM - sum_1p_2p_5p) / 10) + 1):
                sum_10p = 10 * x10p;
                sum_1p_2p_5p_10p = sum_1p_2p_5p + sum_10p;
                for x20p in range(0, ((SUM - sum_1p_2p_5p_10p) / 20) + 1):
                    sum_20p = 20 * x20p;
                    sum_1p_2p_5p_10p_20p = sum_1p_2p_5p_10p + sum_20p;
                    for x50p in range(0, ((SUM - sum_1p_2p_5p_10p_20p) / 50) + 1):
                        sum_50p = 50 * x50p;
                        sum_1p_2p_5p_10p_20p_50p = sum_1p_2p_5p_10p_20p + sum_50p;
                        for x1P in range(0, ((SUM - sum_1p_2p_5p_10p_20p_50p) / 100) + 1):
                            sum_1P = 100 * x1P;
                            sum_1p_2p_5p_10p_20p_50p_1P = sum_1p_2p_5p_10p_20p_50p + sum_1P;
                            for x2P in range(0, ((SUM - sum_1p_2p_5p_10p_20p_50p_1P) / 200) + 1):
                                sum_2P = 200 * x2P;
                                sum_1p_2p_5p_10p_20p_50p_1P_2P = sum_1p_2p_5p_10p_20p_50p_1P + sum_2P;
                                if sum_1p_2p_5p_10p_20p_50p_1P_2P == SUM:
                                    ways += 1;
                                    # print "%dx2P + %dx1P + %dx50p + %dx20p + %dx10p + %dx5p + %dx2p + %dx1p = %d." % (x2P, x1P, x50p, x20p, x10p, x5p, x2p, x1p, SUM);
print "Number of different ways = %d." % ways;

print "Execution time = %f seconds." % (time.time() - start_time);
