from sympy import Matrix,pprint,ones

v1=Matrix([-1,4])
v2=Matrix([3,1])
v3=v1-v2
z=v3.T.nullspace()[0].T
pprint(z)
pprint(z.dot(v1))
pprint(z.dot(v2))