# Lexicographic permutations
#
# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

# (This was not used.)
# 0?????????? : first 9! : 0000001 - 0362880
# 1?????????? : next 9!  : 0362881 - 0725760
# 2?????????? : next 9!  : 0725761 - 1088640

import time;

S = "0123456789";
N = 1000000;

def get_permutations(strings):
    permutations = [];
    for s in range(len(strings)):
        string = strings[s];
        length = len(string);
        if length < 2:
            permutations.append(string);
        else:
            for c in range(length):
                char = string[c];
                stringlet = string[:c] + string[(c + 1):];
                stringlet_permutations = get_permutations([stringlet]);
                for p in range(len(stringlet_permutations)):
                    permutations.append(char + stringlet_permutations[p]);
    return permutations;

start_time = time.time();
strings = [S];
permutations = get_permutations(strings);
print "Number of permutations = %d." % len(permutations);
print "%dth permutation = %s." % (N, permutations[N - 1]);
print "Execution time = %f seconds." % (time.time() - start_time);
