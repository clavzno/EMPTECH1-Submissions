num = int(input("Enter number: "))
isValid = True

count = num - 1
while count > 1:
	if num // count - num / count == 0:
		isValid = False
	count = count - 1

if not isValid:
	print("You Got It!")

	#looks for composite numbers