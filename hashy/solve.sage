from sage.all import *

f=open("invkey","r").read().split("\n")

N=8
C = eval(f[0])
K = eval(f[1])

C = Matrix(Integers(257),C)
K = Matrix(Integers(257),K)

PT=K\C
flag=''
for i in range(N):
	for j in range(N):
		flag+=chr(PT[i][j])

print(flag)
