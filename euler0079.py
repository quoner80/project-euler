# Passcode derivation
#
# A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.
#
# The text file, keylog.txt, contains fifty successful login attempts.
#
# Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.

import time;

start_time = time.time();

FILENAME = "p079_keylog.txt";

def is_ordered_subcode(subcode, passcode):
    valid = True;
    passcode_string = str(passcode);
    subcode_string = str(subcode);
    for digit in subcode_string:
        index = passcode_string.find(digit);
        if index < 0:
            valid = False;
        else:
            passcode_string = passcode_string[index + 1:]
    if valid:
        print "%d is a valid ordered subcode of %d." % (subcode, passcode);
    else:
        print "%d is NOT a valid ordered subcode of %d." % (subcode, passcode);
    return valid;

is_left_of = [];
is_right_of = [];
for i in range(10):
    is_left_of.append(set());
    is_right_of.append(set());
keys = set();
digits = set();
with open(FILENAME) as key_file:
    for key_line in key_file:
        key = str(int(key_line));
        keys.add(key);
        digit0 = int(key[0]);
        digit1 = int(key[1]);
        digit2 = int(key[2]);
        is_left_of[digit0].add(digit1);
        is_left_of[digit1].add(digit2);
        is_right_of[digit2].add(digit1);
        is_right_of[digit1].add(digit0);
        digits.add(digit0);
        digits.add(digit1);
        digits.add(digit2);

print sorted(keys);
print;
print sorted(digits);
print;
print is_left_of;
print;
print is_right_of;
print;

# Solved by inspection from clues above:
N = 73162890;

is_valid_passcode = True;
for subcode in keys:
    if not is_ordered_subcode(int(subcode), N):
        is_valid_passcode = False;
        break;
if is_valid_passcode:
    print "%d is a valid passcode." % N;
else:
    print "%d is NOT a valid passcode." % N;

print;
print "Execution time = %f seconds." % (time.time() - start_time);
