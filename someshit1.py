

# Define if a customer
customer = "yes"
ball = "Ball"
stick = "Stick"
toothpick = "Toothpick"
# Get users name

name = input("Hello, Please enter name to get started? " )
# Respond with users name

print ("Hi,  " + name + " Welcome to Wacky;s fun house please pick a number to place an order.")
# Determine are they a customer
#customer = input("Would you like to order? ")
#if customer != "yes":
    
  #  print("Thank you have a nice day.")

print("[1]Ball")
print("[2]Stick")
print("[3]Toothpick")
# If they are a customer print menu and ask for input
while True:        
    crap = int(input("Please pick a number:"))
   
    if crap == 1:
                    print("Thank you for your support, " + name + " your " + ball + " will be up shortly please be patient.")
                    break 
    if crap == 2:
                    print("Thank you for your support, " + name + " your " + stick + " will be up shortly please be patient.")
                    break    
    if crap == 3:
                    print("Thank you for your support, " + name + " your " + toothpick + " will be up shortly please be patient.")
                    break
    if crap != 1 and crap != 2 and crap != 3:
                    print("Not a valid choice please start over and select 1,2, or 3")
    
    
                               


# Hint to debugging                
#if __name__ == '__main__':
#    app.run(debug=True,port=5001)
