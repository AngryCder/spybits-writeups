from pwn import *

r=process(['python3','server.py'])

r.sendlineafter("> ",b"2")

N = int(r.recvline().strip().decode().split(" ")[6],16)

e=0x10001

r.sendlineafter("> ",b"4")
c = int(r.recvline().strip().decode().split(" ")[6],16)

copy = c

l=0;h=N

fact = pow(2,e,N)

for i in range(1,513):

	c = c*fact

	r.sendlineafter("> ",b"3")
	r.sendlineafter("> ",str(c).encode())
	r.sendlineafter("> ",b"-1")
	hash = int(r.recvline().strip().decode().split(" ")[-1],16)

	print(i)

	if hash&1 :
		l=(l+h)//2
	else:
		h=(l+h)//2

	if l>h:break


	print(l,h)
