'''
In your class, you have started lessons about geometric progression. 
Since you are also a programmer, you have decided to write a function 
that will print first 'n' elements of the sequence with the given constant 
'r' and first element 'a'. Result should be separated by comma and space

Example:

geometric_sequence_elements(2, 3, 5) == '2, 6, 18, 54, 162'

More info: https://en.wikipedia.org/wiki/Geometric_progression

test.assert_equals(geometric_sequence_elements(2, 3, 5), '2, 6, 18, 54, 162')
test.assert_equals(geometric_sequence_elements(2, 2, 10), '2, 4, 8, 16, 32, 64, 128, 256, 512, 1024')
test.assert_equals(geometric_sequence_elements(1, -2, 10), '1, -2, 4, -8, 16, -32, 64, -128, 256, -512')

'''

def geometric_sequence_elements(a, r, n):

	result = str(a)

	for i in range(1, n):
			a = a*r	
			result += ', '+ str(a)	
	return result 
	

print 	geometric_sequence_elements(2, 3, 5)		


