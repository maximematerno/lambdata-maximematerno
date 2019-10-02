"""
Classes to represent games
"""
​


class Game:
    """ General representation of an abstract game"""


​
fun_level = 5
​


def __init__(self, player1="Stefano", player2="Rudy"):
        self.rounds = 2
        self.steps = 5
        self.player1 = player1
        self.player2 = player2


​


def print_players(self):
        """ Print game players"""
        print('{} is playing {}'.format(self.player1, self.player2))


​


def add_round(self):
        """Increment rounds by 1"""
        self.rounds += 1


​


class Tic(Game):
    """
    Tictactoe subclass of game
    """


​


def __init__(self, player1='Anika', player2='Hira'):
        super().__init__(player1, player2)
        self.rounds = 3


​


def print_players(self):
        print(
            '{} is playing TIC TAC TOE with {}'.format(
                self.player1,
                self.player2))
