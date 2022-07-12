#!/usr/bin/env python3

# necessary imports:
# import sys
import getpass
import hashlib



# confirm pw input request:
pw_input = getpass.getpass('Confirm password: ')

# by default, return utf-8 encoded version of pw str:
byte_input = pw_input.encode()

# sha512 hash of the pw, and return as str (double lenth, only hexidecimal digits):
hash_pw = hashlib.sha512(byte_input).hexdigest()

# open and read pwfile.txt to check for EXISTING pw hash, starting at begining of file:
pw_file = open('pwfile.txt', 'r')

# create new variables for count and lines with value of 0:
count=0
lines=0

# use while loop and read lines in file and, if pw found, increase count by 1
while(lines) != '':
    lines = pw_file.readline()
    line = lines.split()
    if hash_pw in line:
        count +=1

# at this point, if count is 1, then it will confirm pw was found and print hash of pw -- otherwise it will say it was NOT found
if count >= 1:
    print(' Password CONFIRMED.\n', 'Password hash is: \n', hash_pw)
else:
    print(' Password NOT FOUND.')

# close file:
pw_file.close()


