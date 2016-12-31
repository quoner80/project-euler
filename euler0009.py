# Special Pythagorean triplet
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

N = 1000;

for a in range(1, ((N - 3) / 3) + 1):
    for b in range (a + 1, (((N - a - 1) / 2)) + 1):
        c = N - a - b;
        # print "%d, %d, %d" % (a, b, c);
        if (a ** 2 + b ** 2 == c ** 2):
            print "%d^2 + %d^2 = %d + %d = %d = %d^2" % (a, b, a ** 2, b ** 2, c ** 2, c);
            print "    %d * %d * %d = %d" % (a, b, c, a * b * c);
