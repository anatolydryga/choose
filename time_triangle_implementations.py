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

#@pytest.mark.skip()
#def test_very_large():
#    for choose in chooses:
#        choose(1000, 5)
