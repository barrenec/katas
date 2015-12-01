'''
Invalid Input - Error Handling #1

Error Handling is very important in coding. Most error handling seems 
to be overlooked or not implemented properly.

Task

Your task is to implement a function which is expected to take a string 
and return an object containing the properties vowels and consonants 
The vowels property must contain the total count of vowels ('y' in this case is not a vowel)
, and consonants are any other letters, you must also trim any spaces. Don't forget 
to handle invalid input, though you must always return valid output.

Input

The input you are expecting is any random string you must then discern what are vowels and 
what are consonants and sum their total occurances in an object. However you may also 
receieve inputs that are not strings. If this happens, then you must return an object 
with the vowel and consonant total of 0 because the input was NOT a string. 
Refer to the Example section for a more visual representation of what inputs 
you may receive and the outputs expected. :)

Input: get_count('test')
Output: {vowels:1,consonants:3}

Input: get_count('tEst')
Output: {vowels:1,consonants:3}

Input get_count('    ')
Output: {vowels:0,consonants:0}

Input get_count()
Output: {vowels:0,consonants:0}

Test.assert_equals(get_count('Test'),{"vowels":1,"consonants":3},'Should return 1 vowel and 3 consonants')
Test.assert_equals(get_count('Here is some text'),{"vowels":6,"consonants":8},'Should return 6 vowel and 8 consonants')
Test.assert_equals(get_count('To be a Codewarrior or not to be'),{"vowels":12,"consonants":13},'Should return 12 vowel and 13 consonants')
Test.assert_equals(get_count('To Kata or not to Kata'),{"vowels":8,"consonants":9},'Should return 8 vowel and 9 consonants')
Test.assert_equals(get_count('aeiou'),{"vowels":5,"consonants":0},'Should return 5 vowel and 0 consonants')

Test.assert_equals(get_count('TEst'),{"vowels":1,"consonants":3},'Should return 1 vowel and 3 consonants')
Test.assert_equals(get_count('HEre Is sOme text'),{"vowels":6,"consonants":8},'Should return 6 vowel and 8 consonants')
Test.assert_equals(get_count(),{"vowels":0,"consonants":0},'Should return 0 vowel and 0 consonants')
Test.assert_equals(get_count(['To Kata or not to Kata']),{"vowels":0,"consonants":0},'Should return 0 vowel and 0 consonants')
Test.assert_equals(get_count(None),{"vowels":0,"consonants":0},'Should return 5 vowel and 0 consonants')

'''



def get_count(words=None):
	
	vowels_count = 0
	consonants_count = 0

	try:

		for char in words:
			if not char.isalpha():
				continue 

			if char.lower() in 'a,e,i,o,u':
				vowels_count += 1
			# one of the tests no eating me using isalpha maybe some local iussue	
			elif char.lower() in ('b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z'):
				consonants_count += 1
	except:
		pass 				

  	return {'vowels':vowels_count, 'consonants':consonants_count}

print get_count('eget cursus sit facilisis, neque, dapibus Morbi posuere ornare')

















