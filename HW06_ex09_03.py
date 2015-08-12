#!/usr/bin/env python
# HW06_ex09_03.py

# (1)
# Write a function named avoids that takes a word and a string of forbidden
# letters, and that returns True if the word doesn't use any of the forbidden
# letters.
#   - write avoids
# (2)
# Modify your program to prompt the user to enter a string of forbidden
# letters and then print the number of words that don't contain any of them.
#   - write function(s)
# (3)
# Can you find a combination of 5 forbidden letters that excludes the smallest
# number of words?
#   - write a function that finds this combination of letters
#   - have that function print the letters and print the # of words excluded
##############################################################################
# Imports
from collections import Counter
# Body
def avoids(word,forbidden):
	flag = ''

	for letter in forbidden:
		#Check if letter is present in word
		if letter in word:
			flag = False
	if flag == False:
		return False
	else:
		return True

def avoids_file():
	count = 0
	flag = False
	input = raw_input("Enter forbidden words: ")
	#Open words.txt file
	with open("words.txt","r") as handler:
		words = handler.read().split()
		for word in words:
			for letter in input:
				if not(letter in word):
					flag = True
				else:
					flag = False
					break
			if flag == True:
				count += 1

	print "{number} words didn't contain {list}".format(number=count,list=input)

def combination():
	count = 0
	with open("words.txt","r") as handler:
		occurance = Counter()
		for word in handler:
			occurance.update(word.strip())
	#Sort the dictionary
	forbidden = sorted(occurance,key=occurance.get)[:5]
	with open("words.txt","r") as handler:
		words = handler.read().split()
		for word in words:
			for letter in forbidden:
				if letter not in word:
					flag = True
				else:
					flag = False
					break
			if flag == True:
				count += 1
	print ' '.join(forbidden) + " excludes the smallest number of words: " + str(count)
		
##############################################################################
def main():
    # print avoids("Proxima","el")
    # avoids_file()
    combination()

if __name__ == '__main__':
    main()
