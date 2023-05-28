# set input
num = int(input("give a number: "))
 
# set value to null
revs = 0
 
# create iteration
while(num>0):
  rem = num % 10
  revs = (revs * 10) + rem
  num = num//10
 
# Display the result
print("the reverse of the number is : {}".format(revs))