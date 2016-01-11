'''
Write a function that removes each 9 that it is in between 7s.

seven_ate9('79712312') => '7712312'
seven_ate9('79797') => '777'

'''

def seven_ate9(str_):
	new_string = ""

	for index in range(0,len(str_)):
		try:
			if index != len(str_) and str_[index] == "9" and str_[index-1] == "7" and str_[index+1] == "7":
				pass
			else:
				new_string +=  str_[index]	
  		except:
  			new_string +=  str_[index] 
  			
  	return new_string


print seven_ate9('1779')