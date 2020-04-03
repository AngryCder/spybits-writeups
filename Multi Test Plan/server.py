from Crypto.Random import get_random_bytes
from binascii import *
from secret import key

data = open("data").read().strip().split("\n")

f = open("flag.otp","w")

for i in range(len(data)):

	block = data[i]

	otp = b""

	for j in range(len(block)):

		otp += hexlify(chr( key[j%len(key)] ^ ord(block[j]) ).encode())


	otp= otp.decode()+"\n"

	f.write(otp)

f.close()
