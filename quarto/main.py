# Free for personal or classroom use; see 'LICENSE.md' for details.
# https://github.com/squillero/computational-intelligence

import logging
import argparse
import random
import quarto
from quarto.players import *
import matplotlib.pyplot as plt


class RandomPlayer(quarto.Player):
    """Random player"""

    def __init__(self, quarto: quarto.Quarto) -> None:
        super().__init__(quarto)

    def choose_piece(self) -> int:
        return random.randint(0, 15)

    def place_piece(self) -> tuple[int, int]:
        return random.randint(0, 3), random.randint(0, 3)


def main():
    count_won= 0
    game = quarto.Quarto()
    robot= RenforcementLearningAgent(game)
    winsHistory= []
    indices= []
    for m in range(50):
        game.reset()
        won= None
        if m%2== 0:  # one time it starts first, another second
            game.set_players((robot, HardCodedPlayer2(game)))
            winner= game.run()
            if winner== 0:
                won= 1
                count_won+= 1
            elif winner== 1:
                won= 0
            else:
                won= -1
        else:
            game.set_players((HardCodedPlayer2(game), robot))
            winner = game.run()
            if winner== 1:
                won= 1
                count_won+= 1
            elif winner== 0:
                won= 0
            else:
                won= -1

        #add the reward for the final state
        reward= robot.get_reward(won)
        board_status= game.get_board_status()
        board_status_t= list()
        for r in range(game.BOARD_SIDE):
            board_status_t+= board_status[r].tolist()
        board_status_t= tuple(board_status_t)
        is_in, state_in_G= state_or_equivalent_in_G(board_status_t, robot.G)
        if not is_in:
            robot.G[board_status_t]= 0
            robot.update_state_history(board_status_t, reward)  
        else:
            robot.update_state_history(state_in_G, reward)
        robot.learn()

        if m % 20 == 0: 
            winsHistory.append(count_won)
            indices.append(m)
            count_won= 0
    plt.plot(indices, winsHistory, label= "won matches")
    plt.xlabel('Number of matches')
    plt.ylabel('Number of won matches for every 5 matches')
    plt.title('How the Reinforcement Learning Agent works:\n')
    plt.show()

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

    main()