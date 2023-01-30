# Free for personal or classroom use; see 'LICENSE.md' for details.
# https://github.com/squillero/computational-intelligence

import logging
import argparse
import quarto
from quarto.hard_coded_players import *
from quarto.rl_agent import *
from quarto.min_max import * 
import matplotlib.pyplot as plt

NUM_MATCHES= 300


def main_RL_agent():
    count_won= 0
    game = quarto.Quarto()
    robot= RenforcementLearningAgent(game)
    opponent= HardCodedPlayer0(game)
    winsHistory= []
    indices= []
    for m in range(NUM_MATCHES):
        game.reset()
        won= None
        lost= None
        if m%2== 0:  # one time it starts first, another second
            game.set_players((robot, opponent))
            winner= game.run()
            won=1 if winner==0 else 0 if winner==1 else -1
            lost=0 if winner==0 else 1 if winner==1 else -1
            if winner== 0:
                count_won+= 1
        else:
            game.set_players((opponent, robot))
            winner = game.run()
            won== 1 if winner==1 else 0 if winner==0 else -1
            lost== 0 if winner==1 else 1 if winner==0 else -1 
            if winner== 1:
                count_won+= 1

        #add the reward for the final state
        reward_won= robot.get_reward(won)
        reward_lost= robot.get_reward(lost)
        board_status= game.get_board_status()
        board_status_t= list()
        for r in range(game.BOARD_SIDE):
            board_status_t+= board_status[r].tolist()
        board_status_t= tuple(board_status_t)
        is_in, state_in_G= state_or_equivalent_in_G(board_status_t, robot.G)
        if not is_in:
            robot.G[board_status_t]= 0
            robot.update_state_history(board_status_t, reward_won) 
            robot.update_state_history_opponent(board_status_t, reward_lost)
        else:
            robot.update_state_history(state_in_G, reward_won)
            robot.update_state_history_opponent(state_in_G, reward_lost)
        robot.learn()

        if m%6== 0: 
            winsHistory.append(count_won)
            indices.append(m)
            count_won= 0
    plt.plot(indices, winsHistory)
    plt.xlabel('Number of matches')
    plt.ylabel('Number of won matches for every 6 matches')
    plt.title('How the Reinforcement Learning Agent works:\n')
    plt.show()


def main_hard_coded_players():
    game = quarto.Quarto()
    my_player= HardCodedPlayer0(game)
    opponent= HardCodedPlayer2(game)
    won_matches=0
    tied_matches=0
    for m in range(NUM_MATCHES):
        game.reset()
        if m%2== 0:  # one time it starts first, another second
            game.set_players((my_player, opponent))
            winner= game.run()
            if winner== 0:
                won_matches+= 1
            if winner== -1:
                tied_matches+=1
        else:
            game.set_players((opponent, my_player))
            winner = game.run()
            if winner== 1:
               won_matches+= 1
            if winner== -1:
                tied_matches+=1
    print(f"The evaluated player won {won_matches} matches and tied {tied_matches} matches")


def main_min_max(): # IT IS THE FUNCTION FOR THE PLAYER TO BE USED FOR THE TOURNAMENT!!!!!!!!!!!!!!
    game= quarto.Quarto()
    my_player= MinMaxPlayer(game) # IT IS THE PLAYER TO BE USED FOR THE TOURNAMENT!!!!!!!!!!!!!!
    opponent= HardCodedPlayer2(game)
    won_matches= 0
    tied_matches= 0
    for m in range(NUM_MATCHES):
        game.reset()
        if m%2== 0:
            my_player.set_maximizing(False) # if my_player is the first, it will minimize, during the min_max for placing the position
            game.set_players((my_player, opponent))
            winner= game.run()
            if winner== 0:
                won_matches+= 1
            elif winner== -1:
                tied_matches+= 1
        else:
            my_player.set_maximizing(True) # if my_player is the second, it will maximize, during the min_max for placing the position
            game.set_players((opponent, my_player))
            winner= game.run()
            if winner== 1:
                won_matches+= 1
            elif winner== -1:
                tied_matches+= 1

    print(f"The evaluated player won {won_matches} matches and tied {tied_matches} matches")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', action='count', default=0, help='increase log verbosity')
    parser.add_argument('-d',
                        '--debug',
                        action='store_const',
                        dest='verbose',
                        const=2,
                        help='log debug messages (same as -vv)')
    args = parser.parse_args()

    if args.verbose == 0:
        logging.getLogger().setLevel(level=logging.WARNING)
    elif args.verbose == 1:
        logging.getLogger().setLevel(level=logging.INFO)
    elif args.verbose == 2:
        logging.getLogger().setLevel(level=logging.DEBUG)

    #main_RL_agent()
    #main_hard_coded_players()
    main_min_max()
    
    