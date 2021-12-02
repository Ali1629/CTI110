# CTI 110
# P4LAB2 - Password Strenght checker
# Name
# Date

# Part 1 - password length

# Declare variables
isGoodPassword = False

# until the user gives a good enough password:
while (False == isGoodPassword):

    # ask user for password
    password = input("Please enter a new password: ")
    # check lenght
    # if it's at least MIN_LENGTH, it's a good password
    if len(password) >= MIN_LENGTH:
         #isGoodPassword = True
         # require upper and lower case
         # note we don't even check this until we have the length down
         if password == password.lower() or password == password.upper():
             print("Password should contain a mix of upper and lower case letters.")
         else:
             isGoodPassword = True
    # otherwise try again
    else:
        print("Password must be at least", MIN_LENGTH, "characters.")
# end of loop
print("Your new password is:",password)
#print("Ihope nobody is looking over your shoulder...")

# Part 2 - swapping characters
#(see 11.16)
# Notes:
"""
   i becomes 1
   a becomes @
   m becomes M
   B becomes 8
   s becomes $
and add ! to the end
"""
print("Now we'll replace some charecters to make it harder to guess.")
newPassword = "" # we will add each charecter one at a time
chars = list(password)

for char in chars:
    # if it's a charecter to replace, then replace it
    if char == "i":
        char = "1"
    if char == "a":
        char = "@"
    if char == "m":
        char = "M"
    if char == "B":
        char = "8"
    if char == "S":
        char = "$"
    #print(char) # testing
    newPassword += char # stick new charecter on the end

# finally add the ending "!"
newPassword += "!"

print("Your fancy new password is:", newPassword)
