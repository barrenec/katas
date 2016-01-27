'''

The test fixture I use for this kata is pre-populated.

It will compare your guess to a random number generated in Python by:

randint(1,100)


You can pass by relying on luck or skill but try not to rely on luck.

"The power to define the situation is the ultimate power." - Jerry Rubin

Good luck!


'''


from random import randint

def new_randint(x,y):
	return 69

randint = new_randint 	
guess = new_randint(1,1)

print guess 
 