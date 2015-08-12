import random

def main():
	with open("random.txt","wb") as handle:
		for x in range(1,10):
			handle.write(str(random.randint(1,100))+"\r\n")

if __name__ == '__main__':
	main()