# Lab 3 - NIM
### Task 3.1
For the first task, implemented in files *lab3_1.ipynb* and *lab3_1.py*, I wrote the code for my personal NIM-SUM optimal strategy (in *lab3_1.ipynb*) (before the Professor wrote his) and the code to play human vs computer (currently with the NIM-SUM optimal strategy, but it is possible to add the function for other strategies, for instance those of the Task 3.2).
### Task 3.2
For the second task, I implemented a sort of genetic algorithm to find the parameters (that are the genes of the genome) for an *evolved hardcoded strategy*.

 Specifically, It generates a lot of genomes and for each it makes an evaluation that is the fitness of the genome; at the end, the best genome found is chosen (the one with the highest fitness). 

Again, the evaluation is used to evaluate a genome, so to compute its fitness: a genome is a tuple of 5 elements (genes) and these are used in 
the function *my_evolved_hard_coded* as parameters of equalities and inequalities, for instance: "if number of active rows is greater than
genome[0], do this", etc. 
In the evaluation, there are 10 matches, 5 in which the *my_evolved_hard_coded* starts first and 5 in which the *my_evolved_hard_coded* starts
second against 5 hard coded rules of different difficulties, so 2 match for each hard coded (doing more than 2 match for each hardcoded is
useless because doing one match in which one starts first and another in which the same starts second, covers all the possibilities, because
the hard coded used are not randomic).

Thus, I added four more hardcoded rules to those defined during lectures: *giovanni*, *reverse_gabriele*, *my_very_silly* and *my_smart*.