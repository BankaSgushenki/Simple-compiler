class Node:
    def __init__(self, type, name = None, value = None, next = None, op1 = None, op2 = None):
        self.type = type
        self.name = name
        self.value = value
        self.next = next
        self.firstOperand = op1
        self.secondOperand = op2

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

		if newNode.type is "VAR" or "NUM":
			token = self.lexer.nextToken()
			if token.type is "OP":
				operationNode = Node(token.type, name = token.value)
				tempNode = newNode
				newNode = operationNode
				newNode.firstOperand = tempNode
				newNode.secondOperand = self.getExpression()
			if token.type is "END":
				return newNode

		if self.lexer.nextToken().value is "EOF": 
			return newNode
		else:
			token = self.lexer.priviousToken()
			newNode.next = self.getExpression()
			return newNode