from variable_neighborhood_descent import VND
from semi_greedy_construction import semi_greedy_construction
from random import randint
   
def is_better(instance, fo_best):
    return instance.current_solution_fo < fo_best or fo_best < 0

def GRASP(instance, GRASP_max, RLC_length_in_percentage, alpha_min, alpha_max, print_execution = False):
    fo_best = -1
    for i in range(GRASP_max):
        alpha = int((randint(alpha_min, alpha_max) / 100) * len(instance.points))
        
        semi_greedy_construction(instance, RLC_length_in_percentage, alpha)
        VND(instance, r=6) 
        
        if is_better(instance, fo_best):
            fo_best = instance.current_solution_fo

        if print_execution == True: print(i, instance.current_solution_fo, fo_best)

    return instance.best_solution()[0]

    





