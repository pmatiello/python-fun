# Generator function
# Reference: http://www.python.org/dev/peps/pep-0318/

class capture_exceptions():
    
    def __init__(self, function):
        self.function = function
    
    def __call__(self, *args, **kwargs):
        try:
            return self.function(*args, **kwargs)
        except Exception as e:
            return e

@capture_exceptions
def divide(dividend, divisor):
    return dividend / divisor

print divide(10, 5)
print divide(0, 0)
