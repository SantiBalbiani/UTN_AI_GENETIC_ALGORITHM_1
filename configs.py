from task_types import Task, Priority

TASKS = [
    Task(name="Task 1: Requirement Analysis",
         priority=Priority.CRITICAL, duration=5, value=10),
    Task(name="Task 2: System Design",
         priority=Priority.HIGH, duration=8, value=12),
    Task(name="Task 3: Database Setup",
         priority=Priority.MEDIUM, duration=4, value=8),
    Task(name="Task 4: User Interface Design",
         priority=Priority.HIGH, duration=6, value=9),
    Task(name="Task 5: Frontend Development",
         priority=Priority.CRITICAL, duration=10, value=15),
    Task(name="Task 6: Backend Development",
         priority=Priority.CRITICAL, duration=12, value=18),
    Task(name="Task 7: API Integration",
         priority=Priority.HIGH, duration=6, value=10),
    Task(name="Task 8: Testing and Quality Assurance",
         priority=Priority.HIGH, duration=8, value=12),
    Task(name="Task 9: Documentation",
         priority=Priority.MEDIUM, duration=4, value=6),
    Task(name="Task 10: Deployment and Release",
         priority=Priority.CRITICAL, duration=6, value=10),
    Task(name="Task 11: User Acceptance Testing",
         priority=Priority.HIGH, duration=5, value=9),
    Task(name="Task 12: Performance Optimization",
         priority=Priority.HIGH, duration=8, value=12),
    Task(name="Task 13: Security Analysis",
         priority=Priority.CRITICAL, duration=4, value=7),
    Task(name="Task 14: Error Handling",
         priority=Priority.MEDIUM, duration=6, value=8),
    Task(name="Task 15: System Maintenance",
         priority=Priority.MEDIUM, duration=8, value=12),
    Task(name="Task 16: Code Review",
         priority=Priority.HIGH, duration=4, value=7),
    Task(name="Task 17: Data Migration",
         priority=Priority.HIGH, duration=6, value=10),
    Task(name="Task 18: Release Notes",
         priority=Priority.MEDIUM, duration=3, value=5),
    Task(name="Task 19: Performance Testing",
         priority=Priority.CRITICAL, duration=8, value=12),
    Task(name="Task 20: System Documentation",
         priority=Priority.MEDIUM, duration=6, value=9),
    Task(name="Task 21: Requirement Gathering",
         priority=Priority.HIGH, duration=5, value=9),
    Task(name="Task 22: Prototyping",
         priority=Priority.MEDIUM, duration=7, value=10),
    Task(name="Task 23: Database Optimization",
         priority=Priority.CRITICAL, duration=9, value=14),
    Task(name="Task 24: UI/UX Testing",
         priority=Priority.HIGH, duration=6, value=10),
    Task(name="Task 25: Server Configuration",
         priority=Priority.CRITICAL, duration=7, value=11),
    Task(name="Task 26: Performance Monitoring",
         priority=Priority.HIGH, duration=5, value=8),
    Task(name="Task 27: Error Resolution",
         priority=Priority.MEDIUM, duration=6, value=9),
    Task(name="Task 28: Data Backup",
         priority=Priority.MEDIUM, duration=4, value=6),
    Task(name="Task 29: Scalability Planning",
         priority=Priority.HIGH, duration=8, value=12),
    Task(name="Task 30: Final Documentation",
         priority=Priority.MEDIUM, duration=5, value=8)
]


CONSTANTS = {
    "MAX_DURATION": 60,
    "K_PRIORITY": 1,
    "VALUE_TIME_COST": 0.1
}


CONFIGS = {
    "Tournament - Random": {
        "num_generations": 200,
        "num_parents_mating": 100,
        "sol_per_pop": 200,  # Population size
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
        "sol_per_pop": 200,  # Population size
        "num_genes": len(TASKS),
        "parent_selection_type": "sss",
        "mutation_type": "random",
        "mutation_probability": 0.05,
        "init_range_low": 0,
        "init_range_high": 2
    }
}
