# Special subset sums: meta-testing
# Problem 106
#
# Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:
#
#    i. S(B) != S(C); that is, sums of subsets cannot be equal.
#   ii. If B contains more elements than C then S(B) > S(C).
#
# For this problem we shall assume that a given set contains n strictly increasing elements and it already satisfies the second rule.
#
# Surprisingly, out of the 25 possible subset pairs that can be obtained from a set for which n = 4, only 1 of these pairs need to be tested for equality (first rule). Similarly, when n = 7, only 70 out of the 966 subset pairs need to be tested.
#
# For n = 12, how many of the 261625 subset pairs that can be obtained need to be tested for equality?
#
# NOTE: This problem is related to Problem 103 and Problem 105.

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

def get_integer_set_sum_string(integer_set):
    sum_set_sum_string = "";
    for integer in integer_set:
        sum_set_sum_string += (str(integer) + '+');
    sum_set_sum_string = sum_set_sum_string[:-1];
    sum_set_sum_string += ('=' + str(sum(integer_set)));
    return sum_set_sum_string;

def are_sets_disjoint(set_a, set_b):
    disjoint = set(set_a).isdisjoint(set(set_b));
    return disjoint;

# If each member of ordered_set_a is less than the corresponding member of ordered_set_b, then the sum of ordered_set_a must be
# less than (and therefore unequal to) the sum of ordered_set_b. If any member of ordered_set_a is greater than or equal to the
# corresponding member of ordered_set_b, then the sums are possibly equal.
def are_sets_possibly_equal(ordered_set_a, ordered_set_b):
    possibly_equal = False;
    set_size = len(ordered_set_a);
    for i in range(set_size):
        if ordered_set_a[i] > ordered_set_b[i]:
            possibly_equal = True;
            break;
    return possibly_equal;

def compare_sum_set_same_sized_disjoint_subset_pairs(sum_set):
    pair_count = 0;
    possibly_equal_pair_count = 0;
    set_size = len(sum_set);
    subsets = [];
    for subset_size in range(1, set_size + 1):
        subsets.extend(get_combinations(sum_set, subset_size));
    subset_pairs = get_combinations(subsets, 2);
    for subset_pair in subset_pairs:
        if are_sets_disjoint(subset_pair[0], subset_pair[1]):
            if len(subset_pair[0]) == len(subset_pair[1]):
                if are_sets_possibly_equal(subset_pair[0], subset_pair[1]):
                    possibly_equal_pair_count += 1;
                    '''
                    print "%s ? %s" % (get_integer_set_sum_string(subset_pair[0]), get_integer_set_sum_string(subset_pair[1]));
                    '''
            pair_count += 1;
    print "n = %d: %d of %d pairs must be tested for equality." % (len(sum_set), possibly_equal_pair_count, pair_count);

compare_sum_set_same_sized_disjoint_subset_pairs([1, 2, 3, 4]);
compare_sum_set_same_sized_disjoint_subset_pairs([1, 2, 3, 4, 5, 6, 7]);
compare_sum_set_same_sized_disjoint_subset_pairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]);

print_execution_time();
