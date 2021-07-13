n = int(input("How many numbers to check: "))

fizz = 3
buzz = 5
output = ""

for i in range(1, n+1):
	if i % fizz == 0: 
		output = output + "Fizz"
	if i % buzz == 0:
		output = output + "Buzz"
	if output == "":
		output = i
	print(output)

	output = ""



#quite nevnimatelnaya