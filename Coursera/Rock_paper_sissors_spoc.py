##rock, paper, scissors, spoc,lizard

"""
rule if you take first item minus the second, and the difference is one or 2,
the first item wins.if the difference is 3 or 4 the second item wins.
"""
import random

def convert_to_number(text):
    if text.lower() == "rock":
        val = 0
    elif text.lower() == "spock":
        val = 1
    elif text.lower() == "paper":
        val = 2
    elif text.lower() == "lizard":
        val = 3
    elif text.lower() == "scissors":
        val = 4
    else:
        print "kill1"
    return val

def number_to_word(val):
    if val == 0:
        text = "rock"
    elif val == 1:
        text = "spock"
    elif val == 2:
        text = "paper"
    elif val == 3:
        text = "lizard"
    elif val == 4:
        text = "scissors"
    else:
        print "kill2"
    return text

        
def operations(mypick):
    print " "
    print "Player chooses " + mypick
    myanswer = convert_to_number(mypick)

    computer = random.randrange(1,5)
    computertext = number_to_word(computer)
    print "Computer choose " + computertext
    
    diff = (computer - myanswer) % 5
    winner = ""
    if computer == myanswer:
        return "tie"
    else:
        if diff in range(3,5):
            winner = myanswer
        else:
            winner = computer
    
    winner = number_to_word(winner)
    return winner
    

print operations("paper")
