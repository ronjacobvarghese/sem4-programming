#!/usr/bin/python3


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LL:
	def __init__(self, ar=None):
		self.top = None
		if ar != None:
			self.create_ll(ar)

	def insert(self, data):
		nd = Node(data)
		if self.top == None:
			self.top = nd
		else:
			node = self.top
			while node.next != None:
				node = node.next
			node.next = nd

	def delete(self):
		if self.top == None:
			raise Exception('Empty Linked List!')
		else:
			nd = self.top
			self.top = self.top.next
			return nd

	def traverse(self):
		node = self.top
		while node:
			print(f"{node.data} ->", end=" ")
			node = node.next
		print('')

	def create_ll(self, ar):
		for i in ar:
			self.insert(i)


def adjacency_lst(ar):
	ret = {}
	for j, i in enumerate(ar):
		lst = [ctr for ctr, j in enumerate(i) if j != 0]
		ret[j] = LL(lst)
	return ret


def adjacency_matrix(ar):
	ret = []
	for ctr, i in enumerate(ar):
		ret += [[0]*len(ar)]
		for j in i.split()[1:]:
			if j != '->':
				ret[ctr][int(j)] = 1
	return ret


def print_lst(ar):
	for ctr, i in ar.items():
		print(ctr, end=' -> ')
		i.traverse()
if __name__ == '__main__':
	st = ["0 -> 1 -> 3","1 -> 0 -> 2 -> 3 -> 5 -> 6","2 -> 1 -> 3 -> 4 -> 5","3 -> 0 -> 1 -> 2 -> 4","4 -> 2 -> 3 -> 6","5 -> 1 -> 2","6 -> 1 -> 4"]
	res = adjacency_lst(adjacency_matrix(st))
	print_lst(res)
