# Named and optional parameters
# Reference: http://diveintopython.org/power_of_introspection/optional_arguments.html
#
# This example: A tail-recursive factorial function (using an accumulator)

def factorial(n, acc=1):
    if (n == 1): return acc
    return factorial(n-1, acc*n)


print factorial(5)