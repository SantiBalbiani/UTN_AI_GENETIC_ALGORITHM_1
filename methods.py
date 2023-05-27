from random import random
from random import randint
from config import CONFIG
from individual import Individual


class Methods:

    def select_population(old_population):
        match CONFIG.SELECTION_FUNCTION:
            case "TOURNAMENT":
                return Methods.select_population_by_tournament(old_population)
            case _:
                return Methods.select_population_by_roulette(old_population)

    def select_individual_by_roulette(_population, fitness_function_sum):
        _random = random() * fitness_function_sum
        _sum = 0
        for i in _population:
            _sum += i.fitness()
            if _sum >= _random:
                return i

    def total_sum_fitness_function(_population):
        _sum = 0
        for individual in _population:
            _sum += individual.fitness()
        return _sum

    def select_population_by_roulette(old_population):
        new_population = []
        fitness_function_sum = Methods.total_sum_fitness_function(old_population)
        for individual_index in range(len(old_population)):
            new_population.append(Methods.select_individual_by_roulette(
                old_population, fitness_function_sum))
        return new_population

# ==============END ROULETTE========================================
    def get_random_individual_not_already_selected(_population, already_selected_individual_indexes):
        _index = randint(0, len(_population) - 1)
        while _index in already_selected_individual_indexes:
            _index = randint(0, len(_population) - 1)
        already_selected_individual_indexes.append(_index)
        return _population[_index]

    def select_individual_by_tournament(_population):
        if CONFIG.POPULATION_SIZE % 2 != 0:
            raise Exception(
                "Cannot perform tournament if population size is not an even number")
        if len(_population) == 1:
            return _population[0]
        else:
            new_population = []
            already_selected = []
            for _i in range(len(_population) // 2):
                individual1 = Methods.get_random_individual_not_already_selected(
                    _population, already_selected)
                individual2 = Methods.get_random_individual_not_already_selected(
                    _population, already_selected)
                new_population.append(
                    Methods.competition_result(individual1, individual2))
            return Methods.select_individual_by_tournament(new_population)

    def select_population_by_tournament(old_population):
        new_population = []
        for individual_index in range(len(old_population)):
            new_population.append(
                Methods.select_individual_by_tournament(old_population))
        return new_population

    def competition_result(individual1, individual2):
        if individual1.fitness() >= individual2.fitness():
            return individual1
        else:
            return individual2

    """Crossover methods"""

    def crossover(individual1, individual2):
        match CONFIG.CROSSOVER_FUNCTION:
            case "RANDOM":
                return Methods.random_crossover(individual1, individual2)
            case "MASK":
                return Methods.mask_crossover(individual1, individual2)
            case _:
                return Methods.single_point_crossover(individual1, individual2) 

    def get_random_child(individual1, individual2):
        child_chromosome = []
        for _i in range(len(individual1.chromosome)):
            if random() <= 0.5:
                child_chromosome.append(individual1.chromosome[_i])
            else:
                child_chromosome.append(individual2.chromosome[_i])
        return Individual(child_chromosome)


    def random_crossover(individual1, individual2):
        return [Methods.get_random_child(individual1, individual2), Methods.get_random_child(individual1, individual2)]

    def single_point_crossover(individual1, individual2):
        cutoff = round(random() * len(individual1.chromosome))
        chromosome1 = individual1.chromosome[0:cutoff] + \
            individual2.chromosome[cutoff::]
        chromosome2 = individual2.chromosome[0:cutoff] + \
            individual1.chromosome[cutoff::]
        child1 = Individual(chromosome1)
        child2 = Individual(chromosome2)
        return [child1, child2]

    def get_child_from_mask(individual1, individual2, mask):
        if len(individual1.chromosome) != len(mask):
            Methods.raise_invalid_mask_exception()
        child_chromosome = []
        for _i in range(len(mask)):
            if mask[_i] == 'X':
                child_chromosome.append(individual1.chromosome[_i])
            elif mask[_i] == 'Y':
                child_chromosome.append(individual2.chromosome[_i])
            else:
                Methods.raise_invalid_mask_exception()
        return Individual(child_chromosome)

    def raise_invalid_mask_exception():
        raise Exception("Invalid mask")

    def mask_crossover(individual1, individual2):
        return [Methods.get_child_from_mask(individual1, individual2, CONFIG.MASK_FIRST_CHILD),
                Methods.get_child_from_mask(individual1, individual2, CONFIG.MASK_SECOND_CHILD)]
