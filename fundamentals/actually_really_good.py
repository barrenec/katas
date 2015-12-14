'''
http://xkcd.com/1609/

Task:

Given an array containing a list of good foods, return a string containing 
the assertion that any two of the individually good foods are really good when combined.

eg: "You know what's actually really good? Pancakes and relish."

Examples:

Good_foods = ["Ice cream", "Ham", "Relish", "Pancakes", "Ketchup"
, "Cheese", "Eggs", "Cupcakes", "Sour cream", "Hot chocolate", "Avocado", "Skittles"]

actually_really_good( Good_foods ) #  "You know what's actually really good? Pancakes and relish."
actually_really_good( ['Peanut butter'] ) #  "You know what's actually really good? Peanut butter and more peanut butter."
actually_really_good( [] ) #  "You know what's actually really good? Nothing!"
Notes:

There are many different valid combinations of 2 foods it doesn't matter which one you choose.
But there should be 2 different foods listed unless there was only one food given in the input array.
Capitalization should be correct, the first given food should be capitalized, but the second should not.
The input array should not be modified by the method.
'''

import random

def actually_really_good(foods):

	result_string = "Nothing!"
	base_string = "You know what's actually really good? {0}"
	list_len = len(foods)
	food1 = food2 = ""

	capitalize_word = lambda word: word[0:1].upper()+word[1:]
	
	if list_len == 1:
		food1 = food2 = foods[0].lower() 
		result_string = capitalize_word(food1) + ' and more ' + food2 + '.' 
	elif list_len > 1:
		while food1 == food2:
			random_food = lambda foods: foods[random.randrange(0,list_len)].lower().lstrip()
			food1 = random_food(foods)
			food2 = random_food(foods)
		result_string = capitalize_word(food1) + ' and ' + food2 + '.'

   	return base_string.format(result_string)

Good_foods = ["Ice cream", "Ham", "Relish", "Pancakes", "Ketchup"
, "Cheese", "Eggs", "Cupcakes", "Sour cream", "Hot chocolate", "Avocado", "Skittles"]
print actually_really_good(Good_foods)
print actually_really_good(['fish Fingers','cUstard', 'sENAPE'])




