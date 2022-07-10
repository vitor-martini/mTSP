from variable_neighborhood_descent import VND
from disturbance import random_neighbor
from random import randint 

def ILS(instance, betta_min, betta_max, ILS_max, print_execution = False):
    VND(instance, r=6)   
    fo, S = instance.best_solution()

    for i in range(ILS_max):
        disturbance_percentage = int((randint(betta_min, betta_max) / 100) * len(instance.points))
        for j in range(disturbance_percentage):                         
            S, fo = random_neighbor(instance, S, fo) 
            instance.refresh(S, fo)

        VND(instance, r=6)        
        fo, S = instance.best_solution()

        if print_execution == True: print(i, instance.current_solution_fo, fo)

    return instance.best_solution()[0]