# Digit cancelling fractions
#
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

import time;

start_time = time.time();

numerator_product = 1;
denominator_product = 1;
for denominator in range(10, 100):
    for numerator in range(10, denominator):
        correct = float(numerator) / denominator;
        numerator_tens = numerator / 10;
        numerator_ones = numerator % 10;
        denominator_tens = denominator / 10;
        denominator_ones = denominator % 10;
        if not (numerator_ones == 0 and denominator_ones == 0):
            if (denominator_ones != 0):
                if (numerator_tens == denominator_tens) and (correct == (float(numerator_ones) / denominator_ones)):
                    print "%d/%d = %d/%d = %f" % (numerator, denominator, numerator_ones, denominator_ones, correct);
                    numerator_product *= numerator_ones;
                    denominator_product *= denominator_ones;
                if (numerator_ones == denominator_tens) and (correct == (float(numerator_tens) / denominator_ones)):
                    print "%d/%d = %d/%d = %f" % (numerator, denominator, numerator_tens, denominator_ones, correct);
                    numerator_product *= numerator_tens;
                    denominator_product *= denominator_ones;
            if (denominator_tens != 0):
                if (numerator_tens == denominator_ones) and (correct == (float(numerator_ones) / denominator_tens)):
                    print "%d/%d = %d/%d = %f" % (numerator, denominator, numerator_ones, denominator_tens, correct);
                    numerator_product *= numerator_ones;
                    denominator_product *= denominator_tens;
                if (numerator_ones == denominator_ones) and (correct == (float(numerator_tens) / denominator_tens)):
                    print "%d/%d = %d/%d = %f" % (numerator, denominator, numerator_tens, denominator_tens, correct);
                    numerator_product *= numerator_tens;
                    denominator_product *= denominator_tens;
print "product = %d/%d" % (numerator_product, denominator_product);
# This is a cheat since I already know the numerator divides the denominator. Otherwise I'd need to write a general factoring and canceling function.
if denominator_product % numerator_product == 0:
    print "product = %d/%d" % (1, denominator_product / numerator_product);

print "Execution time = %f seconds." % (time.time() - start_time);
