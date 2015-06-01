##http://www.codeskulptor.org/#user39_GpFNXzKE3D_0.py


# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

rmguesses = 7
userguess = 0
compguess = random.randrange(0,101)

# helper function to start and restart the game
def new_game():
    global rmguesses
    # initialize global variables used in your code here
    print "New game. Range is from 0 ot 100."
    print "Number of remaining guesses is ", rmguesses

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global userguess, compguess, rmguesses
    userguess = 0
    compguess = random.randrange(0,101)
    rmguesses = 7
    
def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global userguess, compguess, rmguesses
    userguess = 0
    compguess = random.randrange(0,1001)
    rmguesses = 7
def input_guess(guess):
    # main game logic goes here	
    global userguess, compguess, rmguesses
    userguess = float(guess)
    rmguesses -= 1
    print "Guess was", userguess
    print "Number of remainingguesses =", rmguesses
    if rmguesses > 0:
        if userguess == compguess:
            print "Correct!"
            print "Click a range to start a new game"
        elif userguess < compguess:
            print "Higher!"
        else:
            print "Lower!"
    else:
        print "Out of guesses"
        print "The computer was", compguess
        print "Start a new game"
    print " " 
    
# create frame
f = simplegui.create_frame("Guess the number", 200, 300)

# register event handlers for control elements and start frame
f.add_button("Range is [0, 100]", range100, 200)
f.add_button("Range is [0, 1000]", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
