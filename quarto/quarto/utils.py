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


#-----------------------------------------------------------------------------------------------#

def ninghty_degree_rotation(state: tuple):
    # Rotation of 90 degrees
    rotated_state= [0]*len(state) # a list of 16 zeros
    dict_corr= {0: 12, 1: 8, 2: 4, 3: 0} # index matches for rotation
    for i in range(len(state)):
        for j in range(len(state)//4):
            if i%4== j:
                for k in range(len(state)//4):
                    if i//4== k:
                        rotated_state[dict_corr[j]+k]= state[i]  
    return tuple(rotated_state)

def state_or_equivalent_in_G(state: tuple, G: dict):
    # checks if the state or one of its rotations of 90, 180, 270 degrees 
    # (which are equivalent to it) is present in G
    ninghty_rotated_state= ninghty_degree_rotation(state)
    onehundredeighty_rotated_state= ninghty_degree_rotation(ninghty_rotated_state)
    twohundredseventy_rotated_state= ninghty_degree_rotation(onehundredeighty_rotated_state)
    #return True if a state or one of its equivalents is in G, return also the state which is in G
    if state in G:
        return True, state
    elif ninghty_rotated_state in G:
        return True, ninghty_rotated_state
    elif onehundredeighty_rotated_state in G:
        return True, onehundredeighty_rotated_state
    elif twohundredseventy_rotated_state in G:
        return True, twohundredseventy_rotated_state
    else:
        return False, ()

#----------------------------------------------------------------------------------------------------#
