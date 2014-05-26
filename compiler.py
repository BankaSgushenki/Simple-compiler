class Int:
	def __init__(self,name,value = None):
			self.name = name
			self.value = value

def caculate(first, second, operation):
	try: 
		first = int(first)
		second = int(second)
		if operation is "+": return first + second
		if operation is "-": return first - second
		if operation is "*": return first * second
   	except ValueError:
		result = str(first) + str(second)
	return result

def mathOperation(node):
	if node.op1.type is "VAR":
		node.op1.value = Interpreter.variablesList[node.op1.name]
	if node.op2.type is "VAR":
		node.op2.value = Interpreter.variablesList[node.op2.name]
	if node.op2.type is "OP":
		node.op2.value = mathOperation(node.op2)	
	try:
		node.value = caculate(node.op1.value, node.op2.value, node.name)
	except TypeError: pass
	return node.value	


def printFunction(node):
	if node.type is "VAR": 
		print Interpreter.variablesList[node.name]
		return
	if node.type is "NUM" or "STR": print node.value

def inputFunction(node):
	Interpreter.variablesList[node.name] = raw_input()

class Interpreter:
	def __init__(self,tree):
			self.tree = tree

	variablesList = {}

	def execute(self, node):
		if node.name == "print": printFunction(node.op1)
		if node.name == "input": inputFunction(node.op1)
		if node.name == "=":
			self.variablesList[node.op1.name] = mathOperation(node.op2)
		if node.op2: self.execute(node.op2)
		if node.next: self.execute(node.next)

	def findVariables(self, node):
		if node.type is "VAR":
			variable =  Int(node.name)
			self.variablesList[variable.name] = variable.value

		if node.op1: self.findVariables(node.op1)
		if node.op2: self.findVariables(node.op2)
		if node.next: self.findVariables(node.next)		

	def defVariables(self, node):
		if node.name is "=":
			self.variablesList[node.op1.name] = node.op2.value
			if node.op2.type is "VAR":
				self.variablesList[name] = self.variablesList[node.op2.name]

		if node.op1: self.defVariables(node.op1)
		if node.op2: self.defVariables(node.op2)
		if node.next: self.defVariables(node.next)		

	def countVariables(self, node):
		if node.name is "+" or node.name is "-" or node.name is "*":
			if node.op1.type is "VAR":
				node.op1.value = self.variablesList[node.op1.name]
			if node.op2.type is "VAR":
				node.op2.value = self.variablesList[node.op2.name]
			if node.op2.type is "OP":
				self.countVariables(node.op2)
			
			try:
				node.value = caculate(node.op1.value, node.op2.value, node.name)
			except TypeError: pass

		if node.op1: self.countVariables(node.op1)
		if node.op2: self.countVariables(node.op2)
		if node.next: self.countVariables(node.next)
		self.defVariables(self.tree)	

	def showTree(self, node):
		print node.type,", ", node.value, ", ", node.name
		if node.op1: self.showTree(node.op1)
		if node.op2: self.showTree(node.op2)
		if node.next: self.showTree(node.next)		

	def showVars(self):
		print self.variablesList

	def interpretate(self):
		self.findVariables(self.tree)
		self.defVariables(self.tree)
		self.countVariables(self.tree)
		self.execute(self.tree)	