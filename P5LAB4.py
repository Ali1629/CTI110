# CTI 110
# P5LAB4
# Name
# Date

"""
Rock paper scissors. we will break this into many functions.
-play one round
- get player pick
- get cpu pick
- compare to find winner
"""
import random

def playOneRound():
    """plays one round of RPS
       input: none, returns: who won the round ("player" or "cpu")
    """
    print("play one round.")
    winner = None
    player = getPlayerPick()
    cpu = getCpuPick()
    winner = whoWon(player, cpu)
    print("player:", player, "\tcpu:", cpu)
    return winner

def getPlayerPick():
    choice = input("[rock/paper/scissors]? ")
    return choice

def getCpuPick():
    choices = ["rock", "paper", "scissors"]
    roll = random.randint(0, 2) # matches indexes of list above
    choice = choices[roll]
    return choice

def whoWon(player, cpu):
    """ The meat of the RPS program: find out who won.
    input; player pick, cpu pick
    returns: "player" or "cpu" (the winner) """
    winner = None
    # 9 possible options - player has 3 X cpu has 3
    if player == "rock": # compare with 3 cpu picks
        if cpu == "rock":
            winner = None # tie
        if cpu == "Paper":
            winner = "cpu" # paper covers rock
        if cpu == "scissors":
            winner = "play7er" # rock braeks scissors
    # TODO add the remaining if statements below
    if player == "paper":
        pass
    if player == "scissors":
        pass
    return winner



def main():
    print("Rock paper scissors Game")
    playerWins = 0
    cpuWins = 0
    keepGoing = "y"
    while keepGoing == "y":
        winner = playOneRound()
        print("winner is", winner)
        if winner == "player":
            playerWins += 1
        if winner == "cpu":
            cpuWins += 1
        print("SCORE: player", playerWins, "tcpu:", cpuWins)
        keepGoing = input("again(y/n)? ")

# start program
if __name__ == "__main__":
    main()
