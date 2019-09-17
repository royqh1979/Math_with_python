import sympy as sm

sm.init_printing()


def gen_matrix(n):
    m=sm.zeros(n)

    for i in range(1,n+1):
        for j in range(i,n+1):
            m[i-1,j-1]=i
            m[j-1,i-1]=i
    return m

for i in range(10):
    A=gen_matrix(i)
    sm.pprint(A)
    print(A.det())

