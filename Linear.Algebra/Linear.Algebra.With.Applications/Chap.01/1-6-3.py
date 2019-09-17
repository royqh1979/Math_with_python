import sympy as sm

sm.init_printing()

exchange_table_t = sm.Matrix([
    [0.2,0.3,0.5],
    [0.8,0.1,0.1],
    [0.4,0.4,0.2]
])

exchange_table = exchange_table_t.transpose()

sm.pprint(exchange_table)

m=sm.eye(3) - exchange_table

sm.pprint(m)

b=sm.zeros(3).col(0)

sm.pprint(b)

m=m.col_insert(3,b)

sm.pprint(m)

sm.pprint(m.rref())
from sympy.solvers.solveset import linsolve

x,y,z=sm.symbols("x y z")
result=linsolve(m,x,y,z)
sm.pprint(result)