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

def math(node):
	if node.op1.type is "VAR":
		node.op1.value = Interpreter.variables[node.op1.name]
	if node.op2.type is "VAR":
		node.op2.value = Interpreter.variables[node.op2.name]
	if node.op2.type is "OP":
		node.op2.value = math(node.op2)	
	try:
		node.value = caculate(node.op1.value, node.op2.value, node.name)
	except TypeError: pass
	return node.value	

def checkCondition(node):
	if Interpreter.variables[node.op1.name] == node.op2.value: return 1
	else: return 0


def printFunction(node):
	if node.type is "VAR": 
		print Interpreter.variables[node.name]
		return
	if node.type is "NUM" or "STR": print node.value

def inputFunction(node):
	Interpreter.variables[node.name] = raw_input()

class Interpreter:
	def __init__(self,tree):
			self.tree = tree

	variables = {}

	def condition(self, node):
		if node.op1.type is "OP":
			if checkCondition(node.op1): 
				self.execute(node.op2)
			else: 
				self.execute(node.next)


	def execute(self, node):
		if node.name == "print": printFunction(node.op1)
		if node.name == "input": inputFunction(node.op1)
		if node.name == "=":
			if node.op2.type is not "NUM":
				self.variables[node.op1.name] = math(node.op2)
		if node.name == "if": 
			self.condition(node)
			return
		if node.op2: self.execute(node.op2)
		if node.next: self.execute(node.next)

	def findVariables(self, node):
		if node.type is "VAR":
			variable =  Int(node.name)
			self.variables[variable.name] = variable.value

		if node.op1: self.findVariables(node.op1)
		if node.op2: self.findVariables(node.op2)
		if node.next: self.findVariables(node.next)		

	def defVariables(self, node):
		if node.name is "=":
			self.variables[node.op1.name] = node.op2.value
			if node.op2.type is "VAR":
				self.variables[name] = self.variables[node.op2.name]

		if node.op1: self.defVariables(node.op1)
		if node.op2: self.defVariables(node.op2)
		if node.next: self.defVariables(node.next)		

	def countVariables(self, node):
		if node.name is "+" or node.name is "-" or node.name is "*":
			if node.op1.type is "VAR":
				node.op1.value = self.variables[node.op1.name]
			if node.op2.type is "VAR":
				node.op2.value = self.variables[node.op2.name]
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
		print self.variables

	def interpretate(self):
		self.findVariables(self.tree)
		self.defVariables(self.tree)
		self.countVariables(self.tree)
		self.execute(self.tree)	