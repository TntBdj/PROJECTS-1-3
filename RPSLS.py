import random
Quit = False
Win = 0
Loss = 0

def Play():
    Player = input("rock(r), paper(p), scissors(sc), lizard(l), spock(sp) or (q) to quit: ")
    AI = random.choice(["r", "p", "sc", "l", "sp"])
    global Win
    if Player == "r" or Player == "p" or Player == "sc" or Player == "l" or Player == "sp" or Player == "q":
        x = 1
    else:    
        return ("Invalid Input. Make sure to only choose (r), (p), (sc), (l), (sp), or (q)")
        
    if Player == "q":
        global Quit 
        Quit = True
        return ("The final score: ")
    
    print (f"You chose {Player} and the AI chose {AI}")
    if Player == AI:
        return ("It a tie! ")

    elif WinnerWinnerChickenDinner(Player, AI):
        global Win
        Win = Win + 1
        return ("AYYEEEE good job. Easy W's")

    global Loss 
    Loss = Loss + 1
    return("You're trash the AI won")

def WinnerWinnerChickenDinner(Competitor, Opponent):
    if (Competitor == "sp" and (Opponent == "sc" or Opponent == "r") or (Competitor == "sc" and (Opponent == "p" or Opponent == "l")) or (Competitor == "p" and (Opponent == "r" or Opponent == "sp")) or (Competitor == "r" and (Opponent == "l" or Opponent == "sc")) or (Competitor == "l" and (Opponent == "sp" or Opponent == "p"))):
        return True
while True:
    Start = input("play, rock, paper, scissors, lizard, spock(RPSLS)? or (q) to quit: ")
    if Start == "RPSLS":
        Game = True
        break
    elif Start == "q":
        Game = False
        break
    else:
        print("Invalid input. Make sure to choose (RPSLS) or (q). ")
        continue
while Game == True:
    print(Play())
    if Quit == True:
        print(f"You have {Win} wins and the AI has {Loss}")
        if Win > Loss:
            print("Beginners luck I see...")
        elif Loss > Win:
            print("Wow. Leaving when you're losing hey?")
        elif (Loss == 0 and Win == 0):
            print("You could've at least played once man")
        else:
            print("Too scared to play one more???")
        break
    print(f"You have {Win} wins and the AI has {Loss}")
print(f"Come again soon!")
