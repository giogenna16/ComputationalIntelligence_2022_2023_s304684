# Lab 3 - NIM
### Task 3.1
For the first task, implemented in files *lab3_1.ipynb* and *lab3_1.py*, I wrote the code for my personal NIM-SUM optimal strategy (in *lab3_1.ipynb*) (before the Professor wrote his) and the code to play human vs computer (with my NIM-SUM optimal strategy or with the evolved strategy set for the NIM_SIZE=8: if you want to play with a different NIM_SIZE, the current parameters are no longer good: you have to generate new parameters (from the *lab3_2.ipynb*) for the selected NIM_SIZE).
### Task 3.2
For the second task, I implemented a sort of genetic algorithm to find the parameters (that are the genes of the genome) for an *evolved hardcoded strategy*.

Specifically, it generates a lot of genomes (the mutation, actually, is a randomic generation of a new genome). For each of the genomes, it makes an evaluation, that is the fitness of the genome. It gradually saves the best (the one with the highest fitness) genome so far. 

Again, the evaluation is used to evaluate a genome, so to compute its fitness: a genome is a tuple of 5 elements (genes) and these are used in 
the function *my_evolved_hard_coded* as parameters of equalities and inequalities, for instance: "if number of active rows is greater than
genome[0], do this", etc. 
In the evaluation, there are 10 matches, 5 in which the *my_evolved_hard_coded* starts first and 5 in which the *my_evolved_hard_coded* starts
second against 5 hard coded rules of different difficulties, so 2 match for each hard coded (doing more than 2 match for each hardcoded is
useless because doing one match in which one starts first and another in which the same starts second, covers all the possibilities, because
the hard coded used are not randomic).

Thus, I added four more hardcoded rules to those defined during lectures: *giovanni*, *reverse_gabriele*, *my_very_silly* and *my_smart*.

### Task 3.3
For the third task, I implemented an agent using MinMax (without and with Alpha-Beta pruning). The agent wins against the random agent and is on par with the optimal agent: the MinMax Agent is optimal.

Using the Alpha-Beta pruning slightly increases the performance in terms of speed, but already for NIM_SIZE=4 the computational time is very long.

### Task 3.4
For the fourth task, I implemented a Reinforcement Learning Agent which learns only when it wins against the opponent (I chose a random Agent). 


As mentioned, I decided to have it learn only from the moves that lead it to be the winner and not from the moves that lead him to lose.


As the matches played increase, the performances (number of won matches) increase, but it does not converge to the optimal strategy (It does not win all the matches)