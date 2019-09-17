from sympy import Matrix,ones,pprint

v1=Matrix([1,1,3])
v2=Matrix([2,4,1])
v3=Matrix([-1,-2,5])

p1=v1-v3
p2=v2-v3

S=Matrix([[p1,p2]]).T
n=S.nullspace()[0]
pprint(n)
print(n.dot(p1))
print(n.dot(p2))
print(n.dot(v1))
print(n.dot(v2))
print(n.dot(v3))


