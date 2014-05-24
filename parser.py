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

		tocken = self.nextTocken()
		newNode = Node(tocken.type, name = tocken.value)

		if newNode.type == "VAR" or "NUM":
			tocken = self.nextTocken()
			if tocken.type == "OP":
				operationNode = Node(tocken.type, name = tocken.value)
				tempNode = newNode
				newNode = operationNode
				newNode.firstOperand = tempNode
				newNode.secondOperand = self.getExpression()
			if tocken.type == "END":
				return newNode

		if self.nextTocken().value == "EOF": 
			return newNode
		else:
			tocken = self.priviousTocken()
			newNode.next = self.getExpression()
			return newNode

	def nextTocken(self):
		return self.lexer.nextTocken()

	def priviousTocken(self):
		return self.lexer.priviousTocken()