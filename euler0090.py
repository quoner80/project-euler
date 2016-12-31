# Cube digit pairs
# Problem 90
#
# Each of the six faces on a cube has a different digit (0 to 9) written on it; the same is done to a second cube. By placing the two cubes side-by-side in different positions we can form a variety of 2-digit numbers.
#
# For example, the square number 64 could be formed:
#
#     +-----+   +-----+
#    /     /|  /     /|
#   +-----+ | +-----+ |
#   |     | | |     | |
#   |  6  | + |  4  | +
#   |     |/  |     |/
#   +-----+   +-----+
#
# In fact, by carefully choosing the digits on both cubes it is possible to display all of the square numbers below one-hundred: 01, 04, 09, 16, 25, 36, 49, 64, and 81.
#
# For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9} on one cube and {1, 2, 3, 4, 8, 9} on the other cube.
#
# However, for this problem we shall allow the 6 or 9 to be turned upside-down so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows for all nine square numbers to be displayed; otherwise it would be impossible to obtain 09.
#
# In determining a distinct arrangement we are interested in the digits on each cube, not the order.
#
#   {1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
#   {1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}
#
# But because we are allowing 6 and 9 to be reversed, the two distinct sets in the last example both represent the extended set {1, 2, 3, 4, 5, 6, 9} for the purpose of forming 2-digit numbers.
#
# How many distinct arrangements of the two cubes allow for all of the square numbers to be displayed?

import time;

start_time = time.time();

def print_execution_time():
    print "Execution time = %f seconds." % (time.time() - start_time);

# [0, 5, 6, 7, 8, 9] [1, 2, 3, 4, 8, 9]
# [1, 2, 3, 4, 8, 9] [0, 5, 6, 7, 8, 9]
# [0, 5, 6, 7, 8, 9] [1, 2, 3, 4, 6, 7]
# [1, 2, 3, 4, 6, 7] [0, 5, 6, 7, 8, 9]
count = 0;
for a in range(10):
    for b in range(a + 1, 10):
        for c in range(b + 1, 10):
            for d in range(c + 1, 10):
                for e in range(d + 1, 10):
                    for f in range(e + 1, 10):
                        c0 = [a, b, c, d, e, f];
                        for u in range(10):
                            for v in range(u + 1, 10):
                                for w in range(v + 1, 10):
                                    for x in range(w + 1, 10):
                                        for y in range(x + 1, 10):
                                            for z in range(y + 1, 10):
                                                c1 = [u, v, w, x, y, z];
                                                if (0 in c0 and 1 in c1) or (1 in c0 and 0 in c1):
                                                    if (0 in c0 and 4 in c1) or (4 in c0 and 0 in c1):
                                                        if (0 in c0 and (9 in c1 or 6 in c1)) or ((9 in c0 or 6 in c0) and 0 in c1):
                                                            if (1 in c0 and (6 in c1 or 9 in c1)) or ((6 in c0 or 9 in c0) and 1 in c1):
                                                                if (2 in c0 and 5 in c1) or (5 in c0 and 2 in c1):
                                                                    if (3 in c0 and (6 in c1 or 9 in c1)) or ((6 in c0 or 9 in c0) and 3 in c1):
                                                                        if (4 in c0 and (9 in c1 or 6 in c1)) or ((9 in c0 or 6 in c0) and 4 in c1):
                                                                            if ((6 in c0 or 9 in c0) and 4 in c1) or (4 in c0 and (6 in c1 or 9 in c1)):
                                                                                if (8 in c0 and 1 in c1) or (1 in c0 and 8 in c1):
                                                                                    print c0, c1;
                                                                                    count += 1;
# Divide the count by 2 to compensate for the c0 c1 and c1 c0 duplicates.
print "total arrangements = %d." % (count / 2);

print_execution_time();
