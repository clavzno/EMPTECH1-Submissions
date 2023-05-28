## input1 = input("Enter number1: ")
## input2 = input("Enter number2: ")
## _sum = int(input1) + int(input2)
## print("Sum is", _sum)

# (A + 3) >= C and D != B % A + 4 False
# (B - 1) <= A or D != B % A + 4
# (A + 2) % (C * D / B - 4) + D // (B - 1)

# to choose other py file do import <filename>.py
import WL10.py

D = input('inputd')
C = input('inputc')
B = input('inputb')
A = input('inputa')
_sum = (int(A) + 2) % (int(C) * int(D) / int(B) - 4) + int(D) // (int(B) - 1)
print("sum is,", _sum)

exam taken 2021-05-27
score 45/50