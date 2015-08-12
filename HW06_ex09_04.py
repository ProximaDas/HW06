#!/usr/bin/env python
# HW06_ex09_04.py

# (1)
# Write a function named uses_only that takes a word and a string of letters,
# and that returns True if the word contains only letters in the list.
#   - write uses_only
# (2)
# Can you make a sentence using only the letters acefhlo? Other than "Hoe
# alfalfa?"
#   - write function to assist you
#   - type favorite sentence(s) here:
#       1:
#       2:
#       3:
##############################################################################
# Imports

# Body
def uses_only(word,letters):
	flag = False
	for letter in word.lower():
		if letter in letters.lower():
			flag = True
		else:
			flag = False
			break
	return flag		
			

##############################################################################
def main():
    print uses_only("banana","aBn")

if __name__ == '__main__':
    main()
