# Cubic permutations
#
# The cube, 41063625 (345^3), can be permuted to produce two other cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.
#
# Find the smallest cube for which exactly five permutations of its digits are cube.

import time;

start_time = time.time();

PERMUTATION_COUNT = 5;

permutations = {};

n = 0;
while True:
    n_cubed = n ** 3;
    # print n, n_cubed;
    key = "".join(sorted(str(n_cubed)));
    if key in permutations:
        permutations[key].append(n);
        if len(permutations[key]) == PERMUTATION_COUNT:
            print "%s: %s." % (key, permutations[key]);
            for cube_root in permutations[key]:
                print "%d^3 = %d." % (cube_root, cube_root ** 3);
            break;
    else:
        permutations[key] = [n];
    n += 1;

print;
print "Execution time = %f seconds." % (time.time() - start_time);
