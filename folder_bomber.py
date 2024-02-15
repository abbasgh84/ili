import uuid 
import os
import sys

def folder(amt):
	for count in range(amt): # Using our value in main() to loop through the makedirs.
		os.makedirs(str(uuid.uuid4()))
		print(count)

def main():
	amt ='160'
	folder(int(amt)) # just reassuring that its an integer not an ascii character,
    
if __name__ == '__main__':
	main()
	sys.exit()

