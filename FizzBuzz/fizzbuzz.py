n = int(input("How many numbers to check: "))

fizz = 3
buzz = 5

for i in range(1, n+1):
	if i % fizz == 0 and i % buzz == 0:
		print("FizzBuzz")
	elif i % fizz == 0:
		print("Fizz")
	elif i % buzz == 0:
		print("Buzz")
	else:
		print(i)

#actually forgot to make constants qeq just typed 3 and 5 there straightly
#run the code twice