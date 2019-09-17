import sympy as sm

sm.init_printing()


def gen_matrix(n):
    m=sm.zeros(n)

    for i in range(1,n+1):
        for j in range(i,n+1):
            if i==1:
                m[i-1,j-1]=i
                m[j-1,i-1]=i
            else:
                m[i-1,j-1]=(i-1)*3
                m[j-1,i-1]=(i-1)*3

    return m

for i in range(3,6):
    A=gen_matrix(i)
    sm.pprint(A)
    print(A.det())

