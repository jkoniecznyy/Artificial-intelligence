## The purpose of this project is to solve the Traveling Salesman Problem using Generic Algorithm

To do so, the program performs th following steps:
1. Load the distances between cities from a file
2. Create a distance list from given data
3. Initialize a population of random routes through all the cities
4. Calculate the fitness of each route
5. Perform a tournament or probability selection 
6. Perform a pmx crossover 
7. Perform an inversion or replace mutation
8. Repeat steps 4-7 for given amount of generations

## Features:
- The distances between the cities are loaded from a file
- You can choose the population size and the amount of generations
- You can specify how many times the algorith should run, starting from a new random population (launches)
- You cen specify how many steps should be displayed
  (for every step the program prints progress in % and the best score of current generation)
- You can choose the selection type and size
- You can choose the crossover probability, which decreases with every step until it reaches 40%
- You can choose and mutation type and probability, which decreases with every step until it reaches 0%
- At the end the program prints the best score and the best route, as well as how much time it took to find a final solution
