
'''
Longest Palindrome
Find the length of the longest substring in the given string s that is the same in reverse.
As an example, if the input was 'I like racecar that go fast', the substring length would be 7.
If the length of the input string is 0, return value must be 0.

Example:

"a" -> 1 
"aab" -> 2  
"abcde" -> 1
"zzbaabcd" -> 4
"" -> 0

test.assert_equals(longest_palindrome("a"), 1)
test.assert_equals(longest_palindrome("aa"), 2)
test.assert_equals(longest_palindrome("baa"), 2)
test.assert_equals(longest_palindrome("aab"), 2)
test.assert_equals(longest_palindrome("abcdefghba"), 1)
test.assert_equals(longest_palindrome("baablkj12345432133d"), 9)
'''



def longest_palindrome (s):
	temp_string = ""
	max_len = 0
	s_len = len(s)
	count = 0
	while count  < s_len:
		print s[count::]
		count = count +1

	while count  < len(s):
		s = s[count::]
		count = count +1
		for char in s:
			if char.isalnum():
				temp_string = temp_string + char
				#print temp_string + ' ' + temp_string[::-1]
				if temp_string == temp_string[::-1] and len(temp_string) > max_len:
					max_len = len(temp_string)	 	
				s = s[count::]
	return max_len 


print longest_palindrome("zzbaabcd")	
print longest_palindrome("dcbaabzz")	

print longest_palindrome("aab")	
print longest_palindrome("baa")



