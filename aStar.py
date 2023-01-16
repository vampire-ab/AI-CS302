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
#cost, g, h, game
frontier.put([0, 0, 0, game])


def findSum(currentGame):
    result = 0
    for num in currentGame:
        if num is not None:
            result += num
    print(result)


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
        if (summ == 1):
            print("sum = 1", gameSituation)
            finished = True
            win = True
            return

# Exponential Distance from Horizontal or Vertical


def get_estimate(curr_state):
    cost = 0
    for i in range(7):
        for j in range(7):
            if curr_state[i][j] == 1:
                cost += 2**(max(abs(i-3), abs(j-3)))

    return cost


def play():
    global win
    global ans
    global finished
    while not frontier.empty():
        current = frontier.get()
        # next_moves = []

        checkGameSituation(current[3])
        # print(finished)
        if (win):
            ans = list(current[3])
            print("Won")
            break
        if finished:
            finished = False
            continue
        # if(current[3] == )
        if (current[3] in allSituations):
            # print("Found Same 0")
            # print("FOund: ", current[3])
            continue
        rotated1 = tuple(tuple(current[3][col][row] for col in range(
            n)) for row in range(n - 1, -1, -1))
        if (rotated1 in allSituations):
            # print("Found Same 1")
            continue
        rotated2 = tuple(tuple(rotated1[col][row] for col in range(
            n)) for row in range(n - 1, -1, -1))
        if (rotated2 in allSituations):
            # print("Found Same 2")
            continue
        rotated3 = tuple(tuple(rotated2[col][row] for col in range(
            n)) for row in range(n - 1, -1, -1))
        if (rotated3 in allSituations):
            # print("Found Same 3")
            continue

        allSituations.add(current[3])

        for i in range(0, 7):
            for j in range(0, 7):
                if (current[3][i][j] == 1):
                    global checked
                    checked += 1
                    if (i < 6 and validator(current[3], i, j, i+1, j)):
                        newTuple = (updateArray(
                            current[3], i, j, i+1, j))
                        h = get_estimate(newTuple)
                        frontier.put(
                            [current[1]+1+h, current[1]+1, h, newTuple])
                    if (i > 0 and validator(current[3], i, j, i-1, j)):
                        newTuple = (updateArray(
                            current[3], i, j, i-1, j))
                        h = get_estimate(newTuple)
                        frontier.put(
                            [current[1]+1+h, current[1]+1, h, newTuple])
                    if (j < 6 and validator(current[3], i, j, i, j+1)):
                        newTuple = (updateArray(
                            current[3], i, j, i, j+1))
                        h = get_estimate(newTuple)
                        frontier.put(
                            [current[1]+1+h, current[1]+1, h, newTuple])
                    if (j > 0 and validator(current[3], i, j, i, j-1)):
                        newTuple = (updateArray(
                            current[3], i, j, i, j-1))
                        h = get_estimate(newTuple)
                        frontier.put(
                            [current[1]+1+h, current[1]+1, h, newTuple])
        # print(checked)
        print(len(allSituations))


play()
print(ans)
print(time.time() - start)
