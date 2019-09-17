import sympy as sp

sp.init_printing()

B=sp.Matrix([
    [1,-2],
    [-3,4]])

C=sp.Matrix([
    [-7,-5],
    [9,7]
])

C.condition_number()
c_b,freevars=B.gauss_jordan_solve(C)

sp.pprint(c_b)

b_c,freevars=C.gauss_jordan_solve(B)

sp.pprint(b_c)

sp.pprint(c_b*b_c)
