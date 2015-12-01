
'''
Make a function that returns the value multiplied 
by 50 and increased by 6. If the value entered 
is a string it should return "Error".
'''

'''
Test.assert_equals(problem("hello"), "Error")
Test.assert_equals(problem(1), 56)
'''


def problem(a):
	return (a*50)+6 if type(a) != str else "Error"


print problem(2.0)
print problem("hello")