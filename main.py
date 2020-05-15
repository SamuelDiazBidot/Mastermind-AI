import re
import time
import random

from utils import create_mm_codes, validate_input
from genetic_algorithm.mastermindGA import MastermindGA
from sa_algorithm.mastermindSA import MastermindSA

# Corre mastermind con el algoritmo de simulated annealing
def run_SA_mastermind():
    game = MastermindSA()
    game.run()

# Corre mastermind con el algoritmo "Genetic"
def run_GA_mastermind():
    game = MastermindGA()
    game.run()

# Decide que parte del programa se va a correr
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

# Compares lists of all results, helper to prepare the results to be displayed
def compare_algos(algos_res):
    avrg_res = []
    first_avrg = sum(algos_res[0]) / float(len(algos_res[0]))
    second_avrg = sum(algos_res[1]) / float(len(algos_res[1]))
    return first_avrg, second_avrg
        
# Displays the results after running the program with the different algorithms        
def display_results(num_of_runs, comb_algo_res_ls, avrg_ls):
    print(f'\n{"-----Mastermid Algorithms Comparison-----":^60}')
    print(f'{"Attempt:":<20}', f'{"GA Algorithm:":<20}', f'{"SA Algorithm:":<20}')
    for idx, res_tup in enumerate(comb_algo_res_ls):
        print(f'{"#"+str(idx+1):>20}', f'{res_tup[1]:>20.2f}', f'{res_tup[0]:>20.2f}')
    print(f'Average tries of Genetic algorithm: {avrg_ls[1]}')
    print(f'Average tries of Simulated Annealing: {avrg_ls[0]}')

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
    
    avrg_ls = compare_algos([sa_results, ga_results])
    
    display_results(number_runs, combined_res_ls, avrg_ls)


# Main function of the program
def run_games():
    print('Welcome to Mastermind!')
    ask_for_alg()

if __name__=='__main__':
    run_games()

