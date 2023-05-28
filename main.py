from random import random
from random import randint
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from config import CONFIG
from commons import Task
from commons import tasks
from alive_progress import alive_bar
from individual import Individual
from methods import Methods
from helper import Helper

title_text="Comparación de Métodos de Selección"
selection_methods = ["ROULETTE", "TOURNAMENT"]
solutions = []
subgraphs_titles = []
subgraph_x_values = [ x_value for x_value in range(0, CONFIG.NUMBER_OF_GENERATIONS)]
subgraphs_x_values = []
subgraphs_y_values = []

def get_initial_population():
    _population = []
    for i in range(CONFIG.POPULATION_SIZE):
        _population.append(Individual())
    return _population


def get_best_individual(_population):
    return max(_population, key=lambda individual: individual.fitness())


def get_population_after_selection(old_population, selection_method):
    return Methods.select_population(old_population, selection_method)


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


def execute_ga(selection_method):
    population = get_initial_population()
    best = get_best_individual(population)
    with alive_bar(CONFIG.NUMBER_OF_GENERATIONS) as bar:
        for gen_number in range(CONFIG.NUMBER_OF_GENERATIONS):
            # print("generación Nro: ", gen_number)
            population = get_population_after_selection(population, selection_method)
            population = get_population_after_crossover(population)
            population = get_population_after_mutation(population)
            gen_best = get_best_individual(population)
            solutions.append(gen_best.fitness())
            # print(
            #     f'The best individual of generation ${str(gen_number + 1)}: ${gen_best.print()} ')
            # print(f' Fitness function value: ${str(gen_best.fitness())}')
            if gen_best.fitness() > best.fitness():
                best = gen_best
            bar()
    print("Best Fitness Value: ", best.fitness())
    print("Duración Total: ", Helper.get_total(
        best.chromosome, "task_durations"))
    print("Valor Total Agregado: ", Helper.get_total(
        best.chromosome, "earned_value"))
    print("Prioridad Final:", Helper.get_total(best.chromosome, "priorities"))
    print("Tareas a realizar", Helper.get_names(best.get_chromosome()))
    return (best.fitness(), best)



for idx, selection_method in enumerate(selection_methods):
    print('Generando resultados para el método de selección ', selection_method)
    (best_score, the_best) = execute_ga(selection_method)

    graph_title = selection_method + ", Score:" + str(round(best_score,2))
    subgraphs_titles.append(graph_title)
    subgraphs_y_values.append(solutions)
    solutions = []
      #"Mejor Aptitud: " + str(best_score) \ 
       # + " - Generational leap: " + str(CONFIG.GENERATIONAL_LEAP) \
      #  + " - Mutation probability: " + str(CONFIG.MUTATION_PROBABILITY) \
      #  + " - Crossover Method: " + CONFIG.CROSSOVER_FUNCTION \
         
        #  + " \n Best Task Combination " + \ str(get_names(the_best.get_chromosome()))

figure = make_subplots(rows=1, cols=len(
        selection_methods), subplot_titles=subgraphs_titles)
for idx, selection_method in enumerate(selection_methods):
        figure.add_trace(go.Scatter(x=subgraph_x_values,
                            y=subgraphs_y_values[idx]), row=1, col=idx+1)

figure.update_layout(
        height=600, width=1300, title_text="Comparación de Métodos de Selección", showlegend=False)
figure.show()

# Helper.graph(title_text, subgraphs_titles, selection_methods, subgraph_x_values, subgraphs_y_values )


