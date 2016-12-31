# Pandigital Fibonacci ends
# Problem 104
#
# The Fibonacci sequence is defined by the recurrence relation:
# F_n = F_n-1 + F_n-2, where F_1 = 1 and F_2 = 1.
#
# It turns out that F_541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order). And F_2749, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.
#
# Given that F_k is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.

import time;

start_time = time.time();

def print_execution_time():
    print "Execution time = %f seconds." % (time.time() - start_time);

def is_string_pandigital(string):
    is_pandigital = False;
    if string.find("1") >= 0:
        if string.find("2") >= 0:
            if string.find("3") >= 0:
                if string.find("4") >= 0:
                    if string.find("5") >= 0:
                        if string.find("6") >= 0:
                            if string.find("7") >= 0:
                                if string.find("8") >= 0:
                                    if string.find("9") >= 0:
                                        is_pandigital = True;
    return is_pandigital;

fibonacci_n_minus_2 = 1;
fibonacci_n_minus_1 = 1;
n = 3;
while True:
    fibonacci_n = fibonacci_n_minus_1 + fibonacci_n_minus_2;
    # print n, fibonacci_n;
    fibonacci_string = str(fibonacci_n);
    fibonacci_string_first_9 = fibonacci_string[:9];
    fibonacci_string_last_9 = fibonacci_string[-9:];
    first_9_pandigital = is_string_pandigital(fibonacci_string_first_9);
    last_9_pandigital = is_string_pandigital(fibonacci_string_last_9);
    if first_9_pandigital:
        print "First 9 digits are pandigital for F_%d." % n;
    if last_9_pandigital:
        print "Last 9 digits are pandigital for F_%d." % n;
    if first_9_pandigital and last_9_pandigital:
        print fibonacci_string;
        print "First and last 9 digits are pandigital for F_%d." % n;
        break;
    n += 1;
    fibonacci_n_minus_2 = fibonacci_n_minus_1;
    fibonacci_n_minus_1 = fibonacci_n;

print_execution_time();
