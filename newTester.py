import time 
import numpy as np
from numpy import nan
allSituations = set()
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

print(time.time())
def findSum(currentGame):
    result = 0
    for num in currentGame:
        if num is not None:
            result += num
    print(result)

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
      for i in range(0, n):
          for j in range(0, n):
              
              if (j < 6 and gameSituation[i][j] is not None and gameSituation[i][j+1] is not None and gameSituation[i][j]+gameSituation[i][j+1] == 2):
                  finished = True
                  return
              if (i < 6 and gameSituation[i][j] is not None and gameSituation[i][j+1] is not None and gameSituation[i][j]+gameSituation[i+1][j] == 2):
                  finished = True
                  return
checkGameSituation(goal)
print(win)
# def updateArray(prevGame, x1, y1, x2, y2):
#     array = list(prevGame)
#     updatedArray = []    
#     for i in range(0, len(array)):
#         updatedArray.append(list(array[i]))    
#     newValue = 0
#     updatedArray[x1][y1] = 0
#     updatedArray[x2][y2] = 0
#     if (x1 == x2):
#         if (y1 > y2):
#             updatedArray[x2][y2-1] = 1
#         else:
#             updatedArray[x2][y2+1] = 1
#     else:
#         if (x1 > x2):
#             updatedArray[x2-1][y2] = 1
#         else:
#             updatedArray[x2+1][y2] = 1

#     newTuple = tuple(tuple(row) for row in updatedArray)    
#     return newTuple


# def validator(currentGame, x1, y1, x2, y2):
#     x3 = None
#     y3 = None
#     if (currentGame[x2][y2] != 1):
#         return False
#     if (x1 == x2):
#         x3 = x1
#         if (y1 < y2):
#             y3 = y2+1
#         if (y2 < y1):
#             y3 = y2-1
#         if (y3 > 0 and y3 < n and currentGame[x3][y3] != None):
#             su = currentGame[x1][y1]
#             su += currentGame[x2][y2]
#             su += currentGame[x3][y3]
#             if (su == 2):
#                 return True
#             else:
#                 return False
#     if (y1 == y2):
#         y3 = y1
#         if (x1 < x2):
#             x3 = x2+1
#         if (x2 < x1):
#             x3 = x2-1
#         if (x3 > 0 and x3 < n and currentGame[x3][y3] != None):
#             su = currentGame[x1][y1]
#             su += currentGame[x2][y2]
#             su += currentGame[x3][y3]
#             if (su == 2):
#                 return True
#             else:
#                 return False
#     return False




# def nextMove(currentGame):
#     # global checked
#     # checked+=1
#     checkGameSituation(currentGame)
#     # enter = tuple(currentGame.tolist())
#     # print(type(enter))
#     # print(type(allSituations))
#     # allSituations.add(tuple(enter))
#     # print(currentGame)
#     if win:
#         # print("here")
#         ans = list(currentGame)
#         return
#     if (currentGame in allSituations):
#         # print("Found Same 0")
#         return
#     rotated1 = tuple(tuple(currentGame[col][row] for col in range(
#         n)) for row in range(n - 1, -1, -1))
#     if (rotated1 in allSituations):
#         # print("Found Same 1")
#         return
#     rotated2 = tuple(tuple(rotated1[col][row] for col in range(
#         n)) for row in range(n - 1, -1, -1))
#     if (rotated2 in allSituations):
#         # print("Found Same 2")
#         return
#     rotated3 = tuple(tuple(rotated2[col][row] for col in range(
#         n)) for row in range(n - 1, -1, -1))
#     if (rotated3 in allSituations):
#         # print("Found Same 3")
#         return    
#     allSituations.add(currentGame)
#     for i in range(0, 7):
#         for j in range(0, 7):
#             if (currentGame[i][j] == 1):
#                 # print(i, j)
#                 if (i < 6 and validator(currentGame, i, j, i+1, j)):
#                     nextMove(updateArray(currentGame, i, j, i+1, j))
#                 if (i > 0 and validator(currentGame, i, j, i-1, j)):
#                     nextMove(updateArray(currentGame, i, j, i-1, j))
#                 if (j < 6 and validator(currentGame, i, j, i, j+1)):
#                     nextMove(updateArray(currentGame, i, j, i, j+1))
#                 if (j > 0 and validator(currentGame, i, j, i, j-1)):
#                     nextMove(updateArray(currentGame, i, j, i, j-1))

#     # print(currentGame)
#     # print(checked)

# # print(np.nansum(game))


# def play():
#     # The game starts with only 4 possible moves.
#     # The other parameter is above which marble position
#     # we are jumping.
#     nextMove(updateArray(game, 3, 1, 3, 2))  # 3, 1, 3, 2

#     # All other are actually same due to symmetricity.
#     # nextMove(updateArray(game, 1, 3, 2, 3))  # 1, 3, 2, 3
#     # nextMove(updateArray(game, 3, 5, 3, 4))  # 3, 5, 3, 4
#     # nextMove(updateArray(game, 5, 3, 4, 3))  # 5, 3, 4, 3


# play()
# print(ans)
# print((allSituations))
# print(time.time())