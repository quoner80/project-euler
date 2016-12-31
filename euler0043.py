# Sub-string divisibility
#
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
#
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
#   d2d3d4  = 406 is divisible by 2
#   d3d4d5  = 063 is divisible by 3
#   d4d5d6  = 635 is divisible by 5
#   d5d6d7  = 357 is divisible by 7
#   d6d7d8  = 572 is divisible by 11
#   d7d8d9  = 728 is divisible by 13
#   d8d9d10 = 289 is divisible by 17
#
# Find the sum of all 0 to 9 pandigital numbers with this property.

import time;

N = 1234567890;
# N = 123456;

primes = [2, 3, 5, 7, 11, 13, 17];

start_time = time.time();

# Returns the permutations of the "count" chars in each string in "strings".
def get_permutations(strings, count):
    permutations = [];
    for string in strings:
        if count <= 1:
            for char in string:
                permutations.append(char);
        else:
            for c in range(len(string)):
                char = string[c];
                stringlet = string[:c] + string[(c + 1):];
                stringlet_permutations = get_permutations([stringlet], count - 1);
                for p in range(len(stringlet_permutations)):
                    permutations.append(char + stringlet_permutations[p]);
    return permutations;

S = str(N);
length = len(S);
permutations = get_permutations([S], length);
qualifier_sum = 0;
for permutation in permutations:
    qualifies = True;
    for i in range(1, length - 2):
        substring = permutation[i : i + 3];
        if (int(substring) % primes[i - 1] != 0):
            qualifies = False;
            break;
    if qualifies:
        qualifier_sum += int(permutation);
        print permutation;
print "sum = %d." % qualifier_sum;

print "Execution time = %f seconds." % (time.time() - start_time);
