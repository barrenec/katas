'''

Create a function which checks a number for three different properties.

is the number prime?
is the number even?
is the number a multiple of 10?
Each should return either true or false, which should be given as an array. Remark: The Haskell variant uses data Property.

Examples

number_property(7)  # ==> [true,  false, false] 
number_property(10) # ==> [false, true,  true]

The number will always be an integer, either positive or negative. Note that negative numbers cannot be primes, but they can be multiples of 10:

number_property(-7)  # ==> [false, false, false] 
number_property(-10) # ==> [false, true,  true]


Test.assert_equals(number_property(-10),[False,True,True])
Test.assert_equals(number_property(2),[True,True,False])
Test.assert_equals(number_property(120),[False,True,True])
Test.assert_equals(number_property(125),[False,False,False])

'''

def number_property(n):
	is_prime = True
	is_even = False
	is_multiple_of_ten = False

	if n > 1:
		for i in range(2,n):
			if n % i == 0:
				is_prime = False 
				break
	else:
		is_prime = False 			
	

	if n % 2 == 0:
		is_even = True

	if n % 10 == 0:
		is_multiple_of_ten = True 			


	return [is_prime, is_even, is_multiple_of_ten]


print number_property(2)









