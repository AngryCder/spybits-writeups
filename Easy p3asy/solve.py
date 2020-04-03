import string

f=open('flag.enc').read().split('\n')

N=int(f[0].split("= ")[1])
e=0x10001

ciphertext=eval(f[2].strip())

flag=''
for i in ciphertext:
	for j in string.printable:
		if pow(ord(j),e,N) == i:
			flag+=j
			break

print(flag)
