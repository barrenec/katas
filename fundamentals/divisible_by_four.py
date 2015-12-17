'''
Create a function that returns True if a given number is divisible by 4
, otherwise it should return False.
Test.assert_equals(divisible_by_four(9), False)
Test.assert_equals(divisible_by_four(8), True)
'''



divisible_by_four = lambda n:  n % 4 == 0 


print divisible_by_four(9)
print divisible_by_four(8)



