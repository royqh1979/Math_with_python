from sympy import Matrix,ones,zeros,pprint

p1=Matrix([2,-3,1,2])
p2=Matrix([1,2,-1,3])
n1=Matrix([1,2,4,2])
n2=Matrix([2,3,1,5])

d1=p1.dot(n1)
d2=p2.dot(n2)

print(d1)
print(d2)

A=Matrix([n1.T,n2.T])

pprint(A)
b=Matrix([d1,d2])
res=A.gauss_jordan_solve(b)
pprint(res)

v1=Matrix([10,-7,1,0])
v2=Matrix([-4,1,0,1])
p=Matrix([32,-14,0,0])

