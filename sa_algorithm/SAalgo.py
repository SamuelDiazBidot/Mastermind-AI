import random
from itertools import product
import numpy as np

def probability(p):
    return p > random.uniform(0.0, 1.0)

def simulated_annealing(scode):
    T = 0
    possibilities = [''.join(p) for p in product('123456', repeat=4)]  # Crea toda las posibilidades
    current_guess_code = random.choice(possibilities)  # Crea el primer guess
    guesses = []
    guesses.append(current_guess_code)
    while T != 4:
        if len(guesses) > 11:
            break
        possibilities = create_consistent_list(scode, possibilities, current_guess_code)  #Se crea una ista consitente
        neighborhood = create_neigborhood(current_guess_code)  # Crea el una lista de mutaciones del guess
        augmented = neighborhood + possibilities
        next_choice = random.choice(augmented)  # Escoge un codigo random de la lista

        while next_choice in guesses: # Para que no repita
            next_choice = random.choice(neighborhood)
        cost_nextg = calculating_cost(scode, possibilities, next_choice)  # Compara dos guesses

        if cost_nextg == 0 or len(possibilities) == 1:  # Si es 0 significa que el codigo random es mejor que el que esta guardado en current_guess_code
            current_guess_code = next_choice
            guesses.append(current_guess_code)
            print('Guess is : ', current_guess_code)
            print('Black pegs: ', count_pegs(scode, current_guess_code)[1], 'White pegs: ', count_pegs(scode, current_guess_code)[0])
            print(' ')
        elif probability(np.exp(-8/(cost_nextg+1))):  # Si es malo pues hay una probabilidad que lo escoja como quiera
            current_guess_code = next_choice
            guesses.append(current_guess_code)
            print('Guess is : ', current_guess_code)
            print('Black pegs: ', count_pegs(scode, current_guess_code)[1], 'White pegs: ', count_pegs(scode, current_guess_code)[0])
            print(' ')

        T = count_pegs(scode, current_guess_code)[1]

    if len(guesses) <= 10:
        print(current_guess_code)
        print('Congratulations Codebreaker, you guess the code!\nIt took you', len(guesses), 'tries to figure out the code!')
    else:
        print('Congratulations Codesetter, you won!')



# Funcion para contar los numeros de pegs blanco y negros. Mismo que el de GA
def count_pegs(scode, guess_code):
    white_peg = 0
    black_peg = 0

    copy_code = list(scode)
    copy_guess = list(guess_code)
    for i in range(4):
        if scode[i] == guess_code[i]:
            black_peg += 1
            copy_code[i] = 42
            copy_guess[i] = 4242

    for j in copy_guess:
        if j in copy_code:
            white_peg += 1
            for i, c in enumerate(copy_code):
                if c == j:
                    copy_code[i] = 42

    return white_peg, black_peg


# Funcion crea la lista consistente
def create_consistent_list(mcode, possibilities, ngc):
    temp = []
    for item in possibilities:
        if count_pegs(ngc, item) == count_pegs(mcode, ngc):
            temp.append(item)
    possibilities = temp[:]
    return possibilities


#Funcion para comparar el un codigo con todos los guess anteriores
def calculating_cost(c, g, ngc):

    cost = 0
    ngpegs = count_pegs(c, ngc)
    nbg = ngpegs[1]
    nwg = ngpegs[0]
    if len(g) == 0 and nbg >= 1:
        g.append(ngc)
        return nbg+nwg
    elif len(g) == 0 and nwg > 0:
        cost += nbg + nwg
        return cost

    for i in range(len(g)):
        gpegs = count_pegs(c, g[i])
        bg = gpegs[1]
        wg = gpegs[0]
        diff_white = abs(nbg-bg)
        diff_black = abs(nwg-wg)
        cost += diff_black + diff_white
    return cost


#Funcion para remplazar una posicion random con un numero random
def mutate(gen, i, j):
    choice = j
    gen = gen[:i] + choice + gen[i + 1:]
    return gen


# Crea una lista para las mutaciones de un codigo
def create_neigborhood(guess):
    neighborhood = []
    choice = "123456"
    for i in choice:
        for j in range(4):
            mutation = mutate(guess, j, i)
            if mutation not in neighborhood and guess != mutation:
                neighborhood.append(mutation)
    return neighborhood
