from random import random
from random import randint
import plotly.express as px
from config import CONFIG
from commons import Task
from commons import tasks
from commons import task_durations
from commons import task_priorities
from commons import task_earnedValues
from commons import task_names
from alive_progress import alive_bar
from individual import Individual
from methods import Methods

solutions = []


def get_initial_population():
    _population = []
    for i in range(CONFIG.POPULATION_SIZE):
        _population.append(Individual())
    return _population


def get_best_individual(_population):
    return max(_population, key=lambda individual: individual.fitness())


def get_population_after_selection(old_population):
    return Methods.select_population(old_population)


def get_population_after_crossover(old_population):
    gen_leap_length = (
        round((len(old_population) * CONFIG.GENERATIONAL_LEAP))//2) * 2
    parents = old_population[0:gen_leap_length]
    crossed_population = []
    for pi in range(0, len(parents), 2):
        children = Methods.crossover(
            old_population[pi], old_population[pi + 1])
        crossed_population.append(children[0])
        crossed_population.append(children[1])
    return crossed_population + old_population[gen_leap_length::]


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
        print("generación Nro: ", gen_number)
        population = get_population_after_selection(population)
        population = get_population_after_crossover(population)
        population = get_population_after_mutation(population)
        gen_best = get_best_individual(population)
        solutions.append(gen_best.fitness())
       # print(
       #     f'The best individual of generation ${str(gen_number + 1)}: ${gen_best.print()} ')
       # print(f' Fitness function value: ${str(gen_best.fitness())}')
        if gen_best.fitness() > best.fitness():
            best = gen_best
    print("Best Fitness Value: ", best.fitness())
    print("Duración Total: ", get_total(best.chromosome, "task_durations"))
    print("Valor Total Agregado: ", get_total(best.chromosome, "earned_value"))
    print("Prioridad Final:", get_total(best.chromosome, "priorities"))
    print("Tareas a realizar", get_names(best.get_chromosome()))
    return (best.fitness(), best)


def get_names(chromosomes):
    task_names_final = []
    for i, chromosome in enumerate(chromosomes):
        if chromosome == 1:
            task_names_final.append(task_names[i])
    return task_names_final


def get_total(chromosome, attribute):
    task_final = []
    match attribute:
        case "task_durations":
            for i, chromosome in enumerate(chromosome):
                if chromosome == 1:
                    task_final.append(task_durations[i])
        case "earned_value":
            for i, chromosome in enumerate(chromosome):
                if chromosome == 1:
                    task_final.append(task_earnedValues[i])
        case "priorities":
            for i, chromosome in enumerate(chromosome):
                if chromosome == 1:
                    task_final.append(task_priorities[i])
        case _:
            return None
    return sum(task_final)


(best_score, the_best) = execute_ga()

graph_title = "Best score: " + str(best_score) \
              + " - Generational leap: " + str(CONFIG.GENERATIONAL_LEAP) \
              + " - Mutation probability: " + str(CONFIG.MUTATION_PROBABILITY) \
              + " - Crossover function: " + CONFIG.CROSSOVER_FUNCTION \
              + " - Selection function: " + CONFIG.SELECTION_FUNCTION \
              + " \n Best Task Combination " + \
    str(get_names(the_best.get_chromosome()))

figure = px.line(x=range(0, CONFIG.NUMBER_OF_GENERATIONS),
                 y=solutions, title=graph_title)

figure.show()

# pipinstall alive-progress
