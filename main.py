import itertools as iter
import pygad
from dataclasses import dataclass
from alive_progress import alive_bar


@dataclass
class Task:
    name: str
    capable_resources: set[int]
    duration: int


@dataclass
class Step:
    position: int
    task_num: int
    resource_num: int


RESOURCES = {
    1: "Desarrollador Senior",
    2: "Desarrollador Semi-Senior",
    3: "Desarrollador Junior"
}


TASKS = {
    1: Task(name="Centrar DIV", duration=10, capable_resources=set([1, 2, 3])),
    2: Task(name="Hacer Pantalla de Login", duration=4, capable_resources=set([1, 2])),
    3: Task(name="Hacer Pantalla Home", duration=8, capable_resources=set([1, 2])),
    4: Task(name="Hacer Deploy", duration=4, capable_resources=set([1]))
}


def is_valid_resource(resource_num):
    return resource_num in range(1, len(RESOURCES) + 1)


def is_valid_task(task_num):
    return task_num in range(1, len(TASKS) + 1)


def is_valid_step(step: Step):
    return is_valid_task(step.task_num) and \
        is_valid_resource(step.resource_num) and \
        set([step.resource_num]).issubset(TASKS[step.task_num].capable_resources)


def is_valid_solution(solution):
    return all(map(is_valid_step, solution))


def get_steps(chromosome):
    # Group chromosome elements in groups of gene_size.
    gene_size = 2
    genes = [chromosome[i:i+gene_size]
             for i in range(0, len(chromosome), gene_size)]

    return [Step(position=gene[0], task_num=i, resource_num=gene[1])
            for i, gene in enumerate(genes, start=1)]


def fitness(ga, chromosome, solution_idx):
    solution = get_steps(chromosome)
    # Penalize invalid solutions
    if not is_valid_solution(solution):
        return 1 / 999999

    resource_is_free_time = {resource_num: 0 for resource_num in RESOURCES.keys()}
    step_end_times = []
    for step in solution:
        step_end_time = resource_is_free_time[step.resource_num] + TASKS[step.task_num].duration
        resource_is_free_time[step.resource_num] = step_end_time
        step_end_times.append(step_end_time)

    return 1 / max(step_end_times)


def main():
    # Configuration
    config = {
        "num_generations": 200,
        "num_parents_mating": 100,
        "sol_per_pop": 1000,  # Population size
        "num_genes": len(TASKS) * 2,
        "parent_selection_type": "tournament",
        "mutation_type": "random",
        "mutation_probability": 0.05,
        "init_range_low": 1,
        "init_range_high": max(len(TASKS), len(RESOURCES))
    }

    with alive_bar(config["num_generations"]) as bar:
        # Instance GA
        ga = pygad.GA(**config,
                      gene_type=int,
                      fitness_func=fitness,
                      on_generation=lambda _: bar())

        # Run the algorithm.
        ga.run()

    # Returning the details of the best solution
    solution, solution_fitness, _ = ga.best_solution()
    print("Best:", solution, "Time:", 1 / solution_fitness)

    steps = sorted(get_steps(solution), key=lambda step: step.position)
    step_groups = iter.groupby(steps, lambda step: step.position)
    print("Solution:")
    for pos, group in step_groups:
        step_descs = [f"{TASKS[step.task_num].name} ({RESOURCES[step.resource_num]})" for step in group]
        description = " and ".join(step_descs)
        print(f"{pos}. {description}")

    # ga.plot_fitness()


if __name__ == "__main__":
    main()
