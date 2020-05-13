import random

def check_guess(guess, code):
    copy_code = list(code)
    copy_guess = list(guess)
    blackPegs = 0
    whitePegs = 0

    for i in range(len(code)):
        if code[i] == guess[i]:
            blackPegs = blackPegs + 1
            copy_code[i] = 42
            copy_guess[i] = 4242

    for j in copy_guess:
        if j in copy_code:
            whitePegs = whitePegs + 1
            for i,c in enumerate(copy_code):
                if c == j:
                    copy_code[i] = 42

    return (blackPegs, whitePegs)

def initialPopulation(population):
    x = lambda: ''.join(random.choice("123456") for i in range(4))
    arr = []
    for i in range(population):
        arr.append(x())
    return arr

def fitness(c, g, w, b):
  fitness = 0
  for i in range(len(g)):
    fitness += -abs(check_guess(c, g[i])[1] - w[i]) - abs(check_guess(c, g[i])[0] - b[i])
  return fitness

def crossover(parent1, parent2):
  Parentgenes1 = list(parent1)
  Parentgenes2 = list(parent2)
  childGenes1 = Parentgenes1[:2] + Parentgenes2[2:]
  childGenes2 = Parentgenes2[:2] + Parentgenes1[2:]
  child1 = ''.join(childGenes1)
  child2 = ''.join(childGenes2)
  return (child1, child2)

def mutate(gen, mutationProb):
  if random.random() < mutationProb:
    i = random.randrange(len(gen))
    gen[i] = ''.join(random.choice("123456") for i in range(4))
  return gen

def reproduce(prevGen):
  nextGen = []
  for _ in range(int(len(prevGen)/2)):
    parents = random.sample(prevGen, 2)
    (child1, child2) = crossover(parents[0], parents[1])
    nextGen.append(child1)
    nextGen.append(child2)
    nextGen = mutate(nextGen, 0.3)
  return nextGen