import sympy as sp
from sympy.solvers import linsolve

sp.init_printing()

# exercise 05
# b=sp.Matrix([[1,2],
#               [-3,-5]])
# xb = sp.Matrix([-2,1])

# exercise 06
# b=sp.Matrix([[1,5],
#               [-2,-6]])
# xb = sp.Matrix([4,0])

# exercise 07
# b=sp.Matrix([[1,-3,2],
#               [-1,4,-2],
#              [-3,9,4]])
# xb = sp.Matrix([8,-9,6])

# exercise 08
b=sp.Matrix([[1,2,1],
              [0,1,-1],
             [3,8,2]])
xb = sp.Matrix([3,-5,4])



sp.pprint(b)
result =b.LUsolve(xb)

sp.pprint(b*result)

sp.pprint( result)
