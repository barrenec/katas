'''
Make a function that will return a greeting statement that uses input: 
Your program should return, "Hello, (name) how are you doing today?" 
(Make sure you type the exact thing I wrote or the program may not execute properly)
'''

'''
Test.assert_equals(greet('Ryan'), "Hello, Ryan how are you doing today?")
'''

def greet(name):
    return "Hello, {0} how are you doing today?".format(name)



print greet('Ryan')
print greet('Lolo')