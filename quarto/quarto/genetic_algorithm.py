import random
from quarto.objects import Player, Quarto
from copy import deepcopy
from quarto.utils import check_horizontal, check_vertical, check_diagonal
from typing import Callable
from quarto.hard_coded_players import *

class EvolvedHardCodedPlayer(Player):
    """Player using some evolving hard-coded rules"""
    def __init__(self, quarto: Quarto) -> None:
        super().__init__(quarto)
        self.genome= []
    
    def update_genome(self, genome) -> None:
        self.genome= genome

    def choose_piece(self) -> int:
        game= self.get_game()
        board_status= game.get_board_status()
        placed= []  # pieces already placed
        not_placed= []  # pieces have not been placed yet
        for j in range(game.BOARD_SIDE):
            for i in range(game.BOARD_SIDE):
                p= board_status[j, i]
                if p!= -1: # occupied position
                    placed.append(p)
        for i in range(16):
            if i not in placed:
                not_placed.append(i)
        for p in not_placed:
            for j in range(game.BOARD_SIDE):
                for i in range(game.BOARD_SIDE):
                    pos= board_status[j, i] # the value of the (j,i) position on the board
                    if pos== -1: 
                        tmp= deepcopy(game)
                        tmp.select(p) # select an element from the not placed yet list
                        tmp.place(i, j) # place the selected element in the (j, i) position; "swapped" because of the functions place and placeable in objects.py"
                        if(check_horizontal(tmp) % self.genome[0]== self.genome[1] or check_vertical(tmp) % self.genome[2]== self.genome[3] or check_diagonal(tmp) % self.genome[4]== self.genome[5]):
                            return p
        return random.randint(0, 15)

    def place_piece(self) -> tuple[int, int]:
        game= self.get_game()
        board_status= game.get_board_status()
        for j in range(game.BOARD_SIDE):
            for i in range(game.BOARD_SIDE):
                p= board_status[j, i] # the value of the (j,i) position on the board
                if p== -1: # free position
                    tmp= deepcopy(game)
                    tmp.place(i, j) # place the selected element in the (j, i) position; "swapped" because of the functions place and placeable in objects.py"
                    if(check_horizontal(tmp) % self.genome[6]== self.genome[7] or check_vertical(tmp)% self.genome[8]== self.genome[9] or check_diagonal(tmp)% self.genome[10]== self.genome[11]): 
                        return (i, j) # "swapped" because of the functions place and placeable in objects.py"
        return (random.randint(0, 3), random.randint(0, 3))

NUM_MATCHES_EVAL= 40
NUM_GENERATIONS= 200

def evaluate(strategy: Callable, game_ev) -> int:
    won_matches= 0
    challengers= ()
    for m in range(NUM_MATCHES_EVAL):
        game_ev.reset()
        if (m< NUM_MATCHES_EVAL/4):
            challengers = (strategy, HardCodedPlayer1(game_ev)) 
        elif(m>= NUM_MATCHES_EVAL/4 and m< 2*NUM_MATCHES_EVAL/4):
            challengers = (strategy, RandomPlayer(game_ev)) 
        elif(m>= 2*NUM_MATCHES_EVAL/4 and m< 3*NUM_MATCHES_EVAL/4):
            challengers = (strategy, HardCodedPlayer2(game_ev)) 
        else:
            challengers = (strategy, HardCodedPlayer0(game_ev))

        if m%2== 0:  # one time it starts first, another second
            game_ev.set_players((challengers[0], challengers[1]))
            winner= game_ev.run()
            if winner== 0:
                won_matches+= 1
        else:
            game_ev.set_players((challengers[1], challengers[0]))
            winner = game_ev.run()
            if winner== 1:
               won_matches+= 1    

    return won_matches  #this is the fitness: the number of won matches

def mutation(game: Quarto, genome: list):
    selected_gene_1= random.randrange(0, 6)*2
    selected_gene_2= selected_gene_1+1
    genome[selected_gene_1]= random.randrange(1, game.BOARD_SIDE+1)
    genome[selected_gene_2]= random.randrange(0, genome[selected_gene_1])
    return genome

def random_genome(game: Quarto):
    new_genome= []
    for i in range(12):
        if i%2== 0:
            new_genome.append(random.randrange(1, game.BOARD_SIDE+1))
        else:
            new_genome.append(random.randrange(0, new_genome[i-1]))
    return new_genome

def ganeration():
    chosen= tuple()
    max_fit= 0
    game= Quarto()
    evolved_player= EvolvedHardCodedPlayer(game)
    genome= random_genome(game)
    print(genome)
    evolved_player.update_genome(genome)

    for _ in range(NUM_GENERATIONS):
        genome = mutation(game, genome)
        evolved_player.update_genome(genome)
        f= evaluate(evolved_player, game)
        if(f > max_fit):
            max_fit= f
            chosen= genome
    evolved_player.update_genome(chosen)
    print("genome: ",chosen, "fitness: ", max_fit)