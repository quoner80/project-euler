# Anagramic squares
# Problem 98
#
# By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 36^2. What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216 = 96^2. We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not permitted, neither may a different letter have the same digital value as another letter.
#
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).
#
# What is the largest square number formed by any member of such a pair?
#
# NOTE: All anagrams formed must be contained in the given text file.

import csv;
import math;
import sys;
import time;

start_time = time.time();

def print_execution_time():
    print "Execution time = %f seconds." % (time.time() - start_time);

def is_perfect_square(n):
    return (int(math.sqrt(n)) ** 2) == n;

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

class AnagramPair:
    ASCII_A = ord('A');
    word_a = None;
    word_b = None;
    keys = None;
    key_count = None;
    def __init__(self, word_a, word_b):
        self.word_a = word_a.word;
        self.word_b = word_b.word;
        self.keys = [];
        for letter_index in range(26):
            if word_a.letters[letter_index] != 0:
                self.keys.append(chr(self.ASCII_A + letter_index));
        self.key_count = len(self.keys);
    # If the specified permutation produces perfect squares from both words, returns the larger of the two perfect squares.
    # Otherwise returns 0.
    def get_larger_square(self, permutation):
        larger_square = 0;
        if len(permutation) != self.key_count:
            sys.exit("get_larger_square() was given a permutation of incorrect size.");
        dictionary = dict();
        for i in range(self.key_count):
            dictionary[self.keys[i]] = permutation[i];
        number_a = "";
        for letter in self.word_a:
            number_a += dictionary[letter];
        number_b = "";
        for letter in self.word_b:
            number_b += dictionary[letter];
        if number_a[0] != '0' and number_b[0] != '0':
            if is_perfect_square(int(number_a)) and is_perfect_square(int(number_b)):
                larger_square = max(int(number_a), int(number_b));
                print self.word_a, number_a;
                print self.word_b, number_b;
                print;
        return larger_square;

class Word:
    ASCII_A = ord('A');
    word = None;
    letters = None;
    def __init__(self, word):
        self.word = word;
        self.letters = [0] * 26;
        for letter in word:
            letter_index = ord(letter) - self.ASCII_A;
            self.letters[letter_index] += 1;
    def __cmp__(self, other):
        return cmp(self.letters, other.letters);
    def __str__(self):
        return self.word;

FILENAME = "p098_words.txt";

words = [];
pairs = [];

with open(FILENAME) as word_file:
    word_reader = csv.reader(word_file);
    for word_list in word_reader:
        for word in word_list:
            words.append(Word(word));
            # This limits the anagrams to one pair.
            '''
            if len(words) > 212:
                break;
            '''

# One optimization would be to group the pairs by key_count so the get_permutations would be called only one per key_count. It
# however turns out that only key_counts of 9 and 8 (there is no case for 7) are time-consuming, and there is only one each of
# 9 and 8, so there is no significant advantage to this grouping.
#
# Another optimization would be to order the pairs by key_count and stop as soon as one of the key counts produces a solution.
# This would have been beneficial if the solution came from one of the larger key_counts, but the solution turns out to come
# from a key_count of 5.

word_count = len(words);
for i in range(word_count):
    for j in range(i + 1, word_count):
        if words[i] == words[j]:
            pairs.append(AnagramPair(words[i], words[j]));

largest_square = 0;
largest_square_pair = None;
for pair in pairs:
    permutations = get_permutations(["0123456789"], pair.key_count);
    for permutation in permutations:
        larger_square = pair.get_larger_square(permutation);
        if larger_square > largest_square:
            largest_square = larger_square;
            largest_square_pair = pair;
print "The largest square is %d, from the anagram pair '%s' / '%s'." % (largest_square, largest_square_pair.word_a, largest_square_pair.word_b);
print;

print_execution_time();
