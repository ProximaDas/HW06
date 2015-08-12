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
#       1: reproachful coalfishes
#       2: coalfishes reproachfully
#       3: coalfishes reproachfulnesses
##############################################################################
# Imports
import itertools
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
			
def make_sentence():
	letters = "acefhlo"
	flag = False
	word_list = []
	with open("words.txt","r") as handler:
		words = handler.read().split()
		for word in words:
			for letter in letters:
				if letter in word:
					flag = True
				else:
					flag = False
					break
			if flag == True:
				word_list.append(word)
	print ' '.join(word_list)

# def combination():
# 	list_ = list('acefhlo')
# 	new = itertools.chain.from_iterable(itertools.combinations(list_,i) for i in range(len(list_)+1))
# 	# print list(new)
# 	while True:
# 		try:
# 			print ''.join(new.next())
# 		except:
# 			break
			
##############################################################################
def main():
    print uses_only("banana","aBn")
    make_sentence()
    combination()

if __name__ == '__main__':
    main()
