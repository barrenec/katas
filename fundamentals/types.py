'''
Create a program that will return whether an intered value is a str, int, float
, or bool. Return the name of the value.

Ex: Input = 23 --> Output = int 
Ex: Input = 2.3 --> Output = float 
Ex: Input = "Hello" --> Output = str 
Ex: Input = True --> Output = bool


Test.assert_equals(types(10), "int")
Test.assert_equals(types(9.7), "float")
Test.assert_equals("&*("),"str")
Test.assert_equals(types(True), "bool")

'''

types = lambda x: type(x).__name__



print types(10)
print types(9.7)
print types(True)

