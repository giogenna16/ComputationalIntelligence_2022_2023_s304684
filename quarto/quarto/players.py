import random
from quarto.objects import Player, Quarto
from copy import deepcopy

#------------------------------------------------------------------------------------------------------#


class HardCodedPlayer0(Player):
    """Player 0 using some hard-coded rules"""
    def __init__(self, quarto: Quarto) -> None:
        super().__init__(quarto)

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
        element_count= dict() #the keys are the not placed yet pieces, the values are the counts, as as explained below
        for p in not_placed:
            count= 0 
            for j in range(game.BOARD_SIDE):
                for i in range(game.BOARD_SIDE):
                    pos= board_status[j, i] # the value of the (j,i) position on the board
                    if pos== -1: # free position
                        tmp= deepcopy(game)
                        tmp.select(p) # select an element from the not placed yet list
                        tmp.place(i, j) # place the selected element in the (j, i) position; "swapped" because of the functions place and placeable in objects.py"
                        if(check_horizontal(tmp)!= 4 and check_vertical(tmp)!= 4 and check_diagonal(tmp)!= 4): # check if placing the selected element in position (j, i) leads to not win the match; if so, increase by the count of the p element
                            count+= 1 
            element_count[p]= count
        # return the element with the maximum count, so the element that the most of the times respect the 
        # condition "placing the selected element in position (j, i) leads to not win the match"
        return max(element_count, key= lambda x: element_count[x])

    def place_piece(self) -> tuple[int, int]:
        game= self.get_game()
        board_status= game.get_board_status()
        positions_to_avoid= [] # a list of position which creates a sequence of three, position to avoid since they give advantage to the apponet
        num_free= 0 # total number of available position
        for j in range(game.BOARD_SIDE):
            for i in range(game.BOARD_SIDE):
                p= board_status[j, i]
                if p== -1:
                    num_free+= 1
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


#-----------------------------------------------------------------------------------------------------#


class HardCodedPlayer1(Player):
    """Player1 using some hard-coded rules"""
    def __init__(self, quarto: Quarto) -> None:
        super().__init__(quarto)

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
                    if pos== -1: # free position
                        tmp= deepcopy(game)
                        tmp.select(p) # select an element from the not placed yet list
                        tmp.place(i, j) # place the selected element in the (j, i) position; "swapped" because of the functions place and placeable in objects.py"
                        if(check_horizontal(tmp)== 4 or check_vertical(tmp)== 4 or check_diagonal(tmp)== 4): # check if placing the selected element in position (j, i) leads to win the match; if so, return p element
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
                    if(check_horizontal(tmp)!= 4 and check_vertical(tmp)!= 4 and check_diagonal(tmp)!= 4): # check if placing the selected element in position (j, i) leads to not win the match; if so, choose the (j,i) position
                        return (i, j) # "swapped" because of the functions place and placeable in objects.py"
        return (random.randint(0, 3), random.randint(0, 3))
    


#-------------------------------------------------------------------------------------------------------#

class HardCodedPlayer2(Player):
    """Player2 using some hard-coded rules"""
    def __init__(self, quarto: Quarto) -> None:
        super().__init__(quarto)
    
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
                        if(check_horizontal(tmp) % 2!= 0 and check_vertical(tmp) % 2!= 0 and check_diagonal(tmp) % 2!= 0):
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
                    if(check_horizontal(tmp) % 2== 0 or check_vertical(tmp)% 2== 0 or check_diagonal(tmp)% 2== 0): 
                        return (i, j) # "swapped" because of the functions place and placeable in objects.py"
        return (random.randint(0, 3), random.randint(0, 3))


#-------------------------------------------------------------------------------------------------------#

class RenforcementLearningAgent(object):
    def __init__(self, quarto: Quarto, alpha=0.15, random_factor=0.2) -> None:# 80% explore, 20% exploit
        self.quarto = quarto
        self.state_history = []  # state, reward
        self.alpha = alpha
        self.random_factor = random_factor
        self.G = {(-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1) : 0} # the first status
       
    def get_game(self):
        return self.quarto

    def choose_piece(self)->  int:
        game= self.get_game()
        board_status= game.get_board_status()

        placed= []  # pieces already placed
        not_placed= []  # pieces have not been placed yet; in this case, they corresponds to the "allowed moves"
        minG = 10e15
        chosen_piece= None
        for j in range(game.BOARD_SIDE):
            for i in range(game.BOARD_SIDE):
                p= board_status[j, i]
                if p!= -1: # occupied position
                    placed.append(p)
        for i in range(16):
            if i not in placed:
                not_placed.append(i)

        if random.random() < self.random_factor:
            # if random number below random factor, choose random action
            chosen_piece= random.choice(not_placed)
        else:
            for p in not_placed:
                average_reward= 0 # for each p, in not_placed, so among the allowed pieces, compute the "average_reward", i.e. the sum of all the rewards of the states created placing p in all the different free positions
                for j in range(game.BOARD_SIDE):
                    for i in range(game.BOARD_SIDE):
                        pos= board_status[j, i] # the value of the (j,i) position on the board
                        if pos== -1: # free position
                            tmp= deepcopy(game)
                            tmp.select(p) # select an element from the not placed yet list
                            tmp.place(i, j) # place the selected element in the (j, i) position
                            tmp_board_t= list()
                            tmp_board= tmp.get_board_status()
                            for r in range(tmp.BOARD_SIDE):
                                tmp_board_t+= tmp_board[r].tolist()
                            tmp_board_t= tuple(tmp_board_t)
                            temp= None
                            if tmp_board_t not in self.G:
                                temp= 0
                                #self.G[tmp_board_t] = 0 #initialization
                            if temp== 0:
                                average_reward+= temp
                            else:     
                                average_reward+= self.G[tmp_board_t]
                # select the piece with the minimum average point, because it will be the piece for the opponent
                if average_reward<= minG:
                    minG= average_reward
                    chosen_piece= p
        return chosen_piece
    
    def place_piece(self)-> tuple[int, int]:
        game= self.get_game()
        board_status= game.get_board_status()        
        allowed_positions= []
        maxG = -10e15
        chosen_position= None
        for j in range(game.BOARD_SIDE):
            for i in range(game.BOARD_SIDE):
                p= board_status[j, i] # the value of the (j,i) position on the board
                if p== -1: # free position
                    allowed_positions.append((j, i))
        if random.random() < self.random_factor:
            # if random number below random factor, choose random action
            chosen_position= random.choice(allowed_positions)
            chosen_position= (chosen_position[1], chosen_position[0])
        else:
            for board_pos in allowed_positions:
                tmp= deepcopy(game)
                tmp.place(board_pos[1], board_pos[0]) # place the selected element in the (j, i) position
                tmp_board_t= list()
                tmp_board= tmp.get_board_status()
                for r in range(tmp.BOARD_SIDE):
                    tmp_board_t+= tmp_board[r].tolist()
                tmp_board_t= tuple(tmp_board_t)
                temp= None
                if tmp_board_t not in self.G:
                    temp= 0
                    #self.G[tmp_board_t] = 0 #initialization
                if temp== 0:
                    if temp>= maxG:
                        maxG= temp
                        chosen_position= (board_pos[1], board_pos[0])
                else:
                    if self.G[tmp_board_t]>= maxG:
                        maxG= self.G[tmp_board_t]
                        chosen_position= (board_pos[1], board_pos[0])
        
        # inizialize the reward of the status with the chosen position
        tmp= deepcopy(game)
        tmp.place(chosen_position[0], chosen_position[1]) # place the selected element in the (j, i) position
        tmp_board_t= list()
        tmp_board= tmp.get_board_status()
        for r in range(tmp.BOARD_SIDE):
            tmp_board_t+= tmp_board[r].tolist()
        tmp_board_t= tuple(tmp_board_t)
        if tmp_board_t not in self.G:
            self.G[tmp_board_t] = 0 
        reward= self.get_reward() 
        self.update_state_history(tmp_board_t, reward)

        return chosen_position

    def get_reward(self, winner= None):
        if winner != None: 
            if winner:
                return 1 # if the agent won
            else:
                return -1 # if the agent lost       
        else:
            return 0 # if it is not the end of the match

    def update_state_history(self, state, reward):
        self.state_history.append((state, reward))

    def learn(self):
        target = 0
        for prev, reward in reversed(self.state_history):
            self.G[prev] = self.G[prev] + self.alpha * (target - self.G[prev])
            target += reward
        self.state_history = []
        self.random_factor -= 10e-5  # decrease random factor each episode of play


#----------------------------------------------------------------------------------------------------------#

# Some UTILITY FUNCTIONS called by the Players                   

def check_horizontal(game): # verify if there is a winning horizontal sequence 
    game_board= game.get_board_status()         
    for i in range(game.BOARD_SIDE):
        high_values = [elem for elem in game_board[i] if elem >= 0 and game.get_piece_charachteristics(elem).HIGH]
        coloured_values = [elem for elem in game_board[i] if elem >= 0 and game.get_piece_charachteristics(elem).COLOURED]
        solid_values = [elem for elem in game_board[i] if elem >= 0 and game.get_piece_charachteristics(elem).SOLID]
        square_values = [elem for elem in game_board[i] if elem >= 0 and game.get_piece_charachteristics(elem).SQUARE]
        low_values = [elem for elem in game_board[i] if elem >= 0 and not game.get_piece_charachteristics(elem).HIGH]
        noncolor_values = [elem for elem in game_board[i] if elem >= 0 and not game.get_piece_charachteristics(elem).COLOURED]
        hollow_values = [elem for elem in game_board[i] if elem >= 0 and not game.get_piece_charachteristics(elem).SOLID]
        circle_values = [elem for elem in game_board[i] if elem >= 0 and not game.get_piece_charachteristics(elem).SQUARE]
        if len(high_values) == game.BOARD_SIDE or len(coloured_values) == game.BOARD_SIDE or len(solid_values) == game.BOARD_SIDE or len(square_values) == game.BOARD_SIDE or len(
            low_values) == game.BOARD_SIDE or len(noncolor_values) == game.BOARD_SIDE or len(hollow_values) == game.BOARD_SIDE or len(circle_values) == game.BOARD_SIDE:
            return 4 # winning situation
        elif len(high_values) == game.BOARD_SIDE-1 or len(coloured_values) == game.BOARD_SIDE-1 or len(solid_values) == game.BOARD_SIDE-1 or len(square_values) == game.BOARD_SIDE-1 or len(
                low_values) == game.BOARD_SIDE-1 or len(noncolor_values) == game.BOARD_SIDE-1 or len(hollow_values) == game.BOARD_SIDE-1 or len(circle_values) == game.BOARD_SIDE-1:
            return 3 # there is at least a sequence of three
        elif len(high_values) == game.BOARD_SIDE-2 or len(coloured_values) == game.BOARD_SIDE-2 or len(solid_values) == game.BOARD_SIDE-2 or len(square_values) == game.BOARD_SIDE-2 or len(
                low_values) == game.BOARD_SIDE-2 or len(noncolor_values) == game.BOARD_SIDE-2 or len(hollow_values) == game.BOARD_SIDE-2 or len(circle_values) == game.BOARD_SIDE-2:
            return 2 # there is at least a sequence of two
        elif len(high_values) == game.BOARD_SIDE-3 or len(coloured_values) == game.BOARD_SIDE-3 or len(solid_values) == game.BOARD_SIDE-3 or len(square_values) == game.BOARD_SIDE-3 or len(
                low_values) == game.BOARD_SIDE-3 or len(noncolor_values) == game.BOARD_SIDE-3 or len(hollow_values) == game.BOARD_SIDE-3 or len(circle_values) == game.BOARD_SIDE-3:
            return 1 # there is at least a sequence of one
        else:
            return 0

def check_vertical(game): # verify if there is a winning vertical sequence for the winning
    game_board= game.get_board_status()     
    for i in range(game.BOARD_SIDE):
        high_values = [elem for elem in game_board[:, i] if elem >= 0 and game.get_piece_charachteristics(elem).HIGH]
        coloured_values = [elem for elem in game_board[:, i] if elem >= 0 and  game.get_piece_charachteristics(elem).COLOURED]
        solid_values = [elem for elem in game_board[:, i] if elem >= 0 and  game.get_piece_charachteristics(elem).SOLID]
        square_values = [elem for elem in game_board[:, i] if elem >= 0 and  game.get_piece_charachteristics(elem).SQUARE]
        low_values = [elem for elem in game_board[:, i] if elem >= 0 and not  game.get_piece_charachteristics(elem).HIGH]
        noncolor_values = [elem for elem in game_board[:, i] if elem >= 0 and not  game.get_piece_charachteristics(elem).COLOURED]
        hollow_values = [elem for elem in game_board[:, i] if elem >= 0 and not  game.get_piece_charachteristics(elem).SOLID]
        circle_values = [elem for elem in game_board[:, i] if elem >= 0 and not  game.get_piece_charachteristics(elem).SQUARE]
        if len(high_values) == game.BOARD_SIDE or len(coloured_values) == game.BOARD_SIDE or len(solid_values) == game.BOARD_SIDE or len(square_values) == game.BOARD_SIDE or len(
            low_values) == game.BOARD_SIDE or len(noncolor_values) == game.BOARD_SIDE or len(hollow_values) == game.BOARD_SIDE or len(circle_values) == game.BOARD_SIDE:
            return 4 # winning situation
        elif len(high_values) == game.BOARD_SIDE-1 or len(coloured_values) == game.BOARD_SIDE-1 or len(solid_values) == game.BOARD_SIDE-1 or len(square_values) == game.BOARD_SIDE-1 or len(
                low_values) == game.BOARD_SIDE-1 or len(noncolor_values) == game.BOARD_SIDE-1 or len(hollow_values) == game.BOARD_SIDE-1 or len(circle_values) == game.BOARD_SIDE-1:
            return 3 # there is at least a sequence of three
        elif len(high_values) == game.BOARD_SIDE-2 or len(coloured_values) == game.BOARD_SIDE-2 or len(solid_values) == game.BOARD_SIDE-2 or len(square_values) == game.BOARD_SIDE-2 or len(
                low_values) == game.BOARD_SIDE-2 or len(noncolor_values) == game.BOARD_SIDE-2 or len(hollow_values) == game.BOARD_SIDE-2 or len(circle_values) == game.BOARD_SIDE-2:
            return 2 # there is at least a sequence of two
        elif len(high_values) == game.BOARD_SIDE-3 or len(coloured_values) == game.BOARD_SIDE-3 or len(solid_values) == game.BOARD_SIDE-3 or len(square_values) == game.BOARD_SIDE-3 or len(
                low_values) == game.BOARD_SIDE-3 or len(noncolor_values) == game.BOARD_SIDE-3 or len(hollow_values) == game.BOARD_SIDE-3 or len(circle_values) == game.BOARD_SIDE-3:
            return 1 # there is at least a sequence of one
        else:
            return 0
    

def check_diagonal(game): # verify if there is a winning diagonal sequence for the winning
    game_board= game.get_board_status()  
    high_values = []
    coloured_values = []
    solid_values = []
    square_values = []
    low_values = []
    noncolor_values = []
    hollow_values = []
    circle_values = []
    for i in range(game.BOARD_SIDE):
        if game_board[i, i] < 0:
            break
        if game.get_piece_charachteristics(game_board[i, i]).HIGH:
            high_values.append(game_board[i, i])
        else:
            low_values.append(game_board[i, i])
        if game.get_piece_charachteristics(game_board[i, i]).COLOURED:
            coloured_values.append(game_board[i, i])
        else:
            noncolor_values.append(game_board[i, i])
        if game.get_piece_charachteristics(game_board[i, i]).SOLID:
            solid_values.append(game_board[i, i])
        else:
            hollow_values.append(game_board[i, i])
        if game.get_piece_charachteristics(game_board[i, i]).SQUARE:
            square_values.append(game_board[i, i])
        else:
            circle_values.append(game_board[i, i])
    if len(high_values) == game.BOARD_SIDE or len(coloured_values) == game.BOARD_SIDE or len(solid_values) == game.BOARD_SIDE or len(square_values) == game.BOARD_SIDE or len(
            low_values) == game.BOARD_SIDE or len(noncolor_values) == game.BOARD_SIDE or len(hollow_values) == game.BOARD_SIDE or len(circle_values) == game.BOARD_SIDE:
        return 4 # winning situation
    elif len(high_values) == game.BOARD_SIDE-1 or len(coloured_values) == game.BOARD_SIDE-1 or len(solid_values) == game.BOARD_SIDE-1 or len(square_values) == game.BOARD_SIDE-1 or len(
                low_values) == game.BOARD_SIDE-1 or len(noncolor_values) == game.BOARD_SIDE-1 or len(hollow_values) == game.BOARD_SIDE-1 or len(circle_values) == game.BOARD_SIDE-1:
        return 3 # there is at least a sequence of three
    elif len(high_values) == game.BOARD_SIDE-2 or len(coloured_values) == game.BOARD_SIDE-2 or len(solid_values) == game.BOARD_SIDE-2 or len(square_values) == game.BOARD_SIDE-2 or len(
                low_values) == game.BOARD_SIDE-2 or len(noncolor_values) == game.BOARD_SIDE-2 or len(hollow_values) == game.BOARD_SIDE-2 or len(circle_values) == game.BOARD_SIDE-2:
        return 2 # there is at least a sequence of two
    elif len(high_values) == game.BOARD_SIDE-3 or len(coloured_values) == game.BOARD_SIDE-3 or len(solid_values) == game.BOARD_SIDE-3 or len(square_values) == game.BOARD_SIDE-3 or len(
                low_values) == game.BOARD_SIDE-3 or len(noncolor_values) == game.BOARD_SIDE-3 or len(hollow_values) == game.BOARD_SIDE-3 or len(circle_values) == game.BOARD_SIDE-3:
        return 1 # there is at least a sequence of one
    
    high_values = []
    coloured_values = []
    solid_values = []
    square_values = []
    low_values = []
    noncolor_values = []
    hollow_values = []
    circle_values = []
    for i in range(game.BOARD_SIDE):
        if game_board[i, game.BOARD_SIDE - 1 - i] < 0:
            break
        if game.get_piece_charachteristics(game_board[i, game.BOARD_SIDE - 1 - i]).HIGH:
            high_values.append(game_board[i, game.BOARD_SIDE - 1 - i])
        else:
            low_values.append(game_board[i, game.BOARD_SIDE - 1 - i])
        if game.get_piece_charachteristics(game_board[i, game.BOARD_SIDE - 1 - i]).COLOURED:
            coloured_values.append(game_board[i, game.BOARD_SIDE - 1 - i])
        else:
            noncolor_values.append(
                game_board[i, game.BOARD_SIDE - 1 - i])
        if game.get_piece_charachteristics(game_board[i, game.BOARD_SIDE - 1 - i]).SOLID:
            solid_values.append(game_board[i, game.BOARD_SIDE - 1 - i])
        else:
            hollow_values.append(game_board[i, game.BOARD_SIDE - 1 - i])
        if game.get_piece_charachteristics(game_board[i, game.BOARD_SIDE - 1 - i]).SQUARE:
            square_values.append(game_board[i, game.BOARD_SIDE - 1 - i])
        else:
            circle_values.append(game_board[i, game.BOARD_SIDE - 1 - i])
    if len(high_values) == game.BOARD_SIDE or len(coloured_values) == game.BOARD_SIDE or len(solid_values) == game.BOARD_SIDE or len(square_values) == game.BOARD_SIDE or len(
            low_values) == game.BOARD_SIDE or len(noncolor_values) == game.BOARD_SIDE or len(hollow_values) == game.BOARD_SIDE or len(circle_values) == game.BOARD_SIDE:
        return 4 # winning situation
    elif len(high_values) == game.BOARD_SIDE-1 or len(coloured_values) == game.BOARD_SIDE-1 or len(solid_values) == game.BOARD_SIDE-1 or len(square_values) == game.BOARD_SIDE-1 or len(
                low_values) == game.BOARD_SIDE-1 or len(noncolor_values) == game.BOARD_SIDE-1 or len(hollow_values) == game.BOARD_SIDE-1 or len(circle_values) == game.BOARD_SIDE-1:
        return 3 # there is at least a sequence of three
    elif len(high_values) == game.BOARD_SIDE-2 or len(coloured_values) == game.BOARD_SIDE-2 or len(solid_values) == game.BOARD_SIDE-2 or len(square_values) == game.BOARD_SIDE-2 or len(
                low_values) == game.BOARD_SIDE-2 or len(noncolor_values) == game.BOARD_SIDE-2 or len(hollow_values) == game.BOARD_SIDE-2 or len(circle_values) == game.BOARD_SIDE-2:
        return 2 # there is at least a sequence of two
    elif len(high_values) == game.BOARD_SIDE-3 or len(coloured_values) == game.BOARD_SIDE-3 or len(solid_values) == game.BOARD_SIDE-3 or len(square_values) == game.BOARD_SIDE-3 or len(
                low_values) == game.BOARD_SIDE-3 or len(noncolor_values) == game.BOARD_SIDE-3 or len(hollow_values) == game.BOARD_SIDE-3 or len(circle_values) == game.BOARD_SIDE-3:
        return 1 # there is at least a sequence of one
    else:
        return 0
    