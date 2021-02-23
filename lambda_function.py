### Python Lambda
"""
A lambda funciton is a small anonymous function
A lambda function can take any number of arguments,
but can only have one expression.

Syntax: 
	lambda arguments : expression 
"""

#add 10 to argument a, and return the result
x = lambda a : a+10
print(x(5))

x = lambda a,b:a*b
print(x(5,6))

x = lambda a,b,c : a+b+c
print(x(5,6,2))


### Why Use Lambda Funcitons?
"""
The power of lambda is better shown when you use them 
as an anonymous function inside another function.

Say you have a function definition that takes one argument, 
and that argument will be multiplied with an unknown number
"""

def a_function(n):
	return lambda a:a*n

doubler_function = a_function(2)
tripler_function = a_function(3)
#etc...
print(doubler_function(23))
print(tripler_function(23))


### Stackoverflow part
"""
filter is used for testing a function with these set you know
"""
# like			with this function		test these
mult3 = filter(lambda x:x%3 == 0, [1,2,3,4,5,6,7,8,9])
print([i for i in mult3])


#?
print(lambda a, b: '{}, {}'.format(a, b), [1, 2, 3, 4, 5, 6, 7, 8, 9])


print(sorted([1, 2, 3, 4, 5, 6, 7, 8, 9], key=lambda x: abs(5-x)))


# you can think lambda like def that has some parameters 
# and does some stuff
full_name = lambda first, last: f'Full name: {first.title()} {last.title()}'
print(full_name("Mike", "Buttowsky"))

"""
Several examples in this tutorial use this format to highlight 
the anonymous aspect of a lambda function and avoid focusing on 
lambda in Python as a shorter way of defining a function.

Python does not encourage using immediately invoked lambda 
expressions. It simply results from a lambda expression being 
callable, unlike the body of a normal function.

Lambda functions are frequently used with higher-order functions, 
which take one or more functions as arguments or return one or 
more functions.

A lambda function can be a higher-order function by taking a 
function (normal or lambda) as an argument like in the following 
contrived example:
"""

#*
high_ord_func = lambda x, func: x + func(x)
print(high_ord_func(2, lambda x:x*x))

"""
DIFFERENCE BETWEEN DEF AND LAMBDA:
The bytecode interpreted by Python is the same for both functions. 
But you may notice that the naming is different: the function name 
is add for a function defined with def, whereas the Python lambda 
function is seen as lambda.
output of lambda function: <function <lambda> at 0x7f30c6ce9ae0>
output of regular function: <function add at 0x7f30c6ce9f28>
"""
print(
	(lambda x:
		(x%2 and 'odd' or 'even'))(3))


### Arguments in Lambda
"""
Like a normal function object defined with def, 
Python lambda expressions support all the different ways 
of passing arguments. This includes:
	Positional arguments
	Named arguments (sometimes called keyword arguments)
	Variable list of arguments (often referred to as varargs)
	Variable list of keyword arguments
	Keyword-only arguments
"""

print((lambda x, y, z: x + y + z)(1, 2, 3))
print((lambda x, y, z=3: x + y + z)(1, 2))
print((lambda x, y, z=3: x + y + z)(1, y=2))
print((lambda *args: sum(args))(1,2,3))
print((lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3))
print((lambda x, *, y=0, z=0: x + y + z)(1, y=2, z=3))


### Classic Funcitonal Construct
"""
Lambda functions are regularly used with the built-in 
functions map() and filter(), as well as 
functools.reduce(), exposed in the module functools. 
The following three examples are respective 
illustrations of using those functions with lambda 
expressions as companions
"""
print(map(lambda x:x.upper(), ['cat','dog','cow']))
print(list(map(lambda x:x.upper(), ['cat','dog','cow'])))
#check 
print(list(filter(lambda x: 'o' in x, ['cat','dog','cow'])))
from functools import reduce
print(reduce(lambda acc, x: f'{acc} | {x}', ['cat', 'dog', 'cow']))


### Key Functions
"""
ey functions in Python are higher-order functions that 
take a parameter key as a named argument. key receives 
a function that can be a lambda. This function directly 
influences the algorithm driven by the key function itself.
"""

ids = ['id1', 'id2', 'id30', 'id3', 'id22', 'id100']
print(sorted(ids))	#Lexicographic sort
sorted_ids = sorted(ids, key=lambda x:int(x[2:]))
print(sorted_ids)	#Integer sort