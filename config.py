class Config:
    def __init__(self):
        self.TIME_LIMIT = 60
        self.POPULATION_SIZE = 200
        self.GENERATIONAL_LEAP = 0.5
        self.NUMBER_OF_GENERATIONS = 200
        self.MUTATION_PROBABILITY = 0.05
        RANDOM = "RANDOM"  # Random Binomial Crossover
        SINGLE_POINT = "SINGLE_POINT"  # Simple Crossover
        MASK = "MASK"  # Binomial Two-Point Crossover / Double Mask
        self.CROSSOVER_FUNCTION = SINGLE_POINT
        self.MASK_FIRST_CHILD = "XXYYXYXYXYXXYYXYXYXYXXYYXYXYXY"
        self.MASK_SECOND_CHILD = "YYXXYXYXYXYYXXYXYXYXYYXXYXYXYX"
        ROULETTE = "ROULETTE"
        TOURNAMENT = "TOURNAMENT"
        self.SELECTION_FUNCTION = ROULETTE
        self.MAX_SCORE = 99


CONFIG = Config()

# 0: Critic
# 1: High
# 2: Medium
# 3: Low

# Fitness
# Mas Earned Value AND  Higher priority AND less TaskDuration

# Cromosomas:
# Último cromosoma indica 0 "No la hago" 1 "Hago la tarea"
# Prioridad: 11
# Earned value: 255 111
# TaskDuration: Max 255:  111

#  Prioridad - Earned Value - Task Duration  - Include/not Include
#   11   -      111 -          111 -             1
