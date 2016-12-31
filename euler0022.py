# Names scores
#
# Using p022_names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.
#
# What is the total of all the name scores in the file?

import csv;

FILENAME = "p022_names.txt";
# FILENAME = "p022_names_toy.txt";

LETTER_VALUE_EXCESS = ord('A') - 1;

total_score = 0;

with open(FILENAME, "rb") as csvfile:
    reader = csv.reader(csvfile);
    for names in reader:
        name_count = len(names);
        names = sorted(names);
        for i in range(name_count):
            name = names[i];
            # name = "COLIN";
            value = 0;
            for j in range(len(name)):
                value += ord(name[j]) - LETTER_VALUE_EXCESS;
            # Add 1 to convert from 0-based to 1-based index.
            score = value * (i + 1);
            # print name, value, score;
            total_score += score;
print total_score;
