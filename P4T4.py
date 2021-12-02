# CTI 110
# P4T4 - Running Total with Sentinel
# Name
# Date


# we will again add up numbers, this time it's hours worked.
# The user will enter values until they enter a -1
# Here the -1 is a "Sentinel" value that just means "done".
# (We did this because "hours worked" could never be negative.)

# Set up variables
total = 0
currentHours = 0
keepGoing = True

# Explain what's happening
print("Enter each day's hours worked on a different line.")
print("Enter -1 (or any negative number) to finish.")
# Loop until done
while keepGoing == True:

    # Ask the user for number of hours
    currentHours = float(input("Enter number of hours worked: "))
    # if it's -1 or less we're finished
    if currentHours < 0: # catches any negative value
        keepGoing = False
    # otherwise, add it to the total
    else:
        total += currentHours # same as total = total + currentHours

# we're now out of loop
print("Total hours entered:",total)
