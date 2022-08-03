# mTSP
This work was made during the course on metaheuristics at the federal university of são paulo (UNIFESP).
It was focused on learning to develop several metaheuristics to solve the multiple traveling salesman problem.

## How to run it?
- All instances available are in the folder "all_instances". Put the instances that you would like to run in the folder "running_instances".
- Running the script as follows: python3 main.py rounds(int) export_results_option(bin) print_rounds(bin) print_solution_option(bin) print_routes_option(bin) print_execution(bin) plot_solution_option(bin)

    - rounds(int): Indicates how many times the algorithm will be run.
    - export_results_option(bin): During execution, a csv file will be mounted with the results:
    
    ![image](https://user-images.githubusercontent.com/80294295/182500315-29171906-5075-4e6f-b447-fe7bda2b7161.png)
    
    ![image](https://user-images.githubusercontent.com/80294295/182500432-71d68e06-d743-46bf-a71f-0ff9f98f36f6.png)

    - print_rounds(bin): During execution will be printed a header indicating which round and which instance is running:
    
    ![image](https://user-images.githubusercontent.com/80294295/182500485-6ba40451-3dc0-4a2a-a385-fa6ecfe4e82b.png)

    - print_solution_option(bin): By the end of the execution, the best fo will be printed:
    
    ![image](https://user-images.githubusercontent.com/80294295/182500497-0a28a302-5094-4327-af39-bc5fc574be71.png)

    - print_routes_option(bin): By the end of the execution, the best routes will be printed:
    
    ![image](https://user-images.githubusercontent.com/80294295/182500514-7fcc7540-a34f-46ee-81d8-64eb737ad88f.png)

    - print_execution(bin):  During execution the partial results will be printed:
    
    ![image](https://user-images.githubusercontent.com/80294295/182500533-d9bcd611-85a0-4c2a-86da-5ce49a8c0018.png)

    - plot_solution_option(bin): By the end of the execution a graph will be made indicating the best route:
    
    ![image](https://user-images.githubusercontent.com/80294295/182500577-8b49ebdf-ead7-4790-b526-0bece0ea5a4d.png)
