# Prime pair sets
#
# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
#
# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

import math;
import time;
import sys;

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

def test_singles_list_for_new_pairs(prime_singles_list, new_prime):
    new_pairs = [];
    for prime in prime_singles_list:
        if (
            is_prime(int(str(prime) + str(new_prime))) and
            is_prime(int(str(new_prime) + str(prime)))
        ):
            new_pairs.append([prime, new_prime]);
    return new_pairs;

def test_pairs_list_for_new_trios(prime_pairs_list, new_prime):
    new_trios = [];
    for prime_pair in prime_pairs_list:
        if (
            is_prime(int(str(prime_pair[0]) + str(new_prime))) and
            is_prime(int(str(prime_pair[1]) + str(new_prime))) and
            is_prime(int(str(new_prime) + str(prime_pair[0]))) and
            is_prime(int(str(new_prime) + str(prime_pair[1])))
        ):
            new_trios.append(prime_pair + [new_prime]);
    return new_trios;

def test_trios_list_for_new_quartets(prime_trios_list, new_prime):
    new_quartets = [];
    for prime_trio in prime_trios_list:
        if (
            is_prime(int(str(prime_trio[0]) + str(new_prime))) and
            is_prime(int(str(prime_trio[1]) + str(new_prime))) and
            is_prime(int(str(prime_trio[2]) + str(new_prime))) and
            is_prime(int(str(new_prime) + str(prime_trio[0]))) and
            is_prime(int(str(new_prime) + str(prime_trio[1]))) and
            is_prime(int(str(new_prime) + str(prime_trio[2])))
        ):
            new_quartets.append(prime_trio + [new_prime]);
    return new_quartets;

def test_quartets_list_for_new_quintets(prime_quartets_list, new_prime):
    new_quintets = [];
    for prime_quartet in prime_quartets_list:
        if (
            is_prime(int(str(prime_quartet[0]) + str(new_prime))) and
            is_prime(int(str(prime_quartet[1]) + str(new_prime))) and
            is_prime(int(str(prime_quartet[2]) + str(new_prime))) and
            is_prime(int(str(prime_quartet[3]) + str(new_prime))) and
            is_prime(int(str(new_prime) + str(prime_quartet[0]))) and
            is_prime(int(str(new_prime) + str(prime_quartet[1]))) and
            is_prime(int(str(new_prime) + str(prime_quartet[2]))) and
            is_prime(int(str(new_prime) + str(prime_quartet[3])))
        ):
            new_quintets.append(prime_quartet + [new_prime]);
    return new_quintets;

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
print;
sieve = [False] * (prime_max + 1);
for prime in primes:
    sieve[prime] = True;

prime_sum_min = sys.maxint;
prime_sum_argmin_quintet = None;
prime_singles_list = [];
prime_pairs_list = [];
prime_trios_list = [];
prime_quartets_list = [];
prime_quintets_list = [];
for p in primes:
    # If the current prime is as large as the current minimum sum, there can be no subsequent sums smaller than the current
    # minimum sum, so stop the search.
    if p >= prime_sum_min:
        break;
    new_quintets = test_quartets_list_for_new_quintets(prime_quartets_list, p);
    print p, new_quintets;
    if len(new_quintets) > 0:
        prime_quintets_list += new_quintets;
        for prime_quintet in new_quintets:
            prime_sum = sum(prime_quintet);
            if prime_sum < prime_sum_min:
                prime_sum_min = prime_sum;
                prime_sum_argmin_quintet = prime_quintet;

    new_quartets = test_trios_list_for_new_quartets(prime_trios_list, p);
    if len(new_quartets) > 0:
        prime_quartets_list += new_quartets;

    new_trios = test_pairs_list_for_new_trios(prime_pairs_list, p);
    if len(new_trios) > 0:
        prime_trios_list += new_trios;

    new_pairs = test_singles_list_for_new_pairs(prime_singles_list, p);
    if len(new_pairs) > 0:
        prime_pairs_list += new_pairs;
    prime_singles_list += [p];
print;
print prime_quartets_list;
print;
print prime_quintets_list;
print;

if prime_sum_argmin_quintet != None:
    print "%s sum = %d" % (prime_sum_argmin_quintet, prime_sum_min);
else:
    print "No quintets found when prime_max = %d." % prime_max;

print;    
print "Execution time = %f seconds." % (time.time() - start_time);
