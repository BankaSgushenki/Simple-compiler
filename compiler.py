class Compiler:

	def showTree(self, node):
		print node.type,", ", node.value, ", ", node.name
		if node.firstOperand:
			self.showTree(node.firstOperand)
		if node.secondOperand:
			self.showTree(node.secondOperand)
		if node.next:
			self.showTree(node.next)		
		return
		