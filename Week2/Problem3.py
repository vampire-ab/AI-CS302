from string import ascii_lowercase
import random
from itertools import combinations
import numpy as np

#k = 3
print("Enter the number of clauses in the formula")
m = int(input())
print("Enter the number of variables")
n = int(input())


def generateProblems(m, n):
    lower = (list(ascii_lowercase))[:n]
    upper = [c.upper() for c in lower]
    var = upper + lower
    problems = []
    allCombo = list(combinations(var, 3))
    j = 0
    while j < 10:  # threshold value
        c = random.sample(allCombo, m)
        if c not in problems:
            j += 1
            problems.append(list(c))
    
    problems_new = []
    for c in problems:
        temp = []
        temp = [list(sub) for sub in c]
        problems_new.append(temp)
    return problems_new, var


problems, var = generateProblems(m, n)


def assignment(var, n):
    forLowerCase = list(np.random.choice(2, n))
    forUpperCase = [abs(1-i) for i in forLowerCase]
    assign = forLowerCase + forUpperCase
    var_assign = dict(zip(var, assign))
    return var_assign


var_assign = assignment(var, n)
print(var_assign)
print(problems[0])


def solve(problem, assign):
    count = 0
    for sub in problem:
        l = [assign[val] for val in sub]
        count += any(l)
    return count


def hillClimbing(problem, assign, maximum, received, step):
    bestAssign = assign.copy()
    assignValues = list(assign.values())
    assignKeys = list(assign.keys())
    maxNum = maximum
    maxAssign = assign.copy()
    editAssign = assign.copy()
    for i in range(len(assignValues)):
        step += 1
        editAssign[assignKeys[i]] = abs(assignValues[i]-1)
        c = solve(problem, editAssign)
        if maxNum < c:
            received = step
            maxNum = c
            maxAssign = editAssign.copy()
    if maxNum == maximum:
        s = str(received) + "/" + str(step-len(assignValues))
        return bestAssign, maxNum, s
    else:
        maximum = maxNum
        bestassign = maxAssign.copy()
        return hillClimbing(problem, bestassign, maximum, received, step)


def beamSearch(problem, assign, b, stepSize):
    bestAssign = assign.copy()
    assignValues = list(assign.values())
    assignKeys = list(assign.keys())
    steps = []
    possibleAssigns = []
    possibleScores = []
    editAssign = assign.copy()
    initial = solve(problem, assign)
    if initial == len(problem):
        p = str(stepSize) + "/" + str(stepSize)
        return assign, p
    for i in range(len(assignValues)):
        stepSize += 1
        editAssign[assignKeys[i]] = abs(assignValues[i]-1)
        c = solve(problem, editAssign)
        possibleAssigns.append(editAssign.copy())
        possibleScores.append(c)
        steps.append(stepSize)
    selected = list(np.argsort(possibleScores))[-b:]
    if len(problem) in possibleScores:
        index = [i for i in range(len(possibleScores))
                 if possibleScores[i] == len(problem)]
        p = str(steps[index[0]]) + "/" + str(steps[-1])
        return possibleAssigns[index[0]], p
    else:
        selectedAssigns = [possibleAssigns[i] for i in selected]
        for a in selectedAssigns:
            return beamSearch(problem, a, b, stepSize)


def variableNeighbor(problem, assign, b, step):
    bestAssign = assign.copy()
    assignValues = list(assign.values())
    assignKeys = list(assign.keys())
    steps = []
    possibleAssigns = []
    possibleScores = []
    editAssign = assign.copy()
    initail = solve(problem, assign)
    if initial == len(problem):
        p = str(step) + "/" + str(step)
        return assign, p, b
    for i in range(len(assignValues)):
        step += 1
        editAssign[assignKeys[i]] = abs(assignValues[i]-1)
        c = solve(problem, editAssign)
        possibleAssigns.append(editAssign.copy())
        possibleScores.append(c)
        steps.append(step)
    selected = list(np.argsort(possibleScores))[-b:]
    if len(problem) in possibleScores:
        index = [i for i in range(len(possibleScores))
                 if possibleScores[i] == len(problem)]
        p = str(steps[index[0]]) + "/" + str(steps[-1])
        return possibleAssigns[index[0]], p, b
    else:
        selectedAssigns = [possibleAssigns[i] for i in selected]
        for a in selectedAssigns:
            return variableNeighbor(problem, a, b+1, step)


hAssigns = []
assigns = []
h_n = []
initials = []
hill_penetration = []
beam_penetration = []
var_penetration = []
v_n = []
b_var = []
b_n = []
bAssigns = []
vAssigns = []
i = 0

for problem in problems:
    i += 1
    l = []
    assign = assignment(var, n)
    initial = solve(problem, assign)
    bestAssign, score, hp = hillClimbing(problem, assign, initial, 1, 1)
    hAssigns.append(bestAssign)
    assigns.append(assign)
    h_n.append(score)
    initials.append(initial)
    hill_penetration.append(hp)
    h, b3p = beamSearch(problem, assign, 3, 1)
    bAssigns.append(h)
    beam_penetration.append(b3p)
    h4, b4p = beamSearch(problem, assign, 4, 1)
    v, p, bb = variableNeighbor(problem, assign, 1, 1)
    var_penetration.append(p)
    b_var.append(bb)
    vAssigns.append(v)
    print('Problem ', i, ': ', problem)
    print('HillClimbing: ', bestAssign, ', Penetrance:', hp)
    print('Beam search (3): ', h, ', Penetrance:', b3p)
    print('Beam search (4): ', h4, ', Penetrance:', b4p)
    print('Variable Neighborhood: ', v, ', Penetrance:', p)
    print()