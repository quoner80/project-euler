# Product-sum numbers
# Problem 88
#
# A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers, {a1, a2, ... , ak} is called a product-sum number: N = a_1 + a_2 + ... + a_k = a_1 x a_2 x ... x a_k.
#
# For example, 6 = 1 + 2 + 3 = 1 x 2 x 3.
#
# For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number. The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.
#   k = 2:  4 = 2 x 2 = 2 + 2
#   k = 3:  6 = 1 x 2 x 3 = 1 + 2 + 3
#   k = 4:  8 = 1 x 1 x 2 x 4 = 1 + 1 + 2 + 4
#   k = 5:  8 = 1 x 1 x 2 x 2 x 2 = 1 + 1 + 2 + 2 + 2
#   k = 6: 12 = 1 x 1 x 1 x 1 x 2 x 6 = 1 + 1 + 1 + 1 + 2 + 6
#
# Hence for 2 <= k <= 6, the sum of all the minimal product-sum numbers is 4 + 6 + 8 + 12 = 30; note that 8 is only counted once in the sum.
#
# In fact, as the complete set of minimal product-sum numbers for 2 <= k <= 12 is {4, 6, 8, 12, 15, 16}, the sum is 61.
#
# What is the sum of all the minimal product-sum numbers for 2 <= k <= 12000?

import cPickle as pickle;
import time;

start_time = time.time();

MAXIMUM_SET_SIZE = 12;
#MAXIMUM_SET_SIZE = 10;

def print_execution_time():
    print "Execution time = %f seconds." % (time.time() - start_time);

def extend_set_partitions_list(partitions_list):
    new_member = len(partitions_list);
    new_partitions_list = [];
    partitions = partitions_list[-1];
    for partition in partitions:
        new_partition = list(partition);
        new_partition.append([new_member]);
        # print new_partition;
        new_partitions_list.append(new_partition);
        for s in range(len(partition) - 1, -1, -1):
            new_partition = list(partition);
            subset = partition[s];
            new_subset = list(subset);
            new_partition.remove(subset);
            new_subset.append(new_member);
            new_partition.append(sorted(new_subset));
            # print new_partition;
            new_partitions_list.append(new_partition);
    partitions_list.append(new_partitions_list);

set_partitions_list = [
    [
        [
            [0]
        ]
    ]
];

while len(set_partitions_list) < MAXIMUM_SET_SIZE:
    extend_set_partitions_list(set_partitions_list);

pickle.dump(set_partitions_list, open("set_partitions_list.pickle", "wb"));

print_execution_time();
