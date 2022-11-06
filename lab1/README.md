# Set Covering Problem
I tried to implement three different algorithms to find a solution for the Set Covering Problem:

1. A Greedy Algorithm
2. A Depth First Algorithm with heuristics
3. The A* Algorithm

## Greedy Algorithm
A sort of Greedy algorithm. The function used to implement this approach can be used to reach any ADMISSIBLE solution, if it can find one and if one exists: starting from the first list in the listOfLists (after ordering listOfLists in ascending order of length of the lists), it adds other lists if they contains the missing elements, until it finds a solution or until it explores all the lists (the first list is always selected). NO guarantees on the goodness of the solution: it can be the worst, it can be the best. 

## Depth First Algorithm with heuristics

A sort of depth first, but with some heuristics used to reduce the amount of considered combinations (explored nodes). The starting point of the algorithm is the first list of the listOfLists (after ordering listOfLists in ascending order of length of the lists); from this list, the procedure creates the combinations, that, I think, it is more clear to explain with an example. For instance, let's suppose to have 4 lists, already ordered and N=4: l1=[1], l2=[1,2], l3=[1,2], l4=[0,1,3]. It starts from l1 and creates as first concatenation l1-l2, then, normally, l1-l2-l3 and l1-l2-l3-l4, but in this case l1-l2-l3 does not add new numbers for finding the reached sequence, so it is discarded; thus, the created combination are l1-l2, l1-l2-l4. For every created concatenation, it verifies if this contains the reached sequence, in this case [0,1,2,3]; if so, the concatenation is saved. Subsequently, the algorithm keeps on with l2 and creates l2-l4 (not l2-l3 and l2-l3-l4, for the reason explained above) and again it verifies if this contains the reached sequence. Finally, the sequence l3-l4 is created. When it has all the selected combination, it chooses the one with the minimum weight, in this case l2-l4 or l3-l4, with w=5. I also added to the algorithm a bound to limit the execution time: when it has explored more than x number of nodes; it stops and selects the best combination so far.

## A* Algorithm
The code to develop this algorithm used is largely inspired to that of the Professor Giovanni Squillero for resolving the 8-puzzle problem and slighty modified to be adapted to this problem.
To calculate the estimated cost h, I used the difference between n and the lenght of the current state, all over 2, to try to do not overestimate the cost to reach the destination node.

## Results
If the results are ***computed in more than 5 minutes***, they are not listed below.
1. w1= weight of Greedy Algorithm
2. w2= weight of Depth First Algorithm with heuristics
3. w3= weight of A* Algorithm
#
1. nodes1= states explored by Greedy Algorithm
2. nodes2= states explored by  Depth First Algorithm with heuristics
3. nodes3= states explored by A* Algorithm
### N= 5
w1= 5, 
w2= 5, 
w3= 5
##
nodes1= 13, 
nodes2= 13,
nodes3= 32
### N= 10
w1= 13,
w2= 12,
w3= 10
##
nodes1= 14
nodes2= 1275
nodes3= 776
### N= 15
w1= 24,
w2= 20,
w3= 25
##
nodes1= 19,
nodes2= 1540,
nodes3= 9850
### N= 20
w1= 46,
w2= 33,
w3= 23
##
nodes1= 14,
nodes2= 595,
nodes3= 15767
### N= 50
w1= 137,
w2= 101
##
nodes1= 17, 
nodes2= 22791
### N= 100
w1= 332,
w2= 271
##
nodes1= 23,
nodes2= 50001 (the bound)
### N= 200
w1= 714,
w2= 653
##
nodes1= 28,
nodes2= 50001 (the bound)
### N= 500
w1= 2162
##
nodes1= 28
### N= 1000
w1= 4652
##
nodes1= 27



## Cooperations
I tried to develop ideas and possible solutions with Paolo Drago Leon, Diego Gasco, Enrico Magliano and Amine Hamdi, students of the course.
I developed the first two algorithms alone and the third with the big help of the code of the professor Giovanni Squillero, ad mentioned above.


# Algorithms Changes 

After received peer reviews, I decided to follow some advices, so I changed my code to try to improve the performances. 

In particular, I modified the Depth First Algorithm with heuristics: the logic is the same, but I apported some optimizations on the code to make it faster and to visit less nodes.

Moreover, I modified the A* Algorithm and particularly the heuristic, that now should be better than the previous one. The heuristics consists in  calculating the estimated cost as the number of repetitions minus the number of new elements of list to add, w.r.t. the numbers already selected so far. E.g., if N=5 and I already selected [0, 1, 3], the estimated cost of the list [0, 2] is repetitions(= 1) - new elements(= 1) = 0 and the estimated cost of the list [1, 0] is repetitions(= 2) - new elements(= 0) = 2.

In the table below, the new results are listed below (if the results are ***computed in more than 5 minutes***, they are not presented):

| N            | Greedy Algorithm     |Depth First Algorithm with heuristics | A* Algorithm|
|--------------|-----------|------------|------------|
| 5            |  w= 5, nodes=5        | w=5, nodes=13         |    w=5, nodes=32        |      
| 10           |  w= 15, nodes=13         | w=12, nodes=488      |     w=10, nodes=775       |
| 15           | w=24, nodes=17    |   w=20, nodes=528      |          w=17, nodes=9856    |
| 20           |  w=37, nodes=14  |     w=33, nodes=350    |       w=23, nodes=15853      |
| 50           |   w=147, nodes=23 |    w=101, nodes=2865      |            |
| 100          |   w=314, nodes=21  |    w=268, nodes=7542   |            |
| 200          |  w=677, nodes=26 |    w=585, nodes=14586    |            |
| 500          |  w=2436, nodes=28  |  w=1801, nodes=34651      |            |
| 1000         | w=4652, nodes=33  |      |            |
| 2000         | w=12169, nodes=38  |      |            |
| 5000         | w=35246, nodes=56  |      |            |
|10000         | w=73991, nodes=44  |      |            |
