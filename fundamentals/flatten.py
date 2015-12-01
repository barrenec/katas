'''
In this Kata you will create a function that takes 
a list of lists as an input and returns a flat list.
'''

'''
test.assert_equals(flatten([[1,2],[3,4]]),[1,2,3,4])
test.assert_equals(flatten([[1],[2],[3],[4]]),[1,2,3,4])
'''


def flatten(l):
	flatt_list = []
	trick_string = str(l).translate(None, ''.join('[ ]'))

	for i in trick_string.split(","):
		flatt_list.append(int(i)) 
	return flatt_list	
	

	

print flatten([[1,[2,3,[44,77]]],[2],[3],[4]])