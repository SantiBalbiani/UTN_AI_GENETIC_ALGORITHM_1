""" Selection Methods """
""" def get_population_after_selection(old_population):
    
    match CONFIG.SELECTION_FUNCTION:
        case "TOURNAMENT":
            return select_population_by_tournament(old_population)
        case _:
            return select_population_by_roulette(old_population) """

def get_random_individual_not_already_selected(_population, already_selected_individual_indexes):
    _index = randint(0, len(_population) - 1)
    while _index in already_selected_individual_indexes:
        _index = randint(0, len(_population) - 1)
    already_selected_individual_indexes.append(_index)
    return _population[_index]

def select_population_by_tournament(old_population):
    new_population = []
    for individual_index in range(len(old_population)):
        new_population.append(select_individual_by_tournament(old_population))
    return new_population

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


"Crossover methods"

""" def crossover(individual1, individual2):
    match CONFIG.CROSSOVER_FUNCTION:
        case "RANDOM":
            return random_crossover(individual1, individual2)
        case "MASK":
            return mask_crossover(individual1, individual2)
        case _:
            return single_point_crossover(individual1, individual2) """


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

def raise_invalid_mask_exception():
    raise Exception("Invalid mask")

def mask_crossover(individual1, individual2):
    return [get_child_from_mask(individual1, individual2, CONFIG.MASK_FIRST_CHILD),
            get_child_from_mask(individual1, individual2, CONFIG.MASK_SECOND_CHILD)]

