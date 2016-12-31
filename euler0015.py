# Lattice paths
#
# Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20x20 grid?

DEBUG = False;

GRID_ROWS = 20;
GRID_COLUMNS = 20;

# The array cells are intersections of the gride squares, so there will be one more row and one more column.
R = GRID_ROWS + 1;
C = GRID_COLUMNS + 1;

a = [[0 for c in range(C)] for r in range(R)];

c = 0;
for r in range(R):
    a[r][c] = 1;

r = 0;
for c in range(C):
    a[r][c] = 1;

for r in range(1, R):
    for c in range(1, C):
        a[r][c] = a[r-1][c] + a[r][c-1];

if DEBUG:
    for r in range(R):
        print a[r];

print "GRID_ROWS = %d, GRID_COLUMNS = %d" % (GRID_ROWS, GRID_COLUMNS);
print "number of routes = %d" % a[R-1][C-1];
