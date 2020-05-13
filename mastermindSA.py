from SAalgo import simulated_annealing

class MastermindSA():
    def __init__(self):
        self.code = ''

    def validate(self, code, length):
        if not code.isdigit():
            print('Code cannot contain other characters other than digits')
            return False
        elif len(code) > length or len(code) < length:
            print('Invalid code length')
            return False
        else:
            return True

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
        print('Welcome to Mastermind')
        self.askForCode()
        simulated_annealing(self.code)