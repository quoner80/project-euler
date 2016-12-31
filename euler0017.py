# Number letter counts
#
# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

import sys;

N = 1000;

LOWER_LIMIT = 1;
UPPER_LIMIT = 1000;

TEEN     = "teen";
HUNDRED  = "hundred";
THOUSAND = "thousand";

def get_english_string(n):
    if n < LOWER_LIMIT:
        print "%d is beneath the lower limit of %d." % (n, LOWER_LIMIT);
    elif n == 1:
        return "one";
    elif n == 2:
        return "two";
    elif n == 3:
        return "three";
    elif n == 4:
        return "four";
    elif n == 5:
        return "five";
    elif n == 6:
        return "six";
    elif n == 7:
        return "seven";
    elif n == 8:
        return "eight";
    elif n == 9:
        return "nine";
    elif n == 10:
        return "ten";
    elif n == 11:
        return "eleven";
    elif n == 12:
        return "twelve";
    elif n == 13:
        return "thir" + TEEN;
    elif n == 14:
        return get_english_string(4) + TEEN;
    elif n == 15:
        return "fif" + TEEN;
    elif n >= 16 and n <= 17:
        return get_english_string(n - 10) + TEEN;
    elif n == 18:
        return "eigh" + TEEN;
    elif n == 19:
        return get_english_string(9) + TEEN;
    elif n == 20:
        return "twenty";
    elif n >= 21 and n <= 29:
        return get_english_string(20) + "-" + get_english_string(n - 20);
    elif n == 30:
        return "thirty";
    elif n >= 31 and n <= 39:
        return get_english_string(30) + "-" + get_english_string(n - 30);
    elif n == 40:
        return "forty";
    elif n >= 41 and n <= 49:
        return get_english_string(40) + "-" + get_english_string(n - 40);
    elif n == 50:
        return "fifty";
    elif n >= 51 and n <= 59:
        return get_english_string(50) + "-" + get_english_string(n - 50);
    elif n == 60:
        return "sixty";
    elif n >= 61 and n <= 69:
        return get_english_string(60) + "-" + get_english_string(n - 60);
    elif n == 70:
        return "seventy";
    elif n >= 71 and n <= 79:
        return get_english_string(70) + "-" + get_english_string(n - 70);
    elif n == 80:
        return "eighty";
    elif n >= 81 and n <= 89:
        return get_english_string(80) + "-" + get_english_string(n - 80);
    elif n == 90:
        return "ninety";
    elif n >= 91 and n <= 99:
        return get_english_string(90) + "-" + get_english_string(n - 90);
    elif n >= 100 and n <= 999:
        string = get_english_string(n / 100) + " " + HUNDRED;
        remainder = n % 100
        if remainder != 0:
            string += " and " + get_english_string(remainder);
        return string;
    elif n == 1000:
        return get_english_string(1) + " " + THOUSAND;
    elif n > UPPER_LIMIT:
        print "%d exceeds the upper limit of %d." % (n, UPPER_LIMIT);
    print "%d is not supported." % n;
    sys.exit(-1);
    return "";

def get_non_space_non_hypen_count(s):
    count = 0;
    for i in range(len(s)):
        if s[i] != " " and s[i] != "-":
            count += 1;
    return count;

'''
english_string = get_english_string(115);
print english_string
print get_non_space_non_hypen_count(english_string);
english_string = get_english_string(342);
print english_string
print get_non_space_non_hypen_count(english_string);
'''
aggregate_string = "";
for i in range(1, N + 1):
    english_string = get_english_string(i);
    aggregate_string += english_string;
    print english_string;
# print english_string;
# print len(english_string);
print get_non_space_non_hypen_count(aggregate_string);
