from instances import import_instances, export_results
from construction import create_solution
from simulated_annealing import SA
from grasp import GRASP 
from iterated_local_search import ILS
from variable_neighborhood_search import VNS
from large_neighborhood_search import LNS
from sys import setrecursionlimit

def main():
    rounds = 1
    export_results_option = False 
    print_rounds = True
    print_solution_option = True
    print_routes_option = True
    print_execution = True 
    plot_solution_option = False  

    input_string = ('1 -> SA\n' +
                    '2 -> GRASP \n' +
                    '3 -> ILS\n' +
                    '4 -> VNS\n' +
                    '5 -> LNS\n')
    option = input(input_string)
    
    list_of_instance = import_instances()    
    
    for instance in list_of_instance:
        for j in range(rounds):            
            if print_rounds == True: print('======================== ' + str(j+1) + ' ' + instance.name + ' ========================'  + '\n')
            create_solution(instance) 
            if option == '1':
                MH = 'SA'
                result = SA(instance, T0=1000000, SAMax=200, cooling_rate=0.9, print_execution=print_execution)
            if option == '2':
                MH = 'GRASP'
                result = GRASP(instance, GRASP_max=500, RLC_length_in_percentage=20, alpha_min=1, alpha_max=3, print_execution=print_execution)   
            if option == '3':
                MH = 'ILS'
                result = ILS(instance, betta_min=5, betta_max=30, ILS_max=500, print_execution=print_execution)   
            if option == '4':
                MH = 'VNS'
                result = VNS(instance, r=12, VNS_max=500, print_execution=print_execution)   
            if option == '5':
                MH = 'LNS'
                result = LNS(instance, T0=10000, SAMax=50, cooling_rate=0.9, betta_min=5, betta_max=30, RLC_length_in_percentage=20, alpha=0.1, print_execution=print_execution)   
            else:
                exit 

            if print_solution_option == True: instance.print_solution(result, plot_solution_option)
            if print_routes_option == True: instance.print_routes(plot_solution_option)
            if export_results_option == True: export_results(list_of_instance, MH, j, result)
            instance.reset_solutions()                    

setrecursionlimit(1000000000)
main()