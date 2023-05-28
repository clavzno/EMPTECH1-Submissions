def main():
    
        print ('Welcome to the Jellybean Republic Services!')
        print ('')
# A. Hot Air Balloon (1000J for 500g + 1.50J per excess gram
# B. Submarine (5000j for 500g + 5J per excess gram)
# Ask for weight in grams and transport mode
        weight = int(float(input('What is the weight of your package in grams?: ')))
        print ('')
        print ('Here are the modes of transportation that are available:')
        print ('A. Hot Air Balloon: 1000 Jellies for the first 500 grams + 1.50 Jellies for every gram in excess')
        print ('B. Submarine: 5000 Jellies for the first 500 grams + 5 Jellies for every gram in excess')
        print ('')
        mode_transpo = str(input('What mode of transportation would you like to use?: '))
# Compute then display costs
# Ask if they want to deliver another package
# If yes, repeat. If no, "Thank you and have a nice day"
        if mode_transpo == "A":
             if weight > 500:
                shipping_charge = (weight - 500) * 1.50
                cost = 1000 + shipping_charge
                print ('The delivery cost is', cost, 'jellies.')
             elif weight <= 500:
                print ('The delivery cost is 1000 jellies.')
       
        if mode_transpo == "B":
             if weight > 500:
                shipping_charge = (weight - 500) * 5
                cost = 5000 + shipping_charge
                print ('The delivery cost is', cost, 'jellies.')
             elif weight <= 500:
                print ('The delivery cost is 5000 jellies.')
                
        repeat = input('Would you like to send another package? Type "yes" or "no":').lower()
        if repeat == "yes":
           main()
        else:
            print("Thank you and have a nice day!")
            exit()  
main()
            
## You were hired to create a program for the Jellybean Republic. They want to implement a delivery system but first they need to have a machine that can compute for delivery costs. The delivery cost is dependent on the mode of transportation and the weight of the package. There are two modes of transportation (A) hot air balloon   (B) submarine.  Sending the package via hot air balloon costs 1000 Jellies (The currency in the Jellybean Republic is called Jellies) for the first 500 grams and an additional charge of 1.50 Jellies for every gram in excess of 500. If the package is to be sent via submarine, it would cost 5000 Jellies for the first 500 grams and there will be an additional charge of 5.0 Jellies for every gram in excess.

Assume that the weight is given as whole number and that:
>>input value of A stands for hot air balloon transport 
>>B stands for transport via submarine. 

# The program should ask for the weight in grams and the choice of transport and then compute and display the delivery cost. 

After displaying the delivery cost, your program should ask the user if they want to deliver another package and present the same menu as before if the user answers 'y', 

otherwise it should end the program and display the message 'Thank you and have a nice day!'.