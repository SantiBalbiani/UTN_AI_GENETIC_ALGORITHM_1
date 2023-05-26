from task_types import Task, Priority


TASKS = [
    Task(name="A", duration=10, priority=Priority.LOW, value=20),
    Task(name="B", duration=20, priority=Priority.HIGH, value=30),
    Task(name="C", duration=30, priority=Priority.CRITICAL, value=20),
    Task(name="D", duration=10, priority=Priority.MEDIUM, value=10),
    Task(name="E", duration=15, priority=Priority.MEDIUM, value=20),
    Task(name="F", duration=25, priority=Priority.LOW, value=10),
    Task(name="G", duration=10, priority=Priority.LOW, value=15),
]


CONSTANTS = {
    "MAX_DURATION": 40,
    "K_PRIORITY": 1,
    "VALUE_TIME_COST": 0.1
}


CONFIGS = {
    "Tournament - Random": {
        "num_generations": 200,
        "num_parents_mating": 100,
        "sol_per_pop": 1000,  # Population size
        "num_genes": len(TASKS),
        "parent_selection_type": "tournament",
        "mutation_type": "random",
        "mutation_probability": 0.05,
        "init_range_low": 0,
        "init_range_high": 2
    },

    "Steady-state Selection - Random": {
        "num_generations": 200,
        "num_parents_mating": 100,
        "sol_per_pop": 1000,  # Population size
        "num_genes": len(TASKS),
        "parent_selection_type": "sss",
        "mutation_type": "random",
        "mutation_probability": 0.05,
        "init_range_low": 0,
        "init_range_high": 2
    }
}
