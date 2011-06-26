# __getitem__ method
# Reference: http://docs.python.org/reference/datamodel.html#object.__getitem__


class MinhaLista:
	def __init__(self):
		self.l = {}
		self.inicio = 0
	
	def append(self, item):
		self.l[self.inicio] = item
		self.inicio += 1
		
	def __getitem__(self, index):
		return self.l[index]
		
lista = MinhaLista()

lista.append("a")
lista.append("b")
print lista[0]
print lista[1]
