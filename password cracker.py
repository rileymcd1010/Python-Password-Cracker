import hashlib
import datetime
import random

#My plan is to generate a list of hashes for every combination of a 
#password's length until the password is generated and the 2 MD5 hashes
#match. I am using the hashlib library to generate the hashes for each
#random password, the datetime lib to track time to crack, and random lib so 
#I can generate the random passwords to try and match with the given one.

passlist = open("hashes.txt", "r")
print passlist
#theinput = random(str.length of 1)
#for x in range(0,theinput.len()):

#encode() the string to bytes
	generated = hashlib.md5()
#digest() returns the data in bytes