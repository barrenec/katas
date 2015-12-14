'''
Write a program to find count of the most frequent item of an array.

Assume that input is array of integers.

Ex.:
input array: [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]
ouptut: 5
Most frequent number in example array is -1. It occures 5 times in input array.

Test.describe("most_frequent_item_count")

Test.it("works for some examples")
Test.assert_equals(most_frequent_item_count([3, -1, -1]), 2, "didn't work for [3, -1, -1]")
Test.assert_equals(most_frequent_item_count([3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]), 5
, "didn't work for [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]")
Test.assert_equals(most_frequent_item_count([]), 0, "didn't work for []")
Test.assert_equals(most_frequent_item_count([9]), 1, "didn't work for [9]")

'''

def most_frequent_item_count(collection):

	count = 0
	for item in list(set(collection)):
		new_count = len([i for i,x in enumerate(collection) if x == item])
		count = new_count if new_count > count else count 
	return count	



print most_frequent_item_count([3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3])







