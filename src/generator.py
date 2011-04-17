# Generator function
# Reference: http://diveintopython.org/dynamic_functions/stage6.html

def infinite_list(start=1):
    current = start
    while (True):
        yield current
        current = current + 1

for i in infinite_list(start=2):
    print i
