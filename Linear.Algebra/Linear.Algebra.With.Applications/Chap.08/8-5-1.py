from sympy import Matrix,pprint
p1=Matrix([1,0])
p2=Matrix([2,3])
p3=Matrix([-1,2])

S=Matrix([[p1,p2,p3]])
f1=Matrix([[1,-1]])
f2=Matrix([[1,1]])
f3=Matrix([[-3,1]])

pprint(f1*S)
pprint(f2*S)
pprint(f3*S)