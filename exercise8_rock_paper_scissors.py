import os
import time

conditions = ["rock", "paper", "scissors"]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def check_input():
    if play in conditions:
        return True
    else:
        print("Please enter rock, paper, or scissors!")

def winners_must_wait():
    print("Place your bets now...")
    suspense = 5
    while (suspense > 0):
        print(f"{str(suspense)}")
        time.sleep(1)
        suspense = suspense - 1
    print("Here are the results:")

def compare(play1, play2):
    if play1 == play2:
            winners_must_wait()
            print("It's a TIE!")
    elif play1 == "rock":
        if play2 == "scissors": 
            winners_must_wait()
            print(f"{player1_name} WINS!")  # rock beats scissors
        else:
            print(f"{player2_name} WINS!")  # paper beats rock
    elif play1 == "scissors":
        if play2 == "paper": 
            winners_must_wait()
            print(f"{player1_name} WINS!")  # scissors beats paper
        else:
            print(f"{player2_name} WINS!")  # rock beats scissors
    elif play1 == "paper":
        if play2 == "rock":
            print(f"{player1_name} WINS!")  # paper beats rock
        else:
            print(f"{player2_name} WINS!")  # scissors beats paper
    else:
        print("Error")

print("\nThis is Rock-Paper-Scissors, there are two players, each player will select a play.\n")

player1_name = str(input("Player 1, what is your name: "))
player2_name = str(input("Player 2, what is your name: "))

clear_console()

while True:
    while True:
        play1 = str(input(f"{player1_name}, Rock, Paper or Scissors? \n")).lower()
        play = play1
        if check_input() == True:
            break
    clear_console()

    while True:
        play2 = str(input(f"{player2_name}, Rock, Paper or Scissors? \n")).lower()
        play = play2
        if check_input() == True:
            break
    clear_console()

    winners_must_wait()
    compare(play1, play2)
    
    print(f"{player1_name} chose {play1}")
    print(f"{player2_name} chose {play2}")

    keep_going = str(input("\nWould you like to keep laying? (yes/no): ")).lower()
    clear_console()

    if keep_going == "yes":
        pass
    elif keep_going == "no":
        break
    else:
        pass