class Task:
    def __init__(self, name, priority, taskDuration, earnedValue):
        self.name = name
        self.priority = priority
        self.taskDuration = taskDuration
        self.valueAdded = earnedValue


tasks = [Task("limpiar casa", 3, 34, 23),
         Task("Hacer Tarea", 3, 34, 23),
         Task("Pasear al perro", 3, 34, 23),
         Task("Entregable Sprint 1", 3, 34, 23),
         Task("Clase de Danza", 3, 34, 1),
         Task("Reinvertir Obligación Negociable", 3, 3, 54),
         Task("Alimentar mascotas", 1, 10, 23),
         Task("Testear Entregable 1", 3, 34, 230),
         Task("Contactar Cliente", 3, 34, 23),
         Task("Cerrar Cuenta Bancaria", 3, 34, 23),
         Task("Turno con el médico", 1, 34, 23),
         Task("Enviar CV a potencial cliente", 3, 34, 23)]

task_durations = []
task_priorities = []
task_earnedValues = []
for task in tasks:
    task_durations.append(task.taskDuration)
    task_priorities.append(task.priority)
    task_earnedValues.append(task.priority)
