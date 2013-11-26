import pygame as py
from pygame.locals import *

class Reader(object):
	def __init__(self, path):
		self.data = raw_input("Write the text to split here > ")
		self.data = self.data.split(" ")
		
		self.ph = []
		
	def getChars(self, start):
		n = 0
		s = []
		ind = start
		for i in range (start, len(self.data)):
			ln = len(self.data[i])+1
			n += ln
			if n > 140:
				n -= ln
				break
			else:
				s.append(self.data[i])
				ind += 1
			
		s = " ".join(s)
		self.ph.append(s)
		if ind < len(self.data):
			self.getChars(ind)
		
def main():
	reader = Reader("dialog.txt")
	reader.getChars(0)
	
	f = open("nfile.txt", "w")
	for i in range (len(reader.ph)):
		f.write(reader.ph[i]+"\n")
	f.close()
	print "A file has been created on program's directory with your text splitted into 140 chars lines."
	return 0
	
if __name__ == "__main__":
	main()
