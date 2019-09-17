from sympy import Matrix,pprint

B=Matrix([[1,3,5],[0,2,4]])


n=B.nullspace()[0]

pprint(B*n)