from random import choice 
from copy import deepcopy

def sort_by_distance(e):
    return e['distance']

def sort_by_fo(e):
    return e['cost']

def generate_candidates(instance):
    candidates = deepcopy(instance.points) # Todos os pontos
    del candidates[0] # Exclui a garagem    
    S = [[instance.points[0]] for item in range(instance.vehicles_quantity)] # Cria uma lista de listas baseado na quantidade de veículos
    distances = [-1] * len(candidates) # Lista de distâncias dos pontos a garagem, a partir do ponto 1 (0 é a garagem)

    # Para cada ponto da lista de pontos
    for i in range(len(candidates)):
        element = {
                    'distance': instance.matrix[0][i + 1] + instance.matrix[i + 1][0], # Distancia a garagem
                    'point': instance.points[i + 1]
                  }
        distances[i] = element
    
    distances.sort(key=sort_by_distance) # Organiza a lista pelas distâncias de forma crescente

    # Para cada rota da solução
    for i in range(len(S)):
        S[i].append(distances[0]['point']) # Adiciona o menor ponto
        instance.current_solution_fo_per_route[i] = round(distances[0]['distance'], 2)
        del distances[0] # Retira o menor ponto da lista
        candidates.remove(S[i][1]) # Retira o ponto da lista de pontos

    return S, candidates, []

def get_random_candidate(RCL, RLC_length_in_percentage, alpha):
    RCL.sort(key=sort_by_fo)     
    best_candidate_values = RCL[0]
    best_candidate_cost = best_candidate_values['cost']
    worst_candidate_values = RCL[len(RCL) - 1]
    worst_candidate_cost = worst_candidate_values['cost']
    split_index = int(len(RCL) * RLC_length_in_percentage / 100)
    RCL = RCL[:split_index] # Dimunui o tamanho da lista para apenas (RLC_length_in_percentage)%
    condition = best_candidate_cost + alpha * (worst_candidate_cost - best_candidate_cost)

    for item in RCL:
        if (item['cost'] <= condition) == False:
            RCL.remove(item)

    return choice(RCL)

def get_min_candidate(RCL):
    RCL.sort(key=sort_by_fo)     
    return RCL[0]

def calculate_cost(instance, route, point_index, candidate_index, route_length):
    cost = instance.matrix[route[point_index]['index']][candidate_index] # Custo do ponto até o candidato

    if point_index == route_length - 1: # Se o ponto selecionado é o último da lista
        cost += instance.matrix[candidate_index][0] # + Distância do candidato a garagem
        cost -= instance.matrix[route[point_index]['index']][0] # - Distância do ponto corrente a garagem         
    else:
        cost += instance.matrix[candidate_index][route[point_index + 1]['index']] # + Distância do candidato ao próximo ponto
        cost -= instance.matrix[route[point_index]['index']][route[point_index + 1]['index']]# - Distância do ponto corrente ao próximo ponto
    
    return round(cost, 2)

def candidate_values(cost, candidate, route_index, point_index):
    candidate_values = {}
    candidate_values['cost'] = cost
    candidate_values['candidate'] = candidate
    candidate_values['route_index'] = route_index
    candidate_values['point_index'] = point_index

    return candidate_values

def add_candidate_to_route(instance, selected_candidate_values, S, semi_greedy_construction = False):
    selected_candidate = selected_candidate_values['candidate']
    selected_candidate_route = selected_candidate_values['route_index']
    selected_candidate_cost = selected_candidate_values['cost']
    selected_candidate_new_index = selected_candidate_values['point_index'] + 1 
    if semi_greedy_construction == True : instance.current_solution_fo_per_route[selected_candidate_route] += selected_candidate_cost
    S[selected_candidate_route].insert(selected_candidate_new_index, selected_candidate) # Adiciona candidato na solução    
           
def remove_candidate(selected_candidate_values, candidates):    
    candidate = selected_candidate_values['candidate']
    candidates.remove(candidate) # Remove da lista de candidatos

def greedy_random_construction(instance, S, fo, candidates):  
    while len(candidates) > 0: # Enquanto houver candidatos
        candidate = choice(candidates)
        candidates.remove(candidate)
        candidate = instance.points[candidate]
        RCL = []

        for i in range(len(S)): # Para cada rota
            route_length = len(S[i])
            for j in range(route_length): # Para cada ponto da rota
                cost = calculate_cost(instance, S[i], j, candidate['index'], route_length)                    
                RCL.append(candidate_values(cost, candidate, i, j))
            
        selected_candidate_values = get_min_candidate(RCL) 
        add_candidate_to_route(instance, selected_candidate_values, S)  
        fo += selected_candidate_values['cost']   
  
    return S, round(fo, 2)

def greedy_miope_construction(instance, S, fo, candidates): 
    while len(candidates) > 0: # Enquanto houver candidatos
        RCL = []
        for candidate in candidates: # Para cada candidato
            candidate = instance.points[candidate]
            for i in range(len(S)): # Para cada rota
                route_length = len(S[i])
                for j in range(route_length): # Para cada ponto da rota
                    cost = calculate_cost(instance, S[i], j, candidate['index'], route_length)                    
                    RCL.append(candidate_values(cost, candidate, i, j))
                        
        selected_candidate_values = get_min_candidate(RCL) 
        add_candidate_to_route(instance, selected_candidate_values, S)  
        candidates.remove(selected_candidate_values['candidate']['index'])   
        fo += selected_candidate_values['cost']   
  
    return S, round(fo, 2)

def greedy_miope_restrict_construction(instance, S, fo, candidates, RLC_length_in_percentage, alpha):
    while len(candidates) > 0: # Enquanto houver candidatos
        RCL = []
        for candidate in candidates: # Para cada candidato
            candidate = instance.points[candidate]
            for i in range(len(S)): # Para cada rota
                route_length = len(S[i])
                for j in range(route_length): # Para cada ponto da rota
                    cost = calculate_cost(instance, S[i], j, candidate['index'], route_length)                    
                    RCL.append(candidate_values(cost, candidate, i, j))
                        
        selected_candidate_values = get_random_candidate(RCL, RLC_length_in_percentage, alpha)
        add_candidate_to_route(instance, selected_candidate_values, S)  
        candidates.remove(selected_candidate_values['candidate']['index'])   
        fo += selected_candidate_values['cost']   
  
    return S, round(fo, 2)

def semi_greedy_construction(instance, RLC_length_in_percentage, alpha):    
    S, candidates, RCL = generate_candidates(instance) # Gera a lista de candidatos
    while len(candidates) > 0: # Enquanto houver candidatos
        for candidate in candidates: # Para cada candidato
            for i in range(len(S)): # Para cada rota
                route_length = len(S[i])
                for j in range(route_length): # Para cada ponto da rota
                    cost = calculate_cost(instance, S[i], j, candidate['index'], route_length)                    
                    RCL.append(candidate_values(cost, candidate, i, j))
            
        selected_candidate_values = get_random_candidate(RCL, RLC_length_in_percentage, alpha) 
        add_candidate_to_route(instance, selected_candidate_values, S, True)  
        remove_candidate(selected_candidate_values, candidates)      
        RCL.clear()

    instance.refresh(S)
    instance.add_best_solution(instance.current_solution_fo, S)