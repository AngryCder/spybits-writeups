from Crypto.PublicKey import RSA
from Crypto.Util.number import *
from secret import flag
from hashlib import sha512


p = getPrime(256)
q = getPrime(256)
e = 0x10001

N = p * q

d = inverse(e,(p-1)*(q-1))


def encrypt(m):

	return pow(m,e,N)

def sign(m):

	hash = copy = m

	for i in range(0x20):

		hash &= (1<<18)&m + (1<<10)&m + (1<<6)&m + 1

		m |= (1<<6)&hash + (1<<2)&hash

	m = copy

	for i in range(0x20):

		hash += m&(m>>i)


	hash = hash ^ bytes_to_long( sha512( long_to_bytes(m) ).hexdigest().encode() )

	hash &= 0xfffffffffff

	if m&1:
		hash |= 0x1
	else:

		hash &= 0xffffffffffe

	return hash



print("Hi, This is the Local Services Bank. We are the security team of the bank. Try to hack the secret. ".center(135))

while True:

	print("1. Encrypt")
	print("2. Dump the public keys")
	print("3. Verify the service")
	print("4. Get me the secret")
	print("5. Exit\n")

	try:

		type = int(input("Give me your choice > ").strip())

		if type == 1:

			m = int(input("Give me the message to verify > ").strip())

			enc = encrypt(m)

			hash = sign(m)

			print("Here you go : enc = 0x{:x} and hash = 0x{:x}\n".format(enc,hash))

		elif type == 2:

			print("Here goes the public modulus = 0x{:x} and public exponent = 0x{:x}\n".format(N,e))

		elif type == 3:

			c = int(input("To verify our service , Give me the ciphertext > ").strip())

			hash = int(input("I need the hash too to verify > ").strip())

			m = pow(c,d,N)

			trueHash = sign(m)

			if trueHash==hash:

				print("Yep. Thats correct. Verified !!\n")

			else:

				print("Nope. 0x{:x} != 0x{:x}\n".format(hash,trueHash))

		elif type == 4:

			enc = encrypt(bytes_to_long(flag))

			hash = sign(bytes_to_long(flag))

			print("Here goes the my secret : 0x{:x} and hash : 0x{:x}\n".format(enc,hash))

		else:

			print("Ok !! Bye .\n")
			break

	except:

		print("Something wrong happened!!.Exiting\n")
		break
