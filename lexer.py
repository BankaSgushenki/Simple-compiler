import re

class Token:
	def __init__(self,value,stringNumber,stringPosition, type):
        	self.value = value
        	self.strNumber = stringNumber
        	self.Position = stringPosition
        	self.type = type
        	self.id = stringNumber*1000 + stringPosition 
        	if value is ";": self.id += 10  #mdaa....

class Lexer:
	def __init__(self, ROOT_PATH):
        	self.ROOT_PATH = ROOT_PATH

	patterns = {'NUM':'(?<!w|")(\d+)', 'STR':'"(\w|\s|\?|\!|\,)+"',
	'COND':'while|if', "FUNC": 'print|input',  'OP':'[\+\-\*\>\<\=]|is', 
	'BR':'[\(\)]', 'VAR':'(?<!")([a-z]+)', 'END':';|:','WS':'\s'}
	tokens = []
	lines = []
	words = ["while","if","is","print","input"]
	nextTokenIndex = 0

	def openFile(self):
		file = open(self.ROOT_PATH, "r")
		self.lines = file.readlines()
		file.close()

	def showTokens(self):
		for token in self.tokens:
			print "Token:'" ,token.value,"':",token.strNumber,":",token.type

	def findStrings(self):
		for strNumber in range(len(self.lines)):
			regex = re.compile(self.patterns['STR'])
			found = regex.finditer(self.lines[strNumber])
			for match in found :
				self.tokens.append(Token(match.group()[1:-1],strNumber + 1,match.start(), 'STR'))
			self.lines[strNumber] = regex.sub('', self.lines[strNumber])

	def findTokens(self):
		for strNumber in range(len(self.lines)):
			line = temp =  self.lines[strNumber]
			for key, value in self.patterns.items():
				regex = re.compile(value)
				found = regex.finditer(line)
				for match in found :
					if key is 'VAR':
						if match.group() not in self.words:
							self.tokens.append(Token(match.group(),strNumber + 1,match.start(), key))
					elif key is not "WS" and key is not "STR":
							self.tokens.append(Token(match.group(),strNumber + 1,match.start(), key))
				temp = regex.sub('', temp)
			errors = re.finditer('.+',temp)
			for match in errors :
				print "Compilation Error: Unknown token:'", match.group(), ", line: ", strNumber + 1
				
	def parse(self):
		self.openFile()
		self.findStrings()
		self.findTokens()
		self.tokens.sort(key=lambda x: x.id)
		self.tokens.append(Token("EOF", 0, 0, 0))
	
	def nextToken(self):
		if self.tokens[self.nextTokenIndex].value != "EOF":
			token = self.tokens[self.nextTokenIndex]
			self.nextTokenIndex += 1
			return token
		else: return self.tokens[self.nextTokenIndex]

	def currentToken(self):
		return self.tokens[self.nextTokenIndex]

	def priviousToken(self):
		self.nextTokenIndex -= 1
		return self.tokens[self.nextTokenIndex]