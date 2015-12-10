'''
Create a function isDivisible(n,x,y) 
that checks if a number n is divisible by two numbers x AND y

Example:
is_divisible(3,1,3)--> true because 3 is divisible by 1 and 3
is_divisible(12,2,6)--> true because 12 is divisible by 2 and 6
is_divisible(100,5,3)--> false because 100 is not divisible by 3
is_divisible(12,7,5)--> false because 12 is neither divisible by 7 nor 5

Test.assert_equals(is_divisible(3,3,4),False)
Test.assert_equals(is_divisible(12,3,4),True)
Test.assert_equals(is_divisible(8,3,4),False)
Test.assert_equals(is_divisible(48,3,4),True)
'''


is_divisible = lambda n,x,y: (n % x) + (n % y) == 0

print is_divisible(3,3,4)
print is_divisible(12,3,4)
print is_divisible(8,3,4)
print is_divisible(48,3,4)