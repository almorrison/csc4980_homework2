import hashlib
import time

# variables made global for reference in hashCracker function
salt = ""

# used for determining the salt and hash words. if salt has some value (not ""), it concatenates salt to password value before hashing.
def hashCracker(hashInput):
	intialTime = time.time()
	passwordFile = open("C:\\Users\\Aaron M\\Documents\\10-million-password-list-top-1000000.txt", "r", encoding = "utf-8")
	tryCount = 0

	#iterates through password file 
	for password in passwordFile:
		password = password.strip()

		#salt value check
		if(salt != ""):
			passwordHash = hashlib.sha1(bytes(salt + password, "utf-8")).hexdigest()
		else:
			passwordHash = hashlib.sha1(bytes(password, "utf-8")).hexdigest()

		if(passwordHash == hashInput):
			tryCount += 1
			print("\nInput hash:", hashInput)
			print("Compared hash:", passwordHash)
			print("Total number of tries:", tryCount)
			print("Total time taken: %s seconds" %(time.time() - intialTime))
			return password
		else:
			tryCount += 1
			print("\nInput hash:", hashInput)
			print("Compared hash:", passwordHash)
			print("Number of tries:", tryCount)

#get salt
saltInput = input("Input salt (press enter to skip): ")
if(saltInput != ""):
	salt = hashCracker(saltInput)
	print("\nSALT WORD FOUND:", salt)

#get hash
hashInput = input("Input hash (press enter to terminate): ")
if(hashInput != ""):
	print("\nPASSWORD FOUND:", hashCracker(hashInput))
