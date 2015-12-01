'''
For this problem you must create a program that says who ate the last cookie. 
If the input is a string then "Zach" ate the cookie. If the input is a 
float or an int then "Monica" ate the cookie. If the input is anything 
else "the dog" ate the cookie. The way to return the statement is: 
"Who ate the last cookie? It was (name)!"

Ex: Input = "It was Monica" --> 
Output = "Who ate the last cookie? It was Zach! (The reason you return Zach is because the input is a string)

Note: Make sure you return the correct message with correct spaces and punctuation.
'''

'''
Test.assert_equals(cookie("Ryan"), "Who ate the last cookie? It was Zach!")
Test.assert_equals(cookie(2.3), "Who ate the last cookie? It was Monica!")
Test.assert_equals(cookie(26), "Who ate the last cookie? It was Monica!")
Test.assert_equals(cookie(True), "Who ate the last cookie? It was the dog!")
'''


def cookie(x):
	string = "Who ate the last cookie? It was /marker/!" 
	if not str(x).isalpha():
		return string.replace("/marker/", "Monica")
	elif type(x) == bool:
		return string.replace("/marker/", "the dog")
	return 	string.replace("/marker/", "Zach")
	


print cookie("Ryan")
print cookie(2)
print cookie(1.4)
print cookie("True")
