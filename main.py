import re
import time

from mastermind import Mastermind as defaultMastermind
from genetic_algorithm.mastermindGA import MastermindGA
from sa_algorithm.mastermindSA import MastermindSA


def run_SA_mastermind():
    game = MastermindSA()
    game.run()

def run_GA_mastermind():
    game = MastermindGA()
    game.run()

def ask_for_alg():
    while True:
        user_input = input('What is the desired algorithm?\nGenetic Algoriothm --> GA\nSimulated Annealing --> SA\n').lower()
        if user_input == 'sa':
            run_SA_mastermind()
            break
        elif user_input == 'ga':
            run_GA_mastermind()
            break
        else:
            print('Incorrect input, try again.')
            time.sleep(2)

def run_games():
    print('Welcome to Mastermind!')
    user_input = input('Run Mastermind with search algorithms? (y/n)  ')
    if user_input == 'y':
        ask_for_alg()
    else:
        defaultMastermind().run()
    


if __name__=='__main__':
    run_games()

