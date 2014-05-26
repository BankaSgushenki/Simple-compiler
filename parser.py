class Node:
    def __init__(self, type, name = None, value = None, next = None, op1 = None, op2 = None):
        self.type = type
        self.name = name
        self.value = value
        self.next = next
        self.op1 = op1
        self.op2 = op2
        if type is "NUM" or type is "STR": self.value = name

class Parser:

	PROGRAM, VAR, NUMBER, PRINT, OP = range(5)

	def __init__(self, lexer):
		self.lexer = lexer

	def parse(self):
		tree = Node("PROGRAM", next = self.getExpression())
		return tree

	def getExpression(self):
		token = self.lexer.nextToken()
		newNode = Node(token.type, name = token.value)

		if newNode.type is "VAR" or "NUM" or "STR":
			token = self.lexer.nextToken()
			if token.type is "OP":
				operationNode = Node(token.type, name = token.value)
				tempNode = newNode
				newNode = operationNode
				newNode.op1 = tempNode
				newNode.op2 = self.getExpression()
			if token.type is "END":
				return newNode

		if newNode.type is "FUNC":
			if token.type is "VAR" or  "NUM" or "STR":
				operandNode = Node(token.type, name = token.value)
				newNode.op1 = operandNode
				token = self.lexer.nextToken()
			if token.type is "OP":
				newNode.op1 = self.getExpression()
			if token.type is "END":
				newNode.next = self.getExpression()
				return newNode

		if self.lexer.nextToken().value is "EOF": 
			return newNode
		else:
			token = self.lexer.priviousToken()
			newNode.next = self.getExpression()
			return newNode