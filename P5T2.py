# CTI 110
# P5T2 - Lists and Functions
# Name
# Date

"""
Program has two parts:
MakeList() - build a list from user entered values
DisplayLiat() - take a list, display each item
TODO: maybe add input validation
"""

def getNumber():
    """
    input: none
    output: an int
    """
    goodInput = False # repeat until we get good input
    while goodInput == False:
        try:
            num = int(input("Enter a number: "))
            goodInput = True
        except ValueError:
            print("That is not a valid int... please try again.")
    return num

def MakeListOfSize(size):
    """
    Makes a list from user entered numbers
    input: size (int) -length of the list
    returns: a list
    """
    newList = []
    for i in range(size): # repeat size times
        #num = int(input("Enter a number: "))
        num = getNumber()
        newList.append(num)
    return newList

def DisplayList(items):
    """
    Display a list of the items.
    input: a list
    returns: none
    """
    for item in items:
        print(item, end=" ")
    print() #end of line

def removeDupes(items):
    """
    Take a list and remove duplicates (using set)
    input: a list
    returns: a list without duplicate entries
    """
    mySet = set(items)
    noDupeList = list(mySet)

    return noDupeList
def getMinandMaxOf(numbers):
    """
    input: a list
    returns: two numbers, the main and max values in list
    """
    minNum = min(numbers)
    maxNum = max(numbers)
    return minNum, maxNum

def getTotalAndAverage(numbers):
    """
    input: a list
    returns: two  numbers, total and average of all values
    """
    total = 0
    for number in numbers:
        total += number
    average = toatl / len(numbers)
    return total, averge

def main():
    #print("Making a list...")
    size = int(input("How many items in the list? "))
    numbers = MakeListOfSize(size)
    print("Display list...")
    DisplayList(numbers)
    print("removing duplicates...")
    numbersNoDupes = removeDupes(numbers)
    displayList(numbersNoDupes)
    # multiple variable return
    minNum, maxNum = getMinandMaxOf(numbers)
    print("Smallest =", minNum, "Largest =", maxNum)

    toatl,average = getTotalAndAverage(numbers)
    print("toatl =", toatl,"Average =", average)
    print("Done.")

# start
main()
