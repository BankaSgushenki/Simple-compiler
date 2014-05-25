class Int:
	def __init__(self,name,value = None):
			self.name = name
			self.value = value

class Interpreter:
	def __init__(self,tree):
			self.tree = tree

	variablesList = []
	variablesNames = []

	def execute(self, node):

		#print node.type
		if node.type is "FUNC": self.PrintFunction(node.firstOperand.name)

		if node.secondOperand:
			self.execute(node.secondOperand)
		if node.next:
			self.execute(node.next)

	def findVariables(self, node):
		if node.type is "VAR":
			if node.name not in self.variablesNames:
				variable =  Int(node.name)
				self.variablesList.append(variable)
				self.variablesNames.append(node.name)

		if node.firstOperand:
			self.findVariables(node.firstOperand)
		if node.secondOperand:
			self.findVariables(node.secondOperand)
		if node.next:
			self.findVariables(node.next)		
		return

	def defVariables(self, node):

		if node.name is "=":
			name = node.firstOperand.name
			if node.secondOperand.type is "NUM" or "OP":
				for var in self.variablesList:
					if var.name is name:
						var.value = node.secondOperand.value

			if node.secondOperand.type is "VAR":
				for var in self.variablesList:
					if var.name is node.secondOperand.name:
						value = var.value
				for var in self.variablesList:
					if var.name is name:
						var.value = value

		if node.firstOperand:
			self.defVariables(node.firstOperand)
		if node.secondOperand:
			self.defVariables(node.secondOperand)
		if node.next:
			self.defVariables(node.next)		
		return

	def countVariables(self, node):

		self.countConstantes(self.tree)

		if node.name is "+":
				firstVariable = node.firstOperand
				secondVariable = node.secondOperand

				if firstVariable.type is "VAR":
					name = firstVariable.name
					for var in self.variablesList:
						if var.name is name:
							firstVariable.value = var.value

				if secondVariable.type is "VAR":
					name = secondVariable.name
					for var in self.variablesList:
						if var.name is name:
							secondVariable.value = var.value

				if secondVariable.type is "OP":
					self.countVariables(secondVariable)

				node.value = int(firstVariable.value) + int(secondVariable.value)
			
		if node.secondOperand:
			self.countVariables(node.secondOperand)
		if node.next:
			self.countVariables(node.next)

		self.defVariables(self.tree)	
		return 

	def countConstantes(self, node):
		if node.secondOperand:
			self.countConstantes(node.secondOperand)
		if node.next:
			self.countConstantes(node.next)

		if node.name is "+":	
			firstVariable = node.firstOperand
			secondVariable = node.secondOperand
			if firstVariable.type is "NUM" and secondVariable.type is "NUM":
				node.value = int(firstVariable.value) + int(secondVariable.value)
				node.type = "NUM"

		self.defVariables(self.tree)
		return 

	def showTree(self, node):
		print node.type,", ", node.value, ", ", node.name

		if node.firstOperand:
			self.showTree(node.firstOperand)
		if node.secondOperand:
			self.showTree(node.secondOperand)
		if node.next:
			self.showTree(node.next)		
		return

	def showVars(self):
		for var in self.variablesList:
			print "Var:'", var.name,"':", var.value

	def PrintFunction(self,variableToPrint):
		for var in self.variablesList:
			if var.name is variableToPrint:
				print var.value

	def interpretate(self):
		#self.showTree(self.tree)
		self.findVariables(self.tree)
		self.defVariables(self.tree)
		self.countVariables(self.tree)
		#self.showVars()
		self.execute(self.tree)
		#self.showTree(self.tree)



		