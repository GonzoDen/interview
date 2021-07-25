import random

f = open("students_list.txt", "a")

def action_list(filename):
	f = open("students_list.txt", "r")

	for line in f.readlines():
		if line != "end":
			print(line)

action_list(f)

"""def choose_student(filename):
	f = open(filename, "r")
	quit_f = "not"
	students = []

	while quit_f != "end":
		f = open(filename, "r")
		quit_f = filename.splitlines()
		students.append(quit_f)

	ind = random.randrange(len(students))
	chosen_one = students[ind]
	print(chosen_one)

choose_student(f)"""