# ask how many per day
# multiply by 110 pesos
# calculate per week aka 7 days
# calculate per month aka 4 weeks aka 28 days
# calculate per year aka 12 months aka 48 weeks aka 336 days

print("problem #1")
# ask how many per day
a = int(input('How many iced coffees do you order per day? '))
# multiply by 110 pesos
b = a * 110
# calculate per week aka 7 days
wNew = b * 7
# calculate per month aka 4 weeks aka 28 days
mNew = wNew * 4
# calculate per year aka 12 months aka 48 weeks aka 336 days
yNew = mNew * 12
print("Here's how much you spend over time: ")
print(wNew, end=' pesos per week, ')
print()
print(mNew, end=' pesos per month, ')
print()
print('and ', yNew, end=' pesos per year.  ')
print()
print(input('type anything to go to next problem'))


# ask how many days it has been since
# ask how many weeks it has been since // 7 days per 1 week
# ask how many years it has been since // 365 days per 1 year
# calculate total days

print("problem #2")
# ask how many days it has been since
days = int(input("How many days has it been since the event? "))
# ask how many weeks it has been since // 7 days per 1 week
weeks = int(input("How many weeks has it been since the event? "))
# ask how many years it has been since // 365 days per 1 year
years = int(input("How many years has it been since the event? "))
# calculate total days
w = weeks * 7
y = years * 365
days_new = days + w + y
print("Total days: ", days_new, "(" , days, " + ", w, " + ", y, ")")
print()
quit()