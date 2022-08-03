from random import randint
from random import choice 
from copy import deepcopy
from instances import calculate_cost_remove
from semi_greedy_construction import greedy_random_construction, greedy_miope_construction, greedy_miope_restrict_construction

class ConstructionWeight:
    weight = [0, 1, 2]

def random_valid_route(S):
    route_index = randint(0, len(S) - 1)
    while len(S[route_index]) <= 2:        
        route_index = randint(0, len(S) - 1)

    return route_index

def remove_random(instance, S, fo, removed_points):    
    route_index = random_valid_route(S)
    point_index = randint(1, len(S[route_index]) - 1)
    point = S[route_index][point_index]
    removed_points.append(point['index'])
    cost = calculate_cost_remove(instance, S[route_index], point_index)
    fo += cost     
    S[route_index].remove(point)
   
    return S, fo 

def remove_worst(instance, S, fo, removed_points):
    worst = {
        'route_index': -1,
        'point_index': -1,
        'value': -1,
        'distance': -1
    }

    for i in range(len(S)):
        if len(S[i]) > 2:
            for j in range(1, len(S[i])): 
                cost = calculate_cost_remove(instance, S[i], j)
                if cost < worst['distance'] or worst['distance'] == -1:
                    worst['route_index'] = i
                    worst['point_index'] = j 
                    worst['value'] = S[i][j] 
                    worst['distance'] = cost 

    S[worst['route_index']].remove(worst['value'])    
    removed_points.append(worst['value']['index'])
    fo += worst['distance']
    
    return S, fo 

def readjust_weight(fo, fo_original, fo_best, option):    
    if fo < fo_original and fo > fo_best:
        ConstructionWeight.weight.append(option)
    if fo < fo_best:
        ConstructionWeight.weight.append(option)
        ConstructionWeight.weight.append(option)

def destruction_rebuild(instance, S, fo, fo_best, betta_min, betta_max, RLC_length_in_percentage, alpha): 
    fo_original = fo 
    S_copy = deepcopy(S)  

    disturbance_percentage = int((randint(betta_min, betta_max) / 100) * len(instance.points))
    removed_points = []
    for j in range(disturbance_percentage):                         
        option = randint(0, 1) # Sorteia uma das operações      
        if option == 0:
            S_copy, fo = remove_random(instance, S_copy, fo, removed_points) 
        else:
            S_copy, fo = remove_worst(instance, S_copy, fo, removed_points)

    option = choice(ConstructionWeight.weight) # Sorteia uma das operações  
    if option == 0:
        S_copy, fo = greedy_random_construction(instance, S_copy, fo, removed_points)  
    if option == 1:
        S_copy, fo = greedy_miope_construction(instance, S_copy, fo, removed_points)  
    if option == 2:
        S_copy, fo = greedy_miope_restrict_construction(instance, S_copy, fo, removed_points, RLC_length_in_percentage, alpha)    
    
    readjust_weight(fo, fo_original, fo_best, option)
   
    return S_copy, round(fo, 2)
