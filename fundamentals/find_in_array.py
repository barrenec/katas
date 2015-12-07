'''
Create a find function that takes a string and an array. If the string is in the array, return true.

For example:

find("hello", ["bye bye","hello"]) # return true
find("anything", ["bye bye","hello"]) # return false
Note: Hello != hello, case-sensitive.


Test.assert_equals(find("hello", ["bye bye","hello"]), True)
Test.assert_equals(find("anything", ["bye bye","hello"]), False)

'''


def find(string_, list_):
	return string_ in list_


print find("hello", ["hello,bye bye","hello"])
print find("anything", ["bye bye","hello"])	   
