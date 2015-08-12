def main():
	list_names = []
	count = 0
	with open("roster.txt") as handle:
		names = handle.read().split()
		for name in names:
			if 'e' in name.lower():
				count += 1
				list_names.append(name)

	print "{number} names contain the letter 'e'".format(number=count)
	print "The names are: " + ' '.join(list_names)


if __name__ == '__main__':
	main()