## answers
#VARIABLES
quantitypotato = 0
quantityapple = 0
quantityorange = 0
quantitybanana = 0
quantitypopcorn = 0
quantitywater = 0
quantitycola = 0

option = 0

while option != 3:

#STARTING SCREEN
 
    print("Hi welcome to the cash register! What may we assist you with?")
    print("Select an option below:")
    print("[1] New Transaction")
    print("[2] Generate Report")
    print("[3] Cancel Transaction")

    option  = int(input("What option would you like to choose?: "))

    if option != 1 and option != 2 and option !=3:
       print("Oops! Your answer is Invalid. Please try again")
       option  = int(input("What option would you like to choose?: "))

#IF OPTION 1 IS SELECTED:
    if option == 1:
        
          print("[1] Potato")
          print("[2] Apple")
          print("[3] Orange")
          print("[4] Banana")
          print("[5] Popcorn")
          print("[6] Bottled Water")
          print("[7] Cola")
          print("[8] Cancel")

#THE PROGRAM WILL ASK WHICH ITEM WILL BE BOUGHT DURING THAT TRANSACTION
          purchase = int(input("Purchase what item? : "))

          if purchase == 1:
             quantitypotato = quantitypotato + int(input("Input the quantity: "))
             print("You've bought", quantitypotato, "potato(s)")
           

          if purchase == 2:
        
             quantityapple = quantityapple + int(input("Input the quantity: "))
             print("You've bought", quantityapple, "apple(s)")

          if purchase == 3:
       
             quantityorange = quantityorange + int(input("Input the quantity: "))
             print("You've bought", quantityorange, "orange(s)")

          if purchase == 4:
          
             quantitybanana = quantitybanana + int(input("Input the quantity: "))
             print("You've bought", quantitybanana, "banana(s)")

          if purchase == 5:
         
             quantitypopcorn = quantitypopcorn + int(input("Input the quantity: "))
             print("You've bought", quantitypopcorn, "popcorn(s)")

          if purchase == 6:
          
             quantitywater = quantitywater + int(input("Input the quantity: "))
             print("You've bought", quantitywater, "water bottle(s)")

        
          if purchase == 7:
         
             quantitycola = quantitycola + int(input("Input the quantity: "))
             print("You've bought", quantitycola, "cola(s)")

          if purchase == 8:
             print("Hi! Welcome to the cash register!")
             print("Please select an option below:")
             print("[1] New Transaction")
             print("[2] Generate Report")
             print("[3] Exit the program")



             option = int(input("Which option would you like to choose?: "))
        

         
        

            


#IF THE USER CHOOSES TO GENERATE THE REPORT OF PURCHASE
          



    if option == 2:

             
                  
             
              if quantitypotato > 0:
                 potato = (50 * quantitypotato)
                 print("Potato        P50 x", quantitypotato, "=", potato)
              elif quantitypotato <= 0:
                    print("Potato       P50 x 0 =", 0.00)


                    


              if quantityapple > 0:
                 apple = (35 * quantityapple)
                 print("Apple        P35 x", quantityapple, "=", apple)
              elif quantityapple <= 0:
                   print("Apple       P35 x 0 =", 0.00)


                   

              if quantityorange > 0:
                 orange = (40 * quantityorange)
                 print("Orange        P40 x", quantityorange, "=", orange)
              elif quantityapple <= 0:
                   print("Orange      P40 x 0 =", 0.00)


                   

              if quantitybanana > 0:
                 banana = (25 * quantitybanana)
                 print("Banana       P25 x", quantitybanana, "=", banana)
              elif quantitybanana <= 0:
                 print("Banana      P25 x 0 =", 0.00)


               

              if quantitypopcorn > 0:
                 popcorn = (120 * quantitypopcorn)
                 print("Popcorn       P120 x", quantitypopcorn, "=", popcorn)
              elif quantitypopcorn <= 0:
                   print("Popcorn       P120 x 0 =", 0.00)


                   

              if quantitywater > 0:
                 water = (20 * quantitywater)
                 print("Bottled Water       P20 x", quantitywater, "=", water)
              elif quantitywater <= 0:
                   print("Bottled Water       P20 x 0 =", 0.00)


                   

              if quantitycola > 0:
                cola = (40 * quantitycola)
                print("Cola        P40 x", quantitycola, "=", cola)
              elif quantitycola <= 0:
                   print("Cola       P40 x 0 =", 0.00)





              potato = (50 * quantitypotato)
              apple = (35 * quantityapple)
              orange = (40 * quantityorange)
              banana = (25 * quantitybanana)
              popcorn = (120 * quantitypopcorn)
              water = (20 * quantitywater)
              cola = (40 * quantitycola)
              total_each = (potato + apple + orange + banana + popcorn + water + cola)
            

#PRE TOTAL
              print("------------------------------------------")

              print("CURRENT TOTAL: ", total_each, " PESOS")

#AMOUNT TO BE TENDERED

              payment = float(input("How much are you paying?: "))
              if payment < total_each:
                  print("Unfortunately, that is not enough money!")
                  payment = float(input("How much are you paying: "))

#PWD/SENIOR CITIZEN

              PWD = input("Are you a PWD? (Yes/No): ")
              while PWD != "Yes" and PWD != "yes" and PWD != "No" and PWD != "no":
                  
                  print("Oops, your answer is invalid! Try again")
                  PWD =   input("Are you a PWD? (Yes/No): ")

              senior = int(input("What year were you born?: "))
              
              

#DISCOUNTS
              
              if PWD == "Yes" or PWD == "yes":
                  if senior <= 1954:
                      PWDSR = (total_each * 0.15)

                  elif senior > 1954:
                      PWDSR = (total_each * 0.05)

              elif PWD == "No" or PWD == "no":

                  if senior <= 1954:
                      PWDSR = (total_each * 0.1)

                  elif senior > 1954:
                      PWDSR = (total_each * 0)


                

              

             
             




            
              
                  

                  
              
              discount_total = total_each - PWDSR



              print("PWD/SENIOR      ", PWDSR, " PESOS")

              print("DISCOUNTED TOTAL     ", discount_total, " PESOS")
              


#SUMMARY 


              print("CASH TENDERED   ", payment, " PESOS")

              change = (payment - discount_total)

              print("CHANGE   ", change, " PESOS")


              print("Thank you for shopping! Have a great day!")

              quantitypotato = 0
              quantityapple = 0
              quantityorange = 0
              quantitybanana = 0
              quantitypopcorn = 0
              quantitywater = 0
              quantitycola = 0
              PWDSR = 0
              discount_total = 0
              payment = 0
              change = 0

              print("------------------------------------------")