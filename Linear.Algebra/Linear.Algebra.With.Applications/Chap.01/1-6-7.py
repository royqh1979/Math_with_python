import sympy as sm

sm.init_printing()

table = sm.Matrix([
    [1,0,-3,0,0,0],
    [6,0,0,0,0,-1],
    [0,1,0,-2,0,0],
    [0,2,0,0,-1,0],
    [0,8,-4,-3,-2,-1]
])


sm.pprint(table)

m=table
sm.pprint(m)

b=sm.zeros(5).col(0)

sm.pprint(b)

sm.pprint(m.rref())
from sympy.solvers.solveset import linsolve

result=linsolve((m,b))
sm.pprint(result)