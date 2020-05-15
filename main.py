import re
import time
import random

from utils import create_mm_codes, validate_input
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
        user_input = input('What is the desired algorithm?\nGenetic Algoriothm --> GA\nSimulated Annealing --> SA\nAutomatic comparison of analysis --> analysis\n').lower()
        if user_input == 'sa':
            run_SA_mastermind()
            break
        elif user_input == 'ga':
            run_GA_mastermind()
            break
        elif user_input == 'analysis':
            run_auto_algorithms()
            break
        else:
            print('Incorrect input, try again.')
            time.sleep(2)

# Compares lists of all res
def compare_algos(algos_res):
    avrg_res = []
    for res_ls in algos_res:
        avrg_res.append(sum(res_ls) / len(res_ls))
    return avrg_res
        
def display_results(num_of_runs, comb_algo_res_ls, avrg_ls):
    print(f'{"-----Mastermid Algorithms Comparison-----":^60}')
    print(f'{"Attempt":<20}', f'{"GA Algorithm":<20}', f'{"SA Algorithm:":<20}')
    for idx, res_tup in enumerate(comb_algo_res_ls):
        print(f'{"#"+str(idx):<20}', f'{res_tup[0]:<20.2f}', f'{res_tup[1]:<20.2f}')
    print(f'Average tries of Genetic algorithm: {avrg_ls[0]}')
    print(f'Average tries of Simulated Annealing: {avrg_ls[1]}')

def run_auto_algorithms():
    sa_results = []
    ga_results = []
    rnd = random.Random()
    poss_ls = create_mm_codes()
    msg = 'Running Mastermind algorithm comparisons\nHow many times will the game run?\n'
    number_runs = int(validate_input(r'[0-9]+', msg))
    for i in range(number_runs):
        ga_results.append(MastermindGA().run_auto(rnd.choice(poss_ls)))
    for i in range(number_runs):
        print(MastermindSA().run_auto(rnd.choice(poss_ls)))
        sa_results.append(MastermindSA().run_auto(rnd.choice(poss_ls)))

    
    combined_res_ls = list(zip(sa_results, ga_results))
    
    avrg_ls = compare_algos(combined_res_ls)

    display_results(number_runs, combined_res_ls, avrg_ls)



def run_games():
    print('Welcome to Mastermind!')
    user_input = input('Run Mastermind with search algorithms? (y/n)  ')
    if user_input == 'y':
        ask_for_alg()
    else:
        defaultMastermind().run()
    


if __name__=='__main__':
    run_games()

