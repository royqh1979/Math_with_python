import numpy as np

velocity = np.array([0,2,4,6,8,10])
force = np.array([0, 2.90, 14.8, 39.6, 74.3, 119], dtype=np.float)

A=np.array([np.ones(len(velocity)),
              velocity,
              velocity**2,
              velocity**3,
              velocity**4,
              velocity**5])

A=A.transpose()

result=np.linalg.solve(A,force)

print(result)

for v in velocity:
    t=(1,v,v**2,v**3,v**4,v**5)
    print(sum(result*t))

v=7.5
t=(1,v,v**2,v**3,v**4,v**5)
print(f"结果为{sum(result*t)*100}磅")
