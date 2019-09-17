from sympy import Matrix,pprint

B=Matrix([[1,0],[4,2],[-7,-6]])

n=B.T.nullspace()[0]
pprint(n)

pprint(n.T*B)