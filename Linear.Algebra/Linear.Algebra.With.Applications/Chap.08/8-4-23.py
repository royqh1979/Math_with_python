from sympy import Matrix,pprint

v1=Matrix([1,1])
v2=Matrix([3,0])
v3=Matrix([5,3])

p=Matrix([4,1])

p1 = v2-v1
p2 = v3-v1
p3 = v3-v2

pprint(p1)
n=p1.T.nullspace()[0]
pprint(n)
print(n.dot(v1))
print(n.dot(v2))
print(n.dot(v3))
print(n.dot(p))


n=p2.T.nullspace()[0]
pprint(n)
print(n.dot(v1))
print(n.dot(v2))
print(n.dot(v3))
print(n.dot(p))

n=p3.T.nullspace()[0]
pprint(n)
print(n.dot(v1))
print(n.dot(v2))
print(n.dot(v3))
print(n.dot(p))