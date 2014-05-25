class Int:
	def __init__(self,name,value = None):
			self.name = name
			self.value = value

class Interpreter:
	def __init__(self,tree):
			self.tree = tree

	variablesList = {}

	def execute(self, node):
		if node.type is "FUNC": self.PrintFunction(node.op1.name)
		if node.op2: self.execute(node.op2)
		if node.next: self.execute(node.next)

	def findVariables(self, node):
		if node.type is "VAR":
			variable =  Int(node.name)
			self.variablesList[variable.name] = variable.value

		if node.op1: self.findVariables(node.op1)
		if node.op2: self.findVariables(node.op2)
		if node.next: self.findVariables(node.next)		
		return

	def defVariables(self, node):
		if node.name is "=":
			self.variablesList[node.op1.name] = node.op2.value
			if node.op2.type is "VAR":
				self.variablesList[name] = self.variablesList[node.op2.name]

		if node.op1: self.defVariables(node.op1)
		if node.op2: self.defVariables(node.op2)
		if node.next: self.defVariables(node.next)		
		return

	def countVariables(self, node):
		self.countConstantes(self.tree)

		if node.name is "+":
				firstVariable = node.op1
				secondVariable = node.op2
				if firstVariable.type is "VAR":
					firstVariable.value = self.variablesList[firstVariable.name]
				if secondVariable.type is "VAR":
					secondVariable.value = self.variablesList[secondVariable.name]
				if secondVariable.type is "OP":
					self.countVariables(op2)
				node.value = int(firstVariable.value) + int(secondVariable.value)

		if node.op2: self.countVariables(node.op2)
		if node.next: self.countVariables(node.next)
		self.defVariables(self.tree)	
		return 

	def countConstantes(self, node):
		if node.op2: self.countConstantes(node.op2)
		if node.next: self.countConstantes(node.next)

		if node.name is "+":	
			firstVariable = node.op1
			secondVariable = node.op2
			if firstVariable.type is "NUM" and secondVariable.type is "NUM":
				node.value = int(firstVariable.value) + int(secondVariable.value)
				node.type = "NUM"
				
		self.defVariables(self.tree)
		return 

	def showTree(self, node):
		print node.type,", ", node.value, ", ", node.name
		if node.op1: self.showTree(node.op1)
		if node.op2: self.showTree(node.op2)
		if node.next: self.showTree(node.next)		
		return

	def showVars(self):
		print self.variablesList

	def PrintFunction(self,variableToPrint):
		print self.variablesList[variableToPrint]

	def interpretate(self):
		self.findVariables(self.tree)
		self.defVariables(self.tree)
		self.countVariables(self.tree)
		self.execute(self.tree)




		