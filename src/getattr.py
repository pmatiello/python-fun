# __getattr__ method
# Reference: http://www.python.org/dev/peps/pep-0213/
# Reference: http://docs.python.org/reference/datamodel.html#object.__getattr__
# Reference: http://docs.python.org/reference/datamodel.html#object.__setattr__

class WithGambi:
	def __init__(self):
		self.d = {}
	
	def __getattr__(self, name):
		def missing(*args, **kwargs):
			return self.method_missing(name, *args, **kwargs)
		return missing
	
	def method_missing(self, name, *args, **kwargs):
		print "oh no the method is missing", args, kwargs

gambi = WithGambi()
gambi.bla()
