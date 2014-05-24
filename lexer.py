import re

class Token:
	def __init__(self,value,stringNumber,stringPosition, type):
        	self.value = value
        	self.strNumber = stringNumber
        	self.Position = stringPosition
        	self.type = type
        	self.id = stringNumber*1000 + stringPosition

class Lexer:
	def __init__(self, ROOT_PATH):
        	self.ROOT_PATH = ROOT_PATH

	patterns = {'NUM':'\d+', 'COND':'while|if',   'OP':'[\+\-\*\>\<\=]', 'BR':'[\(\)]', 'VAR':'[a-z]+', 'END':';','TYPE':'int|string','WS':'\s'}
	tokens = []
	lines = []
	words = ["while", "if"]
	nextTokenIndex = 0

	def openFile(self):
		file = open(self.ROOT_PATH, "r")
		self.lines = file.readlines()
		file.close()

	def showTokens(self):
		for token in self.tokens:
			if token.type != 'WS':
				print "Token:'" ,token.value,"':",token.strNumber,":",token.type

	def findTokens(self):
		for strNumber in range(len(self.lines)):
			line = temp =  self.lines[strNumber]
			for key, value in self.patterns.items():
				regex = re.compile(value)
				found = regex.finditer(line)
				for match in found :
					if key is 'COND':
						if match.group() not in self.words:
							currentToken = Token(match.group(),strNumber + 1,match.start(), key)
					else:
						currentToken = Token(match.group(),strNumber + 1,match.start(), key)
						if currentToken.type != "WS":
							self.tokens.append(currentToken)
				temp = regex.sub('', temp)
			errors = re.finditer('.',temp)
			for match in errors :
				print "Compilation Error: Unknown token:'", match.group(), ", line: ", strNumber + 1
				exit (0)
				
	def parse(self):
		self.openFile()
		self.findTokens()
		self.tokens.sort(key=lambda x: x.id)
		self.tokens.append(Token("EOF", 0 , 0, 0))
		self.showTokens()
	
	def nextToken(self):
		if self.tokens[self.nextTokenIndex].value != "EOF":
			token = self.tokens[self.nextTokenIndex]
			self.nextTokenIndex += 1
			return token
		else:
			return self.tokens[self.nextTokenIndex]

	def priviousToken(self):
		self.nextTokenIndex -= 1
		return self.tokens[self.nextTokenIndex]






