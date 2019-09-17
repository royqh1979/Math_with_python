import sympy as sp

sp.init_printing()

# exercise 11
# b = sp.Matrix([[3,-4],
#                [-5,6]])
# x = sp.Matrix([2,-6])

# exercise 12
b = sp.Matrix([[4,6],
               [5,7]])
x = sp.Matrix([2,0])

b_inv = b.inv()
xb = b_inv*x

sp.pprint(b)
sp.pprint(b_inv)
sp.pprint(xb)

sp.pprint(b*xb)

