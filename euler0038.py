# Pandigital multiples
#
# Take the number 192 and multiply it by each of 1, 2, and 3:
#   192 x 1 = 192
#   192 x 2 = 384
#   192 x 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
#
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
#
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1, 2, ..., n) where n > 1?

import time;

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

def test_2_term_sum(n):
    string = str(n) + str(n * 2);
    is_pandigital = False;
    if string.find("1") >= 0:
        if string.find("2") >= 0:
            if string.find("3") >= 0:
                if string.find("4") >= 0:
                    if string.find("5") >= 0:
                        if string.find("6") >= 0:
                            if string.find("7") >= 0:
                                if string.find("8") >= 0:
                                    if string.find("9") >= 0:
                                        is_pandigital = True;
                                        print string;
    return is_pandigital;

# The problem description already indicates 918273645 is a solution, so if there is a larger solution, it must start with a 9.
# The base number cannot be 9 by itself since that is the base of the given solution. So it must be at least 2 digits.
# The base cannot be 2 digits because:
#   1 x 9? is 2 digits
#   2 x 9? is 3 digits
#   3 x 9? is 3 digits -> total of  8 digits -> too few
#   4 x 9? is 3 digits -> total of 11 digits -> too many
# The base cannot be 3 digits because:
#   1 x 9?? is 3 digits
#   2 x 9?? is 4 digits -> total of  7 digits -> too few
#   3 x 9?? is 4 digits -> total of 11 digits -> too many
# The base, if it exists, then must be 4 digits because:
#   1 x 9??? is 4 digits
#   2 x 9??? is 5 digits -> total of  9 digits -> just right
# The base must be less than 95?? because 9[5-8]?? x 2 = 19???, which would make the concatenation 9[5-8]??19??? which has 2 9's.
# So start at 94?? and test all the possibilities, then 93??, then 92??, then 91??. The first one found is the largest solution.
# If there is none found, then 918273645 is the largest solution.

permutations = get_permutations(["8765321"], 2);
for permutation in permutations:
    test_2_term_sum(int("94" + permutation));

permutations = get_permutations(["8765421"], 2);
for permutation in permutations:
    test_2_term_sum(int("93" + permutation));

permutations = get_permutations(["8765431"], 2);
for permutation in permutations:
    test_2_term_sum(int("92" + permutation));

permutations = get_permutations(["8765432"], 2);
for permutation in permutations:
    test_2_term_sum(int("91" + permutation));

print "Execution time = %f seconds." % (time.time() - start_time);
