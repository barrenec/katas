'''

http://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python


Your task is to sort a given string. Each word in the String will contain a single number. 
This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input String is empty, return an empty String. The words in the input 
String will only contain valid consecutive numbers.

For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"

Test.assert_equals(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")

'''

def order(s):
	new_string = ""
	for i in range(1,10):
		for word in s.split(' '):
			if len(filter(str.isdigit, word)) and i == int(filter(str.isdigit, word)):  
				new_string += word + " " 
	return new_string.rstrip()	


print order("is2 Thi1s T4est 3a")