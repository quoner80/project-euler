# Pandigital products
#
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

# 123456789 has 9! permutations.
# The x can go into 1 of 7 positions: 1 x 23456789 to 1234567 x 89.
# If the x is after digit i, the = can go into 1 of (8 - i) positions (to the right of the x and after at least 1 digit).
# The total permutations of x and = is thus: 7 + 6 + 5 + 4 + 3 + 2 + 1 = 28.
# Total permuations = 28 * 9! = 28 * 362,880 = 10,160,640 = 10160640.

import time;

start_time = time.time();

S = "123456789";
# S = "12345678";

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

string_length = len(S);
strings = [S];
permutations = get_permutations(strings);
permutation_count = len(permutations);
print "Number of permutations = %d." % permutation_count;
unique_products = set();
for i in range(permutation_count):
    permutation = permutations[i];
    for x in range(1, string_length):
        multiplicand = int(permutation[0 : x]);
        for e in range(x + 1, string_length):
            multiplier = int(permutation[x : e]);
            product = int(permutation[e: string_length]);
            if (multiplicand * multiplier == product):
                print "%d x %d = %d" % (multiplicand, multiplier, product);
                unique_products.add(product);
print "unique products: %s" % unique_products;
unique_product_sum = 0;
for unique_product in unique_products:
    unique_product_sum += unique_product;
print "unique product sum = %d" % unique_product_sum;
print "Execution time = %f seconds." % (time.time() - start_time);
