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

	def __init__(self, lexer):
		self.lexer = lexer

	def parse(self):
		tree = Node("PROGRAM", next = self.getExpression())
		return tree

	def getExpression(self):
		errorsFlag = 0
		token = self.lexer.nextToken()
		newNode = Node(token.type, name = token.value)
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
			if token.type is "VAR" or token.type is "STR":
				operandNode = Node(token.type, name = token.value)
				newNode.op1 = operandNode
				token = self.lexer.nextToken()

			if token.type is "END":
				newNode.next = self.getExpression()
				return newNode
			else: 
				print "Invalid token: ", token.value, ": line: ", token.strNumber 
				exit (0)

		if newNode.type is "COND":
			operandNode1 = Node(token.type, name = token.value)
			token = self.lexer.nextToken()

			if token.type is "OP":
				operationdNode = Node(token.type, name = token.value)
				newNode.op1 = operationdNode
				operationdNode.op1 = operandNode1
				token = self.lexer.nextToken()
				operationdNode.op2 = Node(token.type, name = token.value)
				token = self.lexer.nextToken()
			if token.type is "END":
				newNode.op2 = self.getExpression()
				newNode.next = newNode.op2.op2
				return newNode
			else: 
				print "Invalid token: ", token.value, ": line: ", token.strNumber
				exit (0)

		if self.lexer.nextToken().value is "EOF": 
			return newNode
		else:
			token = self.lexer.priviousToken()
			newNode.next = self.getExpression()
			return newNode