from itertools import islice
import random

initialPopulation = {}
parent1 = []
parent2 = []
initializePopulation()
fitnessAllPospulation()
printPopulation()



def initializePopulation():
    while len(initialPopulation) < 7:
        list = random.sample(range(1,5), 4)
        list.insert(0,0)
        t = tuple(list)
        if t not in initialPopulation.keys():
            initialPopulation[t] = 0  # or = fitnessFunction(t) 
            printPopulation()

def printPopulation():

for i in range(10):