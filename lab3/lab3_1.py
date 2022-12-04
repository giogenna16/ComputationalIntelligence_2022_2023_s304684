import logging
import random 
from collections import namedtuple

Nimply = namedtuple("Nimply", "row, num_objects")

class Nim:
    def __init__(self, num_rows: int, k: int = None) -> None:
        self._rows = [i * 2 + 1 for i in range(num_rows)]
        self._k = k

    def __bool__(self):
        return sum(self._rows) > 0

    def __str__(self):
        return "<" + " ".join(str(_) for _ in self._rows) + ">"

    @property
    def rows(self) -> tuple:
        return tuple(self._rows)

    @property
    def k(self) -> int:
        return self._k

    def nimming(self, ply: Nimply) -> None:
        row, num_objects = ply
        assert self._rows[row] >= num_objects
        assert self._k is None or num_objects <= self._k
        self._rows[row] -= num_objects   

#---------------------------------------------------------------------------------#

def nim_sum(nim: Nim):
    temp= nim._rows.copy()
    row_number= -1
    nim_sum= 0 
    for r in nim._rows:
        nim_sum^= r  # '^' is the bitwise xor operator
    if nim_sum != 0:
        # the goal is to obtain a NIM_SUM equal to 0
        # greedy approach: the first solution reached is choosen (so the first move found that guarantees the bitwise 
        # xor equal to zero is chosen)
        for r in temp:
            row_number+= 1
            for i in range(r):
                j= i + 1 
                with_removal= temp.copy()
                with_removal.remove(r)
                res= r - j
                for e in with_removal:
                    res^= e 
                if res == 0: # the bitwise xor is equal to zero
                    nim.nimming(Nimply(row_number, j))
                    return
    else:
        # if it has arrived here, it means that there are not NIM_SUM solution (the NIM_SUM is already 0): the agent 
        # will remove a random number of object from a random row
        selected= random.choice([e for e in temp if e != 0])
        if selected > 1:
            to_remove= random.randrange(1, selected+1) 
        else:
            to_remove= 1
        row_number= temp.index(selected)
        nim.nimming(Nimply(row_number, to_remove))

#------------------------------------------------------------------------------#

# YOU vs THE AGENT
N= 5
x= Nim(N)
r= random.random()
if r > 0.5:
    p1_turn= True
else:
    p1_turn= False
rounds_number=0
print("Starting point", x._rows, "\n")
while(x):
    if(p1_turn):
        ok= False
        while not ok:
            print("Make your move: select the row and how many objects you want to remove from it!")
            print("Insert the row index (between 0 and N-1, in this case, between 0 and ", N-1, "):")
            ins1= input().strip()
            print("Insert the number of object you want to remove from the selected row:")
            ins2= input().strip()
            if(not ins1.isdigit() or not ins2.isdigit()):
                print("Only numbers are allowed!")
            elif(int(ins1)> N-1):
                print("The row index (the first number to insert) must be between 0 and N-1, in this case, between 0 and ", N-1, "!")
            elif(int(ins2)==0 or int(ins2)> x._rows[int(ins1)]):
                print("The number (the second number to insert) to of objects to be removed must be between 1 and the number of object contained in the considered row!")
            else:
                ok= True
                x.nimming(Nimply(int(ins1), int(ins2)))
                print("After your move", x._rows, "\n")
        rounds_number+=1
        p1_turn= False
    else:
        nim_sum(x)
        print("After p2 move", x._rows, "\n")
        rounds_number+=1
        p1_turn= True

if(not p1_turn):
    print("You won after ", rounds_number, " total moves!")   
else:
    print("Player 2 won (YOU LOST) after ", rounds_number, " total moves!")

  