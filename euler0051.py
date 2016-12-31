# Prime digit replacements
#
# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
#
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.
#
# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

import sys;
import time;

TARGET_REPLACEMENT_PRIME_COUNT = 8;

start_time = time.time();

# Returns the combinations of "count" elements in "array".
# For example, for ([1,2,3,4], 2), returns ([1,2], [1,3], [1,4], [2,3], [2,4], [3,4]).
def get_combinations(array, count):
    combinations = [];
    if count == 1:
        for element in array:
            #print "[element]: " + str([element]);
            combinations.append([element]);
    else:
        for i in range(len(array) - count + 1):
            subcombinations = get_combinations(array[i + 1 : ], count - 1);
            #print "subcombinations: " + str(subcombinations);
            for subcombination in subcombinations:
                #print "[array[i]] + subcombination: " + str([array[i]] + subcombination);
                combinations.append([array[i]] + subcombination);
    return combinations;

# Read the primes from a file, and initialize the Sieve of Eratosthenes.
primes = [];
infile = open("primes.txt", "r");
for line in infile:
    primes.append(int(line));
infile.close();
prime_count = len(primes);
prime_max = primes[-1];
print "known prime count = %d" % prime_count;
print "known prime max   = %d" % prime_max;
sieve = [False] * (prime_max + 1);
for prime in primes:
    sieve[prime] = True;

length = 1;
found = False;
while True:
    # print "length = %d" % length;
    positions = [];
    for position in range(length):
        positions.append(position);
    for replacement_count in range(1, length + 1):
        combinations = get_combinations(positions, replacement_count);
        for combination in combinations:
            anchor_length = length - replacement_count;
            # print str(combination) + " " + str(anchor_length);
            for anchor_number in range(10 ** (anchor_length)):
                # Create the anchor--the part that doesn't get replaced.
                anchor_string = str(anchor_number);
                # Pad with enough leading zeros so the string length = anchor_length.
                anchor_string_length = len(anchor_string);
                if anchor_string_length < anchor_length:
                    for i in range(anchor_length - anchor_string_length):
                        anchor_string = '0' + anchor_string;
                candidate_list = [None] * length;
                anchor_index = 0;
                for candidate_index in range(length):
                    if candidate_index in combination:
                        candidate_list[candidate_index] = '*';
                    else:
                        candidate_list[candidate_index] = anchor_string[anchor_index];
                        anchor_index += 1;

                # Count how many of the results of the replacements are prime.
                candidate_wildcarded = str("".join(candidate_list));
                replacement_prime_count = 0;
                for digit in range(10):
                    digit_char = str(digit);
                    for replacement_index in combination:
                        candidate_list[replacement_index] = digit_char;
                    candidate_string = str("".join(candidate_list));
                    # Don't count numbers that start with 0.
                    if candidate_string[0] != '0':
                        candidate = int(candidate_string);
                        if candidate > prime_max:
                            print "Algorithm failed due to insufficiently large primes table."
                            sys.exit(-1);
                        if sieve[candidate]:
                            replacement_prime_count += 1;
                # print candidate_list, combination, replacement_prime_count;

                # Stop after the target count is found.
                if replacement_prime_count >= TARGET_REPLACEMENT_PRIME_COUNT:
                    found = True;
                    print;
                    print "%s:" % candidate_wildcarded;
                    for digit in range(10):
                        digit_char = str(digit);
                        for replacement_index in combination:
                            candidate_list[replacement_index] = digit_char;
                        candidate_string = str("".join(candidate_list));
                        # Don't count numbers that start with 0.
                        if candidate_string[0] != '0' and sieve[int(candidate_string)]:
                            print " " + candidate_string;
                    print;
                    break;
            if found:
                break;
        if found:
            break;
    if found:
        break;
    length += 1;

print "Execution time = %f seconds." % (time.time() - start_time);
