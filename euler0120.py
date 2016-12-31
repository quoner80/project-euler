# Square remainders
# Problem 120
#
# Let r be the remainder when (a-1)^n + (a+1)^n is divided by a^2.
#
# For example, if a = 7 and n = 3, then r = 42: 6^3 + 8^3 = 728 = 42 mod 49. And as n varies, so too will r, but for a = 7 it turns out that r_max = 42.
#
# For 3 <= a <= 1000, find summation(r_max).

import time;

start_time = time.time();

def print_execution_time():
    print 'Execution time = %f seconds.' % (time.time() - start_time);

"""
# Case studies for various n:
n = 7;
for a in range(3, 1000):
    r = (((a - 1) ** n) + ((a + 1) ** n)) % (a ** 2);
    print a, n, r, r - (2 * n * a);
"""

# n = 1:
# r = [(a + 1)^1 + (a - 1)^1] % a^2 = 
# [
#   a + 1 +
#   a - 1
# ] % a^2 =
# [2a] % a^2 = 2a when a > 2
# 
# n = 2:
# r = [(a + 1)^2 + (a - 1)^2] % a^2 = 
# [
#   a^2 + 2a + 1 +
#   a^2 - 2a + 1
# ] % a^2 =
# [2a^2 + 2] % a^2 = 2
# 
# n = 3:
# r = [(a + 1)^3 + (a - 1)^3] % a^2 = 
# [
#   a^3 + 3a^2 + 3a + 1 +
#   a^3 - 3a^2 + 3a - 1
# ] % a^2 =
# [2a^3 + 6a] % a^2 = 6a % a^2 = 6a when a > 6
# 
# n = 4:
# r = [(a + 1)^4 + (a - 1)^4] % a^2 = 
# [
#   a^4 + 4a^3 + 6a^2 + 4a + 1 +
#   a^4 - 4a^3 + 6a^2 - 4a + 1
# ] % a^2 =
# [2a^4 + 12a^2 + 2] % a^2 = 2
# 
# n = 5:
# r = [(a + 1)^5 + (a - 1)^5] % a^2 = 
# [
#   a^5 + 5a^4 + 10a^3 + 10a^2 + 5a + 1 +
#   a^5 - 5a^4 + 10a^3 - 10a^2 + 5a - 1
# ] % a^2 =
# [2a^5 + 20a^3 + 10a] % a^2 = 10a % a^2 = 10a when a > 10
#
# In general, when n is even:
#   r = 2 != r_max
#
# In general, when n is odd:
#   r = [2 * n-choose-1 * a] % a^2 = 2na % a^2 = 2na when a > 2n or a/2 > n or n < a/2
#   In general, when a is odd:
#       n < a/2 means n = (a - 1) / 2 for r_max
#       r_max = 2na = 2 * [(a - 1) / 2] * a = a(a - 1)
#   In general, when a is even:
#       n < a/2 means n = (a - 2) / 2 for r_max
#       r_max = 2na = 2 * [(a - 2) / 2] * a = a(a - 2)

N = 1000;
N_PLUS_1 = N + 1;

summation = 0;
# Odd a cases, per above:
for a in range(3, N_PLUS_1, 2):
    summation += (a * (a - 1));
# Even a cases, per above:
for a in range(4, N_PLUS_1, 2):
    summation += (a * (a - 2));
print summation;

print_execution_time();
