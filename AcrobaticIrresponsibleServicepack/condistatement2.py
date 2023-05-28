weight = float(input("Input the weight: "))
if weight < 150.0:
	 print("Small")
elif weight >= 150.0 and weight < 165.0:
	print("Medium")
elif weight >= 165.0 and weight <= 195.0:
	print("Large")
else:
	 print("Too heavy")