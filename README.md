# csc4980_homework2
Python SHA1 cracking program
Aaron Morrison

This program prompts user for a salt value and a hash value. If salt value is not applicable, the program iterates through the password list (https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt), hashing each password and comparing it with the input hash value. Once a matching password is found, it is printed to the screen. If salt value is applicable, the program iterates through the password list, hashing the passwords and looking for a match. Once the salt word is found, the program then iterates through the list again, this time hashing each password with the salt word concatenated in front and looking for a matching hash value. Once it is found, it is printed to the screen.

For the testing program hash (b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3), the solution is "letmein".

For the medium hacker hash (801cdea58224c921c21fd2b183ff28ffa910ce31), the solution is "vjhtrhsvdctcegth".

For the leet hacker hash (ece4bb07f2580ed8b39aa52b7f7f918e43033ea1) with salt value f0744d60dd500c92c0d37c16174cc58d3c4bdd8e ("slayer"), the solution is "harib".
