import random
from quarto.objects import Player, Quarto
from copy import deepcopy
from quarto.utils import check_horizontal, check_vertical, check_diagonal

class MinMaxPlayer(Player):
    """MinMax player: IT IS THE PLAYER TO BE USED FOR THE TOURNAMENT!!!!!!!!!!"""
    """MinMax player: IT IS THE PLAYER TO BE USED FOR THE TOURNAMENT!!!!!!!!!!"""
    """MinMax player: IT IS THE PLAYER TO BE USED FOR THE TOURNAMENT!!!!!!!!!!"""

    def __init__(self, quarto: Quarto) -> None:
        super().__init__(quarto)
        self.maximizing= None
        self.threshold_min_max= 10

    def set_maximizing(self, bool): # this is used in the main, to set the variable based on wheter it is the Player 0 or the Player 1
        self.maximizing= bool
    
    def choose_piece(self) -> int:
        # the piece is chosen thanks to an hard-coded rule
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
        element_count= dict() # the keys are the not placed yet pieces, the values are the counts, as as explained below
        for p in not_placed:
            count= 0 
            for j in range(game.BOARD_SIDE):
                for i in range(game.BOARD_SIDE):
                    pos= board_status[j, i] # the value of the (j,i) position on the board
                    if pos== -1: # free position
                        tmp= deepcopy(game)
                        tmp.select(p) # select an element from the not placed yet list
                        tmp.place(i, j) # place the selected element in the (j, i) position; "swapped" because of the functions place and placeable in objects.py"
                        if(check_horizontal(tmp)== 4 or check_vertical(tmp)== 4 or check_diagonal(tmp)== 4): # check if placing the selected element in position (j, i) leads to win the match; if so, decrease by 3 the count of the p element
                            count-= 3
                        elif(check_horizontal(tmp)== 3 or check_vertical(tmp)== 3 or check_diagonal(tmp)== 3): # check if placing the selected element in position (j, i) leads to have at least a sequence; if so, increase by 1 the count of the p element (to give more weight to the placings that lead to win the match)
                            count+= 1
            element_count[p]= count
        # return the element with the maximum count, so the element which will most favor us and disadvantage the opponent
        return max(element_count, key= lambda x: element_count[x])

    def place_piece(self) -> tuple[int, int]:
        game= self.get_game()
        board_status= game.get_board_status()
        num_free= 0
        for j in range(game.BOARD_SIDE):
            for i in range(game.BOARD_SIDE):
                p= board_status[j, i]
                if p== -1: # occupied position
                    num_free+= 1
        if num_free<= self.threshold_min_max: # if there are less than threshold free position do the Min Max, else do an Hard Coded Rule (the same of HardCodedPlayer0)
            (i, j), _= minmax(game, self.maximizing)
            return (i, j)
        else:
            positions_to_avoid= [] # a list of position which creates a sequence of three, position to avoid since they give advantage to the apponet
            for j in range(game.BOARD_SIDE):
                for i in range(game.BOARD_SIDE):
                    p= board_status[j, i] # the value of the (j,i) position on the board
                    if p== -1: # free position
                        tmp= deepcopy(game)
                        tmp.place(i, j) # place the selected element in the (j, i) position; "swapped" because of the functions place and placeable in objects.py"
                        if(check_horizontal(tmp)== 4 or check_vertical(tmp)== 4 or check_diagonal(tmp)== 4): # check if placing the selected element in position (j, i) leads to win the match; if so, choose the (j,i) position
                            return (i, j)  # "swapped" because of the functions place and placeable in objects.py"
                        elif(check_horizontal(tmp)== 3 or check_vertical(tmp)== 3 or check_diagonal(tmp)== 3): # check if placing the selected element in position (j, i) leads to create a sequence of three element; if 
                            positions_to_avoid.append((j, i))                                                     # so, add (j, i) to the position to avoid because it creates a favorable situation for the opponent        
            if len(positions_to_avoid)== num_free: # all the possible positions are "to avoid", choose randomly
                return (random.randint(0, 3), random.randint(0, 3))
            else:
                r= (random.randint(0, 3), random.randint(0, 3))
                while r in positions_to_avoid: 
                    r= (random.randint(0, 3), random.randint(0, 3))
                return (r[1], r[0]) # choose a position which is not to avoid; "swapped" because of the functions place and placeable in objects.py"




def eval_state(game):
    if not game.check_finished() and game.check_winner()< 0: # the match is not finished yet
        return 0
    else:
        if game.check_winner()== 0: 
            return 1 
        else: 
            return -1 

def minmax(game, maximizing, alpha= -1, beta= 1):
    val= eval_state(game)
    if val!= 0:
        return None, val
    board_status= game.get_board_status()
    best_place= ()
    if maximizing:
        best= -1
        for j in range(game.BOARD_SIDE):
            for i in range(game.BOARD_SIDE):
                p= board_status[j, i] 
                if p== -1: # free position
                    tmp= deepcopy(game)
                    tmp.place(i, j)
                    _, val= minmax(tmp, maximizing, alpha, beta)
                    if best<= -val:
                        best_place= (i, j)
                        best= -val
                    alpha= max(alpha, best)
                    if beta<= alpha: #pruning
                        break
        return  best_place, best
    else:
        best= 1
        for j in range(game.BOARD_SIDE):
            for i in range(game.BOARD_SIDE):
                p= board_status[j, i]
                if p== -1: # free position
                    tmp= deepcopy(game)
                    tmp.place(i, j)
                    _, val= minmax(tmp, maximizing, alpha, beta)
                    if best>= -val:
                        best_place= (i, j)
                        best= -val
                    beta= min(beta, best)
                    if beta<= alpha: #pruning
                        break
        return best_place, best    
