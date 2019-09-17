from sympy import Matrix,zeros,ones,pprint

p = Matrix([1,-3,1,2])
n = Matrix([2,1,5,1])
v1 = Matrix([0,1,1,1])
v2= Matrix([-2,0,1,3])
v3= Matrix([1,4,0,4])

print(n.dot(p))
print(n.dot(v1))
print(n.dot(v2))
print(n.dot(v3))
