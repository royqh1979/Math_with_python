import sympy as sp

sp.init_printing()


b = sp.Matrix([[1,0,1],
               [0,1,2],
               [1,1,1]])
x = sp.Matrix([1,4,7])

b_inv = b.inv()
xb = b_inv*x

sp.pprint(b)
sp.pprint(b_inv)
sp.pprint(xb)

sp.pprint(b*xb)

