# Prime pair sets
#
# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
#
# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

import math;
import time;

start_time = time.time();

primes = [];
prime_count = None;
prime_max = None;
sieve = None;

def is_prime(n):
    is_n_prime = True;
    if n <= prime_max:
        is_n_prime = sieve[n];
    else:
        prime_factor_max = int(math.ceil(math.sqrt(n)));
        if prime_factor_max > prime_max:
            print "is_prime(%d) failed due to insufficiently large primes table." % n;
            sys.exit(-1);
        else:
            for p in primes:
                if p > prime_factor_max:
                    break;
                if n % p == 0:
                    is_n_prime = False;
                    break;
    return is_n_prime;

def test_list_internally(prime_list):
    all_prime = True;
    length = len(prime_list);
    for i in range(length):
        p = prime_list[i];
        for j in range(i + 1, length):
            q = prime_list[j];
            pq = int(str(p) + str(q));
            if not is_prime(pq):
                #print "%d+%d = %d is not prime." % (p, q, pq);
                all_prime = False;
                break;
            qp = int(str(q) + str(p));
            if not is_prime(qp):
                #print "%d+%d = %d is not prime." % (q, p, pq);
                all_prime = False;
                break;
        if not all_prime:
            break;
    return all_prime;

def test_list_against_prime(prime_list, prime):
    all_prime = True;
    length = len(prime_list);
    for i in range(length):
        p = prime_list[i];
        if not is_prime(int(str(p) + str(prime))) or not is_prime(int(str(prime) + str(p))):
            all_prime = False;
            break;
    return all_prime;

# Read the primes from a file, and initialize the Sieve of Eratosthenes.
# infile = open("primes_below_2_million.txt", "r");
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

found = False;
array = [3, 7, 109, 673];
for p in primes:
    # print p;
    if test_list_against_prime(array, p):
        print "%s sum = %d" % (array + [p], sum(array) + p);
        break;

print "Execution time = %f seconds." % (time.time() - start_time);
