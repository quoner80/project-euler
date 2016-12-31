# Power digit sum
#
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?

E = 1000;

total = 0;
n = 2 ** E;
print n;
s = str(n);
for i in range(len(s)):
    total += int(s[i]);
print total;
