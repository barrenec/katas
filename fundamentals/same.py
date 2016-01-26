'''
Given two arrays, the purpose of this Kata is to check if these two arrays are the same. 
"The same" in this Kata means the two arrays contains arrays of 2 numbers which are 
same and not necessarily sorted the same way. i.e. [[2,5], [3,6]] is same as [[5,2]
, [3,6]] or [[6,3], [5,2]] or [[6,3], [2,5]] etc

[[2,5], [3,6]] is NOT the same as [[2,3], [5,6]]
Two empty arrays [] are the same
[[2,5], [5,2]] is the same as [[2,5], [2,5]] but NOT the same as [[2,5]]
[[2,5], [3,5], [6,2]] is the same as [[2,6], [5,3], [2,5]] or [[3,5], [6,2], [5,2]], etc
An array can be empty or contain a minimun of one array of 2 integers and up to 100 array of 2 integers
Note:
1. [[]] is not applicable because if the array of array are to contain anything, there have to be two numbers.
2. 100 randomly generated tests that can contains either "same" or "not same" arrays.


Test.describe('Simple 2x2 arrays')
Test.it('same arrays')
Test.assert_equals(same([[2,5], [3,6]], [[5,2], [3,6]]), True, "Value not what is expected for [[2,5], [3,6]] and [[5,2], [3,6]]")
Test.assert_equals(same([[2,5], [3,6]], [[6,3], [5,2]]), True, "Value not what is expected for [[2,5], [3,6]] and [[6,3], [5,2]]")
Test.assert_equals(same([[2,5], [3,6]], [[6,3], [2,5]]), True, "Value not what is expected for [[2,5], [3,6]] and [[6,3], [2,5]]")

Test.describe('Simple 3x3 arrays')
Test.it('same arrays')
Test.assert_equals(same([[2,5], [3,5], [6,2]], [[2,6], [5,3], [2,5]]), True, "Value not what is expected for [[2,5], [3,5], [6,2]] and [[2,6], [5,3], [2,5]]")
Test.assert_equals(same([[2,5], [3,5], [6,2]], [[3,5], [6,2], [5,2]]), True, "Value not what is expected for [[2,5], [3,5], [6,2]] and [[3,5], [6,2], [5,2]]")

Test.describe('Empty arrays')
Test.it('same arrays')
Test.assert_equals(same([], []), True, "Value not what is expected for [] and []")

Test.describe('Unequal arrays')
Test.it('not same arrays')
Test.assert_equals(same([[2,3], [3,4]], [[4,3], [2, 4]]), False, "Value not what is expected for [[2,3], [3,4]] and [[4,3], [2, 4]]")
Test.assert_equals(same([[2,3], [3,2]], [[2,3]]), False, 
	"Value not what is expected for [[2,3], [3,2]] and [[2,3]]")


'''

import numpy as np 

def same(arr_a, arr_b):
	compare = lambda x, y: str(x) == str(y)
	return  compare(sorted(list(np.array(arr_a).flatten())), sorted(list(np.array(arr_b).flatten())))

print same([[2,6], [3,4]], [[4,3], [2, 4]])











