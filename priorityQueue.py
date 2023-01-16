import time
import numpy as np
from numpy import nan
import queue as Q
allSituations = set()
start = time.time()
n = 7
checked = 0
goal = ((None, None, 0, 0, 0, None, None),
        (None, None, 0, 0, 0, None, None),
        (0,    0,    0, 0, 0,    0,    0),
        (0,    0,    0, 1, 0,    0,    0),
        (0,    0,    0, 0, 0,    0,    0),
        (None, None, 0, 0, 0, None, None),
        (None, None, 0, 0, 0, None, None))

game = ((None, None, 1, 1, 1, None, None),
        (None, None, 1, 1, 1, None, None),
        (1,    1,    1, 1, 1,    1,    1),
        (1,    1,    1, 0, 1,    1,    1),
        (1,    1,    1, 1, 1,    1,    1),
        (None, None, 1, 1, 1, None, None),
        (None, None, 1, 1, 1, None, None))
# print(game[2][2])
# allSituations.add(game)
finished = False
win = False
ans = []

frontier = Q.PriorityQueue()
#cost, game
frontier.put([0, game])

#Make a move since the move we are making is valid
def updateArray(prevGame, x1, y1, x2, y2):
    array = list(prevGame)
    updatedArray = []
    for i in range(0, len(array)):
        updatedArray.append(list(array[i]))
    newValue = 0
    updatedArray[x1][y1] = 0
    updatedArray[x2][y2] = 0
    if (x1 == x2):
        if (y1 > y2):
            updatedArray[x2][y2-1] = 1
        else:
            updatedArray[x2][y2+1] = 1
    else:
        if (x1 > x2):
            updatedArray[x2-1][y2] = 1
        else:
            updatedArray[x2+1][y2] = 1

    newTuple = tuple(tuple(row) for row in updatedArray)
    return newTuple

#If a valid move is possible, it increases the path cost as we mve forward.
def validator(currentGame, x1, y1, x2, y2):
    x3 = None
    y3 = None
    if (currentGame[x2][y2] != 1):
        return False
    if (x1 == x2):
        x3 = x1
        if (y1 < y2):
            y3 = y2+1
        if (y2 < y1):
            y3 = y2-1
        if (y3 > 0 and y3 < n and currentGame[x3][y3] != None):
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
        if (x3 > 0 and x3 < n and currentGame[x3][y3] != None):
            su = currentGame[x1][y1]
            su += currentGame[x2][y2]
            su += currentGame[x3][y3]
            if (su == 2):
                return True
            else:
                return False
    return False


def checkGameSituation(gameSituation):
    global finished
    global win
    if (not finished):
        summ = 0
        for i in range(0, n):
            for j in range(0, n):
                if gameSituation[i][j] is not None:
                    summ += gameSituation[i][j]
        if (summ == 1 and gameSituation[3][3] == 1):
            print("sum = 1", gameSituation)
            finished = True
            win = True
            return


def play():
    global win
    global ans
    global finished
    while not frontier.empty():
        current = frontier.get()

        checkGameSituation(current[1])
        # print(finished)
        if (win):
            ans = list(current[1])
            print("Won")
            break
        if (current[1] in allSituations):
            continue
        rotated1 = tuple(tuple(current[1][col][row] for col in range(
            n)) for row in range(n - 1, -1, -1))
        if (rotated1 in allSituations):
            continue
        rotated2 = tuple(tuple(rotated1[col][row] for col in range(
            n)) for row in range(n - 1, -1, -1))
        if (rotated2 in allSituations):
            continue
        rotated3 = tuple(tuple(rotated2[col][row] for col in range(
            n)) for row in range(n - 1, -1, -1))
        if (rotated3 in allSituations):
            continue
        allSituations.add(current[1])
        for i in range(0, 7):
            for j in range(0, 7):
                if (current[1][i][j] == 1):
                    global checked
                    checked += 1
                    #Move Down
                    if (i < 6 and validator(current[1], i, j, i+1, j)):
                        newTuple = (updateArray(
                            current[1], i, j, i+1, j))
                        frontier.put(
                            [current[0]+1, newTuple])
                    
                    #Move Up
                    if (i > 0 and validator(current[1], i, j, i-1, j)):
                        newTuple = (updateArray(
                            current[1], i, j, i-1, j))
                        frontier.put(
                            [current[0]+1, newTuple])

                    #Move Right
                    if (j < 6 and validator(current[1], i, j, i, j+1)):
                        newTuple = (updateArray(
                            current[1], i, j, i, j+1))
                        frontier.put(
                            [current[0]+1, newTuple])

                    #Move Left
                    if (j > 0 and validator(current[1], i, j, i, j-1)):
                        newTuple = (updateArray(
                            current[1], i, j, i, j-1))
                        frontier.put(
                            [current[0]+1, newTuple])
        print(checked)        


play()
print(ans)
print(time.time() - start)
