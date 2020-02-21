# csc4980_homework2
Python SHA1 cracking program

The program will prompt the user to input a hash value. After receiving the input, the program will iterate through the password list (https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt), hashing each password and checking for a match. Once a match is found, the program will return the matching password and total number of tries.
