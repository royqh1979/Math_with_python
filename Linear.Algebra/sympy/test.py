import sympy as sp

sp.init_printing()

B = sp.Matrix([
    [-9,-5],
    [1,-1]
])
C = sp.Matrix([
    [1,3,3],
    [-4,-5,3]
])

B*"1/2"

x1,x2 = sp.symbols("x1 x2")
x,params=C.gauss_jordan_solve(B)

sp.pprint(x)

from sympy import MatrixSymbol, BlockMatrix, symbols,                           Identity, Matrix, ZeroMatrix, block_collapse
n,m,l = symbols('n m l')
X = MatrixSymbol('X', n, n)
Y = MatrixSymbol('Y', m ,m)
Z = MatrixSymbol('Z', n, m)
# B = BlockMatrix([[X, Z], [ZeroMatrix(m, n), Y]])
# print(B)
# C = BlockMatrix([[Identity(n), Z]])
# print(C)
# print(C*B)
A = sp.Matrix(sp.BlockMatrix([[C,B]]))
sp.pprint(X.inverse())

