class LinkedList:

	centinel = 	None
	size = None

	def __init__(self):
		self.size = 0
		self.centinel = Node(None)
		self.centinel.setRight(self.centinel)
		self.centinel.setLeft(self.centinel)

	def __str__(self):
		representation = ""
		node = self.centinel.getRight()
		for i in range(self.size):
			if (i+1 < self.size):
				representation += str(node.getValue()) + ","
			else:
				representation += str(node.getValue())
			node = node.getRight()
		return representation

	def pushLeft(self, value):
		newNode = Node(value)
		newNode.setRight(self.centinel.getRight())
		newNode.setLeft(self.centinel)
		self.centinel.getRight().setLeft(newNode)
		self.centinel.setRight(newNode)
		self.size += 1

	def pushRight(self, value):
		newNode = Node(value)
		newNode.setRight(self.centinel)
		newNode.setLeft(self.centinel.getLeft())
		self.centinel.getLeft().setRight(newNode)
		self.centinel.setLeft(newNode)
		self.size += 1

	def popLeft(self):
		node = self.centinel.getRight()
		node.getRight().setLeft(self.centinel)
		self.centinel.setRight(node.getRight())
		self.size -= 1
		return node

	def popRight(self):
		node = self.centinel.getLeft()
		node.getLeft().setRight(self.centinel)
		self.centinel.setLeft(node.getLeft())
		self.size -= 1
		return node

	def getRight(self):
		return self.centinel.getRight()

	def getLeft(self):
		return self.centinel.getLeft()

	def pushRightNode(self, node, value):
		newNode = Node(value)
		newNode.setRight(node.getRight())
		newNode.setLeft(node)
		node.getRight().setLeft(newNode)
		node.setRight(newNode)
		self.size += 1

	def pushLeftNode(self, node):
		newNode = Node(value)
		newNode.setRight(node)
		newNode.setLeft(node.getLeft)
		node.getLeft().setRight(newNode)
		node.setLeft(newNode)
		self.size += 1

	def popRightNode(self, node):
		pass

	def popLeftNode(self, node):
		pass

	def getValues(self):
		representation = []
		node = self.centinel.getRight()
		for i in range(self.size):
			representation.append(node.getValue())
			node = node.getRight()
		return representation


class Node:

	value = None
	left = None
	right = None

	def __init__(self, value):
		self.value = value

	def __str__(self):
		return str(self.left) + " " + str(self.value) + " " + str(self.right)

	def setRight(self, right):
		self.right = right

	def setLeft(self, left):
		self.left = left

	def getRight(self):
		return self.right

	def getLeft(self):
		return self.left

	def getValue(self):
		return self.value


"""ls = LinkedList()
ls.pushRight(2)
ls.pushRight(2)
ls.pushLeft(1)
ls.pushRight(3)
print(ls.getValues())
ls.popLeft()
print(ls.getValues())
ls.popRight()
print(ls.getValues())"""
ls = LinkedList()
node1 = Node(2)
node2 = Node(9)
node3 = Node(33)
ls.pushRight(1)
ls.pushRight(2)
