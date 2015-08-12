#!/usr/bin/env python
# HW06_ex09_02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
##############################################################################
# Imports

# Body
def has_no_e(word):
	if not('e' in word.lower()):
		return True
	else:
		return False

def has_no_e_mod(list):
	count = 0
	for word in list:
		if not('e' in word.lower()):
			print word
			count += 1
	# Compute percentage of words that have no "e"
	percent = float(count)/len(list) * 100
	print percent
	
##############################################################################
def main():
    print has_no_e('Proxima')
    has_no_e_mod(['Proxima', 'Das', 'Mohapatra', 'Etsy'])

if __name__ == '__main__':
    main()
