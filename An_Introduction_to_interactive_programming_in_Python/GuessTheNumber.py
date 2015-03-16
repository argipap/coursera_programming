# author:Anargyros Papaefstathiou (based on given template)
# Course:An Introduction to Interactive Programming in Python
# Guess the Number Game: Try to guess the number between a range
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    #global variable for defining range
    global num_range
    #global variable to compute the number the user tries to find
    global secret_number
    #number of guesses which user has
    global numOfGuesses
    #new game message when the game starts
    global message
    #if/else statement for initializing global variables in each case
    if num_range == 100:
        #when num_range == 100
        secret_number = random.randrange(0,100)
        numOfGuesses = 7
        message = "New game. Range is from 0 to 100"
    elif num_range == 1000:
        #when num_range == 1000
        secret_number = random.randrange(0,1000)
        numOfGuesses = 10
        message = "New game. Range is from 0 to 1000"
    else:
        print "bad input"
    #print messages
    print message
    print "Number of remaining guesses is",numOfGuesses,"\n"

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    #global variables
    global num_range
    global secret_number
    global message
    global numOfGuesses
    #set the num_range
    num_range = 100
    #call new_game to start
    new_game()
def range1000():
    # button that changes the range to [0,1000) and starts a new game
    #global variables
    global num_range
    global secret_number
    global message
    global numOfGuesses
    #set the num_range
    num_range = 1000
    #call new_game to start
    new_game()
    
def input_guess(guess):
    # main game logic goes here
    #global number of guesses variable
    global numOfGuesses
    #if statement for run out guesses
    if(numOfGuesses == 0):
        #if user has no more guesses print a message and start a new game
        print"You ran out of guesses!The number was",secret_number
        new_game()
    else:
        #else if user has more guesses continue
        #if input is empty string tell user that has to enter a number
        if guess == "":
            print "Please Enter a number!"
        else:
            #decrease numOfGuesses by 1
            numOfGuesses-=1
            #convert sring guess to integer
            iguess = int(guess)
            #print messages
            print "Guess was",iguess
            print "Number of remaining guesses is",numOfGuesses
            #if/else statement for printing messages for every guess
            if iguess==secret_number:
                print "Correct\n"
                #when user finds the correct answer, automatically is starting a new game
                new_game()
            elif iguess > secret_number:
                print "Lower\n"
            else:
                print "Higher\n"

    
# create frame
frame = simplegui.create_frame("Guess the number",200,200,100)

# register event handlers for control elements and start frame
#add input to frame
inp = frame.add_input('Enter Number', input_guess, 100)
#add buttons
button1 = frame.add_button("0 - 100", range100, 107)
button2 = frame.add_button("0 - 1000", range1000, 107)
#start the frame
frame.start()

# initialize global vars
num_range=100
numOfGuesses=7
message = "New game. Range is from 0 to 100"
# call new_game
new_game()
