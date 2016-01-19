
'''

http://www.codewars.com/kata/55eeddff3f64c954c2000059/train/python


You are given a list/array which contains only integers (positive and negative). 
Your job is to sum only the numbers that are the same and consecutive. The result should be one list.

Extra credit if you solve it in one line. You can asume there is never an empty 
list/array and there will always be an integer.

Same meaning: 1 == 1

1 != -1

Examples:

[1,4,4,4,0,4,3,3,1] # should return [1,12,0,4,6,1]

"""So as you can see sum of consecutives 1 is 1 
sum of 3 consecutives 4 is 12 
sum of 0... and sum of 2 
consecutives 3 is 6 ..."""

[1,1,7,7,3] # should return [2,14,3]
[-5,-5,7,7,12,0] # should return [-10,14,12,0]

Test.describe("Basic tests")
Test.assert_equals(sum_consecutives([1,4,4,4,0,4,3,3,1]),[1,12,0,4,6,1], "on list [1,4,4,0,4,3,3,1] you get ")
Test.assert_equals(sum_consecutives([1,1,7,7,3]),[2,14,3], "on list [1,1,7,7,3] you get ")
Test.assert_equals(sum_consecutives([-5,-5,7,7,12,0]),[-10,14,12,0], "on list [-5,-5,7,7,12,0] you get ")
Test.assert_equals(sum_consecutives([3,3,3,3,1]),[12, 1], "on list [3,3,3,3,1] you get " )

'''


def sum_consecutives(s):
	new_list = []
	sum_number = 0 
	for index, number in enumerate(s):
		if index != 0:
			try:
				if s[index] == s[index+1] or s[index] == s[index-1]:
					sum_number += number 

					if s[index] != s[index+1]:
						new_list.append(sum_number)
						sum_number = 0
				else:
					new_list.append(number) 
			except:
				new_list.append(number) 

	
	if s[-2] == s[-1]:
		new_list[-1] =  s[-2] + s[-1]

	if s[0] == s[1]:
		new_list[0] +=  s[0]
	else:	
		new_list = [s[0]] + new_list			

	return new_list 


# on list [0, 1, 1, 2, 2] you get : [0, 2, 2] should equal [0, 2, 4]

print sum_consecutives([0, 1, 1, 2, 2])


'''
#Nice one 

from itertools import groupby

def sum_consecutives(s):
    return [sum(group) for c, group in groupby(s)]
'''



