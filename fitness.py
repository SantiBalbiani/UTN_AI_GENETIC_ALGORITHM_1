MAX_DURATION = 500

TASKS = {
    1: {"prioridad": 3, "duracion": 100, "valor": 10},
    2: {"prioridad": 2, "duracion": 100, "valor": 10},
    3: {"prioridad": 1, "duracion": 100, "valor": 10}
}

example = [1, 0, 1]

A, B = 10, 20


def fitness(chromosome):
    total_duration = 0
    for i in range(len(TASKS)):
        task = TASKS[i]
        if chromosome[i] == 1:
            total_duration += task["duration"]

    if total_duration > MAX_DURATION:
        return 0

    total_priority = 0
    for i in range(len(TASKS)):
        task = TASKS[i]
        if chromosome[i] == 1:
            total_priority += task["prioridad"]

    total_value = 0
    for i in range(len(TASKS)):
        task = TASKS[i]
        if chromosome[i] == 1:
            total_value += task["valor"]

    return A * total_priority + total_value - B * total_duration
