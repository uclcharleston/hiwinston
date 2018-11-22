''' Implement an AI to play tetris '''
from random import Random
from te_settings import Direction

class AutoPlayer():
    ''' A very simple dumb AutoPlayer controller '''
    def __init__(self, controller):
        self.controller = controller
        self.rand = Random()

    def next_move(self, gamestate):
        ''' next_move() is called by the game, once per move.
            gamestate supplies access to all the state needed to autoplay the game.'''
        self.random_next_move(gamestate)

    def random_next_move(self, gamestate):
        ''' make a random move and a random rotation.  Not the best strategy! '''
        clone = gamestate.clone(True)
        rnd = self.rand.randint(-1, 1)
        if rnd == -1:
            direction = Direction.LEFT
        elif rnd == 1:
            direction = Direction.RIGHT
        if rnd != 0:
            clone.move(direction)
        rnd = self.rand.randint(-1, 1)
        if rnd == -1:
            direction = Direction.LEFT
        elif rnd == 1:
            direction = Direction.RIGHT
        if rnd != 0:
            clone.rotate(direction)
        get_Maxdepth(self)
        print(C1)
        gamestate.update()


def get_Maxdepth(gamestate):
    C1 = 0
    T = gamestate.get_tiles()
    for x in (0, len(T)):
        for y in (0, len(T[x])):
            row = y[1]
            if C1 < row:
                C1 = row