import pygad
import matplotlib.pyplot as plt
from operator import attrgetter
from alive_progress import alive_bar
from configs import TASKS, CONSTANTS, CONFIGS
from task_types import Priority


def get_total(chromosome, key):
    values = [key(task)
              for id, task in enumerate(TASKS) if chromosome[id] == 1]
    return sum(values)


def total_duration(chromosome):
    return get_total(chromosome, key=attrgetter("duration"))


def total_value(chromosome):
    return get_total(chromosome, key=attrgetter("value"))


def total_priority(chromosome):
    return get_total(chromosome, key=attrgetter("priority"))


def fitness(_, chromosome, __):
    normalized_duration = total_duration(chromosome) \
        / CONSTANTS["MAX_DURATION"]
    if normalized_duration >= 1:
        return 0

    normalized_value = total_value(chromosome) / sum([t.value
                                                      for t in TASKS])

    normalized_priority = total_priority(chromosome) / sum([p.value
                                                            for p in Priority])

    return CONSTANTS["K_PRIORITY"] * normalized_priority + \
        normalized_value - CONSTANTS["VALUE_TIME_COST"] * normalized_duration


def main():
    for name, config in CONFIGS.items():
        print("Config Name:", name)
        with alive_bar(config["num_generations"]) as bar:
            # Instance GA
            ga = pygad.GA(**config,
                          gene_type=int,
                          fitness_func=fitness,
                          on_generation=lambda _: bar())

            # Run the algorithm.
            ga.run()
            ga.plot_fitness()

        # Returning the details of the best solution
        solution, solution_fitness, _ = ga.best_solution()

        print("Best:", solution, "Score:", solution_fitness)
        print("Total Duration:", total_duration(solution))
        print("Total Value:", total_value(solution))
        print("Priority Score:", total_priority(solution))

        solution_names = [f"- {task.name}"
                          for id, task in enumerate(TASKS)
                          if solution[id] == 1]

        print("Solution Tasks:")
        print("\n".join(solution_names))


if __name__ == "__main__":
    main()
