# Callable object
# Reference: http://docs.python.org/reference/datamodel.html#object.__call__

class Accumulator:
    
    def __init__(self):
        self.acc = 0
    
    def __call__(self, more):
        self.acc = self.acc + more
        return self.acc

acc = Accumulator()

print acc(0)
print acc(10)
print acc(5)
