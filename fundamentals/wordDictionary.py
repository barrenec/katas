
'''
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)

search(word) can search a literal word or a regular expression string 
containing only letters a-z or .. A . means it can represent any one letter.

For example:

add_word("bad")
add_word("dad")
add_word("mad")
search("pad") == False
search("bad") == True
search(".ad") == True
search("b..") == True
'''

import fnmatch

class WordDictionary:
  	
	words = []

	def add_word(self, word):
		self.words.append(word)		    
  

	def search(self, word):
		for original_word in self.words:
			if fnmatch.fnmatch(original_word, word.replace('.', '?')):
				return True

		return False 
					
        
wd = WordDictionary()
wd.add_word('gqg')
wd.add_word('in')
wd.add_word('lhow')
wd.add_word('dh')
wd.add_word('a')



print wd.search('b')








