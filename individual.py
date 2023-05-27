from commons import task_durations
from commons import task_priorities
from commons import task_earnedValues
from commons import task_names
from commons import tasks
from random import random
from random import randint
from config import CONFIG


class Individual:
    def __init__(self, chromosome=[]):
        if not chromosome:
            self.chromosome = []
            for i in range(len(tasks)):
                if random() <= 0.5:
                    self.chromosome.append(0)
                else:
                    self.chromosome.append(1)
        else:
            self.chromosome = chromosome

    def fitness(self):
        score = 0
        total_duration = 0
        total_value = 0
        total_priority = 0

        #max_duration = max(task.taskDuration for task in tasks)
        max_duration = CONFIG.TIME_LIMIT
        #max_priority = max(task.priority for task in tasks)
        max_priority = 4
        max_value = max(task.valueAdded for task in tasks)

        # Usarlo si tengo chromosomas compuestos
        #for gen_index in range(len(self.chromosome)):    
        # 1er idea de criterio para ponderar    
        #+ (CONFIG.MAX_SCORE - task_durations[gen_index]) + 999 if (
        #  task_priorities[gen_index] == 0) else task_priorities[gen_index]*10
        for gen_index in range(len(tasks)):
              if self.chromosome[gen_index] == 1:              
                total_value += task_earnedValues[gen_index]                 
                total_duration += task_durations[gen_index]
                total_priority += task_priorities[gen_index]
        
        normalized_duration = total_duration / max_duration
        normalized_priority = total_priority / max_priority
        normalized_value = total_value / max_value

        if total_duration >= CONFIG.TIME_LIMIT:
            score = 0
        else:
            score = normalized_priority + normalized_value - 0.1*normalized_duration # $1 por cada 10 hs 
        return score

    def get_chromosome(self):
        return self.chromosome