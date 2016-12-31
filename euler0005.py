# Smallest multiple
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

N = 20;
# The primes <= 20:
# Index: 00 01 02 03 04 05 06 07
# Prime: 02 03 05 07 11 13 17 19
primes = [2, 3, 5, 7, 11, 13, 17, 19];
prime_count = len(primes);
# print prime_count;

factorizations = [[0] * prime_count] * (N + 1);

factorizations[2]  = [1, 0, 0, 0, 0, 0, 0, 0]; # 2  = 2^1
factorizations[3]  = [0, 1, 0, 0, 0, 0, 0, 0]; # 3  = 3^1
factorizations[4]  = [2, 0, 0, 0, 0, 0, 0, 0]; # 4  = 2^2
factorizations[5]  = [0, 0, 1, 0, 0, 0, 0, 0]; # 5  = 5^1
factorizations[6]  = [1, 1, 0, 0, 0, 0, 0, 0]; # 6  = 2^1 * 3^1
factorizations[7]  = [0, 0, 0, 1, 0, 0, 0, 0]; # 7  = 7^1
factorizations[8]  = [3, 0, 0, 0, 0, 0, 0, 0]; # 8  = 2^3
factorizations[9]  = [0, 2, 0, 0, 0, 0, 0, 0]; # 9  = 3^2
factorizations[10] = [1, 0, 1, 0, 0, 0, 0, 0]; # 10 = 2^1 * 5^1
factorizations[11] = [0, 0, 0, 0, 1, 0, 0, 0]; # 11 = 11^1
factorizations[12] = [2, 1, 0, 0, 0, 0, 0, 0]; # 12 = 2^2 * 3^1
factorizations[13] = [0, 0, 0, 0, 0, 1, 0, 0]; # 13 = 13^1
factorizations[14] = [1, 0, 0, 1, 0, 0, 0, 0]; # 14 = 2^1 * 7^1
factorizations[15] = [0, 1, 1, 0, 0, 0, 0, 0]; # 15 = 3^1 * 5^1
factorizations[16] = [4, 0, 0, 0, 0, 0, 0, 0]; # 16 = 2^4
factorizations[17] = [0, 0, 0, 0, 0, 0, 1, 0]; # 17 = 17^1
factorizations[18] = [1, 2, 0, 0, 0, 0, 0, 0]; # 18 = 2^1 * 3^2
factorizations[19] = [0, 0, 0, 0, 0, 0, 0, 1]; # 19 = 19^1
factorizations[20] = [2, 0, 1, 0, 0, 0, 0, 0]; # 20 = 2^2 * 5^1

x = 1;
x_factorization = [0] * prime_count;
for prime_index in range(prime_count):
    for n in range(N + 1):
        x_factorization[prime_index] = max(x_factorization[prime_index], factorizations[n][prime_index]);
    x *= primes[prime_index] ** x_factorization[prime_index];

print x_factorization;
print "x = %d" % x
