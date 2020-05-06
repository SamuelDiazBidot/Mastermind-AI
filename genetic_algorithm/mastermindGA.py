from genetic_algorithm.genetic_algorithm import initialPopulation, reproduce, fitness

class MastermindGA():
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
        population = initialPopulation(100)
        guess = '1122'
        guesses = []
        blackPegs = []
        whitePegs = []
        print('Welcome to Mastermind')
        self.askForCode()
        for tries in range(10):
            if guess == self.code:
                print('Congratulations Codebreaker, you guess the code!\nIt took you',  tries,'tries to figure out the code!')
                return
            else:
                print(guess)
                (b1, w1) = self.giveGuessInfo() 
                guesses.append(guess)
                blackPegs.append(b1)
                whitePegs.append(w1)

                population = reproduce(population)

                fitness_list = []
                for individual in population:
                    fitness_list.append(fitness(individual, guesses, whitePegs, blackPegs))

                fittedPopulation = list(tuple(zip(population, fitness_list)))
                fittedPopulation = sorted(fittedPopulation, key= lambda tup: tup[1])
                guess = fittedPopulation.pop()[0]

        print('Congratulations Codesetter, you won!')