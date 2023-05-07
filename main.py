from random import random
from random import randint
import plotly.express as px
from config import CONFIG
from commons import Task
from commons import tasks
from commons import task_durations
from commons import task_priorities
from commons import task_earnedValues


class Individual:
    def __init__(self, chromosome=[]):
        if not chromosome:
            self.chromosome = []
            for i in range(len(tasks)):
                if random() <= 0.5:
                    self.chromosome.append(0)
                else:
                    self.chromosome.append(1)
        else:
            self.chromosome = chromosome

    def fitness(self):
        score = 0
        sum_durations = 0
        for gen_index in range(len(self.chromosome)):
            if self.chromosome[gen_index] == 1:
                score += task_earnedValues[gen_index] + (CONFIG.MAX_SCORE - task_durations[gen_index]) + 999 if (
                    task_priorities[gen_index] == 0) else task_priorities[gen_index]*10
                sum_durations += task_durations[gen_index]
        if sum_durations > CONFIG.TIME_LIMIT:
            score = 1
        return score

    def print(self):
        print(self.chromosome)


solutions = []


def get_initial_population():
    _population = []
    for i in range(CONFIG.POPULATION_SIZE):
        _population.append(Individual())
    return _population


def select_individual_by_roulette(_population, fitness_function_sum):
    _random = random() * fitness_function_sum
    _sum = 0
    _index = 0
    while _index < len(_population):
        _sum += _population[_index].fitness()
        if _sum >= _random:
            return _population[_index]
        else:
            _index += 1


def select_population_by_roulette(old_population):
    new_population = []
    fitness_function_sum = total_sum_fitness_function(old_population)
    for individual_index in range(len(old_population)):
        new_population.append(select_individual_by_roulette(
            old_population, fitness_function_sum))
    return new_population


def get_random_individual_not_already_selected(_population, already_selected_individual_indexes):
    _index = randint(0, len(_population) - 1)
    while _index in already_selected_individual_indexes:
        _index = randint(0, len(_population) - 1)
    already_selected_individual_indexes.append(_index)
    return _population[_index]


def competition_result(individual1, individual2):
    if individual1.fitness() >= individual2.fitness():
        return individual1
    else:
        return individual2


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
            individual1 = get_random_individual_not_already_selected(
                _population, already_selected)
            individual2 = get_random_individual_not_already_selected(
                _population, already_selected)
            new_population.append(competition_result(individual1, individual2))
        return select_individual_by_tournament(new_population)


def select_population_by_tournament(old_population):
    new_population = []
    for individual_index in range(len(old_population)):
        new_population.append(select_individual_by_tournament(old_population))
    return new_population


def get_population_after_selection(old_population):
    
    match CONFIG.SELECTION_FUNCTION:
        case "TOURNAMENT":
            return select_population_by_tournament(old_population)
        case _:
            return select_population_by_roulette(old_population)


def single_point_crossover(individual1, individual2):
    cutoff = round(random() * len(individual1.chromosome))
    chromosome1 = individual1.chromosome[0:cutoff] + \
        individual2.chromosome[cutoff::]
    chromosome2 = individual2.chromosome[0:cutoff] + \
        individual1.chromosome[cutoff::]
    child1 = Individual(chromosome1)
    child2 = Individual(chromosome2)
    return [child1, child2]


def get_random_child(individual1, individual2):
    child_chromosome = []
    for _i in range(len(individual1.chromosome)):
        if random() <= 0.5:
            child_chromosome.append(individual1.chromosome[_i])
        else:
            child_chromosome.append(individual2.chromosome[_i])
    return Individual(child_chromosome)


def random_crossover(individual1, individual2):
    return [get_random_child(individual1, individual2), get_random_child(individual1, individual2)]


def raise_invalid_mask_exception():
    raise Exception("Invalid mask")


def get_child_from_mask(individual1, individual2, mask):
    if len(individual1.chromosome) != len(mask):
        raise_invalid_mask_exception()
    child_chromosome = []
    for _i in range(len(mask)):
        if mask[_i] == 'X':
            child_chromosome.append(individual1.chromosome[_i])
        elif mask[_i] == 'Y':
            child_chromosome.append(individual2.chromosome[_i])
        else:
            raise_invalid_mask_exception()
    return Individual(child_chromosome)


def mask_crossover(individual1, individual2):
    return [get_child_from_mask(individual1, individual2, CONFIG.MASK_FIRST_CHILD),
            get_child_from_mask(individual1, individual2, CONFIG.MASK_SECOND_CHILD)]


def crossover(individual1, individual2):
    match CONFIG.CROSSOVER_FUNCTION:
        case "RANDOM":
            return random_crossover(individual1, individual2)
        case "MASK":
            return mask_crossover(individual1, individual2)
        case _:
            return single_point_crossover(individual1, individual2)


def get_population_after_crossover(old_population):
    gen_leap_length = (
        round((len(old_population) * CONFIG.GENERATIONAL_LEAP))//2) * 2
    parents = old_population[0:gen_leap_length]
    crossed_population = []
    for pi in range(0, len(parents), 2):
        children = crossover(old_population[pi], old_population[pi + 1])
        crossed_population.append(children[0])
        crossed_population.append(children[1])
    return crossed_population + old_population[gen_leap_length::]


def get_best_individual(_population):
    best_fitness = -1
    best_ind = 0
    for ind in _population:
        current_fitness = ind.fitness()
        if current_fitness > best_fitness:
            best_fitness = current_fitness
            best_ind = ind
    return best_ind


def get_mutation_position(_population):
    return round(random() * len(_population) * len(_population[0].chromosome))


def get_population_after_mutation(_population):
    mutation_probability = random()
    if mutation_probability <= CONFIG.MUTATION_PROBABILITY:
        mutation_pos = len(_population)

        while mutation_pos == len(_population):
            mutation_pos = get_mutation_position(_population)

        individual_index = mutation_pos // len(_population)
        chromosome_index = mutation_pos % len(_population[0].chromosome)

        if _population[individual_index].chromosome[chromosome_index] == 0:
            _population[individual_index].chromosome[chromosome_index] = 1
        else:
            _population[individual_index].chromosome[chromosome_index] = 0

    return _population


def total_sum_fitness_function(_population):
    _sum = 0
    for individual in _population:
        _sum += individual.fitness()
    return _sum


def select_individual_by_roulette(_population, fitness_function_sum):
    _random = random() * fitness_function_sum
    _sum = 0
    _index = 0
    while _index < len(_population):
        _sum += _population[_index].fitness()
        if _sum >= _random:
            return _population[_index]
        else:
            _index += 1

def execute_ga():
    population = get_initial_population()
    best = get_best_individual(population)
    for gen_number in range(CONFIG.NUMBER_OF_GENERATIONS):
        population = get_population_after_selection(population)
        population = get_population_after_crossover(population)
        population = get_population_after_mutation(population)
        gen_best = get_best_individual(population)
        solutions.append(gen_best.fitness())
        print(
            f'The best individual of generation ${str(gen_number + 1)}: ${gen_best.print()} ')
        print(f' Fitness function value: ${str(gen_best.fitness())}')
        if gen_best.fitness() > best.fitness():
            best = gen_best
    return best.fitness()


best_score = execute_ga()

graph_title = "Best score: " + str(best_score) \
              + " - Generational leap: " + str(CONFIG.GENERATIONAL_LEAP) \
              + " - Mutation probability: " + str(CONFIG.MUTATION_PROBABILITY) \
              + " - Crossover function: " + CONFIG.CROSSOVER_FUNCTION \
              + " - Selection function: " + CONFIG.SELECTION_FUNCTION

figure = px.line(x=range(0, CONFIG.NUMBER_OF_GENERATIONS),
                 y=solutions, title=graph_title)
figure.show()
