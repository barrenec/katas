'''

http://www.codewars.com/kata/5202ef17a402dd033c000009/train/python

A string is considered to be in title case if each word in the string is either
(a) capitalised (that is, only the first letter of the word is in upper case) or
(b) considered to be an exception and put entirely into lower case unless it
is the first word, which is always capitalised.

Write a function that will convert a string into title case,
 given an optional list of exceptions (minor words). The list of minor
 words will be given as a string with each word separated by a space.
 Your function should ignore the case of the minor words string -- it should
 behave in the same way even if the case of the minor word string is changed.


Arguments (Other languages)

First argument (required): the original string to be converted.
Second argument (optional): space-delimited list of minor words that must always be
lowercase except for the first word in the string.

Test.assert_equals(title_case(''), '')
Test.assert_equals(title_case('a clash of KINGS',
                   'a an the of'), 'A Clash of Kings')
Test.assert_equals(title_case('THE WIND IN THE WILLOWS',
                   'The In'), 'The Wind in the Willows')
Test.assert_equals(title_case('the quick brown fox'), 'The Quick Brown Fox')


Gave title='First a of in', minor_words='an often into'. Expected 'First A Of In' but got 'First a of in'.


'''
import re


def title_case(title, minor_words=""):

    if len(title) == 0:
        return title

    new_title = ""

    for count, word in enumerate(title.split()):
        if len(re.findall('\\b' + word + '\\b', minor_words, flags=re.IGNORECASE)) == 0 or count == 0:
            new_title += word.capitalize() + " "
        else:
            new_title += word.lower() + " "

    return new_title.rstrip()

print title_case(title='First a of in', minor_words='an often into')
