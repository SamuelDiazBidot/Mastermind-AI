from .SAalgo import simulated_annealing
from utils import validate


# Clase la cual se encarga del juego de mastermind  con el algoritmo de simulated annealing
class MastermindSA():
    def __init__(self):
        self.code = ''

    # valida la entrada de datos
    def validate(self, code, length):
        return validate(code, length)
    # Pregunta por el el codigo que se estara utilizando durante el juego
    def askForCode(self):
        isValidCode = False
        while not isValidCode:
            print('CodeSetter, enter a 4 digit code')
            self.code = input('> ')
            isValidCode = self.validate(self.code, 4)

    # Maneja el estado del juego cada vez que toca entrar un nuevo codigo secreto para compararlo
    def newGuess(self):
        isValidGuess = False
        guess = ''
        while not isValidGuess:
            print('CodeBreaker, enter a 4 digit guess')
            guess = input('> ')
            isValidGuess = self.validate(guess, 4)
        return guess

    # Funcion principal del programa que permite que el usuario decida cual sera el codigo secreto
    def run(self):
        print('Welcome to Mastermind with Simulated Annealing Algorithm search')
        self.askForCode()
        return simulated_annealing(self.code)

    # Funcion principal del programa la cual corre automaticamente el programa con un codigo secreto generado aleatoriamente
    def run_auto(self, code_to_break):
        print('Welcome to Mastermind with Simulated Annealing Algorithm search')
        print('Codesetter, enter a 4 digit code.\n>', code_to_break)
        self.code = code_to_break
        # self.askForCode()
        return simulated_annealing(self.code)