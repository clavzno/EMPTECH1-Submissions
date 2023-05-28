var = int(input("Give me a number"))
var1 = var % 2
if var1 == 1:
	print("A")
else:
	if var >= 2 and var <= 5:
		print("B")
	elif var >= 6 and var <= 20:
		print("C")
	else:
		print("D")