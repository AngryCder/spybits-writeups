from pwn import *
import string
from hashlib import sha512
from base64 import *


r = process(['python3','server.py'])


lookup = { sha512(i.encode()).hexdigest().encode() : i for i in string.printable }

flag = b""

while True:

	r.recvuntil("= ")

	enc = r.recvline().strip()

	for i in range(3):

		enc = b64decode(enc)


	flag += lookup[enc].encode()

	r.sendline(chr(flag[-1]))

	print(flag)

	if flag[-1] == ord('}'): break
