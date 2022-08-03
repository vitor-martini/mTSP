from local_search import inter_route_swap, inter_route_shift, intra_route_shift, intra_route_swap, intra_route_2opt

def VND(instance, r):
    fo_best, best_S = instance.best_solution()
    fo_S = fo_best
    k = 1
    
    while k <= r:        
        fo_initial = fo_S
        if k >= 1:                    
            intra_route_swap(instance, instance.current_solution)        
        if k >= 2:                    
            intra_route_shift(instance, instance.current_solution)      
        if k >= 3:                    
            intra_route_2opt(instance, instance.current_solution)      
        if k >= 4:                    
            inter_route_shift(instance, instance.current_solution)       
        if k >= 5:                    
            inter_route_swap(instance, instance.current_solution)  
        if k == 6:                    
            intra_route_2opt(instance, instance.current_solution)   

        fo_S = instance.current_solution_fo

        if fo_S < fo_best:
            fo_best = fo_S
            k = 1
        else:
            k+=1      


