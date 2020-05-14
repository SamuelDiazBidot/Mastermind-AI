from .SAalgo import simulated_annealing
from utils import validate

class MastermindSA():
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

    def newGuess(self):
        isValidGuess = False
        guess = ''
        while not isValidGuess:
            print('CodeBreaker, enter a 4 digit guess')
            guess = input('> ')
            isValidGuess = self.validate(guess, 4)
        return guess


    def run(self):
        print('Welcome to Mastermind with Simulated Annealing Algorithm search')
        self.askForCode()
        simulated_annealing(self.code)