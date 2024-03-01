# importing re module for creating
# regex expression
import re

# reading line by line
with open('data.txt', 'r') as f:

	# looping the para and iterating 
	# each line
	text = f.read() 
	
	# getting the pattern for [],(),{} 
	# brackets and replace them to empty 
	# string
	# creating the regex pattern & use re.sub()
	patn = re.sub(r"[\([{})\]]", "", text) 

print(patn)
