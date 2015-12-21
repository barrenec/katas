'''
DESCRIPTION

Beginning Spanish classes always require students to practice 
matching Spanish articles with Spanish nouns based on the noun's gender.

In a very general sense, if a noun ends in an "-a" or "-as"
, it is feminine and is preceded by either "la" or "las", respectively.

Masculine nouns tend to end in all other letters. If it does not end in 
an "-s", it is probably singular and should be preceded by the article "el". 
Plural nouns that are masculine and end in "-s" are preceded by "los".

por ejemplo

el ordenador, el chico, el parque la comida, la cocina, la gamba los hombros, 
los bailadores, los pies las chicas, las botellas, las marcas

TASK

Create a function that can take an infinite number 
of arguments and return them in an array with their likely article in front.

For example, gender("cerveza") should return ["la cerveza"]
, and gender("botellones", "vaca") should return ["los botellones","la vaca"].

MORE DETAILS

If a non-string value is passed to the function, it should return that value unchanged.
All strings will be lower

Test.describe("gender")

Test.it("works for some examples")
Test.assert_equals(gender('genio'),['el genio'])
Test.assert_equals(gender('chico', 'esquinas'),['el chico','las esquinas'])
Test.assert_equals(gender("parques"), ['los parques'])
Test.assert_equals(gender("vino", 5, None), ['el vino',5,None])
Test.assert_equals(gender('lampas'),["las lampas"])
'''


def gender(*nouns):
	words = []
	for word in nouns:

		if type(word) != str:
			words.append(word)
			continue	

		article = "el"

		if word[-2:] == "as":
			article = "las"  				
		elif word[-1:] == "a":
			article = "la"	
		elif word[-1:] == "s":
			article = "los"	
		
		words.append(article + ' ' + word.lower())			

	return words 
	

print gender("pajas", "piojos", "puta", "coche", "tetas", 6.4)		














