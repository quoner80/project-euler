# Coded triangle numbers
#
# The nth term of the sequence of triangle numbers is given by, t_n = n(n+1)/2; so the first ten triangle numbers are:
#   1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.
#
# Using p042_words.txt, a 16K text file containing nearly two-thousand common English words, how many are triangle words?

import csv;
import sys;
import time;

start_time = time.time();

FILENAME = "p042_words.txt";
# FILENAME = "p042_words_toy.txt";

LETTER_VALUE_EXCESS = ord('A') - 1;

MAX_TRIANGLE_N = 32;

triangles = [];
for n in range(1, MAX_TRIANGLE_N + 1):
    triangles.append(n * (n + 1) / 2);
max_triangle = triangles[-1];

triangle_count = 0;
with open(FILENAME, "rb") as csvfile:
    reader = csv.reader(csvfile);
    for words in reader:
        for word in words:
            value = 0;
            for letter in word:
                value += ord(letter) - LETTER_VALUE_EXCESS;
            if value > max_triangle:
                print "Failed due to insufficiently large triangles array.";
                sys.exit(-1);
            if value in triangles:
                print word, value;
                triangle_count += 1;
print "triangle_count = %d." % triangle_count;

print "Execution time = %f seconds." % (time.time() - start_time);
