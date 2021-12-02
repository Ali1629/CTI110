#CTI 110
# Random Number Demo
# Name
# Date

# we will start off with a coin flip, then do
# rock, paper, scissors.

import random

def coinFlip():
    """ returns: "heads" or "tails" """
    result = None # fallback, if none of the ifs are used
    flip = random.randint(0, 1)
    if flip == 0:
        result = "heads"
    if flip == 1:
        result = "tails"

    return result

def main():
    # to start off, let's just count heads and tails
    numHeads = 0
    numTails = 0
    numTries = int(input("How many coin flips? "))
    for count in range(numTries):
        flip = coinFlip()
        if flip == "heads":
            numHeads += 1
        if flip == "tails":
            numTails += 1
    print(numTries, "flips: heads=", numHeads, "tails=", numTails)

def callTheCoin():
    """ The "call it in the air" minigame
    input: none
    return: none (might change this later)
    """
    # ask the user to call the flip
    choice = input("call it (heads/tails): ")

    #flip the coin
    flip = coinflip()

    # compare -- did they call it correctly?
    # the easy way:
    """
    if choice == flip:
        print("You called it! it was", flip)
    else:
        pritn("Nope, it was", flip)
    """
    # the hard way:
    winner = None
    if choice == "heads":
        if flip == "heads":
            winner = "player"
        if flip == "tails":
            winner = "cpu"
    if choice == "tails":
        if flip == "heads":
            winner = "cpu"
        if flip == "tails":
            winner = "player"
    print("You called", choice, "the flip was", flip)
    print("winner is:", winner)


def main():
    
    #countFlips()
    keepGoing = "y"
    while keepGoing == "y":
        callTheCoin()
        keepGoing = input("again(y/n) : ")

#print("I'm the module being run")
#print(__name__)
# start program
if __name__== "__main__":
    main()
