# P4LAB3
#






# A simple menu, which can be expanded.
# a menu with 4 or more options. One of the options should be "Quit".
# The program should print the menu and then ask the the user to make a choice.
# If the user makes a choice other than those listed, they are asked to make the choice again.
# Once the user picks a menu option, print a message specific to that choice,
# and then return to the main menu.

def budgetEscape(sponsor):
    """
    This method just keeps you in a room until you leave.
    (our budget was $0.)
    Input: sponsor - display a message
    output: none
    """
    print("This escape room brought to you by:", sponsor)
    # this time we loop based on user input
    leave = "no"
    #leave = input("will you leave (yes/no)? ")
    while leave != "yes" and leave != "y":
        print("You're in a room. There is a door.")
        # more description could go here
        levae = input("Will you leave (yes/no)? ")
        print("You leave. Nice job.")

def tacoTruck():
    taco = "" # add toppings later
    orderUp = False
    while (orderUp == False):
        answer = input("Would you like a taco? (y/n)")
        if answer == "y":
            taco += "A taco"
            orderUp = True
            answer = input("Do you want lettuce? (y/n)")
            if answer == "y":
                taco += "with lettuce"
                answer = input("Do you want tomatoes? (y/n)")
                if answer == "y":
                    taco += "add tomatoes"
            if answer == "n":
                taco += "nothing"
                orderUp = True


    print("Here's your order of", taco)

def surprise():
    # this example doesn't loop, but it could.
    print("Put your surprise code here.")
    print("Example: A sub-menu.")
    print("a. Option A")
    print("b. Option B")
    print("c. Option C")
    # example of returning a value
    option = None # no value at all

    Choice = input("choose: ")
    if choice == "a" or choice == "A":
        print("Option A")
        option = "A"
    if choice.lower() == "b": # compare what they typed but in lowercase
        print("Option B")
        option = "B"
    if choice == "c" or choice == "C":
        print("Option C")
        option = "C"
    # return the option

def main():
    print("Simple Menu")

    # declare variables
    repeat = True
    selection = 0

    while repeat == True:
         # print the menu, ask the user to make a choice.
         print () # add whitespace
         print ("Menu:")
         print (" " * 10)
         print ("1. option 2")
         print ("2. option 2")
         print ("3. option 3")
         print ("4. Quit")
         # Exception handling
         try:
             selection = int(input("Choose option: "))
         except:
             print("That is not a valid choice. please try again.")
             selection = 0 # so we don't pick the previous menu option
         # either pick a branch based on the selction,
         # or print error and repeat (if not from listed options)
         if selection == 1:
             print("You chose option", selection)
             budgetEscape("Raid Shadow Legends") # run the escape
         elif selection == 2:
             print("You chose option", selection) # for testing
             tacoTruck()
         elif selection == 3:
             print("You chose option", selection) # for testing
             surprise()
         elif selection == 4:
             print("Exiting...")
             repeat = False # next time through, we won't loop
         else: # anything else
             print(selection,"is not a valid choice. Please try again.")


    # end of while loop
    print("Goodbye.")

# program starts here
main()

# the complex version (this is optional for now)
# TLDR: prevents multiple main() from running at once
"""
if __name__ ==" __main__":
"""
                 
