#Node data structure to represent the linked list
class Node:
	def __init__(self, init_data):
		self.data = init_data
		self.next = None

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_data(self, new_data):
		self.data = new_data

	def set_next(self, new_next):
		self.next = new_next

#Unordered list done through nodes
class UnorderedList:
	def __init__(self):
		self.head = None
		self.tail = None

	#Add a new item into the list
	def add(self, item):
		temp = Node(item)
		if self.head == None and self.tail == None:
			temp.set_next(self.head)
			self.head = temp
			self.tail = temp
		elif self.head == self.tail:
			temp.set_next(self.head)
			self.tail = self.head
			self.head = temp
		else:
			temp.set_next(self.head)
			self.head = temp



	#Remove a node from the list given the item that it contains
	#Assumes that the item is within the list
	def remove(self, item):
		current = self.head
		previous = None
		found = False

		while not found and current != None:
			if item == current.get_data():
				found = True
			else:
				previous = current
				current = current.get_next()

		if previous == None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())

	#Append an item to the end of the list (The tail of the unordered list)
	def append(self, item):
		new_node = Node(item)
		self.tail.set_next(new_node)
		self.tail = new_node

	#Inserts a item into a specified index within the list
	#Assumes that the index is a valid index within the list
	def insert(self, index, item):
		current = self.head
		previous = None
		node_to_insert = Node(item)
		count = 0

		while count != index:
			previous = current
			current = current.get_next()
			count += 1
		
		if previous == None:
			node_to_insert.set_next(current)
			self.head = node_to_insert
		else:
			previous.set_next(node_to_insert)
			node_to_insert.set_next(current)

	#Finds the index of an item within the list
	#Assumes that the item does exist in the list
	def index(self, item):
		current = self.head
		index = 0

		while item != current.get_data():
			current = current.get_next()
			index += 1

		return index

	#Pops an item out of the list
	#Assumes that the index is within the list
	def pop(self, index=0):
		current = self.head
		previous = None
		node_to_pop = None
		count = 0

		if index == 0:
			node_to_pop = self.head
			self.head = node_to_pop.get_next()
		else:
			while count != index:
				previous = current
				current = current.get_next()
				count += 1

			node_to_pop = current
			previous.set_next(current.get_next())

		return node_to_pop.get_data()



	#Searches for an node in our list that contains data matching the item
	#we're looking for
	def search(self, item):
		current = self.head
		found = False

		while not found and current != None:
			if item == current.get_data():
				found = True
			else:
				current = current.get_next()

		return found
	
	#Checks if the unordered list is none
	def is_empty(self):
		return self.head == None

	#Gets the size of the list by traversing through nodes
	def get_size(self):
		current = self.head
		count = 0
		while current != None:
			count += 1
			current = current.get_next()

		return count


#Ordered list that sorts the items by their characteristics 
class OrderedList:
	
	def __init__(self):
		self.head = None

	#Add an item to the list based upon it's value
	def add(self, item):
		current = self.head
		previous = None
		stop = False

		while current != None and not stop:
			if current.get_data() > item:
				stop = True
			else:
				previous = current
				current = current.get_next()
		
		node_to_add = Node(item)
		
		if previous == None:
			node_to_add.set_next(self.head)
			self.head = node_to_add
		else:
			node_to_add.set_next(current)
			previous.set_next(node_to_add)

	#remove an item from the list based upon it's value
	def remove(self, item):
		current = self.head
		previous = None
		found = False

		while not found and current != None:
			if current.get_data() == item:
				found = True
			else:
				previous = current
				current = current.get_next()

		if previous == None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next())

	#Search for an item within the list and return true or false
	#depending on if it is or not
	def search(self, item):
		current = self.head

		while current != None:
			if current.get_data() == item:
				return True
			else:
				if current.get_data() > item:
					return False
				else:
					current = current.get_next()

		return False

	#retrieve the index of an item in the list and then return it
	#Assumes that the item is inside of the list
	def index(self, item):
		current = self.head
		index = 0
		found = False

		while not found and current != None:
			if current.get_data() == item:
				found = True
			else:
				index += 1
				current = current.get_next()

		return index

	#Pop an item out of the list by index and then return it's data
	#Assumes index is within the size of the list
	def pop(self, index=0):
		current = self.head
		previous = None
		count = 0
		node_to_pop = None

		if index == 0:
			node_to_pop = current
			self.head = current.get_next()
		else:
			while count < index:
				previous = current
				current = current.get_next()

			node_to_pop = current
			previous.set_next(current.get_next())

		return node_to_pop.get_data()

	#Check to see whether or not the list is empty
	def is_empty(self):
		return self.head == None

	#Get the size of the list that we're currently working in
	def get_size(self):
		current = self.head
		count = 0

		while current != None:
			count += 1

		return count

