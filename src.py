import random
import time

def game_start():
    #Fuction to introduce game, present rules and get the number range from terminal input
    welcome_message = "Hi!\nWelcome to the number guessing game!\nToday I (the computer) will play against you."
    print(welcome_message)
    lower = int(input("To start, please tell me the lowest number of the bound to guess from: ")) 
    upper = int(input("Great thanks!\nNow can you tell me the highest bound: "))
    return (lower,upper)


def computer_chose_number(range_tuple):
    #use rand to get a random number in input range 
    min = range_tuple[0]
    max = range_tuple[1]
    computer_number = random.randint(min,max)
    #return number to be guessed by human player
    return computer_number


def computer_choice(num_range):
    #Function which handles the turn where the human player guesses the computers number
    #Counter for number of guesses human has made
    player_guesses = 0
    correct = False
    #make choice of number to be guessed
    computer_choice = computer_chose_number((num_range))
    print("I am chosing a number for you to guess. Good Luck!")
    #loop until number is guessed
    while correct == False:
        player_guess = int(input("Please enter your guess: "))
        player_guesses += 1
        if player_guess > computer_choice:
            print("Sorry the number is lower than " + str(player_guess) + " please try again.")
        elif player_guess < computer_choice:
            print("Sorry the number is higher than " + str(player_guess) + " please try again.")
        else:
            print("Congrats that was the number!")
            correct = True
            print("That took you " + str(player_guesses) + " guesses!")
    #retrun number of guesses attempted by player to find the number
    return player_guesses


def human_choice(num_range):
    #function similar to tha of computer_choice, but now human choses number and computer guesses
    #create variable for number of guesses the computer makes
    cpu_guesses = 0
    correct = False
    #Create variables which will be updated as the computer makes guesses
    lower_bound = num_range[0]
    upper_bound = num_range[1]
    #get input dor number to be guessed
    player_choice = int(input("Please enter your numer between " + str(lower_bound) + " and " + str(upper_bound) + " : "))
    print("Great! I will now try to guess your number")
    #loop unitl number is guessed
    while correct == False:
        #cpu's guess
        cpu_guess = random.randint(lower_bound, upper_bound)
        print("I chose", cpu_guess)
        cpu_guesses += 1
        if cpu_guess > player_choice:
            print("cpu is wrong!")
            #update upper bound to make guesses more accurate by reducing range in which the number is
            upper_bound = cpu_guess - 1
        elif cpu_guess < player_choice:
            print("cpu is wrong!")
            #update lower bound
            lower_bound = cpu_guess + 1
        else:
            print("Congrats that was the number!")
            correct = True
            print("That took me " + str(cpu_guesses) + " guesses!")
        #sleep to give the game a sense of realism
        time.sleep(1.0)
    
    return cpu_guesses




def end_game(cpu_guesses, player_guesses):
    
    print("\n\nGAME OVER!")
    if(cpu_guesses == player_guesses):
        print("Its a tie!")
    elif cpu_guesses < player_guesses:
        print("Sorry you lost")
    else:
        print("Congratulations! You won!")