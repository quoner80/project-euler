# Special subset sums: optimum
# Problem 103
#
# Let S(A) represent the sum of elements in set A of size n. We shall call it a special sum set if for any two non-empty disjoint subsets, B and C, the following properties are true:
#
#    i. S(B) != S(C); that is, sums of subsets cannot be equal.
#   ii. If B contains more elements than C then S(B) > S(C).
#
# If S(A) is minimised for a given n, we shall call it an optimum special sum set. The first five optimum special sum sets are given below.
#   n = 1: {1}
#   n = 2: {1, 2}
#   n = 3: {2, 3, 4}
#   n = 4: {3, 5, 6, 7}
#   n = 5: {6, 9, 11, 12, 13}
#
# It seems that for a given optimum set, A = {a1, a2, ... , an}, the next optimum set is of the form B = {b, a1+b, a2+b, ... ,an+b}, where b is the "middle" element on the previous row.
#
# By applying this "rule" we would expect the optimum set for n = 6 to be A = {11, 17, 20, 22, 23, 24}, with S(A) = 117. However, this is not the optimum set, as we have merely applied an algorithm to provide a near optimum set. The optimum set for n = 6 is A = {11, 18, 19, 20, 22, 25}, with S(A) = 115 and corresponding set string: 111819202225.
#
# Given that A is an optimum special sum set for n = 7, find its set string.
#
# NOTE: This problem is related to Problem 105 and Problem 106.

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
                """
                print "%s is not special: condition 1 not met -> sums[%d][%d] = sums[%d][%d] = %d." \
                    % (sum_set, subset_size, i, subset_size, i + 1, subset_sums[subset_size][i]);
                """
                is_special = False;
                break;
        if not is_special:
            break;
    if is_special:
        # Condition ii. If B contains more elements than C then S(B) > S(C).
        for subset_size in range(1, set_size):
            if subset_sums[subset_size][-1] >= subset_sums[subset_size + 1][0]:
                """
                print "%s is not special: condition 2 not met -> sums[%d][-1] = %d >= sums[%d][0] = %d." \
                    % (sum_set, subset_size, subset_sums[subset_size][-1], subset_size + 1, subset_sums[subset_size + 1][0]);
                """
                is_special = False;
                break;
    """
    if is_special:
        print "%s is special." % sum_set;
    """
    return is_special;

#   n = 1: {1};                      sum =   1; differences = {}
#   n = 2: {1, 2};                   sum =   3; differences = {1}
#   n = 3: {2, 3, 4};                sum =   9; differences = {1, 1}
#   n = 4: {3, 5, 6, 7};             sum =  21; differences = {2, 1, 1}
#   n = 5: {6, 9, 11, 12, 13};       sum =  41; differences = {3, 2, 1, 1}
#   n = 6: {11, 18, 19, 20, 22, 25}; sum = 115; differences = {7, 1, 1, 2, 3}

sum_set_5_optimal = [6, 9, 11, 12, 13];
sum_set_6         = [11, 17, 20, 22, 23, 24];
sum_set_6_optimal = [11, 18, 19, 20, 22, 25];
# deltas          = [0,  +1, -1, -2, -1, +1] = -2

# Apply the "rule" to sum_set_6_optimal to get sum_set_7.
sum_set_7 = [20, 31, 38, 39, 40, 42, 45];
if not is_sum_set_special(sum_set_7):
    print "Premise failed! Program failed!";
else:
    sum_set_7_sum = sum(sum_set_7);
    sum_set_7_sum_optimal = sum_set_7_sum;
    sum_set_7_optimal = list(sum_set_7);
    print sum_set_7, sum_set_7_sum;
    deltas = [-4, -3, -2, -1, 0, 1, 2, 3];
    for a in deltas:
        sum_set_a = list(sum_set_7);
        sum_set_a[0] += a;
        for b in deltas:
            sum_set_b = list(sum_set_a);
            sum_set_b[1] += b;
            for c in deltas:
                sum_set_c = list(sum_set_b);
                sum_set_c[2] += c;
                for d in deltas:
                    sum_set_d = list(sum_set_c);
                    sum_set_d[3] += d;
                    for e in deltas:
                        sum_set_e = list(sum_set_d);
                        sum_set_e[4] += e;
                        for f in deltas:
                            sum_set_f = list(sum_set_e);
                            sum_set_f[5] += f;
                            for g in deltas:
                                sum_set_g = list(sum_set_f);
                                sum_set_g[6] += g;
                                if sum(sum_set_g) < sum_set_7_sum and is_sum_set_special(sum_set_g):
                                    sum_set_7_sum_optimal = sum(sum_set_g);
                                    sum_set_7_optimal = list(sum_set_g);
                                    print sum_set_7_optimal, sum_set_7_sum_optimal;
    print;
    print "optimal special sum set = %s; sum = %d." % (sum_set_7_optimal, sum_set_7_sum_optimal);
    set_string = "";
    for element in sum_set_7_optimal:
        set_string += str(element);
    print "optimal special sum set string = %s." % set_string;
    print;

print_execution_time();
