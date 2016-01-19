


'''
Implement String#ipv4_address?, which should return true if given object 
is an IPv4 address - four numbers (0-255) separated by dots.

It should only accept addresses in canonical 
representation, so no leading 0s, spaces etc.
'''

import re 


def ipv4_address(address):
	if '\n' in address: return False 
	ipv4_address = re.compile('^(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$')
	return ipv4_address.match(address)!= None 


print ipv4_address("127.0.0.1\n")

