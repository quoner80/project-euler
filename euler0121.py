# Disc game prize fund
# Problem 121
#
# A bag contains one red disc and one blue disc. In a game of chance a player takes a disc at random and its colour is noted. After each turn the disc is returned to the bag, an extra red disc is added, and another disc is taken at random.
#
# The player pays 1 pound-sterling to play and wins if they have taken more blue discs than red discs at the end of the game.
#
# If the game is played for four turns, the probability of a player winning is exactly 11/120, and so the maximum prize fund the banker should allocate for winning in this game would be 10 pounds-sterling before they would expect to incur a loss. Note that any payout will be a whole number of pounds and also includes the original 1 pound-sterling paid to play the game, so in the example given the player actually wins 9 pounds-sterling.
#
# Find the maximum prize fund that should be allocated to a single game in which fifteen turns are played.

# The given example of 4 rounds:
#
# 1:              +---------------------B---------------------+                           +---------------------R---------------------+
#                /                      |                      \                         /                      |                      \
# 2:     +------B------+         +------R------+         +------R------+         +------B------+         +------R------+         +------R------+
#       /    /    \     \       /    /    \     \       /    /    \     \       /    /    \     \       /    /    \     \       /    /    \     \    
# 3:   B     R     R     R     B     R     R     R     B     R     R     R     B     R     R     R     B     R     R     R     B     R     R     R
#    //|\\ //|\\ //|\\ //|\\ //|\\ //|\\ //|\\ //|\\ //|\\ //|\\ //|\\ //|\\ //|\\ //|\\ //|\\ //|\\ //|\\ //|\\ //|\\ //|\\ //|\\ //|\\ //|\\ //|\\
# 4: BRRRR BRRRR BRRRR BRRRR BRRRR BRRRR BRRRR BRRRR BRRRR BRRRR BRRRR BRRRR BRRRR BRRRR BRRRR BRRRR BRRRR BRRRR BRRRR BRRRR BRRRR BRRRR BRRRR BRRRR
#
# 4 B's: B-B-B-B = 1 way; total 1 way
# 3 B's: B-B-B-R = 4 ways, B-B-R-B = 3 ways, B-R-B-B = 2 ways, R-B-B-B = 1 way; total 10 ways
# 2 B's: B-B-R-R = 3 * 4 = 12 ways, B-R-B-R = 2 * 4 = 8 ways, B-R-R-B = 2 * 3 = 6 ways, R-B-B-R = 4 ways, R-B-R-B = 3 ways, R-R-B-B = 2 ways; total 35 ways
# 1 B  : B-R-R-R = 2 * 3 * 4 = 24 ways, R-B-R-R = 3 * 4 = 12 ways, R-R-B-R = 2 * 4 = 8 ways, R-R-R-B = 2 * 3 = 6 ways; total 50 ways
# 0 B's: R-R-R-R = 2 * 3 * 4 = 24 ways; total 24 ways
# Grand total = 1 + 10 + 35 + 50 + 24 = 120 ways
# Grand total = 5! = 120 ways, confirmed
# Total winning ways = 4 B's + 3 B's = 1 + 10 = 11 ways
# Probability of winning = 11 / 120, confirmed

# In general, n rounds, postulated:
# n   B's: 1 way; total 1 way
# n-1 B's: n, n-1, n-2, ... 1; total [n * (n - 1) / 2] ways
# n-2 B's: sum[product(subsets of 1..n of size 2)] ways
# ...
# n-k B's: sum[product(subsets of 1..n of size k)] ways
# ...
# 2   B's: sum[product(subsets of 1..n of size n-2)] ways
# 1   B  : sum[product(subsets of 1..n of size n-1)] ways
# 0   B's: sum[product(subsets of 1..n of size n)] ways = n! ways
# Grand total = (n+1)!

# Check general postulate when n = 4:
# 4 B's: 1 way, confirmed
# 3 B's: 4 + 3 + 2 + 1 = 10 ways, confirmed
# 2 B's: (4 * 3) + (4 * 2) + (4 * 1) + (3 * 2) + (3 * 1) + (2 * 1) = 12 + 8 + 4 + 6 + 3 + 2 = 35 ways, confirmed
# 1 B  : (4 * 3 * 2) + (4 * 3 * 1) + (4 * 2 * 1) + (3 * 2 * 1) = 24 + 12 + 8 + 6 = 50 ways, confirmed
# 0 B's: 4 * 3 * 2 * 1 = 24 ways, confirmed
# Grand total = 5! = 120 ways, confirmed

import math;
import time;

start_time = time.time();

def print_execution_time():
    print 'Execution time = %f seconds.' % (time.time() - start_time);

# Returns the combinations of "count" elements in "array".
# For example, for ([1,2,3,4], 2), returns ([1,2], [1,3], [1,4], [2,3], [2,4], [3,4]).
def get_combinations(array, count):
    combinations = [];
    if count == 1:
        for element in array:
            combinations.append([element]);
    else:
        for i in range(len(array) - count + 1):
            subcombinations = get_combinations(array[i + 1 : ], count - 1);
            for subcombination in subcombinations:
                combinations.append([array[i]] + subcombination);
    return combinations;

n = 15;
minimum_blues_to_win = (n / 2) + 1;
print 'n =', n;
print 'minimum blue discs needed to win =', minimum_blues_to_win;

one_to_n_list = [];
for i in range(1, n + 1):
    one_to_n_list.append(i);

ways_to_get_i_blues = [None] * (n + 1);
ways_to_get_i_blues[n] = 1;

for subset_size in range(1, n + 1):
    summation = 0;
    combinations = get_combinations(one_to_n_list, subset_size);
    for combination in combinations:
        product = 1;
        for factor in combination:
            product *= factor;
        # print combination, product;
        summation += product;
    ways_to_get_i_blues[n - subset_size] = summation;
    # print subset_size, summation;

for i in range(len(ways_to_get_i_blues)):
    print 'ways to get', i, 'blue disc(s) =', ways_to_get_i_blues[i];
total_ways = sum(ways_to_get_i_blues);
ways_to_win = 0;
for i in range(minimum_blues_to_win, len(ways_to_get_i_blues)):
    ways_to_win += ways_to_get_i_blues[i];
ways_to_lose = total_ways - ways_to_win;
n_plus_one_factorial = math.factorial(n + 1);
loss_to_win_ratio = float(ways_to_lose) / ways_to_win;
# The plus one is for the original bet.
maximum_payout = int(math.floor(loss_to_win_ratio)) + 1;
print 'ways to win =', ways_to_win;
print 'total ways =', total_ways;
print '(n + 1)!   =', n_plus_one_factorial;
print 'total ways - (n + 1)! =', total_ways - n_plus_one_factorial, '(should be zero)';
print 'probability of winning =', ways_to_win, '/', total_ways;
print 'ways to lose / ways to win =', ways_to_lose, '/', ways_to_win, '=', loss_to_win_ratio;
print;
print 'maximum non-loss incurring payout for a 1 pound-sterling bet =', maximum_payout, 'pounds-sterling';
print;

print_execution_time();
