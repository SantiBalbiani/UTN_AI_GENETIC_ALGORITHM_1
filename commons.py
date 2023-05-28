class Task:
    # Duración en horas
    def __init__(self, name, priority, taskDuration, earnedValue):
        self.name = name
        self.priority = priority
        self.taskDuration = taskDuration
        self.valueAdded = earnedValue


tasks = [
    Task("Task 1: Requirement Analysis", 3, 5, 10),
    Task("Task 2: System Design", 2, 8, 12),
    Task("Task 3: Database Setup", 1, 4, 8),
    Task("Task 4: User Interface Design", 2, 6, 9),
    Task("Task 5: Frontend Development", 3, 10, 15),
    Task("Task 6: Backend Development", 3, 12, 18),
    Task("Task 7: API Integration", 2, 6, 10),
    Task("Task 8: Testing and Quality Assurance", 2, 8, 12),
    Task("Task 9: Documentation", 1, 4, 6),
    Task("Task 10: Deployment and Release", 3, 6, 10),
    Task("Task 11: User Acceptance Testing", 2, 5, 9),
    Task("Task 12: Performance Optimization", 2, 8, 12),
    Task("Task 13: Security Analysis", 3, 4, 7),
    Task("Task 14: Error Handling", 1, 6, 8),
    Task("Task 15: System Maintenance", 1, 8, 12),
    Task("Task 16: Code Review", 2, 4, 7),
    Task("Task 17: Data Migration", 2, 6, 10),
    Task("Task 18: Release Notes", 1, 3, 5),
    Task("Task 19: Performance Testing", 3, 8, 12),
    Task("Task 20: System Documentation", 1, 6, 9),
    Task("Task 21: Requirement Gathering", 2, 5, 9),
    Task("Task 22: Prototyping", 1, 7, 10),
    Task("Task 23: Database Optimization", 3, 9, 14),
    Task("Task 24: UI/UX Testing", 2, 6, 10),
    Task("Task 25: Server Configuration", 3, 7, 11),
    Task("Task 26: Performance Monitoring", 2, 5, 8),
    Task("Task 27: Error Resolution", 1, 6, 9),
    Task("Task 28: Data Backup", 1, 4, 6),
    Task("Task 29: Scalability Planning", 2, 8, 12),
    Task("Task 30: Final Documentation", 1, 5, 8)
]

task_durations = []
task_priorities = []
task_earnedValues = []
task_names = []
for task in tasks:
    task_durations.append(task.taskDuration)
    task_priorities.append(task.priority)
    task_earnedValues.append(task.valueAdded)
    task_names.append(task.name)

