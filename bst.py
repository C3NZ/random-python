#Binary search tree class
#This module includes:
#The Node class implementation to represent the nodes on the tree
#The BST class Which will construct a tree from the Node class
#The testing code


#Node implemented for binary tree use
class Node:

	def __init__(self, data):
		self.data = data
		self.left_child = None
		self.right_child = None

	#Insert a node into the tree recursively if need be
	def insert(self, data):
		if data < self.data:
			if self.left_child is None:
				self.left_child = Node(data)
			else:
				self.left_child.insert(data)
		else:
			if self.right_child is None:
				self.right_child = Node(data)
			else:
				self.right_child.insert(data)

	#Remove a node from the tree recursively
	#In the event of their being a left and right child node attached
	#to the node we're removing, we select the smallest smallest number
	#from the right childs tree and set that to be the node we just 
	#removed and then attach other nodes to it
	def remove(self, data, parent_node=None):
		if data < self.data:
			if self.left_child is not None:
				self.left_child.remove(data, self)
		elif data > self.data:
			if self.right_child is not None:
				self.right_child.remove(data, self)
		else:
			if self.left_child and self.right_child:
				self.data = self.right_child.get_min()
				self.right_child.remove(self.data, self)	
			elif parent_node.left_child == self:	
				#Attach branch of tree to the parent node
				if self.left_child:
					temp_node = self.left_child
				else:
					temp_node = self.right_child
				parent_node.left_child = temp_node

			elif parent_node.right_child == self:	
				#Attach branch of tree to the parent node
				if self.left_child:
					temp_node = self.left_child
				else:
					temp_node = self.right_child

				parent_node.right_child = temp_node

	#Get the data that the node is holding
	def get_data(self):
		return self.data

	#Retrieve the smallest number from the tree recursively
	def get_min(self):
		if self.left_child is None:
			return self.data
		else:
			return self.left_child.get_min()
	
	#Retrieve the largest number from the tree recursively
	def get_max(self):
		if self.right_child is None:
			return self.data
		else:
			return self.right_child.get_max()

	#Traverse the tree in order (Ascending value)
	def traverse_in_order(self):
		if self.left_child is not None:
			self.left_child.traverse_in_order()

		print(self.data)

		if self.right_child is not None:
			self.right_child.traverse_in_order()


#Binary search tree implementation
class BST:

	def __init__(self):
		self.root_node = None

	#Insert a node into the tree
	def insert(self, data):
		if self.root_node is None:
			self.root_node = Node(data)
		else:
			self.root_node.insert(data)

	#Remove node from the tree
	def remove(self, data_to_remove):
		if self.root_node:
			if self.root_node.get_data() == data_to_remove:
				temp_node = Node(None)
				temp_node.left_child = self.root_node
				self.root_node.remove(data_to_remove, temp_node)
			else:
				self.root_node.remove(data_to_remove)

	#Get the max value from the tree if a root node is set
	def get_max(self):
		if self.root_node:
			return self.root_node.get_max()
	
	#get the minimum value from the tree if a root node is set
	def get_min(self):
		if self.root_node:
			return self.root_node.get_min()

	#Traverse the tree in ascending order if a root node is set
	def traverse_in_order(self):
		if self.root_node:
			print('Traversing the tree:')
			self.root_node.traverse_in_order()

#Testing area to make sure the Binary search tree works,
#It does!
if __name__ == '__main__':
	bst = BST()
	bst.insert(12)
	bst.insert(10)
	bst.insert(-2)
	bst.insert(1)

	bst.traverse_in_order()

	bst.remove(10)

	bst.traverse_in_order()
