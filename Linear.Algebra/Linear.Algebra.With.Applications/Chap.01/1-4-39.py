

import sympy as sm

sm.init_printing()
m=sm.Matrix([[12,-7,11,-9,5],
    [-9,4,-8,7,-3],
    [-6,11,-7,3,-9],
    [4,-6,10,-5,12]])

r,pivots=m.rref()

sm.pprint(r)

if len(pivots)<4:
    print("无法生成R4")