# Code from the Artificial Intelligence classes
## The purpose of this program is to solve the Traveling Salesman Problem using Genetic Algorithm

To do so, the program performs th following steps:
1. Load the distances between cities from a file
2. Create a distance list from given data
3. Initialize a population of random routes through all the cities
4. Calculate the length of each route
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


## Example:
### Input: 
```
13 # number of cities
0  # distance from city 0 to city 0
666 0 # distance from city 1 to city 0 and 1
281 649 0 
396 1047 604 0 
291 945 509 104 0 
326 978 543 70 35 0 
641 45 611 1026 924 957 0 
427 956 308 525 471 492 918 0 
600 1135 486 611 584 596 1096 183 0 
561 1133 487 534 513 523 1096 180 83 0 
1041 1639 1267 663 761 726 1627 1145 1166 1083 0 
655 1259 891 294 382 349 1245 812 874 792 387 0 
975 1440 1248 711 769 744 1440 1234 1317 1237 443 452 0 
```
### Output:
```
0% done, generation best score: 6123
20% done, generation best score: 4564
40% done, generation best score: 4564
60% done, generation best score: 4564
80% done, generation best score: 4564
Solution:
9-10-12-11-3-5-4-0-1-6-2-7-8 4564
Time: 8.69 sec
```
