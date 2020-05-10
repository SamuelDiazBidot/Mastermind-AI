import random
import numpy as np

def probability(p):
    return p > random.uniform(0.0, 1.0)

def simulated_annealing(scode):
    T = 10000
    current_guess_code = ''.join(random.choice("123456") for i in range(4))  #Crea el primer guess
    guesses = []
    next_choice = calculating_cost(scode, guesses, current_guess_code)
    while T > 1:
        neighborhood = create_neigborhood(current_guess_code)  #Crea el una lista de permutaciones y mutaciones del guess
        next_choice = random.choice(neighborhood)  #Escoge un codigo random de la lista
        while next_choice in guesses: # Para que no repita
            next_choice = random.choice(neighborhood)
        cost_nextg = calculating_cost(scode, guesses, next_choice) #Compara dos guesses

        if cost_nextg == 0:  # Si es 0 significa que el codigo random es mejor que el que esta guardado en current_guess_code
            current_guess_code = next_choice
            guesses.append(current_guess_code)
        elif probability(2/(cost_nextg+1)): #Si es malo pues hay una probabilidad que lo escoja como quiera
            current_guess_code = next_choice

        pegs = count_pegs(scode, current_guess_code)
        if pegs[1] == 4: #Si consiguio el codigo correcto
            print(current_guess_code)
            break
        T *= 0.997
    print(current_guess_code)
    print(guesses)


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
def mutate(gen):
    i = random.randrange(len(gen)-1)
    rand_choice = random.choice("123456")
    gen = gen[:i] + rand_choice + gen[i + 1:]
    return gen

#Crea una lista para de permutaciones y mutaciones de un codigo
def create_neigborhood(guess):
    neighborhood = []
    for i in range(40):
        permutation = ''.join(random.sample(guess, len(guess)))
        mutation = mutate(permutation)
        if mutation not in neighborhood:
            neighborhood.append(mutation)
    return neighborhood
