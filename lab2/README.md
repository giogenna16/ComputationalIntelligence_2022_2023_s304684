# Set Covering Problem with EA

## Personal Algorithm
This algorithm is obtained combining different techiques used in EA. It starts with an exploration (it finds a solution with a greedy algorithm), and then, it continues with the exploitation (try to find new better solutions changing a bit the previous). In particular, the exploitation is a mutation: remove a list from current the solution and add another list to it, with the following logic: 

1. remove the list with the maximum cost from the set of selected lists so far. The cost is calculated as the number of repetitions minus the number of new elemements of the considered list, w.r.t. the selected lists so far without the considered list (an heuristic)
2. add the list with the minimum cost from all the lists at disposal. The cost is caculated as the number of repetitions minus the number of new elemements of the considered list, w.r.t. the selected lists so far (already without the removed list)

To try not to get to a steady state right away, the algorithm cannot add the list just removed and it cannot remove the list just added.


Being a heuristic exploitation, it is not possile to know if, at the end of it, the selected lists are still a solution or not, so, if necessary, the algorithm continues with another exploration until it finds a solution.


## Genetic Algorithm
This algorithm is created along the lines of the code of the Professor Giovanni Squillero for the one-max problem. 

The logic used to order the population is the following: if a genome contains all the numbers from 0 to N-1, it comes first; if 1 number is missing to be a solution, it comes after the genome that contains all the numbers, but before the genome which has 2 missing numbers, and so on (hence, they are sorted in ascending order of missing numbers). If there are two genomes with the same number of missing numbers, the genome with the minimum weight comes first (hence, they are sorted in ascending order of weight). I used two types of cross-over and a mutation.

# Results
In the following table, there are the results, in terms of weight, obtained. It is possible to compare them with the updated results of the lab1 (present in its README.md file). If the results are ***computed in more than 5 minutes***, they are not presented. Mainly for the GA, the values of NUM_GENERATIONS, OFFSPRING_SIZE, POPULATION_SIZE are not fixed: they vary according to N, but without a precise proportionality (chosen with trial and error method); so, it is possible that different combinations of this numbers reach better results. The Ratio is the average proportion between the ones (the list is considered) and the zeros (the list is not considered) in the initial genomes; also this parameter is chosen by trial and error.

| N            | Personal Algorithm    |Genetic Algorithm| 
|--------------|-----------|------------|
| 5            |  w=5, NUM_GENERATIONS=100   |  w=5, NUM_GENERATIONS=100, OFFSPRING_SIZE=6, POPULATION_SIZE=10,   Ratio=1:1  |
| 10           |    w=10, NUM_GENERATIONS=100    |  w=11, NUM_GENERATIONS=100, OFFSPRING_SIZE=6, POPULATION_SIZE=10,  Ratio=1:1      |
| 15          |    w=20, NUM_GENERATIONS=100      |    w=21, NUM_GENERATIONS=100, OFFSPRING_SIZE=20, POPULATION_SIZE=30,    Ratio=1:1  |
| 20           |   w=27, NUM_GENERATIONS=100      |   w=26,    NUM_GENERATIONS=100, OFFSPRING_SIZE=30, POPULATION_SIZE=40,     Ratio=1:3     |
| 50           |     w=80, NUM_GENERATIONS=100    |   w=98, NUM_GENERATIONS=100, OFFSPRING_SIZE=20, POPULATION_SIZE=30,       Ratio=1:1  |
| 100          |       w=214, NUM_GENERATIONS=100   |   w=221, NUM_GENERATIONS=500, OFFSPRING_SIZE=20, POPULATION_SIZE=30,      Ratio=1:1   |
| 200           |      w=569, NUM_GENERATIONS=500      |      w=526, NUM_GENERATIONS=1000, OFFSPRING_SIZE=20, POPULATION_SIZE=30,  Ratio=1:50      |
| 500          |  w=1713,  NUM_GENERATIONS=1000        |   w=1630,  NUM_GENERATIONS=2000, OFFSPRING_SIZE=20, POPULATION_SIZE=30,    Ratio=1:1     |
| 1000           |  w=4295,  NUM_GENERATIONS=1000       |  w=3966,  NUM_GENERATIONS=1000, OFFSPRING_SIZE=20, POPULATION_SIZE=30,     Ratio=1:100    |
| 2000           |   w=10371,  NUM_GENERATIONS=100      |  w=9564,  NUM_GENERATIONS=1000, OFFSPRING_SIZE=20, POPULATION_SIZE=30,     Ratio=1:200   |
| 5000          |    w=30709,  NUM_GENERATIONS=50     |    w=28126,  NUM_GENERATIONS=1000, OFFSPRING_SIZE=20, POPULATION_SIZE=30, Ratio=1:400       |
| 10000          |        |     w=61745,  NUM_GENERATIONS=500, OFFSPRING_SIZE=20, POPULATION_SIZE=30,  Ratio=1:500    |
