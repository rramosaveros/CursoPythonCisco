# module.py

#!/usr/bin/env python3 

print("I like to be a module.")
print(__name__) 

counter = 0
if __name__ == "__main__":
    print("I prefer to be a module")
else:
    print("I like to be a module") 

""" module.py - an example of Python module """

__counter2 = 0
def sum1(list):
    global __counter2
    __counter2 += 1
    sum = 0
    for e1 in list:
        sum += e1
    return sum

def prod1(list):
	global __counter2	
	__counter2 += 1
	prod = 1
	for el in list:
		prod *= el
	return prod

if __name__ == "__main__":
	print("I prefer to be a module, but I can do some tests for you")
	l = [i+1 for i in range(5)]
	print(suml(l) == 15)
	print(prodl(l) == 120)
