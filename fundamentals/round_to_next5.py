'''
Given an integer as input, can you round it to the next 5?

Examples:

input:    output:
0    ->   0
2    ->   5
3    ->   5
12   ->   15
21   ->   25
30   ->   30
etc.
Input may be any positive or negative integer (including 0).

You can assume that all inputs are valid integers.
'''

def round_to_next5(n):

	while n % 5 !=0:
		n +=1	
	return n	

print round_to_next5(0)
print round_to_next5(2)
print round_to_next5(3)
print round_to_next5(12)
print round_to_next5(30)    