from random import uniform
from math import exp
from copy import deepcopy
from destruction_rebuild import destruction_rebuild, ConstructionWeight
from variable_neighborhood_descent import VND

def LNS(instance, T0, SAMax, cooling_rate, betta_min, betta_max, RLC_length_in_percentage, alpha, print_execution = False):
    S = deepcopy(instance.current_solution)
    fo_S = instance.current_solution_fo
    S_best = deepcopy(S)
    fo_best = instance.current_solution_fo
    i = 0
    T = T0
    while T > 0.0001:
        while i < SAMax:
            i += 1
            S_neighbor, fo_neighbor = destruction_rebuild(instance, S, fo_S, fo_best, betta_min, betta_max, RLC_length_in_percentage, alpha)   
            delta = fo_neighbor - fo_S

            if delta <= 0:
                S = deepcopy(S_neighbor)
                fo_S = fo_neighbor
                instance.refresh(S, fo_S)
                if fo_neighbor < fo_best:
                    S_best = deepcopy(S_neighbor)
                    fo_best = fo_neighbor
                    instance.add_best_solution(fo_best, S_best)
            else:
                x = uniform(0, 1)
                if x < exp(-delta/T):                    
                    S = deepcopy(S_neighbor)    
                    fo_S = fo_neighbor 
                    instance.refresh(S, fo_S)
                  
        VND(instance, r=6)  
        fo_best, S_best = instance.best_solution()
        if print_execution == True: print(T, fo_S, fo_best)
        T = T * cooling_rate
        i = 0
        ConstructionWeight.weight = [0, 1, 2]

    return instance.best_solution()[0]





