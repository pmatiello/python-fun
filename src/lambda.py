# Lambda
# Reference: http://diveintopython.org/power_of_introspection/lambda_functions.html

numbers = [0,1,2,3,4,5,6,7,8,9]
square_func = lambda x: x**2
squared = map(square_func, numbers)
print squared