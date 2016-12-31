# Red, green, and blue tiles
# Problem 117
#
# Using a combination of black square tiles and oblong tiles chosen from: red tiles measuring two units, green tiles measuring three units, and blue tiles measuring four units, it is possible to tile a row measuring five units in length in exactly fifteen different ways.
#
#       +---+---+---+---+---+    +---+---+---+---+---+    +---+---+---+---+---+    +---+---+---+---+---+
#       |   |   |   |   |   |    | R---R |   |   |   |    |   | R---R |   |   |    |   |   | R---R |   |
#       +---+---+---+---+---+    +---+---+---+---+---+    +---+---+---+---+---+    +---+---+---+---+---+
#
#       +---+---+---+---+---+    +---+---+---+---+---+    +---+---+---+---+---+    +---+---+---+---+---+
#       | R---R |   |   |   |    | R---R | R---R |   |    | R---R |   | R---R |    |   | R---R | R---R |
#       +---+---+---+---+---+    +---+---+---+---+---+    +---+---+---+---+---+    +---+---+---+---+---+
#
#       +---+---+---+---+---+    +---+---+---+---+---+    +---+---+---+---+---+    +---+---+---+---+---+
#       | G---G---G |   |   |    |   | G---G---G |   |    |   |   | G---G---G |    | R---R | G---G---G |
#       +---+---+---+---+---+    +---+---+---+---+---+    +---+---+---+---+---+    +---+---+---+---+---+
#
#       +---+---+---+---+---+    +---+---+---+---+---+    +---+---+---+---+---+
#       | G---G---G | R---R |    | B---B---B---B |   |    |   | B---B---B---B |
#       +---+---+---+---+---+    +---+---+---+---+---+    +---+---+---+---+---+
#
# How many ways can a row measuring fifty units in length be tiled?
#
# NOTE: This is related to Problem 116.

import time;

start_time = time.time();

def print_execution_time():
    print 'Execution time = %f seconds.' % (time.time() - start_time);

m = 50;
row = [0] * m;
row[1] = 1;
row[2] = 2;
row[3] = 4;
row[4] = 7;
for i in range(5, m):
    row[i] += 3;
    for j in range(1, i - 1):
        row[i] += row[j];
    for j in range(1, i - 2):
        row[i] += row[j];
    for j in range(1, i - 3):
        row[i] += row[j];
print row;
print;
# Add 1 for the completely empty row.
print sum(row) + 1;
print;

print_execution_time();
