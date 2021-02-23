### The __init__ Function

"""
The examples above are classes and objects in 
their simplest form, and are not really useful in 
real life applications.

To understand the meaning of classes
we have to understand the built-in __init__() function.

All classes have a function called __init__(), 
which is always executed when the class is being initiated.

Use the __init__() function to assign values 
to object properties, or other operations 
that are necessary to do when the object is being created

NOTE: The __init__() function is called automatically 
every time the class is being used to 
create a new object.
"""

class Person:
	def __init__(self, name, age):
		self.person_name = name
		self.person_age = age
	def say_my_name(self):
		print(self.person_name + " said: " + "Hello my name is " + self.person_name)

person = Person("Harmonica", 42)
#	print(person.name) this will cause error
print(person.person_name)
print(person.person_age)
person.say_my_name()


print("\n###############################################\n")
### The self Parameter
"""
The self parameter is a reference to the current 
instance of the class, and is used to access variables 
that belongs to the class.

It does not have to be named self , you can call it 
whatever you like, but it has to be the first parameter 
of any function in the class

But it is not orange :(
"""

class Person:
	def __init__(first_parameter, name, age):
		first_parameter.name = name
		first_parameter.age = age
	def say_my_name(not_even_first_parameter):
		print(not_even_first_parameter.name + " said: " + "Hello my name is " + not_even_first_parameter.name)

person = Person("Katyusha", 36)
person.say_my_name()

print("\n###############################################\n")
### Modify Object Properties


person.age = 24
print(person.age)


del person.age
try:
	print(person.age)
except:
	print("ERROR")


print("\n###############################################\n")
#### Python Inheritance
"""
Inheritance allows us to define a class that inherits 
all the methods and properties from another class.

Parent class is the class being inherited from, 
also called base class.

Child class is the class that inherits from another class, 
also called derived class.
"""
print("\n###############################################\n")

### Create a Parent Class
"""
Any class can be a parent class, so the syntax is the 
same as creating any other class
"""

class Person:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname

	def print_name(self):
		print(self.firstname, self.lastname)

person = Person("Gul", "Dan")
person.print_name()


print("\n###############################################\n")
### Create a Child Class
"""
To create a class that inherits the functionality 
from another class, send the parent class as a parameter 
when creating the child class
"""

class Student(Person):
	pass

student = Student("Mike","Buttowsky")
student.print_name()


print("\n###############################################\n")
### __init__() in Child Classes
"""
When you add the __init__() function, 
the child class will no longer inherit 
the parent's __init__() function.

The child's __init__() function "overrides" the inheritance 
of the parent's __init__() function.

"""

#???
class Student(Person):
	def __init__(self, fname, lname):
		Person.__init__(self,fname,lname)
		


print("\n###############################################\n")
### The super() Function
"""
will make the child class inherit all the methods
and properties from its parent.

By using the super() function, you do not have to use the name of
the parent element, it will automatically inherit the methods 
and properties from its parent.
"""

class Student(Person):
	def __init__(self, fname, lname, year):
		super().__init__(fname, lname)
		"""
		gets init of parent like 
		self.firstname = fname
		...
		"""
		self.graduationyear = year

	def welcome(self):
		print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

"""
In the example below, the year year should be a variable, 
and passed into the Student class when creating student objects. 
To do so, add another parameter in the __init__() function.
"""

student = Student("Karl", "Marx", 2019)
student.welcome()

