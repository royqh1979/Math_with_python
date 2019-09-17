from sympy import Matrix,ones,zeros,pprint

v1=Matrix([-1,-3,4])
v2=Matrix([0,-3,1])
v3=Matrix([1,-1,4])
v4=Matrix([1,1,-2])

S=Matrix([[v1,v2,v3,v4]])

p1=Matrix([1,-1,2])
p2=Matrix([0,-2,2])

S1=S.row_join(p1).col_join(ones(1,5))

pprint(S1.rref())

S2=S.row_join(p2).col_join(ones(1,5))
pprint(S2.rref())