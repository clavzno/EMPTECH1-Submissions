ctr = 0
threshold = int(input("Enter threshold: "))
n = int(input("Enter n: "))
fs = 0
ctr = 1
while ctr * ctr <= n:
	if n % ctr == 0:
		fs = fs + 1
	ctr = ctr + 1
if fs < threshold:
	 print("ACCEPTABLE Condition")
else:
	print("UNACCEPTABLE Condition")

# probably finds prime numbers idk