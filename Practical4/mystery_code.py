# What does this piece of code do?
# Answer: get the number of iterations needed to get the same number on two 6-sided dices

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

progress=0						# Initialize progress		
while progress>=0:				# Start a loop
	progress+=1					# Increase progress by 1
	first_n = randint(1,6)		# Draw a random number between 1 and 6
	second_n = randint(1,6)		# Draw a random number between 1 and 6
	if first_n == second_n:		# If the two numbers are the same
		print(progress)			# Print the number of iterations
		break					# Exit the loop

