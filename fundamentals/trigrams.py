'''
Trigrams are a special case of the n-gram, where n is 3. One trigram is a continious sequence of 3 chars in phrase. 
Wikipedia

You have to return all trigrams for the given phrase. Return an empty string for phrases shorter than 3.

Example:

trigrams('the quick red') == 'the he_ e_q qu qui uic ick ck k_r _re red'
'''


'''
test.assert_equals(trigrams("the quick red"), "the he_ e_q _qu qui uic ick ck_ k_r _re red")
test.assert_equals(trigrams('Hi'),'')
'''

def trigrams(phrase):
    if len(phrase) < 3: return ''

    solution = ''

    count = 0
    for char in phrase:
    	if count+3 <= len(phrase):
    		solution = solution + ' ' + phrase[count:count+3].replace(' ', '_') 
    	count+=1

    return solution.lstrip()	

print trigrams('the quick red')
