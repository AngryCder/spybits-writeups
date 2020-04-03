import numpy,os
from secret import flag


def generateMatrix(m,N):

	message = numpy.empty((N,N),dtype=numpy.int)

	for i in range(N):
		for j in range(N):
			message[i][j]=m[N*i+j]

	return message


def encrypt(key,m,N):

	while len(m)%(N*N)!=0: m+=b'#'

	pt = generateMatrix(m,N)

	return (numpy.matmul(key,pt))%257

def main():

	global flag

	N=8

	key = generateMatrix(os.urandom(N*N),N)

	secret = encrypt(key,flag.encode(),N)

	print("Welcome to the Service.\n".center(100))
	print("We allow only Encryption as our previous challs were hacked.\n")

	print("Take my secret and shut up :\n{}".format(secret.tolist()))



	while True:

		print("\n1 . Encryption")
		print("2 . Exit\n")

		try:

			type = int(input("Give me your choice : "))

			if type==1:

				m = input("Give me your message : ").strip()

				secret = encrypt(key, m.encode(), N)

				print("Yeah, got your secret message :\n{}".format(secret.tolist()))

			else:
				print("Ok,bye!!")
				break
		except:

			print("Give me a number. Bye!!")
			break

if __name__ == '__main__':
	main()
