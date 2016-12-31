# Roman numerals
# Problem 89
#
# For a number written in Roman numerals to be considered valid there are basic rules which must be followed. Even though the rules allow some numbers to be expressed in more than one way there is always a "best" way of writing a particular number.
#
# For example, it would appear that there are at least six ways of writing the number sixteen:
#
#   IIIIIIIIIIIIIIII
#   VIIIIIIIIIII
#   VVIIIIII
#   XIIIIII
#   VVVI
#   XVI
#
# However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most efficient, as it uses the least number of numerals.
#
# The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid, but not necessarily minimal, Roman numerals; see About... Roman Numerals for the definitive rules for this problem.
#
# Find the number of characters saved by writing each of these in their minimal form.
#
# Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.

import sys;
import time;

start_time = time.time();

I = 1;
V = 5;
X = 10;
L = 50;
C = 100;
D = 500;
M = 1000;

def print_execution_time():
    print "Execution time = %f seconds." % (time.time() - start_time);

def get_integer_from_roman_character(roman_character):
    integer = 0;
    if roman_character == 'I':
        integer = I;
    elif roman_character == 'V':
        integer = V;
    elif roman_character == 'X':
        integer = X;
    elif roman_character == 'L':
        integer = L;
    elif roman_character == 'C':
        integer = C;
    elif roman_character == 'D':
        integer = D;
    elif roman_character == 'M':
        integer = M;
    else:
        sys.exit("%s is an invalid Roman numeral character." % roman_character);
    return integer;

def get_integer_from_roman_string(roman_string):
    integer = 0;
    length_minus_1 = len(roman_string) - 1;
    for i in range(length_minus_1):
        integer_1 = get_integer_from_roman_character(roman_string[i]);
        integer_2 = get_integer_from_roman_character(roman_string[i + 1]);
        if integer_1 < integer_2:
            integer -= integer_1;
        else:
            integer += integer_1;
    integer += get_integer_from_roman_character(roman_string[length_minus_1]);
    return integer;

def get_roman_string_from_integer_ones(ones):
    string = "";
    if ones == 4:
        string = "IV";
    elif ones == 9:
        string = "IX";
    else:
        if ones >= 5:
            string = "V";
            ones -= 5;
        string += ("I" * ones);
    return string;

def get_roman_string_from_integer_tens(tens):
    string = "";
    if tens == 4:
        string = "XL";
    elif tens == 9:
        string = "XC";
    else:
        if tens >= 5:
            string = "L";
            tens -= 5;
        string += ("X" * tens);
    return string;

def get_roman_string_from_integer_hundreds(hundreds):
    string = "";
    if hundreds == 4:
        string = "CD";
    elif hundreds == 9:
        string = "CM";
    else:
        if hundreds >= 5:
            string = "D";
            hundreds -= 5;
        string += ("C" * hundreds);
    return string;

def get_roman_string_from_integer_thousands(thousands):
    string = ("M" * thousands);
    return string;

def get_roman_string_from_integer(integer):
    string = get_roman_string_from_integer_thousands(integer / 1000);
    integer %= 1000;
    string += get_roman_string_from_integer_hundreds(integer / 100);
    integer %= 100;
    string += get_roman_string_from_integer_tens(integer / 10);
    integer %= 10;
    string += get_roman_string_from_integer_ones(integer);
    return string;

"""
for n in range(1, 10):
    print get_roman_string_from_integer_ones(n);
for n in range(1, 10):
    print get_roman_string_from_integer_tens(n);
for n in range(1, 10):
    print get_roman_string_from_integer_hundreds(n);
for n in range(1, 10):
    print get_roman_string_from_integer_thousands(n);

for n in range(1, 50):
    print get_roman_string_from_integer(n);
"""

total_length_difference = 0;
infile = open("p089_roman.txt", "r");
for roman_string in infile:
    if roman_string[-1] == '\n':
        roman_string = roman_string[:-1];
    integer = get_integer_from_roman_string(roman_string);
    string = get_roman_string_from_integer(integer);
    length_difference = len(roman_string) - len(string);
    total_length_difference += length_difference;
    print roman_string, integer, string, length_difference;
infile.close();
print "total_length_difference = %d." % total_length_difference;

print_execution_time();
