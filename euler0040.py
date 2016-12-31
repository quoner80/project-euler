# Champernowne's constant
#
# An irrational decimal fraction is created by concatenating the positive integers:
#   0.123456789101112131415161718192021...
#                ^
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If d_n represents the nth digit of the fractional part, find the value of the following expression.
#   d_1 x d_10 x d_100 x d_1000 x d_10000 x d_100000 x d_1000000

import time;

start_time = time.time();

# This works for n <= 189, but it got too complicated after that, considering the actual string of the required length could be constructed directly.
def d_n(n):
    d = -1;
    # 1 - 9:
    # n = 1 to 9
    if n > 0 and n <= 9:
        d = n;
    # 10 - 99:
    # n = (9 + 1) to (9 + 90 * 2) = 10 to 189
    elif n <= 189:
        modulo = n % 2;
        if modulo == 0:
            d = (n + 10) / 20;
        else:
            d = ((n - 10) % 20) / 2;
    # 100 - 999:
    # n = (189 + 1) to (189 + 900 * 3) = 190 to 2889
    #
    # 1000 - 9999:
    # n = (2889 + 1) to (2889 + 9000 * 4) = 2890 to 38889
    #
    # 10000 - 99999:
    # n = (38889 + 1) to (38889 + 90000 * 5) = 38890 to 488889
    #
    # 100000 - 999999:
    # n = (488889 + 1) to (488889 + 900000 * 6) = 488890 to 5888889
    return d;

string = "";
# Since n = (488889 + 1) to (488889 + 900000 * 6) for i = 10000 - 99999 (see d_n() above), to construct a string with at least n = 1000000 digits requires:
#   n = 488889 + (i - 100000) * 6 = 1000000
#   (i - 100000) * 6 = 1000000 - 488889
#   i - 100000 = (1000000 - 488889) / 6
#   i = 100000 + ((1000000 - 488889) / 6) = 185185
# Add 1 to compensate for possible truncation during the division by 6:
#   i = 185186;
for i in range(1, 185186):
    string += str(i);
print "string length = %d. (Must be at least 1000000.)" % len(string);
product = 1;
for n in range(1, 191):
    if int(string[n - 1]) != d_n(n):
        print "d_n(%d) fails: %s != %d. (Does not affect correctness of this program.)" % (n, string[n - 1], d_n(n));
for n in [1, 10, 100, 1000, 10000, 100000, 1000000]:
    print "d_n(%d) = %s." % (n, string[n - 1]);
    product *= int(string[n - 1]);
print "product = %d." % product;

print "Execution time = %f seconds." % (time.time() - start_time);
