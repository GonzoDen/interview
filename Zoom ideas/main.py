import random

f = open("students_list.txt", "a")

def action_list(filename):
	f = open("students_list.txt", "r")

	chosen_one
	inds = 0

	for line in f.readlines():
		if line != "end":
			inds += 1 
	
	ind = random.randrange(inds)
	
	#TODO: add getting a certain line by inex
	
	#TODO: read on python memory allocation
	print(chosen_one)

action_list(f)