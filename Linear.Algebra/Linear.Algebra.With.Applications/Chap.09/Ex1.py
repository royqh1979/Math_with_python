from matplotlib import pyplot as plt
from sympy import Matrix,zeros,ones
from sympy import simplify as S

x=[0,1]
y=(1,4)
plt.plot(x,y,color="red")
y=(5,0)
plt.plot(x,y,color="orange")
y=(3,1)
plt.plot(x,y,color="blue")
y=(6,2)
plt.plot(x,y,color="darkgreen")

plt.show()

