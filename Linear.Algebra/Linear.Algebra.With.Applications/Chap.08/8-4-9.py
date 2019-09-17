from sympy import Matrix,zeros,ones,pprint

v1 = Matrix([1,0,1,0])
v2 = Matrix([2,3,1,0])
v3 = Matrix([1,2,2,0])
v4 = Matrix([1,1,1,1])

p1= v2 - v1
p2 = v3 - v1
p3 = v4 - v1

S=Matrix([[p1,p2,p3]])
n=S.T.nullspace()[0]

pprint(n)
pprint(n.dot(v1))
pprint(n.dot(v2))
pprint(n.dot(v3))
pprint(n.dot(v4))


