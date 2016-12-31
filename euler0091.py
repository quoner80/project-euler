# Right triangles with integer coordinates
# Problem 91
#
# The points P (x1, y1) and Q (x2, y2) are plotted at integer co-ordinates and are joined to the origin, O(0,0), to form Triangle-OPQ.
#
#    ^
#    |       P
#    |       /.
#    |      /   .
#    |     /      .
#    |    /         . Q
#    |   /       .
#    |  /     .
#    | /   .
#    |/ .
#    +-------------------->
#   O
#
# There are exactly fourteen triangles containing a right angle that can be formed when each co-ordinate lies between 0 and 2 inclusive; that is,
#   0 <= x1, y1, x2, y2 <= 2.
#
#    +-----+-----+    +-----+-----+    +-----+-----+    +-----+-----+    +-----+-----+
#    |     |     |    |     |     |    |\    |     |    |    /|     |    |     |     |
#    |     |     |    |     |     |    |x\   |     |    |   /x|     |    |     |     |
#    +-----+-----+    +-----+-----+    +xx\--+-----+    +--/xx+-----+    +-----+-----+
#    |x.   |     |    |   .x|     |    |xxx\ |     |    | /xxx|     |    |xx.__      |
#    |xxx. |     |    | .xxx|     |    |xxxx\|     |    |/xxxx|     |    |xxxxxxx.___|
#    +-----+-----+    +-----+-----+    +-----+-----+    +-----+-----+    +-----+-----+
#
#    +-----+-----+    +-----+-----+    +-----+-----+    +-----+-----+    +-----+-----+
#    |     |     |    |     |     |    |x.   |     |    |     |   .x|    |     |     |
#    |     |     |    |     |     |    |xxx. |     |    |     | .xxx|    |     |     |
#    +-----+-----+    +-----+-----+    +xxxxx.-----+    +-----.xxxxx+    +-----+-----+
#    |   .xxx.   |    |     ___.xx|    |xxxxxxx.   |    |   .xxxxxxx|    |xxx' |     |
#    | .xxxxxxx. |    |___.xxxxxxx|    |xxxxxxxxxx.|    |.xxxxxxxxxx|    |x'   |     |
#    +-----+-----+    +-----+-----+    +-----+-----+    +-----+-----+    +-----+-----+
#
#    +-----+-----+    +-----+-----+    +-----+-----+    +-----+-----+
#    |     |     |    |x.   |     |    |xxxx/|     |    |xxxxxxxxx' |
#    |     |     |    |xxx. |     |    |xxx/ |     |    |xxxxxxx'   |
#    +-----+-----+    +xxxxx+-----+    +xx/--+-----+    +xxxxx+-----+
#    |xxxxxxx.---|    |xxx' |     |    |x/   |     |    |xxx' |     |
#    |.--- |     |    |x'   |     |    |/    |     |    |x'   |     |
#    +-----+-----+    +-----+-----+    +-----+-----+    +-----+-----+
#
# Given that 0 <= x1, y1, x2, y2 <= 50, how many right triangles can be formed?

import time;

start_time = time.time();

N = 2;
N = 50;

def print_execution_time():
    print "Execution time = %f seconds." % (time.time() - start_time);

right_triangle_count = 0;
for Px in range(N + 1):
    for Qx in range(N + 1):
        for Py in range(N + 1):
            for Qy in range(N + 1):
                # Checking for Px * Qy != Qx * Py (equivalent to Px/Py != Qx/Qy) checks for colinear P and Q as well as equal
                # P and Q. 
                if (Px * Qy) != (Qx * Py):
                    aSquared = (Px ** 2) + (Py ** 2);
                    bSquared = (Qx ** 2) + (Qy ** 2);
                    cSquared = ((Px - Qx) ** 2) + ((Py - Qy) ** 2);
                    if (aSquared + bSquared == cSquared) or (aSquared + cSquared == bSquared) or (bSquared + cSquared == aSquared):
                        right_triangle_count += 1;
                        '''
                        print "(%d, %d), (%d, %d)" % (Px, Py, Qx, Qy);
                        print aSquared, bSquared, cSquared;
                        print;
                        '''
# Divide the count by 2 to compensate for the c0 c1 and c1 c0 duplicates.
print "Right triangle count = %d." % (right_triangle_count / 2);

print_execution_time();
