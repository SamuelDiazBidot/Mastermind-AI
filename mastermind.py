import utils
# Clase que contiene la logica del juego Mastermind original sin ningun algoritmo presente
class Mastermind():
    def __init__(self):
        self.code = ''

# Valida la entrada de datos parael juego
    def validate(self, code, length):
        return utils.validate(code, length)

# Pregunta por el codigo secreto al usuario
    def askForCode(self):
        isValidCode = False
        while not isValidCode:
            print('CodeSetter, enter a 4 digit code')
            self.code = input('> ')
            isValidCode = self.validate(self.code, 4)

# Funcion que se utiliza para obtener un nuevo numero del 'codebreaker'
    def newGuess(self):
        isValidGuess = False
        guess = ''
        while not isValidGuess:
            print('CodeBreaker, enter a 4 digit guess')
            guess = input('> ') 
            isValidGuess = self.validate(guess, 4)
        return guess

# Compara y devuelve el feedback necesario dado dos codigos secretos
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

# Funcion principal que se ecarga de la logica del juego
    def run(self):
        print('Welcome to Mastermind')
        self.askForCode()
        for tries in range(0,10):
            guess = self.newGuess()
            if guess == self.code:
                print('Congratulations Codebreaker, you guess the code!\nIt took you',  tries + 1,'tries to figure out the code!')
                return
            else:
                self.count_pegs(self.code,guess)
                self.giveGuessInfo() 
        print('Congratulations Codesetter, you won!')
