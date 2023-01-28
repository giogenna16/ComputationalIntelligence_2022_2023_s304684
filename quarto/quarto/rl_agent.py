import random
from quarto.objects import Player, Quarto
from copy import deepcopy
from quarto.utils import state_or_equivalent_in_G

class RenforcementLearningAgent(Player):
    def __init__(self, quarto: Quarto, alpha=0.15, random_factor=0.2) -> None:# 80% explore, 20% exploit
        super().__init__(quarto)
        self.state_history = []  # state, reward
        self.state_history_opponent= []
        self.alpha = alpha
        self.random_factor = random_factor
        self.G = {}

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
                        is_in, state_in_G= state_or_equivalent_in_G(tmp_board_t, self.G)
                        if is_in:     
                            average_reward+= self.G[state_in_G]
            # select the piece with the minimum average point, because it will be the piece for the opponent
            if average_reward<= minG:
                minG= average_reward
                chosen_piece= p

        if chosen_piece== None:
            chosen_piece= random.choice(not_placed)

        return chosen_piece
    
    def place_piece(self)-> tuple[int, int]:
        game= self.get_game()
        board_status= game.get_board_status()  
        
        # inizialize the reward of the state before you place piece, so after opponent's ply and save it in
        # the state history of the opponent
        board_status_t= list()
        for r in range(game.BOARD_SIDE):
            board_status_t+= board_status[r].tolist()
        board_status_t= tuple(board_status_t)
        is_in, state_in_G= state_or_equivalent_in_G(board_status_t, self.G)
        reward= self.get_reward() 
        if not is_in:
            self.G[board_status_t]= 0 
            self.update_state_history_opponent(board_status_t, reward)
        else:
            self.update_state_history_opponent(state_in_G, reward)
           
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
                is_in, state_in_G= state_or_equivalent_in_G(tmp_board_t, self.G)
                if not is_in:
                    if maxG< 0: # if the state with the chosen position is not in G and maxG is negative, set maxG to 0
                        maxG= 0
                        chosen_position= (board_pos[1], board_pos[0])
                else:
                    if self.G[state_in_G]>= maxG:
                        maxG= self.G[state_in_G]
                        chosen_position= (board_pos[1], board_pos[0])
        
        # inizialize the reward of the status with the chosen position and save it in your state history 
        tmp= deepcopy(game)
        tmp.place(chosen_position[0], chosen_position[1]) # place the selected element in the (j, i) position
        tmp_board_t= list()
        tmp_board= tmp.get_board_status()
        for r in range(tmp.BOARD_SIDE):
            tmp_board_t+= tmp_board[r].tolist()
        tmp_board_t= tuple(tmp_board_t)
        is_in, state_in_G= state_or_equivalent_in_G(tmp_board_t, self.G)
        reward= self.get_reward() 
        if not is_in:
            self.G[tmp_board_t]= 0 
            self.update_state_history(tmp_board_t, reward)
        else:
            self.update_state_history(state_in_G, reward)
        
        return chosen_position

    def get_reward(self, won= None):
        if won!= None: 
            if won== 1:
                return 3 # if the agent won
            elif won== 0:
                return -3 # if the agent lost  
            else:
                return 1  # on par    
        else:
            return 0 # if it is not the end of the match

    def update_state_history(self, state, reward):
        self.state_history.append((state, reward))
    
    def update_state_history_opponent(self, state, reward):
        self.state_history_opponent.append((state, reward))

    def learn(self):
        target = 0
        for prev, reward in reversed(self.state_history):
            self.G[prev] = self.G[prev] + self.alpha * (target - self.G[prev])
            target += reward
        target = 0
        for prev, reward in reversed(self.state_history_opponent):
            self.G[prev] = self.G[prev] + self.alpha * (target - self.G[prev])
            target += reward
        self.state_history = []
        self.state_history_opponent = []
        self.random_factor -= 10e-5  # decrease random factor each episode of play

