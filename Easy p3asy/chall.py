from Crypto.Util.number import *
from secret import flag
import json

def genkey():
	p = getPrime(512)
	q = getPrime(512)
	e = 0x10001
	n = p*q
	return n,e

def enc(c,e,n):
	c=ord(c)
	return pow(c,e,n)

n,e=genkey()

f=open("flag.enc","w")

ciphertext = [ enc(flag[i],e,n) for i in range(len(flag)) ]

f.write("N = {}\ne = {}\n".format(n,e))

f.write(json.dumps(ciphertext))

f.close()
