import os
import re

ROOT_PATH = os.path.dirname(__file__) + "/source.txt"

class Lexer:

	class Tocken:
		def __init__(self,value,stringNumber,stringPosition, type):
        		self.value = value
        		self.strNumber = stringNumber
        		self.Position = stringPosition
        		self.type = type
        		self.id = stringNumber*1000 + stringPosition

	patterns = {'NUM':'\d+', 'COND':'while|if',   'OP':'[\+\-\*\>\<\=]', 'BR':'[\(\)]', 'VAR':'[a-z]+', 'END':';','TYPE':'int|string','WS':' '}
	tockens = []
	lines = []
	words = ["while", "if"]
	nextTockenIndex = -1
	currentTockenIndex = -1

	def openFile(self, ROOT_PATH):
		file = open(ROOT_PATH, "r")
		lines = file.readlines()
		file.close()
		self.lines = lines

	def showTockens(self):
		for i in range(len(self.tockens)):
			tocken = self.tockens[i]
			if tocken.type != 'WS':
				print "Tocken:'" ,tocken.value,"':",tocken.strNumber,":", tocken.Position,":",tocken.type

	def findTokens(self):
		for strNumber in range(len(self.lines)):
			line = self.lines[strNumber]
			temp = line
			for key, value in self.patterns.items():
				regex = re.compile(value)
				found = regex.finditer(line)
				for match in found :
					if key == 'COND':
						if match.group() not in self.words:
							currentTocken = self.Tocken(match.group(),strNumber + 1,match.start(), key)
					else:
						currentTocken = self.Tocken(match.group(),strNumber + 1,match.start(), key)
						if currentTocken.type != "WS":
							self.tockens.append(currentTocken)
				temp = regex.sub('', temp)
			err = re.compile('.')
			found = err.finditer(temp)
			for match in found :
				print "Compilation Error: Unknown tocken:'", match.group(), ", line: ", strNumber + 1

	def parse(self):
		self.openFile(ROOT_PATH)
		self.findTokens()
		self.tockens.sort(key=lambda x: x.id)
		self.tockens.append(self.Tocken("EOF", 0 , 0, 0))
		self.showTockens()
	
	def nextTocken(self):
		if self.currentTockenIndex < len(self.tockens) - 1:
			self.nextTockenIndex += 1
			self.currentTockenIndex += 1
			return self.tockens[self.nextTockenIndex]
		else:
			return self.tockens[self.nextTockenIndex]

	def priviousTocken(self):
		self.nextTockenIndex -= 1
		self.currentTockenIndex -= 1
		return self.tockens[self.currentTockenIndex]






