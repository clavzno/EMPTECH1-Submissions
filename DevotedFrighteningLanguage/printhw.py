"""
Problem : PRINT HELLO WORLD!
   
   Name: [REMOVED FOR PUBLIC DISPLAY]    
   Section: ADT11A
   
"""

output_value = "HeLLo World!"
choice_1 = 0
choice_2 = 0
choice_3 = 0
choice_4 = 0

print("Welcome to the print HeLLo World program \n\Here are your choices:")
print("1. Add one (1) HeLLo World!")
print("2. Add five (5) HeLLo World!")
print("3. Add twenty five (25) HeLLo World!")
print("4. Add fifty (50) HeLLo World!")
print("5. Stop program")

choice = int(input("What do you want to do? "))

#
while 0 < choice < 5:
    if choice == 1:
        choice_1 += 1
        choice = int(input("What do you want to do? "))

#option2 
    if choice ==2:
        choice_2 += 5
        choice = int(input("What do you want to do? "))

#option3        
    if choice == 3:
        choice_3 += 25
        choice = int(input("What do you want to do? "))

#option4        
    if choice == 4:
        choice_4 += 50
        choice = int(input("What do you want to do? "))

#option5        
    if choice == 5:
        answer = (1 + choice_1 + choice_2 + choice_3 + choice_4)

    
print(("HeLLo World!")* answer)
print("Total HeLLo WOlrd:",answer)