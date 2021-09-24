
# Define menu
def menu():
    print("Wacky's fun shack pick a number to place your order: ")
    print("[1]1.Ball")
    print("[2]2.Stick")
    print("[3]3.Toothpick")
# Define if a customer
customer = "yes"
Ball = "Ball"
Stick = "Stick"
Toothpick = "Toothpick"
# Get users name

name = input("Hello, Please enter name to get started? ")
# Respond with users name

print ("Hi,  " + name)
# Determine are they a customer
customer = input("Would you like to order? ")
if customer != "yes":
        print("Thank you have a nice day.")
# If they are a customer print menu and ask for input
else:
        menu ()   
        crap = int(input("Please pick a number:"))
        while crap != 0:
            if crap == 1:
                print("Thank you for you support your ," + Ball + " will be up shortly please be patient.") 
            if crap == 2:
                print("Thank you for you support your ," + Stick + " will be up shortly please be patient.")    
            if crap == 3:
                print("Thank you for you support your ," + Toothpick + " will be up shortly please be patient.")  
# Hint to debugging                
#if __name__ == '__main__':
#    app.run(debug=True,port=5001)
