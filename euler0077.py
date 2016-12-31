# Prime summations
#
# It is possible to write ten as the sum of primes in exactly five different ways:
#
#   7 + 3
#   5 + 5
#   5 + 3 + 2
#   3 + 3 + 2 + 2
#   2 + 2 + 2 + 2 + 2
#
# What is the first value which can be written as the sum of primes in over five thousand different ways?

import time;

start_time = time.time();

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79]; #, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131];
PRIME_COUNT = len(PRIMES);

def calculate_prime_sums(n):
    global PRIMES;
    global PRIME_COUNT;

    max_counts    = [0] * PRIME_COUNT;
    factor_counts = [0] * PRIME_COUNT;
    remainders    = [0] * PRIME_COUNT;

    # Cannot put this itself into a loop because it would give the error "SystemError: too many statically nested blocks".
    # for n in range(2, PRIMES[20]):
    ways = 0;
    remainders[21] = n;

    remainders[20] = remainders[21] - (factor_counts[21] * PRIMES[21]);
    max_counts[20] = remainders[20] / PRIMES[20];
    for factor_counts[20] in range(max_counts[20] + 1):
        remainders[19] = remainders[20] - (factor_counts[20] * PRIMES[20]);
        max_counts[19] = remainders[19] / PRIMES[19];
        for factor_counts[19] in range(max_counts[19] + 1):
            remainders[18] = remainders[19] - (factor_counts[19] * PRIMES[19]);
            max_counts[18] = remainders[18] / PRIMES[18];
            for factor_counts[18] in range(max_counts[18] + 1):
                remainders[17] = remainders[18] - (factor_counts[18] * PRIMES[18]);
                max_counts[17] = remainders[17] / PRIMES[17];
                for factor_counts[17] in range(max_counts[17] + 1):
                    remainders[16] = remainders[17] - (factor_counts[17] * PRIMES[17]);
                    max_counts[16] = remainders[16] / PRIMES[16];
                    for factor_counts[16] in range(max_counts[16] + 1):
                        remainders[15] = remainders[16] - (factor_counts[16] * PRIMES[16]);
                        max_counts[15] = remainders[15] / PRIMES[15];
                        for factor_counts[15] in range(max_counts[15] + 1):
                            remainders[14] = remainders[15] - (factor_counts[15] * PRIMES[15]);
                            max_counts[14] = remainders[14] / PRIMES[14];
                            for factor_counts[14] in range(max_counts[14] + 1):
                                remainders[13] = remainders[14] - (factor_counts[14] * PRIMES[14]);
                                max_counts[13] = remainders[13] / PRIMES[13];
                                for factor_counts[13] in range(max_counts[13] + 1):
                                    remainders[12] = remainders[13] - (factor_counts[13] * PRIMES[13]);
                                    max_counts[12] = remainders[12] / PRIMES[12];
                                    for factor_counts[12] in range(max_counts[12] + 1):
                                        remainders[11] = remainders[12] - (factor_counts[12] * PRIMES[12]);
                                        max_counts[11] = remainders[11] / PRIMES[11];
                                        for factor_counts[11] in range(max_counts[11] + 1):
                                            remainders[10] = remainders[11] - (factor_counts[11] * PRIMES[11]);
                                            max_counts[10] = remainders[10] / PRIMES[10];
                                            for factor_counts[10] in range(max_counts[10] + 1):
                                                remainders[9] = remainders[10] - (factor_counts[10] * PRIMES[10]);
                                                max_counts[9] = remainders[9] / PRIMES[9];
                                                for factor_counts[9] in range(max_counts[9] + 1):
                                                    remainders[8] = remainders[9] - (factor_counts[9] * PRIMES[9]);
                                                    max_counts[8] = remainders[8] / PRIMES[8];
                                                    for factor_counts[8] in range(max_counts[8] + 1):
                                                        remainders[7] = remainders[8] - (factor_counts[8] * PRIMES[8]);
                                                        max_counts[7] = remainders[7] / PRIMES[7];
                                                        for factor_counts[7] in range(max_counts[7] + 1):
                                                            remainders[6] = remainders[7] - (factor_counts[7] * PRIMES[7]);
                                                            max_counts[6] = remainders[6] / PRIMES[6];
                                                            for factor_counts[6] in range(max_counts[6] + 1):
                                                                remainders[5] = remainders[6] - (factor_counts[6] * PRIMES[6]);
                                                                max_counts[5] = remainders[5] / PRIMES[5];
                                                                for factor_counts[5] in range(max_counts[5] + 1):
                                                                    remainders[4] = remainders[5] - (factor_counts[5] * PRIMES[5]);
                                                                    max_counts[4] = remainders[4] / PRIMES[4];
                                                                    for factor_counts[4] in range(max_counts[4] + 1):
                                                                        remainders[3] = remainders[4] - (factor_counts[4] * PRIMES[4]);
                                                                        max_counts[3] = remainders[3] / PRIMES[3];
                                                                        for factor_counts[3] in range(max_counts[3] + 1):
                                                                            remainders[2] = remainders[3] - (factor_counts[3] * PRIMES[3]);
                                                                            max_counts[2] = remainders[2] / PRIMES[2];
                                                                            for factor_counts[2] in range(max_counts[2] + 1):
                                                                                remainders[1] = remainders[2] - (factor_counts[2] * PRIMES[2]);
                                                                                max_counts[1] = remainders[1] / PRIMES[1];
                                                                                for factor_counts[1] in range(max_counts[1] + 1):
                                                                                    remainders[0] = remainders[1] - (factor_counts[1] * PRIMES[1]);
                                                                                    if remainders[0] % PRIMES[0] == 0:
                                                                                        ways += 1;
                                                                                        factor_counts[0] = remainders[0] / PRIMES[0];
                                                                                        # print "%d: way = \t%s\n\tx \t%s" % (n, factor_counts, PRIMES);

    print "%d has %d ways" % (n, ways);

for n in range(2, PRIMES[20]):
    calculate_prime_sums(n);

print;
print "Execution time = %f seconds." % (time.time() - start_time);
