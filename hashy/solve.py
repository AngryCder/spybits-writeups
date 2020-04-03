#!/usr/bin/env python3

from pwn import *
import numpy
import json

#r = process(['python3','server.py'])

r=remote('52.205.18.68',5000)

N=8

key = numpy.zeros((N,N))

def getMatrix(N):

	r.recvuntil(":\n")

	return eval(r.recvline().strip())

def getoutput(i,m,N):

	r.sendlineafter(": ","1")

	r.sendlineafter(": ",str(m))

	r.recvuntil(":\n")

	M = eval(r.recvline().strip())

	for j in range(N):
		key[j][i]=M[j][0]

secret = getMatrix(N)

for i in range(N):

	m = '\x00'*i*N+'\x01'+'\x00'*(N*N-i*N-1)

	getoutput(i,m,N)

open("invkey","w").write(json.dumps(secret)+"\n"+json.dumps(key.tolist()))

