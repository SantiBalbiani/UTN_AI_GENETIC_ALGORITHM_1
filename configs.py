from task_types import Task, Priority


TASKS = [
    Task(name="A", duration=10, priority=Priority.LOW, value=20),
    Task(name="B", duration=20, priority=Priority.HIGH, value=30),
    Task(name="C", duration=30, priority=Priority.CRITICAL, value=20),
    Task(name="D", duration=10, priority=Priority.MEDIUM, value=10),
    Task(name="E", duration=15, priority=Priority.MEDIUM, value=20),
    Task(name="F", duration=25, priority=Priority.LOW, value=10),
    Task(name="G", duration=10, priority=Priority.LOW, value=15),
    Task(name="H", duration=10, priority=Priority.MEDIUM, value=10),
    Task(name="I", duration=15, priority=Priority.MEDIUM, value=20),
    Task(name="J", duration=25, priority=Priority.LOW, value=10),
    Task(name="K", duration=10, priority=Priority.LOW, value=15),
    Task(name="L", duration=10, priority=Priority.LOW, value=20),
    Task(name="M", duration=20, priority=Priority.HIGH, value=30),
    Task(name="N", duration=30, priority=Priority.CRITICAL, value=20),
    Task(name="O", duration=10, priority=Priority.MEDIUM, value=10),
    Task(name="P", duration=15, priority=Priority.MEDIUM, value=20),
    Task(name="Q", duration=25, priority=Priority.LOW, value=10),
    Task(name="R", duration=10, priority=Priority.LOW, value=15),
    Task(name="S", duration=10, priority=Priority.MEDIUM, value=10),
    Task(name="T", duration=15, priority=Priority.MEDIUM, value=20),
    Task(name="U", duration=25, priority=Priority.LOW, value=10),
    Task(name="V", duration=10, priority=Priority.LOW, value=15),
]


CONSTANTS = {
    "MAX_DURATION": 60,
    "K_PRIORITY": 1,
    "VALUE_TIME_COST": 0.1
}


CONFIGS = {
    "Tournament - Random": {
        "num_generations": 50,
        "num_parents_mating": 10,
        "sol_per_pop": 10,  # Population size
        "num_genes": len(TASKS),
        "parent_selection_type": "tournament",
        "mutation_type": "random",
        "mutation_probability": 0.05,
        "init_range_low": 0,
        "init_range_high": 2
    },

    "Steady-state Selection - Random": {
        "num_generations": 50,
        "num_parents_mating": 10,
        "sol_per_pop": 10,  # Population size
        "num_genes": len(TASKS),
        "parent_selection_type": "sss",
        "mutation_type": "random",
        "mutation_probability": 0.05,
        "init_range_low": 0,
        "init_range_high": 2
    }
}
