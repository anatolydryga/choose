from timeit import default_timer as timer

from choose_triangle import *
from choose_triangle_bottomUp_DP import *
from choose_triangle_topDown_DP import *

chooses = {"recursive" : choose_triangle_recursive, 
    "topDown DP" : choose_triangle_topDown, 
    "bottomUp DP" : choose_triangle_bottomUp}

for name, choose in chooses.items():
    start = timer()
    assert choose(52, 5) ==  2598960
    end = timer()
    print name + " takes : " + str(end - start)

print
print "Dynamic Programming Comparison"
for name, choose in chooses.items():
    if name == "recursive": continue
    start = timer()
    for i in range(0, 10):
        for j in range(0, 50):
            choose(500, j)
    end = timer()
    print name + " takes : " + str(end - start)

