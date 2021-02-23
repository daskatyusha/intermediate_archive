### Built-in Data Types
"""
Variables can store data of different types, and different types
can do different things. 
"""
print("TEXT TYPES")
print("hello world", type('hello world'))
print("NUMERIC TYPES")
print(3, type(3))
print(3.0, type(3.0))
print(2+3j, type(2+3j))
print("Also see some real and imag parts of complex types:")
print("Real of 2+3j is:", ((2+3j).real))
print("Imag of 2+3j is:", ((2+3j).imag))
print("As you can see here built-in functions can be written like this")
print("SQUENCE TYPES")
print([1,2,3], type([1,2,3]))
print((1,2,3), type((1,2,3)))
print(range(6), type(range(6)))
print("MAPPING TYPE")
print({'name':'John', 'age':42}, type({'name':'John', 'age':42}))
print("SET TYPES")
print({'apple', 'banana', 'cherry'}, type({'apple', 'banana', 'cherry'}))
print(frozenset({"apple", "banana", "cherry"}), type(frozenset({"apple", "banana", "cherry"})))
print('BOOLEAN TYPE')
print(True, False, type(True))
print('BINARY TYPES')
print(b"Hello", type(b"Hello"))
print(bytearray(5), type(bytearray(5)))
print(memoryview(bytes(5)), type(memoryview(bytes(5))))

