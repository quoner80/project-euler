# Largest exponential
# Problem 99
#
# Comparing two numbers written in index form like 2^11 and 3^7 is not difficult, as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.
#
# However, confirming that 632382^518061 > 519432^525806 would be much more difficult, as both numbers contain over three million digits.
#
# Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.
#
# NOTE: The first two lines in the file represent the numbers in the example given above.

import csv;
import math;
import time;

start_time = time.time();

def print_execution_time():
    print "Execution time = %f seconds." % (time.time() - start_time);

FILENAME = "p099_base_exp.txt";

max_log_number = 0;
argmax_line_number = 0;
argmax_base = 0;
argmax_exp = 0;
with open(FILENAME) as base_exp_file:
    base_exp_reader = csv.reader(base_exp_file);
    line_number = 1;
    for base_exp in base_exp_reader:
        base = int(base_exp[0]);
        exp = int(base_exp[1]);
        log_number = exp * math.log(base);
        print line_number, base, exp, log_number;
        if log_number > max_log_number:
            max_log_number = log_number;
            argmax_line_number = line_number;
            argmax_base = base;
            argmax_exp = exp;
        '''
        if line_number >= 2:
            break;
        '''
        line_number += 1;
print;
print "%d ^ %d is the largest, from line number %d." % (argmax_base, argmax_exp, argmax_line_number);
print;

print_execution_time();
