from genetic_algorithm.genetic_algorithm import initialPopulation, reproduce, fitness, check_guess
import re
from utils import validate


class MastermindGA():
    def __init__(self):
        self.code = ''

    def validate(self, code, length):
        return validate(code, length)

    def askForCode(self):
        isValidCode = False
        while not isValidCode:
            print('CodeSetter, enter a 4 digit code')
            self.code = input('> ')
            isValidCode = self.validate(self.code, 4)

    def giveGuessInfo(self):
        validDigitInfo = False
        validPossitionAndDigitInfo = False
        while not validDigitInfo:
            print('CodeSetter, number of digits that are correct')
            correctDigits = input('> ')
            validDigitInfo = self.validate(correctDigits, 1)
        while not validPossitionAndDigitInfo: 
            print('CodeSetter, number of digits that are correct and in correct position')
            correctDigitsAndPosition = input('> ')
            validPossitionAndDigitInfo = self.validate(correctDigitsAndPosition, 1)
        return (int(correctDigitsAndPosition), int(correctDigits))

    def run(self):
        population = initialPopulation(500)
        guess = '1234'
        guesses = []
        blackPegs = []
        whitePegs = []

        print('Welcome to Mastermind with Genetic Algorithm Search')
        self.askForCode()
        
        for tries in range(10):
            if guess == self.code:
                print('The genetic algorithm codebreaker took', tries + 1, 'tries to guess the code')
                return
            else:
                (b1,w1) = check_guess(guess, self.code)
                print('Guess is : ', guess)
                print('Black pegs: ', b1, 'White pegs: ', w1, '\n')
                guesses.append(guess)
                blackPegs.append(b1) 
                whitePegs.append(w1)

                for _ in range(15):
                    population = reproduce(population)
  
                fitness_list = []
                for individual in population:
                    fitness_list.append(fitness(individual, guesses, whitePegs, blackPegs))

                fittedPopulation = list(tuple(zip(population, fitness_list)))
                fittedPopulation = sorted(fittedPopulation, key= lambda tup: tup[1])
                guess = fittedPopulation.pop()[0]
                while guess in guesses:
                    guess = fittedPopulation.pop()[0]
                
        print('The genetic algorithm could not guess the correct code in less than 10 turns')