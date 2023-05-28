count = 0
val1 = 0
val2 = 0
while count < 10:
	num = int(input("Enter number: "))
	if num % 2 == 0:
		val1 = val1 + num
	elif num % 2 == 1:
		val2 = val2 + num
	count = count + 1
print("The output is", val1, "and", val2)

#val1 is all even sum
#val2 is all odd sum