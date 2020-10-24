import random
import time

def game_start():
    welcome_message = "Hi!\nWelcome to the number guessing game!\nToday I (the computer) will play against you."
    print(welcome_message)
    lower = int(input("To start, please tell me the lowest number of the bound to guess from: ")) 
    upper = int(input("Great thanks!\nNow can you tell me the highest bound: "))
    return (lower,upper)


def computer_chose_number(range_tuple):
    min = range_tuple[0]
    max = range_tuple[1]
    computer_number = random.randint(min,max)
    return computer_number


def computer_choice(num_range):
    #computer choses num, player guesses
    player_guesses = 0
    correct = False
    
    computer_choice = computer_chose_number((num_range))
    print("I am chosing a number for you to guess. Good Luck!")

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

    return player_guesses


def human_choice(num_range):  
    cpu_guesses = 0
    correct = False
    lower_bound = num_range[0]
    upper_bound = num_range[1]

    player_choice = int(input("Please enter your numer between " + str(lower_bound) + " and " + str(upper_bound) + " : "))
    print("Great! I will now try to guess your number")
    
    while correct == False:
        cpu_guess = random.randint(lower_bound, upper_bound)
        print("I chose", cpu_guess)
        cpu_guesses += 1
        if cpu_guess > player_choice:
            print("cpu is wrong!")
            upper_bound = cpu_guess - 1
        elif cpu_guess < player_choice:
            print("cpu is wrong!")
            lower_bound = cpu_guess + 1
        else:
            print("Congrats that was the number!")
            correct = True
            print("That took me " + str(cpu_guesses) + " guesses!")
        
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