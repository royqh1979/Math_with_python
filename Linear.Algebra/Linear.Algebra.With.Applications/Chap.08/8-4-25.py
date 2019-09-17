from sympy import Matrix,pprint,zeros,simplify


o=zeros(2,1)
p=Matrix([4,1])

d=3*p.normalized()
pprint(d)

n=p.T.nullspace()[0]
pprint(n)

n1=d+n
pprint(n1.dot(p).evalf())
n2=(p.norm()-1)*p.normalized()+n
pprint(n2.dot(p).evalf())

