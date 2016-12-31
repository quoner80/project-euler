# Poker hands
#
# In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:
#   High Card: Highest value card.
#   One Pair: Two cards of the same value.
#   Two Pairs: Two different pairs.
#   Three of a Kind: Three cards of the same value.
#   Straight: All cards are consecutive values.
#   Flush: All cards of the same suit.
#   Full House: Three of a kind and a pair.
#   Four of a Kind: Four cards of the same value.
#   Straight Flush: All cards are consecutive values of same suit.
#   Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
#
# The cards are valued in the order:
#   2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
#
# If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.
#
# Consider the following five hands dealt to two players:
#   Hand   Player 1            Player 2              Winner
#   1      5H 5C 6S 7S KD      2C 3S 8S 8D TD        Player 2
#          Pair of Fives       Pair of Eights
#   2      5D 8C 9S JS AC      2C 5C 7D 8S QH        Player 1
#          Highest card Ace    Highest card Queen
#   3      2D 9C AS AH AC      3D 6D 7D TD QD        Player 2
#          Three Aces          Flush with Diamonds
#   4      4D 6S 9H QH QC      3D 6D 7H QD QS        Player 1
#          Pair of Queens,     Pair of Queens,
#          highest card Nine   highest card Seven
#   5      2H 2D 4C 4D 4S      3C 3D 3S 9S 9D        Player 1
#          Full House,         Full House,
#          with Three Fours    with Three Threes
#
# The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.
#
# How many hands does Player 1 win?

import csv;
import time;

start_time = time.time();

# The whole part of a score denotes the type of hand, as indicated in the following constants. The fractional part denotes the card values, with the appropriate
# significance assigned to the individual card groups (quadruplets, triplets, pairs and/or singlets).
SCORE_NOTHING         = 0.0;
SCORE_ONE_PAIR        = 1.0;
SCORE_TWO_PAIRS       = 2.0;
SCORE_THREE_OF_A_KIND = 3.0;
SCORE_STRAIGHT        = 4.0;
SCORE_FLUSH           = 5.0;
SCORE_FULL_HOUSE      = 6.0;
SCORE_FOUR_OF_A_KIND  = 7.0;
SCORE_STRAIGHT_FLUSH  = 8.0;

# Replaces T with a, J with b, Q with c, K with d, and A with e. This makes ASCII-sorting match the card values and enables
# evaluation as hexadecimal values through int(char, 16).
def get_sortable_hand(hand):
    sortable_hand = list(hand);
    for i in range(5):
        if sortable_hand[i][0] == 'T':
            sortable_hand[i] = 'a' + sortable_hand[i][1];
        elif sortable_hand[i][0] == 'J':
            sortable_hand[i] = 'b' + sortable_hand[i][1];
        elif sortable_hand[i][0] == 'Q':
            sortable_hand[i] = 'c' + sortable_hand[i][1];
        elif sortable_hand[i][0] == 'K':
            sortable_hand[i] = 'd' + sortable_hand[i][1];
        elif sortable_hand[i][0] == 'A':
            sortable_hand[i] = 'e' + sortable_hand[i][1];
    return sortable_hand;

def get_nothing_score(value0, value1, value2, value3, value4):
    # The values are sorted low to high, so value4 should have the greatest significance, value3 the next highest, and so on.
    score = SCORE_NOTHING + (value4 / 100.0) + (value3 / 10000.0) + (value2 / 1000000.0) + (value1 / 100000000.0) + (value0 / 10000000000.0);
    return score;

def get_one_pair_score(value0, value1, value2, value3, value4):
    score = SCORE_NOTHING;
    # The values are sorted low to high, so the only possible pattenns for one pair are: xyzAA, xyAAz, xAAyz and AAxyz. The pair value should have the highest
    # significance, the highest singlet value the next highest, the next highest singlet value the next highest, and so on.
    if value3 == value4:
        score = SCORE_ONE_PAIR + (value3 / 100.0) + (value2 / 10000.0) + (value1 / 1000000.0) + (value0 / 100000000.0);
    elif value2 == value3:
        score = SCORE_ONE_PAIR + (value2 / 100.0) + (value4 / 10000.0) + (value1 / 1000000.0) + (value0 / 100000000.0);
    elif value1 == value2:
        score = SCORE_ONE_PAIR + (value1 / 100.0) + (value4 / 10000.0) + (value3 / 1000000.0) + (value0 / 100000000.0);
    elif value0 == value1:
        score = SCORE_ONE_PAIR + (value0 / 100.0) + (value4 / 10000.0) + (value3 / 1000000.0) + (value2 / 100000000.0);
    return score;

def get_two_pairs_score(value0, value1, value2, value3, value4):
    score = SCORE_NOTHING;
    # The values are sorted low to high, so the only possible pattenns for two pairs are: xAABB, AAxBB and AABBx. The BB pair value should have the highest
    # significance, the AA pair value the next highest, and the singlet value the lowest.
    if value1 == value2 and value3 == value4:
        score = SCORE_TWO_PAIRS + (value3 / 100.0) + (value1 / 10000.0) + (value0 / 1000000.0);
    elif value0 == value1 and value3 == value4:
        score = SCORE_TWO_PAIRS + (value3 / 100.0) + (value0 / 10000.0) + (value2 / 1000000.0);
    elif value0 == value1 and value2 == value3:
        score = SCORE_TWO_PAIRS + (value2 / 100.0) + (value0 / 10000.0) + (value4 / 1000000.0);
    return score;

def get_three_of_a_kind_score(value0, value1, value2, value3, value4):
    score = SCORE_NOTHING;
    # The values are sorted low to high, so the only possible pattenns for three of a kind are: xyAAA, xAAAy and AAAxy. The triplet value should have the highest
    # significance, the higher singlet value the next highest, the lower singlet value the lowest.
    if value2 == value3 and value2 == value4:
        score = SCORE_THREE_OF_A_KIND + (value2 / 100.0) + (value1 / 10000.0) + (value0 / 1000000.0);
    elif value1 == value2 and value1 == value3:
        score = SCORE_THREE_OF_A_KIND + (value1 / 100.0) + (value4 / 10000.0) + (value0 / 1000000.0);
    elif value0 == value1 and value0 == value2:
        score = SCORE_THREE_OF_A_KIND + (value0 / 100.0) + (value4 / 10000.0) + (value3 / 1000000.0);
    return score;

def get_straight_score(value0, value1, value2, value3, value4):
    score = SCORE_NOTHING;
    # The values are sorted, so a straight must have values in sequence, one unit apart.
    if value4 - value3 == 1 and value4 - value2 == 2 and value4 - value1 == 3 and value4 - value0 == 4:
        score = SCORE_STRAIGHT + get_nothing_score(value0, value1, value2, value3, value4);
    return score;

def get_flush_score(value0, value1, value2, value3, value4, suit0, suit1, suit2, suit3, suit4):
    score = SCORE_NOTHING;
    if suit0 == suit1 and suit0 == suit2 and suit0 == suit3 and suit0 == suit4:
        score = SCORE_FLUSH + get_nothing_score(value0, value1, value2, value3, value4);
    return score;

def get_full_house_score(value0, value1, value2, value3, value4):
    score = SCORE_NOTHING;
    # The values are sorted, so the only possible pattenns for four of a kind are: BBAAA, and AAABB. The triplet value should have the higher significance, and
    # the pair value should have the lower.
    if value0 == value1 and value2 == value3 and value2 == value4:
        score = SCORE_FULL_HOUSE + (value2 / 100.0) + (value0 / 10000.0);
    elif value0 == value1 and value0 == value2 and value3 == value4:
        score = SCORE_FULL_HOUSE + (value0 / 100.0) + (value3 / 10000.0);
    return score;

def get_four_of_a_kind_score(value0, value1, value2, value3, value4):
    score = SCORE_NOTHING;
    # The values are sorted, so the only possible pattenns for four of a kind are: xAAAA, and AAAAx. The quadruplet value should have the higher significance,
    # and the singlet value should have the lower.
    if value1 == value2 and value1 == value3 and value1 == value4:
        score = SCORE_FOUR_OF_A_KIND + (value1 / 100.0) + (value0 / 10000.0);
    elif value0 == value1 and value0 == value2 and value0 == value3:
        score = SCORE_FOUR_OF_A_KIND + (value0 / 100.0) + (value4 / 10000.0);
    return score;

def get_straight_flush_score(value0, value1, value2, value3, value4, suit0, suit1, suit2, suit3, suit4):
    score = SCORE_NOTHING;
    if get_straight_score(value0, value1, value2, value3, value4) and get_flush_score(value0, value1, value2, value3, value4, suit0, suit1, suit2, suit3, suit4):
        score = SCORE_STRAIGHT_FLUSH + get_nothing_score(value0, value1, value2, value3, value4);
    return score;

def get_hand_score(hand):
    score = SCORE_NOTHING;
    sorted_hand = sorted(get_sortable_hand(hand));
    value0 = int(sorted_hand[0][0], 16);
    value1 = int(sorted_hand[1][0], 16);
    value2 = int(sorted_hand[2][0], 16);
    value3 = int(sorted_hand[3][0], 16);
    value4 = int(sorted_hand[4][0], 16);
    suit0 = sorted_hand[0][1];
    suit1 = sorted_hand[1][1];
    suit2 = sorted_hand[2][1];
    suit3 = sorted_hand[3][1];
    suit4 = sorted_hand[4][1];
    score = get_straight_flush_score(value0, value1, value2, value3, value4, suit0, suit1, suit2, suit3, suit4);
    if score != SCORE_NOTHING:
        return score;
    score = get_four_of_a_kind_score(value0, value1, value2, value3, value4);
    if score != SCORE_NOTHING:
        return score;
    score = get_full_house_score(value0, value1, value2, value3, value4);
    if score != SCORE_NOTHING:
        return score;
    score = get_flush_score(value0, value1, value2, value3, value4, suit0, suit1, suit2, suit3, suit4);
    if score != SCORE_NOTHING:
        return score;
    score = get_straight_score(value0, value1, value2, value3, value4);
    if score != SCORE_NOTHING:
        return score;
    score = get_three_of_a_kind_score(value0, value1, value2, value3, value4);
    if score != SCORE_NOTHING:
        return score;
    score = get_two_pairs_score(value0, value1, value2, value3, value4);
    if score != SCORE_NOTHING:
        return score;
    score = get_one_pair_score(value0, value1, value2, value3, value4);
    if score != SCORE_NOTHING:
        return score;
    return get_nothing_score(value0, value1, value2, value3, value4);

FILENAME = "p054_poker.txt";
# FILENAME = "p054_poker_toy.txt";

with open(FILENAME) as csvfile:
    reader = csv.reader(csvfile, delimiter = ' ');
    game = 0;
    player_1_victories = 0;
    for hands in reader:
        game += 1;
        hand1 = hands[: 5];
        hand2 = hands[5 :];
        score1 = get_hand_score(hand1);
        score2 = get_hand_score(hand2);
        winner = 2;
        if score1 > score2:
            winner = 1;
            player_1_victories += 1;
        print "%04d: %s score1 = %.010f; %s score2 = %.010f: player%s wins." % (game, str(sorted(hand1)), score1, str(sorted(hand2)), score2, winner);
print "player1 won %d games." % player_1_victories;

print "Execution time = %f seconds." % (time.time() - start_time);
