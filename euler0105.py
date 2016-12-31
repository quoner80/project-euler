# Special subset sums: testing
# Problem 105
#
# Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:
#
#    i. S(B) != S(C); that is, sums of subsets cannot be equal.
#   ii. If B contains more elements than C then S(B) > S(C).
#
# For example, {81, 88, 75, 42, 87, 84, 86, 65} is not a special sum set because 65 + 87 + 88 = 75 + 81 + 84, whereas {157, 150, 164, 119, 79, 159, 161, 139, 158} satisfies both rules for all possible subset pair combinations and S(A) = 1286.
#
# Using sets.txt (right click and "Save Link/Target As..."), a 4K text file with one-hundred sets containing seven to twelve elements (the two examples given above are the first two sets in the file), identify all the special sum sets, A_1, A_2, ..., A_k, and find the value of S(A_1) + S(A_2) + ... + S(A_k).
#
# NOTE: This problem is related to Problem 103 and Problem 106.

import csv;
import time;

start_time = time.time();

def print_execution_time():
    print "Execution time = %f seconds." % (time.time() - start_time);

# Returns the combinations of "count" elements in "array".
# For example, for ([1,2,3,4], 2), returns ([1,2], [1,3], [1,4], [2,3], [2,4], [3,4]).
def get_combinations(array, count):
    combinations = [];
    if count == 1:
        for element in array:
            combinations.append([element]);
    else:
        for i in range(len(array) - count + 1):
            subcombinations = get_combinations(array[i + 1 : ], count - 1);
            for subcombination in subcombinations:
                combinations.append([array[i]] + subcombination);
    return combinations;

def is_sum_set_special(sum_set):
    is_special = True;
    set_size = len(sum_set);
    subset_sums = [None] * (set_size + 1);
    for subset_size in range(1, set_size + 1):
        subsets = get_combinations(sum_set, subset_size);
        subset_sums[subset_size] = [];
        for subset in subsets:
            subset_sums[subset_size].append(sum(subset));
        subset_sums[subset_size].sort();
        # Condition i. S(B) != S(C); that is, sums of subsets cannot be equal.
        subset_count = len(subset_sums[subset_size]);
        for i in range(subset_count - 1):
            if subset_sums[subset_size][i] == subset_sums[subset_size][i + 1]:
                print "%s not special: c1 -> sums[%d][%d] = sums[%d][%d] = %d." \
                    % (sum_set, subset_size, i, subset_size, i + 1, subset_sums[subset_size][i]);
                is_special = False;
                break;
        if not is_special:
            break;
    if is_special:
        # Condition ii. If B contains more elements than C then S(B) > S(C).
        for subset_size in range(1, set_size):
            if subset_sums[subset_size][-1] >= subset_sums[subset_size + 1][0]:
                print "%s not special: c2 -> sums[%d][last] = %d >= sums[%d][0] = %d." \
                    % (sum_set, subset_size, subset_sums[subset_size][-1], subset_size + 1, subset_sums[subset_size + 1][0]);
                is_special = False;
                break;
    if is_special:
        print "%s is special." % sum_set;
    return is_special;

FILENAME = "p105_sets.txt";

special_sum_set_sum = 0;
with open(FILENAME) as sum_set_file:
    sum_set_reader = csv.reader(sum_set_file);
    for sum_set in sum_set_reader:
        sum_set_size = len(sum_set);
        for i in range(sum_set_size):
            sum_set[i] = int(sum_set[i]);
        if is_sum_set_special(sum_set):
            special_sum_set_sum += sum(sum_set);
print;
print "special_sum_set_sum = %d." % special_sum_set_sum;
print;

print_execution_time();
