from secret import flag
from hashlib import sha512
from base64 import *


print("Nothing to be said. I think you will get the flag progressively as you solve the levels.\n")
for i in flag:

	enc = sha512(chr(i).encode()).hexdigest().encode()

	for j in range(3):
		enc = b64encode(enc)

	print("Take this encryption and send me the correct decryption to progress = {}\n".format(enc.decode()))

	char = input("Ok, time to give me the solution > ").strip()

	if char == chr(i) :

		print("Correct on this one. Go for the next.\n")

	else:

		print("Incorrect bro. Breaking...\n")
		quit()


print("I think you got your flag now. GG\n")
