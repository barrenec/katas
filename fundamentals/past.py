
'''
Clock shows 'h' hours, 'm' minutes and 's' seconds after midnight.

Your task is to make 'Past' function which returns time converted to miliseconds.

Example:

past(0, 1, 1) == 61000

test.assert_equals(past(0,1,1),61000)
test.assert_equals(past(1,1,1),3661000)
test.assert_equals(past(0,0,0),0)
test.assert_equals(past(1,0,1),3601000)
test.assert_equals(past(1,0,0),3600000)
'''


def past(h=0, m=0, s=0):
	return ((h*60*60) + (m*60) + s) * 1000 