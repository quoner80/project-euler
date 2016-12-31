# 1000-digit Fibonacci number
#
# The Fibonacci sequence is defined by the recurrence relation:
#   Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
#
# Hence the first 12 terms will be:
#   F1 = 1
#   F2 = 1
#   F3 = 2
#   F4 = 3
#   F5 = 5
#   F6 = 8
#   F7 = 13
#   F8 = 21
#   F9 = 34
#   F10 = 55
#   F11 = 89
#   F12 = 144
#
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

'''
import math;
import time;

SQRT_5 = math.sqrt(5.0);
PHI = (1.0 + SQRT_5) / 2.0;

def get_fibonacci_n(n):
    global PHI;
    global SQRT_5;
    fibonacci_n = ((PHI ** n) - (1.0 - PHI) ** n) / SQRT_5;
    digits = len(str(int(fibonacci_n)));
    print "fibonacci(%d){%d digit%s} = %f." % (n, digits, ("s" if digits != 1 else ""), fibonacci_n);
    return fibonacci_n;

start_time = time.time();
print "PHI = %s." % str(PHI);
for n in range(1, 13):
    get_fibonacci_n(n);
get_fibonacci_n(1000);
get_fibonacci_n(1474);
# get_fibonacci_n(1475); # Causes OverflowError.
print "Execution time = %f seconds." % (time.time() - start_time);
'''

import decimal;
import time;

# Don't initialize these until after setting the decimal precision.
SQRT_5 = 0;
PHI = 0;

def get_fibonacci_n(n, display_f = True):
    global PHI;
    global SQRT_5;
    n = decimal.Decimal(n);
    fibonacci_n = decimal.Decimal.to_integral_exact(((PHI ** n) - (decimal.Decimal(1.0) - PHI) ** n) / SQRT_5);
    digits = len(str(fibonacci_n));
    if display_f:
        print "fibonacci(%d){%d digit%s} = %s." % (n, digits, ("s" if digits != 1 else ""), fibonacci_n);
    else:
        print "fibonacci(%d){%d digit%s}." % (n, digits, ("s" if digits != 1 else ""));        
    return fibonacci_n;

start_time = time.time();
decimal.getcontext().prec = 1100;
print decimal.getcontext();
SQRT_5 = decimal.Decimal(5.0).sqrt();
PHI = (decimal.Decimal(1.0) + SQRT_5) / decimal.Decimal(2.0);
print "SQRT_5 = %s." % str(SQRT_5);
print "PHI = %s." % str(PHI);
for n in range(1, 13):
    get_fibonacci_n(n);
get_fibonacci_n(1000, False);
get_fibonacci_n(1474, False);
get_fibonacci_n(1475, False);
get_fibonacci_n(2000, False);
get_fibonacci_n(5000, False);
get_fibonacci_n(4900, False);
get_fibonacci_n(4800, False);
get_fibonacci_n(4790, False);
get_fibonacci_n(4780, False);
for n in range(4780, 4790):
    get_fibonacci_n(n, False);
f_4780 = get_fibonacci_n(4780);
f_4781 = get_fibonacci_n(4781);
f_4782 = get_fibonacci_n(4782);
print "f_4780 + f_4781 - f_4782 = %s." % (f_4780 + f_4781 - f_4782);
print "Execution time = %f seconds." % (time.time() - start_time);
