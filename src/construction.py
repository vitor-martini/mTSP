from random import sample
from copy import deepcopy

def sort_by_distance(e):
    return e['distance']

def create_solution(instance):    
    S = [[instance.points[0]] for item in range(instance.vehicles_quantity)] # Cria uma lista de listas baseado na quantidade de veículos    
    points = deepcopy(instance.points) # Lista de pontos
    del points[0] # Remove a garagem
    distances = [-1] * len(points) # Lista de distâncias dos pontos a garagem, a partir do ponto 1 (0 é a garagem)

    # Para cada ponto da lista de pontos
    for i in range(len(points)):
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
        points.remove(S[i][1]) # Retira o ponto da lista de pontos

    # Para cada ponto embaralhado da instância
    for point in sample(points, len(points)): 
        i = point['index']
        fos = []
        for j in range(len(S)): # Seleciona uma rota   
            last_point = S[j][-1]['index']
            depot = 0            
            value_of_fo = (instance.current_solution_fo_per_route[j] # FO atual daquela rota
                           + instance.matrix[last_point][i] # + Distância do último ponto da rota ao ponto atual
                           + instance.matrix[depot][i] # + Distância da garagem ao ponto atual
                           - instance.matrix[last_point][depot]) # - Distância do último ponto da rota a garagem            
            fos.append(round(value_of_fo, 2)) # Adiciona o valor encontrado na lista de FO's de rotas

        best_fo_value =  min(fos)  # Seleciona o melhor valor de FO
        route_index = fos.index(best_fo_value) # Seleciona o index da rota com menor FO
        instance.current_solution_fo_per_route[route_index] = best_fo_value # Atualiza o valor da FO da rota
        S[route_index].append(point) # Adiciona ponto a rota

    instance.current_solution_fo = round(sum(instance.current_solution_fo_per_route), 2) # Soma o FO de todas as rotas, formando o FO da solução
    instance.current_solution = S
    instance.add_best_solution(instance.current_solution_fo, S)
    
def create_test_solution(instance, i = 0):   
    if i == 0:
        S = [
            [{'index': 0, 'xy': [37.0, 52.0]}, {'index': 18, 'xy': [13.0, 13.0]}, {'index': 14, 'xy': [36.0, 16.0]}, {'index': 43, 'xy': [30.0, 15.0]}, {'index': 11, 'xy': [31.0, 32.0]}, {'index': 40, 'xy': [10.0, 17.0]}, {'index': 6, 'xy': [17.0, 63.0]}, {'index': 21, 'xy': [42.0, 57.0]}, {'index': 37, 'xy': [45.0, 35.0]}, {'index': 48, 'xy': [48.0, 28.0]}, {'index': 41, 'xy': [21.0, 10.0]}, {'index': 31, 'xy': [38.0, 46.0]}, {'index': 36, 'xy': [32.0, 22.0]}, {'index': 10, 'xy': [42.0, 41.0]}, {'index': 33, 'xy': [61.0, 33.0]}, {'index': 1, 'xy': [49.0, 49.0]}, {'index': 8, 'xy': [52.0, 33.0]}],
            [{'index': 0, 'xy': [37.0, 52.0]}, {'index': 12, 'xy': [5.0, 25.0]}, {'index': 13, 'xy': [12.0, 42.0]}, {'index': 22, 'xy': [16.0, 57.0]}, {'index': 25, 'xy': [27.0, 68.0]}, {'index': 24, 'xy': [7.0, 38.0]}, {'index': 42, 'xy': [5.0, 64.0]}, {'index': 7, 'xy': [31.0, 62.0]}, {'index': 26, 'xy': [30.0, 48.0]}, {'index': 5, 'xy': [21.0, 47.0]}, {'index': 16, 'xy': [27.0, 23.0]}, {'index': 46, 'xy': [25.0, 32.0]}, {'index': 20, 'xy': [62.0, 42.0]}, {'index': 9, 'xy': [51.0, 21.0]}, {'index': 32, 'xy': [46.0, 10.0]}, {'index': 38, 'xy': [59.0, 15.0]}, {'index': 44, 'xy': [39.0, 10.0]}, {'index': 39, 'xy': [5.0, 6.0]}, {'index': 3, 'xy': [20.0, 26.0]}],
            [{'index': 0, 'xy': [37.0, 52.0]}, {'index': 2, 'xy': [52.0, 64.0]}, {'index': 49, 'xy': [56.0, 37.0]}, {'index': 29, 'xy': [58.0, 27.0]}, {'index': 19, 'xy': [57.0, 58.0]}, {'index': 28, 'xy': [58.0, 48.0]}, {'index': 35, 'xy': [63.0, 69.0]}, {'index': 15, 'xy': [52.0, 41.0]}, {'index': 27, 'xy': [43.0, 67.0]}, {'index': 30, 'xy': [37.0, 69.0]}, {'index': 50, 'xy': [30.0, 40.0]}, {'index': 47, 'xy': [25.0, 55.0]}, {'index': 34, 'xy': [62.0, 63.0]}, {'index': 45, 'xy': [32.0, 39.0]}, {'index': 17, 'xy': [17.0, 33.0]}, {'index': 4, 'xy': [40.0, 30.0]}, {'index': 23, 'xy': [8.0, 52.0]}]
        ]   
        instance.current_solution_fo_per_route[0] = 419.54
        instance.current_solution_fo_per_route[1] = 435.57
        instance.current_solution_fo_per_route[2] = 412.36

    if i == 1:
        S = [[{'index': 0, 'xy': [37.0, 52.0]}, {'index': 50, 'xy': [30.0, 40.0]}, {'index': 46, 'xy': [25.0, 32.0]}, {'index': 16, 'xy': [27.0, 23.0]}, {'index': 43, 'xy': [30.0, 15.0]}, {'index': 32, 'xy': [46.0, 10.0]}, {'index': 44, 'xy': [39.0, 10.0]}, {'index': 14, 'xy': [36.0, 16.0]}, {'index': 36, 'xy': [32.0, 22.0]}, {'index': 11, 'xy': [31.0, 32.0]}, {'index': 45, 'xy': [32.0, 39.0]}, {'index': 26, 'xy': [30.0, 48.0]}], [{'index': 0, 'xy': [37.0, 52.0]}, {'index': 21, 'xy': [42.0, 57.0]}, {'index': 1, 'xy': [49.0, 49.0]}, {'index': 15, 'xy': [52.0, 41.0]}, {'index': 49, 'xy': [56.0, 37.0]}, {'index': 33, 'xy': [61.0, 33.0]}, {'index': 29, 'xy': [58.0, 27.0]}, {'index': 38, 'xy': [59.0, 15.0]}, {'index': 9, 'xy': [51.0, 21.0]}], [{'index': 0, 'xy': [37.0, 52.0]}, {'index': 31, 'xy': [38.0, 46.0]}, {'index': 10, 'xy': [42.0, 41.0]}, {'index': 37, 'xy': [45.0, 35.0]}, {'index': 4, 'xy': [40.0, 30.0]}, {'index': 48, 'xy': [48.0, 28.0]}, {'index': 8, 'xy': [52.0, 33.0]}, {'index': 20, 'xy': [62.0, 42.0]}, {'index': 28, 'xy': [58.0, 48.0]}, {'index': 19, 'xy': [57.0, 58.0]}, {'index': 34, 'xy': [62.0, 63.0]}, {'index': 35, 'xy': [63.0, 69.0]}, {'index': 2, 'xy': [52.0, 64.0]}, {'index': 27, 'xy': [43.0, 67.0]}, {'index': 30, 'xy': [37.0, 69.0]}, {'index': 25, 'xy': [27.0, 68.0]}, {'index': 6, 'xy': [17.0, 63.0]}, {'index': 22, 'xy': [16.0, 57.0]}, {'index': 42, 'xy': [5.0, 64.0]}, {'index': 23, 'xy': [8.0, 52.0]}, {'index': 13, 'xy': [12.0, 42.0]}, {'index': 24, 'xy': [7.0, 38.0]}, {'index': 12, 'xy': [5.0, 25.0]}, {'index': 40, 'xy': [10.0, 
        17.0]}, {'index': 39, 'xy': [5.0, 6.0]}, {'index': 18, 'xy': [13.0, 13.0]}, {'index': 41, 'xy': [21.0, 10.0]}, {'index': 3, 'xy': [20.0, 26.0]}, {'index': 17, 'xy': [17.0, 33.0]}, {'index': 5, 'xy': [21.0, 47.0]}, {'index': 47, 'xy': [25.0, 55.0]}, {'index': 7, 'xy': [31.0, 62.0]}]]

        instance.current_solution_fo_per_route[0] = 113.16
        instance.current_solution_fo_per_route[1] = 101.06
        instance.current_solution_fo_per_route[2] = 304.41

    if i == 2:
        S = [[{'index': 0, 'xy': [37.0, 52.0]}, {'index': 21, 'xy': [42.0, 57.0]}, {'index': 30, 'xy': [37.0, 69.0]}, {'index': 27, 'xy': [43.0, 67.0]}, {'index': 2, 'xy': [52.0, 64.0]}, {'index': 35, 'xy': [63.0, 69.0]}, {'index': 34, 'xy': [62.0, 63.0]}, {'index': 19, 'xy': [57.0, 58.0]}], [{'index': 0, 'xy': [37.0, 52.0]}, {'index': 47, 'xy': [25.0, 55.0]}, {'index': 7, 'xy': [31.0, 62.0]}, {'index': 25, 'xy': [27.0, 68.0]}, {'index': 6, 'xy': [17.0, 63.0]}, {'index': 22, 'xy': [16.0, 57.0]}, {'index': 42, 'xy': [5.0, 64.0]}, {'index': 23, 'xy': [8.0, 52.0]}, {'index': 13, 'xy': [12.0, 42.0]}, {'index': 24, 'xy': [7.0, 38.0]}, {'index': 12, 'xy': [5.0, 25.0]}, {'index': 40, 'xy': [10.0, 17.0]}, {'index': 39, 'xy': [5.0, 6.0]}, {'index': 18, 'xy': [13.0, 13.0]}, {'index': 41, 'xy': [21.0, 10.0]}, {'index': 3, 'xy': [20.0, 26.0]}, {'index': 17, 'xy': [17.0, 33.0]}, {'index': 5, 'xy': [21.0, 47.0]}], [{'index': 0, 'xy': [37.0, 52.0]}, {'index': 31, 'xy': [38.0, 46.0]}, {'index': 1, 
            'xy': [49.0, 49.0]}, {'index': 37, 'xy': [45.0, 35.0]}, {'index': 8, 'xy': [52.0, 33.0]}, {'index': 15, 'xy': [52.0, 41.0]}, {'index': 28, 'xy': [58.0, 48.0]}, {'index': 20, 'xy': [62.0, 42.0]}, {'index': 49, 'xy': [56.0, 37.0]}, {'index': 33, 'xy': [61.0, 33.0]}, {'index': 29, 'xy': [58.0, 27.0]}, {'index': 38, 'xy': [59.0, 15.0]}, {'index': 9, 'xy': [51.0, 21.0]}, {'index': 48, 'xy': [48.0, 28.0]}, {'index': 4, 'xy': [40.0, 30.0]}, {'index': 10, 'xy': [42.0, 41.0]}, {'index': 45, 'xy': [32.0, 39.0]}, {'index': 50, 'xy': [30.0, 40.0]}, {'index': 46, 'xy': [25.0, 32.0]}, {'index': 16, 'xy': [27.0, 23.0]}, {'index': 43, 'xy': [30.0, 15.0]}, {'index': 44, 'xy': [39.0, 10.0]}, {'index': 32, 'xy': [46.0, 10.0]}, {'index': 14, 'xy': [36.0, 16.0]}, {'index': 36, 'xy': [32.0, 22.0]}, 
            {'index': 11, 'xy': [31.0, 32.0]}, {'index': 26, 'xy': [30.0, 48.0]}]]
        instance.current_solution_fo_per_route[0] = 81.99
        instance.current_solution_fo_per_route[1] = 197.44
        instance.current_solution_fo_per_route[2] = 243.7

    if i == 3:
        S = [[{'index': 0, 'xy': [37.0, 52.0]}, {'index': 26, 'xy': [30.0, 48.0]}], [{'index': 0, 'xy': [37.0, 52.0]}, {'index': 21, 'xy': [42.0, 57.0]}], [{'index': 0, 'xy': [37.0, 52.0]}, {'index': 7, 'xy': [31.0, 62.0]}, {'index': 25, 'xy': [27.0, 68.0]}, {'index': 30, 'xy': [37.0, 69.0]}, {'index': 27, 'xy': [43.0, 67.0]}, {'index': 2, 'xy': [52.0, 64.0]}, {'index': 35, 'xy': [63.0, 69.0]}, {'index': 34, 'xy': [62.0, 63.0]}, {'index': 19, 'xy': [57.0, 58.0]}, {'index': 28, 'xy': [58.0, 48.0]}, {'index': 1, 'xy': [49.0, 49.0]}, {'index': 15, 'xy': [52.0, 41.0]}, {'index': 49, 'xy': [56.0, 37.0]}, {'index': 20, 'xy': [62.0, 42.0]}, {'index': 33, 'xy': [61.0, 33.0]}, {'index': 29, 'xy': [58.0, 27.0]}, {'index': 8, 'xy': [52.0, 33.0]}, {'index': 48, 'xy': [48.0, 28.0]}, {'index': 9, 'xy': [51.0, 21.0]}, {'index': 38, 'xy': [59.0, 15.0]}, {'index': 32, 'xy': [46.0, 10.0]}, {'index': 44, 'xy': [39.0, 10.0]}, {'index': 14, 'xy': [36.0, 16.0]}, {'index': 43, 'xy': [30.0, 15.0]}, {'index': 41, 'xy': [21.0, 10.0]}, {'index': 18, 'xy': [13.0, 13.0]}, {'index': 39, 'xy': [5.0, 6.0]}, {'index': 40, 'xy': [10.0, 17.0]}, {'index': 12, 'xy': [5.0, 25.0]}, {'index': 24, 'xy': [7.0, 38.0]}, {'index': 13, 'xy': [12.0, 42.0]}, {'index': 23, 'xy': [8.0, 52.0]}, {'index': 42, 'xy': [5.0, 64.0]}, {'index': 6, 'xy': [17.0, 63.0]}, {'index': 22, 'xy': [16.0, 57.0]}, {'index': 47, 'xy': [25.0, 55.0]}, {'index': 5, 'xy': [21.0, 47.0]}, {'index': 50, 'xy': [30.0, 40.0]}, {'index': 45, 'xy': [32.0, 39.0]}, {'index': 11, 'xy': [31.0, 32.0]}, {'index': 46, 'xy': [25.0, 32.0]}, {'index': 17, 'xy': [17.0, 33.0]}, {'index': 3, 'xy': [20.0, 26.0]}, {'index': 16, 
            'xy': [27.0, 23.0]}, {'index': 36, 'xy': [32.0, 22.0]}, {'index': 4, 'xy': [40.0, 30.0]}, {'index': 37, 'xy': [45.0, 35.0]}, {'index': 10, 'xy': [42.0, 41.0]}, {'index': 31, 'xy': [38.0, 46.0]}]]
        instance.current_solution_fo_per_route[0] = 16.12
        instance.current_solution_fo_per_route[1] = 14.14
        instance.current_solution_fo_per_route[2] = 415.71


    instance.current_solution_fo = sum(instance.current_solution_fo_per_route)  
    instance.current_solution = deepcopy(S)
    instance.add_best_solution(instance.current_solution_fo, S)

