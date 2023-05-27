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
        total_duration = 0
        total_value = 0
        total_priority = 0

        #max_duration = max(task.taskDuration for task in tasks)
        max_duration = CONFIG.TIME_LIMIT
        #max_priority = max(task.priority for task in tasks)
        max_priority = 4
        max_value = max(task.valueAdded for task in tasks)

        # Usarlo si tengo chromosomas compuestos
        #for gen_index in range(len(self.chromosome)):    
        # 1er idea de criterio para ponderar    
        #+ (CONFIG.MAX_SCORE - task_durations[gen_index]) + 999 if (
        #  task_priorities[gen_index] == 0) else task_priorities[gen_index]*10
        for gen_index in range(len(tasks)):
              if self.chromosome[gen_index] == 1:              
                total_value += task_earnedValues[gen_index]                 
                total_duration += task_durations[gen_index]
                total_priority += task_priorities[gen_index]
        
        normalized_duration = total_duration / max_duration
        normalized_priority = total_priority / max_priority
        normalized_value = total_value / max_value

        if total_duration >= CONFIG.TIME_LIMIT:
            score = 0
        else:
            score = normalized_priority + normalized_value - 0.1*normalized_duration # $1 por cada 10 hs 
        return score

    def get_chromosome(self):
        return self.chromosome


solutions = []

# First
def get_initial_population():
    _population = []
    for i in range(CONFIG.POPULATION_SIZE):
        _population.append(Individual())
    return _population

#Second

def get_best_individual(_population):
    best_fitness = -1
    best_ind = 0

    return max(_population, key = lambda individual: individual.fitness())

"""     for ind in _population:
        current_fitness = ind.fitness()
        if current_fitness > best_fitness:
            best_fitness = current_fitness
            best_ind = ind
    return best_ind """


def select_individual_by_roulette(_population, fitness_function_sum):
    _random = random() * fitness_function_sum
    _sum = 0
    #_index = 0

    for i in _population:
        _sum += i.fitness()
        if _sum >= _random:
            return i
        

"""     while _index < len(_population):
        _sum += _population[_index].fitness()
        if _sum >= _random:
            return _population[_index]
        else:
            _index += 1
 """

def select_population_by_roulette(old_population):
    new_population = []
    fitness_function_sum = total_sum_fitness_function(old_population)
    for individual_index in range(len(old_population)):
        new_population.append(select_individual_by_roulette(
            old_population, fitness_function_sum))
    return new_population


def get_population_after_selection(old_population):
    return select_population_by_roulette(old_population)


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

def crossover(individual1, individual2):
    return random_crossover(individual1, individual2)

def get_population_after_crossover(old_population):
    gen_leap_length = (round((len(old_population) * CONFIG.GENERATIONAL_LEAP))//2) * 2
    parents = old_population[0:gen_leap_length]
    crossed_population = []
    for pi in range(0, len(parents), 2):
        children = crossover(old_population[pi], old_population[pi + 1])
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
        print("generación Nro: " , gen_number)
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
    print("Best Fitness Value: " , best.fitness())
    print("Duración Total: " , get_totalDuration(best.chromosome))
    print( "Valor Total Agregado: ", get_total_value(best.chromosome))
    return (best.fitness(), best)

def get_names(chromosomes):
    task_names_final = []
    for i, chromosome in enumerate(chromosomes):
        if chromosome == 1:
            task_names_final.append( task_names[i])
    return task_names_final

def get_total_value(chromosome):
    task_value_final = []
    for i, chromosome in enumerate(chromosome):
        if chromosome == 1:
            task_value_final.append( task_earnedValues[i])
    return sum(task_value_final)

def get_totalDuration(chromosomes):
    task_durations_final = []
    for i, chromosome in enumerate(chromosomes):
        if chromosome == 1:
            task_durations_final.append( task_durations[i])
    return sum(task_durations_final)

def get_total(chromosome, attribute):
    task_final = []
    for i, chromosome in enumerate(chromosome):
        if chromosome == 1:
            task_final.append( task_durations[i])
    return sum(task_final)

(best_score, the_best) = execute_ga()

graph_title = "Best score: " + str(best_score) \
              + " - Generational leap: " + str(CONFIG.GENERATIONAL_LEAP) \
              + " - Mutation probability: " + str(CONFIG.MUTATION_PROBABILITY) \
              + " - Crossover function: " + CONFIG.CROSSOVER_FUNCTION \
              + " - Selection function: " + CONFIG.SELECTION_FUNCTION \
              + " \n Best Task Combination " + str(get_names(the_best.get_chromosome())) 
             
figure = px.line(x=range(0, CONFIG.NUMBER_OF_GENERATIONS),
                 y=solutions, title=graph_title)
figure.show()

#pipinstall alive-progress