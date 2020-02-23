import hashlib
import time

# variables made global for reference in hash_cracker function
salt = ""


# used for determining the salt and hash words. if salt has some value (not ""),
# it concatenates salt to password value before hashing.
def hash_cracker(hash_input):
    initial_time = time.time()
    password_file = open("C:\\Users\\Aaron M\\Documents\\10-million-password-list-top-1000000.txt",
                         "r", encoding="utf-8")
    try_count = 0

    # iterates through password file
    for password in password_file:
        password = password.strip()

        # salt value check
        if salt != "":
            password_hash = hashlib.sha1(bytes(salt + password, "utf-8")).hexdigest()
        else:
            password_hash = hashlib.sha1(bytes(password, "utf-8")).hexdigest()

        if password_hash == hash_input:
            try_count += 1
            print("\nInput hash:", hash_input)
            print("Compared hash:", password_hash)
            print("Total number of tries:", try_count)
            print("Total time taken: %s seconds" % (time.time() - initial_time))
            return password
        else:
            try_count += 1
            print("\nInput hash:", hash_input)
            print("Compared hash:", password_hash)
            print("Number of tries:", try_count)


# get salt
salt_input = input("Input salt (press enter to skip): ")
if salt_input != "":
    salt = hash_cracker(salt_input)
    print("\nSALT WORD FOUND:", salt)

# get hash
hash_input = input("Input hash (press enter to terminate): ")
if hash_input != "":
    print("\nPASSWORD FOUND:", hash_cracker(hash_input))
