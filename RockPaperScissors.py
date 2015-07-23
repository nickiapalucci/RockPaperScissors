# Students Name = Nick Iapalucci

# Date = October 5, 2014

# Assignment 4.2, #4.17
# Write a program that plays rock-paper-scissor.  The program randomly
# generates a number 0, 1, pr 2 representing scissor, rock and paper,
# respectively. The program prompts the user to enter a number 0, 1, or
# 2 and displays a message indicating whether the user or the computer
# wins, loses, or draws.
# Time Spent = 2 hours

# Honor Code: I pledge that this program represents my own program code.
# I received help from no one in designing and debugging my program.

# include random module to generate opponent hand in this game of chance
import random

# Welcome, title, explanation
print("\n\nWelcome to Rock, Paper, Scissors!\n\n\n"
      "This is a game of luck, you versus the computer.\n"
      "You both will secretly pick a rock, paper, or scissors.\n\n"
      "The winner is determined by classic rock, paper, scissor standards:\n"
      "Rock smashes Scissors, Scissors cut Paper, and "
      "Paper covers a Rock\n\n")

# Prompt user to enter a number
print("When you are ready, choose your weapon, then press [ENTER] \n")
print("Press 0 for scissors, 1 for rock, or 2 for paper\n")

# Assign input to Player1
Player1 = input("=> ")

# Test input to see if user typed an integer.
# If input string cannot be converted integer, replace with an integer
# that will represent a loss for player 1
try :
    Player1 = int(Player1)
except :
    Player1 = -1

# Assign random choice to Player2
Player2 = random.randint(0, 2)

# Determine winner or tie
if Player1 == Player2 :
    Winner = 0
elif Player1 == 0 and Player2 == 1 :
    Winner = 2
elif Player1 == 0 and Player2 == 2 :
    Winner = 1
elif Player1 == 1 and Player2 == 0 :
    Winner = 1
elif Player1 == 1 and Player2 == 2 :
    Winner = 2
elif Player1 == 2 and Player2 == 0 :
    Winner = 2
elif Player1 == 2 and Player2 == 1 :
    Winner = 1
elif Player1 <= -1 or Player1 >= 3 :
    Winner = 2
else :
    Winner = -1


# Create result strings
Player1ch = 'you'
if Player1 == 0 :
    Player1ch = Player1ch + ' picked scissors'
elif Player1 == 1 :
    Player1ch = Player1ch + ' picked rock'
elif Player1 == 2 :
    Player1ch = Player1ch + ' picked paper'
else :
    Player1ch = Player1ch + ' did not enter 0, 1, or 2'

Player2ch = 'The computer'
if Player2 == 0 :
    Player2ch = Player2ch + ' picked scissors'
elif Player2 == 1 :
    Player2ch = Player2ch + ' picked rock'
elif Player2 == 2 :
    Player2ch = Player2ch + ' picked paper'
else :
    Player2ch = Player2ch + ' messed up (which is weird)'

# Translate results to character string
if Winner == 0 :
    Winnerch = 'It is a draw.'
elif Winner == 1 :
    Winnerch = 'You won!'
elif Winner == 2 :
    Winnerch = 'The computer won.'
else :
    Winnerch = 'Nobody won.  Something went wrong.'

# Display results
print("\n", Player2ch, ", and ", Player1ch, ".  ",
      Winnerch, "\n", sep = '')
