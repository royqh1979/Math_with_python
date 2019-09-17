from sympy import Matrix,ones,zeros,pprint

a1 = Matrix([2,-1,5])
a2 = Matrix([3,1,3])
a3 = Matrix([-1,6,0])

b1=Matrix([0,5,-1])
b2=Matrix([1,-3,-2])
b3=Matrix([2,2,1])

n=Matrix([3,1,-2])

print(n.dot(a1))
print(n.dot(a2))
print(n.dot(a3))
print(n.dot(b1))
print(n.dot(b2))
print(n.dot(b3))