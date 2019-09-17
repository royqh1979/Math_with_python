import sympy as sp
from sympy.solvers import linsolve

sp.init_printing()

# exercise 01
# b=sp.Matrix([[3,-4],
#               [-5,6]])
#
# xb = sp.Matrix((5,3))

# exercise 02
# b=sp.Matrix([[4,6],[5,7]])
# xb = sp.Matrix([8,-5])

# exercise 03
# b = sp.Matrix([[1,5,4],
#                [-4,2,-7],
#                [3,-2,0]])
# xb = sp.Matrix([3,0,-1])

# exercise 04
b = sp.Matrix([
    [-1,3,4],
    [2,-5,7],
    [0,2,3]
])

xb = sp.Matrix([-4,8,-7])

sp.pprint(b)
sp.pprint(b*xb)
