def capitals_first(string):
	lower_words = upper_words = ""
	for word in string.split():
		first_char = word[0]
		if first_char.isalpha(): 
			if first_char.isupper():
				upper_words = upper_words + word + ' ' 
			else:
				lower_words = lower_words + word + ' '	

	return (upper_words  + lower_words).strip()


def capitals_first_best(string):
	lower_words = ' '.join([word for word in string.split() if word[0].islower()])
	upper_words = ' '.join([word for word in string.split() if word[0].isupper()])
	
	return upper_words + ' ' + lower_words


# Test.assert_equals(capitals_first("sense Does to That Make you?")
#, "Does That Make sense to you?")

a = "sense Does to That Make you?"
print capitals_first_best(a)
#print dir(a)