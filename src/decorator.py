# Generator function
# Reference: http://www.python.org/dev/peps/pep-0318/

class capture_exceptions():
    
    def __init__(self, function):
        self.function = function
    
    def __call__(self, *args, **kwargs):
        return self.function(*args, **kwargs)

@capture_exceptions
def divide(dividend, divisor):
    try:
        return dividend / divisor
    except Exception as e:
        return e

print divide(10, 5)
print divide(0, 0)