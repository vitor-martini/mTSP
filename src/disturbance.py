from random import randint
from copy import deepcopy
from instances import calculate_cost_shift, calculate_cost_swap

def intra_route_swap(instance, S, route_index, point_one_index, point_one_value, point_two_index, point_two_value):   
    cost = calculate_cost_swap(instance, S[route_index], S[route_index], point_one_index, point_two_index)  
    S[route_index][point_one_index] = point_two_value    
    S[route_index][point_two_index] = point_one_value   
    return cost 
    
def intra_route_shift(instance, S, route_index, point_one_index, point_one_value, point_two_index):  
    cost = calculate_cost_shift(instance, S[route_index], S[route_index], point_one_index, point_two_index)
    S[route_index].remove(point_one_value)
    S[route_index].insert(point_two_index, point_one_value)
    return cost 

def inter_route_swap(instance, S, route_one_index, route_two_index, point_one_index, point_one_value, point_two_index, point_two_value):  
    cost = calculate_cost_swap(instance, S[route_one_index], S[route_two_index], point_one_index, point_two_index)   
    S[route_one_index][point_one_index] = point_two_value
    S[route_two_index][point_two_index] = point_one_value
    return cost 

def inter_route_shift(instance, S, route_one_index, route_two_index, point_one_index, point_one_value, point_two_index): 
    cost = calculate_cost_shift(instance, S[route_one_index], S[route_two_index], point_one_index, point_two_index)
    S[route_one_index].remove(point_one_value)
    S[route_two_index].insert(point_two_index, point_one_value)
    return cost 

def random_route(S):
    # Sorteia uma das rotas que tenha pelo menos dois pontos além da garagem
    route_index = randint(0, len(S) - 1)
    while len(S[route_index]) <= 2:
        route_index = randint(0, len(S) - 1)
    return route_index

def random_route_two(S, route_one_index):    
    route_two_index = route_one_index
    while(route_one_index == route_two_index):
        route_two_index = randint(0, len(S) - 1) # Sorteia uma rota, diferente da primeira
    return route_two_index

def random_point(point_one_index, S, route_index):
    point_two_index = point_one_index
    while point_two_index == point_one_index:
        point_two_index = randint(1, len(S[route_index]) - 1) # Sorteia um outro ponto, diferente do primeiro     
    point_two_value = S[route_index][point_two_index]
    return point_two_index, point_two_value

def inter_route_shift_is_valid(S, route_index):
    return len(S[route_index]) > 2

def random_neighbor(instance, S, current_fo):    
    S_copy = deepcopy(S)
    route_one_index = random_route(S)
    point_one_index = randint(1, len(S[route_one_index]) - 1) # Sorteia um ponto da rota selecionada
    point_one_value = S[route_one_index][point_one_index]    
    option = randint(0, 3) # Sorteia uma das operações

    # Intra rota
    if option <= 1: 
        point_two_index, point_two_value = random_point(point_one_index, S, route_one_index) 
        if abs(point_one_index - point_two_index) == 1:
            option = 0
            
        if option == 0:
            current_fo += intra_route_swap(instance, S_copy, route_one_index, point_one_index, point_one_value, point_two_index, point_two_value)
            
        if option == 1:
            current_fo += intra_route_shift(instance, S_copy, route_one_index, point_one_index, point_one_value, point_two_index)            

    # Inter rota
    if option > 1:
        route_two_index = random_route_two(S, route_one_index) 
        point_two_index = randint(1, len(S[route_two_index]) - 1) # Sorteia um ponto da rota 2  
        point_two_value = S[route_two_index][point_two_index]  
        
        if inter_route_shift_is_valid(S_copy, route_one_index) == False:
            option = 2        

        if option == 2:
            current_fo += inter_route_swap(instance, S_copy, route_one_index, route_two_index, point_one_index, point_one_value, point_two_index, point_two_value)

        if option == 3:
            current_fo += inter_route_shift(instance, S_copy, route_one_index, route_two_index, point_one_index, point_one_value, point_two_index)

    return S_copy, round(current_fo, 2)
