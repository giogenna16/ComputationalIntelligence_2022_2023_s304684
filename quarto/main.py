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
    count=0
    game = quarto.Quarto()
    robot= RenforcementLearningAgent(game)
    winsHistory = []
    indices = []
    for m in range(10):
        game.reset()
        game.set_players((robot, HardCodedPlayer2(game)))
        winner = game.run()
        
        #add the reward for the final status
        reward= robot.get_reward(winner)
        board_status= game.get_board_status()
        board_status_t= list()
        for r in range(game.BOARD_SIDE):
            board_status_t+= board_status[r].tolist()
        board_status_t= tuple(board_status_t)
        if board_status_t not in robot.G:
            robot.G[board_status_t] = 0
        robot.update_state_history(board_status_t, reward)   

        robot.learn()

        if winner==0:
            count+=1
        if m % 2 == 0: 
            winsHistory.append(count)
            indices.append(m)
            count= 0
    plt.plot(indices, winsHistory)
    plt.xlabel('Number of matches')
    plt.ylabel('Number of matches won for every 5 matches')
    plt.title('How the Reinforcement Learning Agent works:\n')
    plt.show()
    print(winsHistory)

    # game = quarto.Quarto()
    # game.set_players((HardCodedPlayer2(game), HardCodedPlayer1(game)))
    # winner = game.run()
    # print("win", winner)
    # logging.warning(f"main: Winner: player {winner}")


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