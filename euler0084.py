# Monopoly odds
# Problem 84
#
# In the game, Monopoly, the standard board is set up in the following way:
#
#   GO   A1  CC1   A2   T1   R1   B1   CH1  B2   B3 JAIL
#   H2                                                C1
#   T2                                                U1
#   H1                                                C2
#   CH3                                               C3
#   R4                                                R2
#   G3                                                D1
#   CC3                                              CC2
#   G2                                                D2
#   G1                                                D3
#   G2J  F3   U2   F2   F1   R3   E3   E2   CH2  E1   FP
#
# A player starts on the GO square and adds the scores on two 6-sided dice to determine the number of squares they advance in a clockwise direction. Without any further rules we would expect to visit each square with equal probability: 2.5%. However, landing on G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.
#
# In addition to G2J, and one card from each of CC and CH, that orders the player to go directly to jail, if a player rolls three consecutive doubles, they do not advance the result of their 3rd roll. Instead they proceed directly to jail.
#
# At the beginning of the game, the CC and CH cards are shuffled. When a player lands on CC or CH they take a card from the top of the respective pile and, after following the instructions, it is returned to the bottom of the pile. There are sixteen cards in each pile, but for the purpose of this problem we are only concerned with cards that order a movement; any instruction not concerned with movement will be ignored and the player will remain on the CC/CH square.
#
#   Community Chest (2/16 cards):
#       1. Advance to GO
#       2. Go to JAIL
#   Chance (10/16 cards):
#       1. Advance to GO
#       2. Go to JAIL
#       3. Go to C1
#       4. Go to E3
#       5. Go to H2
#       6. Go to R1
#       7. Go to next R (railway company)
#       8. Go to next R
#       9. Go to next U (utility company)
#      10. Go back 3 squares
#
# The heart of this problem concerns the likelihood of visiting a particular square. That is, the probability of finishing at that square after a roll. For this reason it should be clear that, with the exception of G2J for which the probability of finishing on it is zero, the CH squares will have the lowest probabilities, as 5/8 request a movement to another square, and it is the final square that the player finishes at on each roll that we are interested in. We shall make no distinction between "Just Visiting" and being sent to JAIL, and we shall also ignore the rule about requiring a double to "get out of jail", assuming that they pay to get out on their next turn.
#
# By starting at GO and numbering the squares sequentially from 00 to 39 we can concatenate these two-digit numbers to produce strings that correspond with sets of squares.
#
# Statistically it can be shown that the three most popular squares, in order, are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. So these three most popular squares can be listed with the six-digit modal string: 102400.
#
# If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.

import random;
import time;

start_time = time.time();

TURN_COUNT = 10 ** 6;

DIE_SIDE_COUNT = 6;
DIE_SIDE_COUNT = 4;

GO   = 0;   JAIL = 10;   FP  = 20;   G2J = 30;
A1   = 1;   C1   = 11;   E1  = 21;   G1  = 31;
CC1  = 2;   U1   = 12;   CH2 = 22;   G2  = 32;
A2   = 3;   C2   = 13;   E2  = 23;   CC3 = 33;
T1   = 4;   C3   = 14;   E3  = 24;   G3  = 34;
R1   = 5;   R2   = 15;   R3  = 25;   R4  = 35;
B1   = 6;   D1   = 16;   F1  = 26;   CH3 = 36;
CH1  = 7;   CC2  = 17;   F2  = 27;   H1  = 37;
B2   = 8;   D2   = 18;   U2  = 28;   T2  = 38;
B3   = 9;   D3   = 19;   F3  = 29;   H2  = 39;

SQUARE_COUNT = 40;

CC_CARD_COUNT = 16;
CH_CARD_COUNT = 16;

visits = [0] * SQUARE_COUNT;

# random.seed(0);
random.seed(start_time);
current = 0;
consecutive_doubles = 0;
cc = 0;
ch = 0;
for turn_count in range(TURN_COUNT):
    if current == G2J:
        current = JAIL;
    elif current == CH1 or current == CH2 or current == CH3:
        ch = random.randint(1, CH_CARD_COUNT);
        # ch = (ch + 1) % CH_CARD_COUNT;
        if ch == 1:
            current = GO;
        elif ch == 2:
            current = JAIL;
        elif ch == 3:
            current = C1;
        elif ch == 4:
            current = E3;
        elif ch == 5:
            current = H2;
        elif ch == 6:
            current = R1;
        elif ch == 7 or ch == 8:
            if ch == CH1:
                current = R2;
            elif ch == CH2:
                current = R3;
            elif ch == CH3:
                current = R1;
        elif ch == 9:
            if ch == CH1 or ch == CH3:
                current = U1;
            elif ch == CH2:
                current = U2;
        elif ch == 10:
            current -= 3;
    # This is an "if" rather than an "elif" because one of the cases above (current == CH3 and ch == 10) can result in current == CC3.
    if current == CC1 or current == CC2 or current == CC3:
        cc = random.randint(1, CC_CARD_COUNT);
        # cc = (cc + 1) % CC_CARD_COUNT;
        if cc == 1:
            current = GO;
        elif cc == 2:
            current = JAIL;
    visits[current] += 1;
    '''
    for v in range(SQUARE_COUNT):
        print "%2d" % int(float(visits[v]) * 1000.0 / sum(visits)),
    print;
    '''
    die1 = random.randint(1, DIE_SIDE_COUNT);
    die2 = random.randint(1, DIE_SIDE_COUNT);
    if die1 == die2:
        consecutive_doubles += 1;
    else:
        consecutive_doubles = 0;
        current = (current + die1 + die2) % SQUARE_COUNT;
    # print "%d + %d = %d" % (die1, die2, die1 + die2);
    if consecutive_doubles == 3:
        # print "3 consecutive doubles!";
        consecutive_doubles = 0;
        current = JAIL;

print visits;
print;
print visits[CH1];
print visits[CH2];
print visits[CH3];
print;
print visits[CC1];
print visits[CC2];
print visits[CC3];
print;
print visits[R1];
print visits[R2];
print visits[R3];
print visits[R4];
print;
print visits[U1];
print visits[U2];
print;
visits_sorted = sorted(visits);
modal = "";
for i in range(-1, -4, -1):
    count = visits_sorted[i];
    square = visits.index(count);
    print "%02d: %f" % (square, 100.0 * count / TURN_COUNT);
    modal += "{:02d}".format(square);
print;
print "modal = %s" % modal;

print;

print "Execution time = %f seconds." % (time.time() - start_time);
