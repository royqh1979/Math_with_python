import sympy as sm
from sympy.solvers.solveset import linsolve

sm.init_printing()

m=sm.Matrix([
[8,-3,0,-7,2],
[-9,4,5,11,-7],
[6,-2,2,-4,4],
[5,-1,7,0,10],
])

r,pivots = m.rref()

sm.pprint(r)

print(pivots)

n=sm.Matrix()
n=n.col_insert(0,m.col(0))
n=n.col_insert(1,m.col(1))
n=n.col_insert(2,m.col(4))

b=m.col(3)

sm.pprint(n)

sm.pprint(linsolve((n,b)))

