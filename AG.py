
from pyeasyga import pyeasyga

def AGFunction(data,mw,mv):
    MAX_WEIGHT = mw
    MAX_VOLUME = mv
    ga = pyeasyga.GeneticAlgorithm(data)  # intitialiser l'AG avec les données
    ga.population_size = 200  # Taille de la population a 200 chromosomes
    print("wei")
    print(MAX_WEIGHT)
    def fitness(individual, data):
        weight, volume, priority = 0, 0, 0
        for (selected, item) in zip(individual, data):
            if selected:
                weight += item[0]
                volume += item[1]
                priority += item[2]
        if weight > MAX_WEIGHT or volume > MAX_VOLUME:
            priority = 0
        return priority

    ga.fitness_function = fitness  # set the GA's fitness function
    ga.run()  # run the GA
    return ga.best_individual()
