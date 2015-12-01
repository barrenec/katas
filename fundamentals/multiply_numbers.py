

'''
Given two strings representing positive integers, such as "12" and "35"
, return a string containing their product.

Disabled:
1. use of `eval`
2. use of ints
3. use of floats
4. use of unsigned longs
5. use of bitwise operators

Accepted:
strings
booleans
arrays
Inputs will never have leading zeros, and neither should your output. 
Your function, multiplyMyNumbers, should handle numbers 
with up to 5 characters, "13255" for example.


test.assert_equals(multiplyMyNumbers('1', '5'), '5')
test.assert_equals(multiplyMyNumbers('7', '2'), '14')
test.assert_equals(multiplyMyNumbers('11', '42'), '462')

'''
#	3*2 = 1+1+1+1+1+1


def multiplyMyNumbers(a, b):
	solution = []
	num_list = "01234567890123456789"

	reached_first = False
	reached_second = False

	for num in num_list:
		if num != a[0] and reached_first == False:
			solution.append("1")
		else:
			reached_first = True
			if num != a[1]:
				solution.append("1")
			else:
				reached_second = True	
				break		
					
				

	'''
	for char in b:
		for num in num_list:
			if char != num:
				for char2 in a:
					for num2 in num_list:
						if char2 != num2:
							solution.append("1")
						else: break
			else:break
	'''

	return str(len(solution))



print multiplyMyNumbers("91","4")
#print  dir([])





