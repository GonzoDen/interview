import random

students = ['student0', 'student1', 'student2', 'student3', 'student3']

def choose_student(students):
	ind = random.randrange(len(students))
	chosen_one = students[ind]
	print(chosen_one)

choose_student(students)