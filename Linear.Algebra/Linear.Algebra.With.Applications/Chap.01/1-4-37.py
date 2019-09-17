import sympy as sm

sm.init_printing()
m=sm.Matrix([[7,2,-5,8],
    [-5,-3,4,-9],
    [6,10,-2,7],
    [-7,9,2,15]])

r,pivots=m.rref()

sm.pprint(r)

if len(pivots)<4:
    print("无法生成R4")