import random
import currentData

def checkWin():
    win = 0

    # vertical: |
    for x in range(0, 7):
        for y in range(0, 3):
            if currentData.currentGame[x][y] != 0:
                if (currentData.currentGame[x][y] == currentData.currentGame[x][y+1] and
                    currentData.currentGame[x][y] == currentData.currentGame[x][y+2] and
                    currentData.currentGame[x][y] == currentData.currentGame[x][y+3]):
                    win += 1

    # horizontal: -
    for y in range(0, 6):
        for x in range(0, 4):
            if currentData.currentGame[x][y] != 0:
                if (currentData.currentGame[x][y] == currentData.currentGame[x+1][y] and
                    currentData.currentGame[x][y] == currentData.currentGame[x+2][y] and
                    currentData.currentGame[x][y] == currentData.currentGame[x+3][y]):
                    win += 1

    # diagonal left: \
    for x in range(0, 4):
        for y in range(0, 3):
            if currentData.currentGame[x][y] != 0:
                if (currentData.currentGame[x][y] == currentData.currentGame[x+1][y+1] and
                    currentData.currentGame[x][y] == currentData.currentGame[x+2][y+2] and
                    currentData.currentGame[x][y] == currentData.currentGame[x+3][y+3]):
                    win += 1

    # diagonal right: /
    for x in range(0, 4):
        for y in range(0, 3):
            if currentData.currentGame[x+3][y] != 0:
                if (currentData.currentGame[x+3][y] == currentData.currentGame[x+2][y+1] and
                    currentData.currentGame[x+3][y] == currentData.currentGame[x+1][y+2] and
                    currentData.currentGame[x+3][y] == currentData.currentGame[x][y+3]):
                    win += 1

    if win > 0:
        return True
    else:
        return False

#///////////////////////////////////////////////////////////////////////////////////////////////

def checkChangeToWin(player):
    winIsHere = []

    # VERTICAL: |
    for x in range(0, 7):
        for y in range(1, 4):
            if (currentData.currentGame[x][y] == currentData.currentGame[x][y+1] and
                currentData.currentGame[x][y] == currentData.currentGame[x][y+2] and
                currentData.currentGame[x][y] == int(player) + 1 and
                currentData.currentGame[x][y-1] == 0):
                winIsHere.append(x + 1)

    #--------------------------------------------------------------------------------------------------
    # HORIZONTAL: -
    # first case: ○●●●
    for x in range(0, 4):
        for y in range(0, 6):
            if (currentData.currentGame[x+1][y] == currentData.currentGame[x+2][y] and
                currentData.currentGame[x+1][y] == currentData.currentGame[x+3][y] and
                currentData.currentGame[x+1][y] == int(player) + 1 and
                currentData.currentGame[x][y] == 0):
                if (y == 5):
                    winIsHere.append(x + 1)
                elif (currentData.currentGame[x][y+1] != 0):
                    winIsHere.append(x + 1)
    # socond case: ●●●○
    for x in range(0, 4):
        for y in range(0, 6):
            if (currentData.currentGame[x][y] == currentData.currentGame[x+1][y] and
                currentData.currentGame[x][y] == currentData.currentGame[x+2][y] and
                currentData.currentGame[x][y] == int(player) + 1 and
                currentData.currentGame[x+3][y] == 0):
                if (y == 5):
                    winIsHere.append(x + 1 + 3)
                elif (currentData.currentGame[x+3][y+1] != 0):
                    winIsHere.append(x + 1 + 3)
    # third case: ●●○●
    for x in range(0, 4):
        for y in range(0, 6):
            if (currentData.currentGame[x][y] == currentData.currentGame[x+1][y] and
                currentData.currentGame[x][y] == currentData.currentGame[x+3][y] and
                currentData.currentGame[x][y] == int(player) + 1 and
                currentData.currentGame[x+2][y] == 0):
                if (y == 5):
                    winIsHere.append(x + 1 + 2)
                elif (currentData.currentGame[x+2][y+1] != 0):
                    winIsHere.append(x + 1 + 2)
    # fourth case: ●○●●
    for x in range(0, 4):
        for y in range(0, 6):
            if (currentData.currentGame[x][y] == currentData.currentGame[x+2][y] and
                currentData.currentGame[x][y] == currentData.currentGame[x+3][y] and
                currentData.currentGame[x][y] == int(player) + 1 and
                currentData.currentGame[x+1][y] == 0):
                if (y == 5):
                    winIsHere.append(x + 1 + 1)
                elif (currentData.currentGame[x+1][y+1] != 0):
                    winIsHere.append(x + 1 + 1)

    #--------------------------------------------------------------------------------------------------
    # DIAGONAL LEFT: \
    # first case: ○●●●
    for x in range(0, 4):
        for y in range(0, 3):
            if (currentData.currentGame[x+1][y+1] == currentData.currentGame[x+2][y+2] and
                currentData.currentGame[x+1][y+1] == currentData.currentGame[x+3][y+3] and
                currentData.currentGame[x+1][y+1] == int(player) + 1 and
                currentData.currentGame[x][y] == 0 and
                currentData.currentGame[x][y+1] != 0):
                winIsHere.append(x + 1)
    # socond case: ●●●○
    for x in range(0, 4):
        for y in range(0, 3):
            if (currentData.currentGame[x][y] == currentData.currentGame[x+1][y+1] and
                currentData.currentGame[x][y] == currentData.currentGame[x+2][y+2] and
                currentData.currentGame[x][y] == int(player) + 1 and
                currentData.currentGame[x+3][y+3] == 0):
                if (y == 2):
                    winIsHere.append(x + 1 + 3)
                elif (currentData.currentGame[x+3][y+3+1] != 0):
                    winIsHere.append(x + 1 + 3)
    # third case: ●●○●
    for x in range(0, 4):
        for y in range(0, 3):
            if (currentData.currentGame[x][y] == currentData.currentGame[x+1][y+1] and
                currentData.currentGame[x][y] == currentData.currentGame[x+3][y+3] and
                currentData.currentGame[x][y] == int(player) + 1 and
                currentData.currentGame[x+2][y+2] == 0 and
                currentData.currentGame[x+2][y+2+1] != 0):
                winIsHere.append(x + 1 + 2)
    # fourth case: ●○●●
    for x in range(0, 4):
        for y in range(0, 3):
            if (currentData.currentGame[x][y] == currentData.currentGame[x+2][y+2] and
                currentData.currentGame[x][y] == currentData.currentGame[x+3][y+3] and
                currentData.currentGame[x][y] == int(player) + 1 and
                currentData.currentGame[x+1][y+1] == 0 and
                currentData.currentGame[x+1][y+1+1] != 0):
                winIsHere.append(x + 1 + 1)

    #--------------------------------------------------------------------------------------------------
    # DIAGONAL RIGHT: /
    # first case: ○●●●
    for x in range(0, 4):
        for y in range(0, 3):
            if (currentData.currentGame[x+1][y+2] == currentData.currentGame[x+2][y+1] and
                currentData.currentGame[x+1][y+2] == currentData.currentGame[x+3][y]   and
                currentData.currentGame[x+1][y+2] == int(player) + 1 and
                currentData.currentGame[x][y+3] == 0):
                if (y == 2):
                    winIsHere.append(x + 1)
                elif (currentData.currentGame[x][y+3+1] != 0):
                    winIsHere.append(x + 1)
    # socond case: ●●●○
    for x in range(0, 4):
        for y in range(0, 3):
            if (currentData.currentGame[x][y+3] == currentData.currentGame[x+1][y+2] and
                currentData.currentGame[x][y+3] == currentData.currentGame[x+2][y+1] and
                currentData.currentGame[x][y+3] == int(player) + 1 and
                currentData.currentGame[x+3][y] == 0 and
                currentData.currentGame[x+3][y+1] != 0):
                winIsHere.append(x + 1 + 3)
    # third case: ●●○●
    for x in range(0, 4):
        for y in range(0, 3):
            if (currentData.currentGame[x][y+3] == currentData.currentGame[x+1][y+2] and
                currentData.currentGame[x][y+3] == currentData.currentGame[x+3][y]   and
                currentData.currentGame[x][y+3] == int(player) + 1 and
                currentData.currentGame[x+2][y+1] == 0 and
                currentData.currentGame[x+2][y+1+1] != 0):
                winIsHere.append(x + 1 + 2)
    # fourth case: ●○●●
    for x in range(0, 4):
        for y in range(0, 3):
            if (currentData.currentGame[x][y+3] == currentData.currentGame[x+2][y+1] and
                currentData.currentGame[x][y+3] == currentData.currentGame[x+3][y]   and
                currentData.currentGame[x][y+3] == int(player) + 1 and
                currentData.currentGame[x+1][y+2] == 0 and
                currentData.currentGame[x+1][y+2+1] != 0):
                winIsHere.append(x + 1 + 1)

    if winIsHere != []:
        return winIsHere[random.randint(0, len(winIsHere) - 1)]
    else:
        return 0

#///////////////////////////////////////////////////////////////////////////////////////////////

def checkBlock(player):
    blockIsHere = []
    # first case: □□●●□
    for y in range(0, 6):
        for x in range(0, 3):
            if (currentData.currentGame[x][y] == 0 and
                currentData.currentGame[x+1][y] == 0 and
                currentData.currentGame[x+2][y] == int(player) + 1 and
                currentData.currentGame[x+3][y] == int(player) + 1 and
                currentData.currentGame[x+4][y] == 0):
                if y == 5:
                    blockIsHere.append(x+1)
                    blockIsHere.append(x+1+1)
                    blockIsHere.append(x+1+4)
                else:
                    if (currentData.currentGame[x][y+1] != 0 and
                        currentData.currentGame[x+1][y+1] != 0 and
                        currentData.currentGame[x+4][y+1] != 0):
                        blockIsHere.append(x+1)
                        blockIsHere.append(x+1+1)
                        blockIsHere.append(x+1+4)

    # second case: □●●□□
    for y in range(0, 6):
        for x in range(0, 3):
            if (currentData.currentGame[x][y] == 0 and
                currentData.currentGame[x+1][y] == int(player) + 1 and
                currentData.currentGame[x+2][y] == int(player) + 1 and
                currentData.currentGame[x+3][y] == 0 and
                currentData.currentGame[x+4][y] == 0):
                if y == 5:
                    blockIsHere.append(x+1)
                    blockIsHere.append(x+1+3)
                    blockIsHere.append(x+1+4)
                else:
                    if (currentData.currentGame[x][y+1] != 0 and
                        currentData.currentGame[x+3][y+1] != 0 and
                        currentData.currentGame[x+4][y+1] != 0):
                        blockIsHere.append(x+1)
                        blockIsHere.append(x+1+3)
                        blockIsHere.append(x+1+4)

    if blockIsHere != []:
        return blockIsHere[random.randint(0, len(blockIsHere) - 1)]
    else:
        return 0

#///////////////////////////////////////////////////////////////////////////////////////////////

def checkPotentialLoss(prediction, player):
    lossIsHere = []

    # HORIZONTAL: -
    # first case: ○●●●
    for x in range(0, 4):
        for y in range(0, 6):
            if (currentData.currentGame[x+1][y] == currentData.currentGame[x+2][y] and
                currentData.currentGame[x+1][y] == currentData.currentGame[x+3][y] and
                currentData.currentGame[x+1][y] == int(player) + 1 and
                currentData.currentGame[x][y] == 0):
                if (y != 5):
                    if (currentData.currentGame[x][y+1] == 0):
                        lossIsHere.append(x + 1)

    # socond case: ●●●○
    for x in range(0, 4):
        for y in range(0, 6):
            if (currentData.currentGame[x][y] == currentData.currentGame[x+1][y] and
                currentData.currentGame[x][y] == currentData.currentGame[x+2][y] and
                currentData.currentGame[x][y] == int(player) + 1 and
                currentData.currentGame[x+3][y] == 0):
                if (y != 5):
                    if (currentData.currentGame[x+3][y+1] == 0):
                        lossIsHere.append(x + 1 + 3)
    # third case: ●●○●
    for x in range(0, 4):
        for y in range(0, 6):
            if (currentData.currentGame[x][y] == currentData.currentGame[x+1][y] and
                currentData.currentGame[x][y] == currentData.currentGame[x+3][y] and
                currentData.currentGame[x][y] == int(player) + 1 and
                currentData.currentGame[x+2][y] == 0):
                if (y != 5):
                    if (currentData.currentGame[x+2][y+1] == 0):
                        lossIsHere.append(x + 1 + 2)
    # fourth case: ●○●●
    for x in range(0, 4):
        for y in range(0, 6):
            if (currentData.currentGame[x][y] == currentData.currentGame[x+2][y] and
                currentData.currentGame[x][y] == currentData.currentGame[x+3][y] and
                currentData.currentGame[x][y] == int(player) + 1 and
                currentData.currentGame[x+1][y] == 0):
                if (y != 5):
                    if (currentData.currentGame[x+1][y+1] == 0):
                        lossIsHere.append(x + 1 + 1)

    #--------------------------------------------------------------------------------------------------
    # DIAGONAL LEFT: \
    # first case: ○●●●
    for x in range(0, 4):
        for y in range(0, 3):
            if (currentData.currentGame[x+1][y+1] == currentData.currentGame[x+2][y+2] and
                currentData.currentGame[x+1][y+1] == currentData.currentGame[x+3][y+3] and
                currentData.currentGame[x+1][y+1] == int(player) + 1 and
                currentData.currentGame[x][y] == 0 and
                currentData.currentGame[x][y+1] == 0):
                lossIsHere.append(x + 1)
    # socond case: ●●●○
    for x in range(0, 4):
        for y in range(0, 3):
            if (currentData.currentGame[x][y] == currentData.currentGame[x+1][y+1] and
                currentData.currentGame[x][y] == currentData.currentGame[x+2][y+2] and
                currentData.currentGame[x][y] == int(player) + 1 and
                currentData.currentGame[x+3][y+3] == 0):
                if (y != 2):
                    if (currentData.currentGame[x+3][y+3+1] == 0):
                        lossIsHere.append(x + 1 + 3)
    # third case: ●●○●
    for x in range(0, 4):
        for y in range(0, 3):
            if (currentData.currentGame[x][y] == currentData.currentGame[x+1][y+1] and
                currentData.currentGame[x][y] == currentData.currentGame[x+3][y+3] and
                currentData.currentGame[x][y] == int(player) + 1 and
                currentData.currentGame[x+2][y+2] == 0 and
                currentData.currentGame[x+2][y+2+1] == 0):
                lossIsHere.append(x + 1 + 2)
    # fourth case: ●○●●
    for x in range(0, 4):
        for y in range(0, 3):
            if (currentData.currentGame[x][y] == currentData.currentGame[x+2][y+2] and
                currentData.currentGame[x][y] == currentData.currentGame[x+3][y+3] and
                currentData.currentGame[x][y] == int(player) + 1 and
                currentData.currentGame[x+1][y+1] == 0 and
                currentData.currentGame[x+1][y+1+1] == 0):
                lossIsHere.append(x + 1 + 1)

    #--------------------------------------------------------------------------------------------------
    # DIAGONAL RIGHT: /
    # first case: ○●●●
    for x in range(0, 4):
        for y in range(0, 3):
            if (currentData.currentGame[x+1][y+2] == currentData.currentGame[x+2][y+1] and
                currentData.currentGame[x+1][y+2] == currentData.currentGame[x+3][y]   and
                currentData.currentGame[x+1][y+2] == int(player) + 1 and
                currentData.currentGame[x][y+3] == 0):
                if (y != 2):
                    if (currentData.currentGame[x][y+3+1] == 0):
                        lossIsHere.append(x + 1)

    # socond case: ●●●○
    for x in range(0, 4):
        for y in range(0, 3):
            if (currentData.currentGame[x][y+3] == currentData.currentGame[x+1][y+2] and
                currentData.currentGame[x][y+3] == currentData.currentGame[x+2][y+1] and
                currentData.currentGame[x][y+3] == int(player) + 1 and
                currentData.currentGame[x+3][y] == 0 and
                currentData.currentGame[x+3][y+1] == 0):
                lossIsHere.append(x + 1 + 3)
    # third case: ●●○●
    for x in range(0, 4):
        for y in range(0, 3):
            if (currentData.currentGame[x][y+3] == currentData.currentGame[x+1][y+2] and
                currentData.currentGame[x][y+3] == currentData.currentGame[x+3][y]   and
                currentData.currentGame[x][y+3] == int(player) + 1 and
                currentData.currentGame[x+2][y+1] == 0 and
                currentData.currentGame[x+2][y+1+1] == 0):
                lossIsHere.append(x + 1 + 2)
    # fourth case: ●○●●
    for x in range(0, 4):
        for y in range(0, 3):
            if (currentData.currentGame[x][y+3] == currentData.currentGame[x+2][y+1] and
                currentData.currentGame[x][y+3] == currentData.currentGame[x+3][y]   and
                currentData.currentGame[x][y+3] == int(player) + 1 and
                currentData.currentGame[x+1][y+2] == 0 and
                currentData.currentGame[x+1][y+2+1] == 0):
                lossIsHere.append(x + 1 + 1)

    if lossIsHere != []: # if lossIsHere is empty
        if len(set(lossIsHere)) < 7: # if lossIsHere is full
            loss = 0
            for value in lossIsHere:
                if (value == prediction):
                    loss += 1

            if (loss > 0): # if lossIsHere contains prediction value
                notLoss = []
                for i in range(1, 8):
                    contains = 0
                    for value in lossIsHere:
                        if (value == i):
                            contains += 1
                    if (contains == 0):
                        notLoss.append(i)
                
                return notLoss[random.randint(0, len(notLoss) - 1)]
            else:
                return prediction

        else:
            return random.randint(0, 7)
    else:
        return prediction
    