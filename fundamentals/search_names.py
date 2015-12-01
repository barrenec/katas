'''
While developing a website, you detect that some of the members 
have troubles logging in. Searching through the code you find that 
all logins ending with a "_" make problems. So you want to write a 
function that takes an array of pairs of login-names and e-mails
, and outputs an array of all login-name, e-mails-pairs from the login-names that end with "_".


If you have the input-array:

[ [ "foo", "foo@foo.com" ], [ "bar_", "bar@bar.com" ] ]

it should output
[ [ "bar_", "bar@bar.com" ] ]


You have to use the filter-method of Python
, which returns each element of the array for which the filter-method returns true.

https://docs.python.org/3/library/functions.html#filter


a = [[ "foo", "foo@foo.com" ], [ "bar_", "bar@bar.com" ] ]
b = [ [ "bar_", "bar@bar.com" ] ]
test.assert_equals(search_names(a), b)
test.assert_equals(filter_used, True, 'Use filter function' )

a = [[ "foobar_", "foo@foo.com" ], [ "bar_", "bar@bar.com" ] ]
b = [[ "foobar_", "foo@foo.com" ], [ "bar_", "bar@bar.com" ] ]
test.assert_equals(search_names(a), b)
test.assert_equals(filter_used, True, 'Use filter function' )

a = [[ "foo", "foo@foo.com" ], [ "bar", "bar@bar.com" ] ]
b = []
test.assert_equals(search_names(a), b)
test.assert_equals(filter_used, True, 'Use filter function' )

'''


def find_wrong_logins(element):
	for i in element:
		if i.find('_') > 0:
			return element  
	return None 

def search_names(logins):	
	return  filter(find_wrong_logins, logins)


print search_names([["foo", "foo@foo.com"], ["bar_", "bar@bar.com"]])    











