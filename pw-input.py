#!/usr/bin/env python3

# necessary imports:
# import sys
import getpass
import hashlib


# new pw input request:
pw_input = getpass.getpass('Enter a new password: ')

# by default, return utf-8 encoded version of pw str:
byte_input = pw_input.encode()

# sha512 hash of the pw, and return as str (double length, only hexidecimal digits):
hash_pw = hashlib.sha512(byte_input).hexdigest()

# read, write, create pwfile.txt (if it doesn't exist) and position new content at end:
pw_file = open('pwfile.txt', 'a+')

# write the hashed pw to the file and add a new line:
pw_file.write(hash_pw)
pw_file.write('\n')

# print statment after pw is written to file
print(' Thank you for your input.')

# close file:
pw_file.close()
