'''
Calculate the sum of all the arguments passed to a function.

Note: If any of the arguments is not a finite number the 
function should return false/False instead of the sum of the arguments.

For example:

sum(1,2,3,4)         should return 10
sum(1, "two", 3)     should return false
sum(1, 2, [3], NaN)  should return false


Test.assert_equals(sum_all(6,2,3), 11)
Test.assert_equals(sum_all(756,2,1,10), 769)
Test.assert_equals(sum_all(76856,-32,1981,1076), 79881)
Test.assert_equals(sum_all(1,-32,"codewars",1076), False)
Test.assert_equals(sum_all(7,-3452,1981,1076), -388)

'''

def sum_all(*args):
	try : return sum(args)
	except : return False 	
	
print sum_all('a',2,3,4)	
print sum_all(7,-3452,1981,1076)