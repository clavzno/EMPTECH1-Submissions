num = int(input("Enter number: "))
value = 0

while num > 0:
	value = value + num % 10
	num = num // 10

print("The output is", value)

# gets sum of all the digits