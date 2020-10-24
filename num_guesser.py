import random
import src
import time



def main():
    num_range = src.game_start()
    #let the games beginnnnn!!!!
    player_guesses = src.computer_choice(num_range)
    cpu_guesses = src.human_choice(num_range)
    #lets see who won
    src.end_game(cpu_guesses, player_guesses)
   

main()



