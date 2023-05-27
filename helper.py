from commons import task_durations
from commons import task_priorities
from commons import task_earnedValues
from commons import task_names

class Helper:
    
    def get_names(chromosomes):
        task_names_final = []
        for i, chromosome in enumerate(chromosomes):
            if chromosome == 1:
                task_names_final.append(task_names[i])
        return task_names_final


    def get_total(chromosome, attribute):
        task_final = []
        match attribute:
            case "task_durations":
                for i, chromosome in enumerate(chromosome):
                    if chromosome == 1:
                        task_final.append(task_durations[i])
            case "earned_value":
                for i, chromosome in enumerate(chromosome):
                    if chromosome == 1:
                        task_final.append(task_earnedValues[i])
            case "priorities":
                for i, chromosome in enumerate(chromosome):
                    if chromosome == 1:
                        task_final.append(task_priorities[i])
            case _:
                return None
        return sum(task_final)