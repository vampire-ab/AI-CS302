import numpy as np
from numpy import nan
allSituations = set()
n = 7
game = np.array([[nan, nan, 1, 1, 1, nan, nan],
                 [nan, nan, 1, 1, 1, nan, nan],
                 [1,    1,    1, 1, 1,    1,    1],
                 [1,    1,    1, 0, 1,    1,    1],
                 [1,    1,    1, 1, 1,    1,    1],
                 [nan, nan, 1, 1, 1, nan, nan],
                 [nan, nan, 0, 1, 1, nan, nan], ])

def validator(currentGame, x1, y1, x2, y2):
    x3 = None
    y3 = None
    if (currentGame[x2][y2] != 1):
        return False
    if (currentGame[x1][y1] != 1):
        return False
    if (x1 == x2):
        x3 = x1
        if (y1 < y2):
            y3 = y2+1
        if (y2 < y1):
            y3 = y2-1
        if (y3 > 0 and y3 < n):
            su = currentGame[x1][y1]
            su += currentGame[x2][y2]
            su += currentGame[x3][y3]
            if (su == 2):
                return True
            else:
                return False
    if (y1 == y2):
        y3 = y1
        if (x1 < x2):
            x3 = x2+1
        if (x2 < x1):
            x3 = x2-1
        if (x3 > 0 and x3 < n):
            su = currentGame[x1][y1]
            su += currentGame[x2][y2]
            su += currentGame[x3][y3]
            if (su == 2):
                return True
            else:
                return False
    return False

print(validator(game, 3,1,3,2))



pq = PriorityQueue()


