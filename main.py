import currentData
import checksFunctions

import customtkinter as ctk
from tkinter import *
import json
import joblib
from sklearn.neural_network import MLPClassifier

# set window style
with open('settings/darkMode.json') as f:
    data = json.load(f)
    if (data['darkMode'] == 0):
        currentData.darkMode = 0
        ctk.set_appearance_mode("light")
    else:
        currentData.darkMode = 1
        ctk.set_appearance_mode("dark")

# set color theme
ctk.set_default_color_theme("blue")

# creating window
window = ctk.CTk()
window.title("Connect four")
window.iconbitmap('img/icon.ico')
window.geometry("582x405")

# images
logoImage = PhotoImage(file='img/logo.png')
redCircle = PhotoImage(file='img/red.png')
greenCircle = PhotoImage(file='img/green.png')
redSmallCircle = PhotoImage(file='img/redSmall.png')
greenSmallCircle = PhotoImage(file='img/greenSmall.png')
emptyLightCircle = PhotoImage(file='img/emptyLight.png')
emptyDarkCircle = PhotoImage(file='img/emptyDark.png')
redMouseCircle = PhotoImage(file='img/redMouse.png')
greenMouseCircle = PhotoImage(file='img/greenMouse.png')
emptyLightMouseCircle = PhotoImage(file='img/emptyLightMouse.png')
emptyDarkMouseCircle = PhotoImage(file='img/emptyDarkMouse.png')

# instances
imageLabels = [[], [], [], [], [], [], []]
currentPlayerLbl = Label()
currentRound = ctk.CTkLabel()
gameGuiFrame = ctk.CTkFrame()
MLPmodel = MLPClassifier()
exitGameGuiButton = ctk.CTkButton()

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

def clearAllWidgets():
    for widget in window.winfo_children():
        widget.destroy()

def clearAllParameters():
    currentData.currentPlayer = False
    currentData.currentGameInString = []
    currentData.roundNumber = 1
    currentData.currentGame = [[0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0]]
    global imageLabels
    global currentPlayerLbl
    global currentRound
    global gameGuiFrame
    global MLPmodel
    global exitGameGuiButton
    imageLabels = [[], [], [], [], [], [], []]
    currentPlayerLbl = Label()
    currentRound = ctk.CTkLabel()
    gameGuiFrame = ctk.CTkFrame()
    MLPmodel = MLPClassifier()
    exitGameGuiButton = ctk.CTkButton()

def switchCommand(darkModeSwitchValue):
    if (darkModeSwitchValue == 0):
        ctk.set_appearance_mode("light")
        currentData.darkMode = 0
    else:
        ctk.set_appearance_mode("dark")
        currentData.darkMode = 1
    with open('settings/darkMode.json', 'w') as f:
        json.dump({"darkMode": currentData.darkMode}, f)

def exitButton():
    clearAllWidgets()
    showMenuGui()
    currentData.endGame = False

def refreshCurrentRound():
    currentData.roundNumber += 1
    global currentRound
    currentRound['text'] = "Round " + str(currentData.roundNumber)

def endGame():
    currentData.endGame = True
    # global exitGameGuiButton
    # exitGameGuiButton['state'] = DISABLED # not working
    for x in range(1, 8):
        mouseLeave(0, x)

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

def mouseEnter(event, numberOfColumn):
    if currentData.endGame == False:
        global imageLabels
        for y in range(0, 6):
            if currentData.currentGame[numberOfColumn-1][y] == 0:
                if currentData.darkMode == 0:
                    imageLabels[numberOfColumn-1][y]['image'] = emptyLightMouseCircle
                else:
                    imageLabels[numberOfColumn-1][y]['image'] = emptyDarkMouseCircle
            elif currentData.currentGame[numberOfColumn - 1][y] == 1:
                imageLabels[numberOfColumn-1][y]['image'] = redMouseCircle
            elif currentData.currentGame[numberOfColumn - 1][y] == 2:
                imageLabels[numberOfColumn-1][y]['image'] = greenMouseCircle

def mouseLeave(event, numberOfColumn):
    global imageLabels
    for y in range(0, 6):
        if currentData.currentGame[numberOfColumn-1][y] == 0:
            if currentData.darkMode == 0:
                imageLabels[numberOfColumn-1][y]['image'] = emptyLightCircle
            else:
                imageLabels[numberOfColumn-1][y]['image'] = emptyDarkCircle
        elif currentData.currentGame[numberOfColumn - 1][y] == 1:
            imageLabels[numberOfColumn-1][y]['image'] = redCircle
        elif currentData.currentGame[numberOfColumn - 1][y] == 2:
            imageLabels[numberOfColumn-1][y]['image'] = greenCircle

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

def showMenuGui():
    # main window
    window.minsize(width=562, height=350)

    # menu frame
    menuFrame = ctk.CTkFrame(master=window, corner_radius=20)
    menuFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

    # logo frame
    logoFrame = ctk.CTkFrame(master=menuFrame, corner_radius=10)
    logoFrame.pack(padx=10, pady=10)

    # label with logo image
    imageLbl = ctk.CTkLabel(master=logoFrame, image=logoImage)
    imageLbl.grid(row=0, column=0, padx=10, pady=10)

    # title label
    titleLbl = ctk.CTkLabel(master=logoFrame, text="Connect four")
    titleLbl.config(font=("Arial", 40))
    titleLbl.grid(row=0, column=1, padx=10)

    # player vs player button
    playerVSplayerButton = ctk.CTkButton(master=menuFrame, text="Player VS Player", width=175, height=40, command=playerVSplayer)
    playerVSplayerButton.pack(padx=5, pady=5)

    # player vs AI button
    playerVSaiButton = ctk.CTkButton(master=menuFrame, text="Player VS AI", width=175, height=40, command=playerVSai)
    playerVSaiButton.pack(padx=5, pady=5)

    # exit button
    exitBtn = ctk.CTkButton(master=menuFrame, text="Exit", width=175, height=40, command=window.destroy)
    exitBtn.pack(padx=5, pady=5)

    # dark mode switch
    darkModeSwitch = ctk.CTkSwitch(master=menuFrame, text="Dark Mode", command=lambda: switchCommand(darkModeSwitch.get()))
    if (currentData.darkMode == 1):
        darkModeSwitch.toggle()
    darkModeSwitch.pack(padx=5, pady=10)

def showGameGui():
    window.geometry("838x576")
    window.minsize(width=838, height=576)

    # frames
    gameFrame = ctk.CTkFrame(master=window, corner_radius=20)
    gameFrame.place(relx=0.5, rely=0.5, anchor=CENTER)
    global gameGuiFrame
    gameGuiFrame = gameFrame

    if (currentData.currentGameType == 1):
        # current player
        currentPlayerFrame = ctk.CTkFrame(master=gameFrame, corner_radius=10)
        currentPlayerFrame.grid(row=0, column=0, padx=10, pady=10)

        title = ctk.CTkLabel(master=currentPlayerFrame, text="Current player:")
        title.pack(padx=5, pady=5)

        currentPlr = ctk.CTkLabel(master=currentPlayerFrame, image=redSmallCircle)
        global currentPlayerLbl
        currentPlayerLbl = currentPlr
        currentPlayerLbl.pack(padx=5, pady=5)

        # round frame
        roundFrame = ctk.CTkFrame(master=gameFrame, corner_radius=10)
        roundFrame.grid(row=1, column=0, padx=10, pady=10)
    else:
        # round frame
        roundFrame = ctk.CTkFrame(master=gameFrame, corner_radius=10)
        roundFrame.grid(row=0, column=0, padx=10, pady=10)
    
    # round number
    round = ctk.CTkLabel(master=roundFrame, text="Round 1")
    global currentRound
    currentRound = round
    currentRound.pack(padx=5, pady=5)

    # exit button
    exitBtn = ctk.CTkButton(master=gameFrame, text="Exit", command=exitButton)
    global exitGameGuiButton
    exitGameGuiButton = exitBtn
    exitGameGuiButton.grid(row=5, column=0, padx=10, pady=10)

    # image labels
    global imageLabels
    if currentData.darkMode == 0:
        for x in range(0, 7):
            for y in range(0, 6):
                imageLbl = Label(gameFrame, image=emptyLightCircle, bg='#e3e4e5')
                imageLabels[x].append(imageLbl)
    else:
        for x in range(0, 7):
            for y in range(0, 6):
                imageLbl = Label(gameFrame, image=emptyDarkCircle, bg='#292929')
                imageLabels[x].append(imageLbl)

    # set on the tabel
    for x in range(0, 7):
        for y in range(0, 6):
            imageLabels[x][y].grid(row=y, column=x+1)

    # set mouse enter event
    for y in range(0, 6):
        imageLabels[0][y].bind("<Enter>", lambda event: mouseEnter(event, numberOfColumn=1))
    for y in range(0, 6):
        imageLabels[1][y].bind("<Enter>", lambda event: mouseEnter(event, numberOfColumn=2))
    for y in range(0, 6):
        imageLabels[2][y].bind("<Enter>", lambda event: mouseEnter(event, numberOfColumn=3))
    for y in range(0, 6):
        imageLabels[3][y].bind("<Enter>", lambda event: mouseEnter(event, numberOfColumn=4))
    for y in range(0, 6):
        imageLabels[4][y].bind("<Enter>", lambda event: mouseEnter(event, numberOfColumn=5))
    for y in range(0, 6):
        imageLabels[5][y].bind("<Enter>", lambda event: mouseEnter(event, numberOfColumn=6))
    for y in range(0, 6):
        imageLabels[6][y].bind("<Enter>", lambda event: mouseEnter(event, numberOfColumn=7))
    

    # set mouse leave event
    for y in range(0, 6):
        imageLabels[0][y].bind("<Leave>", lambda event: mouseLeave(event, numberOfColumn=1))
    for y in range(0, 6):
        imageLabels[1][y].bind("<Leave>", lambda event: mouseLeave(event, numberOfColumn=2))
    for y in range(0, 6):
        imageLabels[2][y].bind("<Leave>", lambda event: mouseLeave(event, numberOfColumn=3))
    for y in range(0, 6):
        imageLabels[3][y].bind("<Leave>", lambda event: mouseLeave(event, numberOfColumn=4))
    for y in range(0, 6):
        imageLabels[4][y].bind("<Leave>", lambda event: mouseLeave(event, numberOfColumn=5))
    for y in range(0, 6):
        imageLabels[5][y].bind("<Leave>", lambda event: mouseLeave(event, numberOfColumn=6))
    for y in range(0, 6):
        imageLabels[6][y].bind("<Leave>", lambda event: mouseLeave(event, numberOfColumn=7))

    # set mouse click event
    for y in range(0, 6):
        imageLabels[0][y].bind("<Button-1>", lambda event: addPawn(event, numberOfColumn=1))
    for y in range(0, 6):
        imageLabels[1][y].bind("<Button-1>", lambda event: addPawn(event, numberOfColumn=2))
    for y in range(0, 6):
        imageLabels[2][y].bind("<Button-1>", lambda event: addPawn(event, numberOfColumn=3))
    for y in range(0, 6):
        imageLabels[3][y].bind("<Button-1>", lambda event: addPawn(event, numberOfColumn=4))
    for y in range(0, 6):
        imageLabels[4][y].bind("<Button-1>", lambda event: addPawn(event, numberOfColumn=5))
    for y in range(0, 6):
        imageLabels[5][y].bind("<Button-1>", lambda event: addPawn(event, numberOfColumn=6))
    for y in range(0, 6):
        imageLabels[6][y].bind("<Button-1>", lambda event: addPawn(event, numberOfColumn=7))

    for y in range(0, 6):
        imageLabels[0][y].bind("<Button-3>", lambda event: addPawn(event, numberOfColumn=1))
    for y in range(0, 6):
        imageLabels[1][y].bind("<Button-3>", lambda event: addPawn(event, numberOfColumn=2))
    for y in range(0, 6):
        imageLabels[2][y].bind("<Button-3>", lambda event: addPawn(event, numberOfColumn=3))
    for y in range(0, 6):
        imageLabels[3][y].bind("<Button-3>", lambda event: addPawn(event, numberOfColumn=4))
    for y in range(0, 6):
        imageLabels[4][y].bind("<Button-3>", lambda event: addPawn(event, numberOfColumn=5))
    for y in range(0, 6):
        imageLabels[5][y].bind("<Button-3>", lambda event: addPawn(event, numberOfColumn=6))
    for y in range(0, 6):
        imageLabels[6][y].bind("<Button-3>", lambda event: addPawn(event, numberOfColumn=7))

    # pause label
    pauseLbl = ctk.CTkLabel(master=gameFrame, text='', width=0)
    pauseLbl.grid(row=0, column=8)

def showWinGui(winner):
    # win frame
    winFrame = ctk.CTkFrame(master=gameGuiFrame)
    winFrame.place(x=429, rely=0.5, anchor=CENTER)

    # win label
    winLbl = ctk.CTkLabel(master=winFrame)
    winLbl.config(font=("Arial", 14))
    winLbl.pack(padx=15, pady=15)

    if currentData.currentGameType == 1:
        if winner == False:
            winLbl['text'] = "Red player win"
        else:
            winLbl['text'] = "Green player win"
    else:
        if winner == False:
            winLbl['text'] = "You win"
        else:
            winLbl['text'] = "AI win"

    # OK button
    okBtn = ctk.CTkButton(master=winFrame, text="OK", command=exitButton)
    okBtn.pack(padx=15, pady=15)

def showDrawGui():
    # draw frame
    drawFrame = ctk.CTkFrame(master=gameGuiFrame)
    drawFrame.place(x=429, rely=0.5, anchor=CENTER)

    # draw label
    drawLbl = ctk.CTkLabel(master=drawFrame, text="Draw")
    drawLbl.config(font=("Arial", 14))
    drawLbl.pack(padx=15, pady=15)

    # OK button
    okBtn = ctk.CTkButton(master=drawFrame, text="OK", command=exitButton)
    okBtn.pack(padx=15, pady=15)

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

def addPawn(event, numberOfColumn):
    global imageLabels

    if currentData.endGame == False:
        if currentData.currentGame[numberOfColumn - 1][0] == 0:
            # CURRENTGAME ARRAY ACTUALIZATION AND GAME LABELS IMAGES ACTUALIZATION
            if currentData.currentGame[numberOfColumn - 1][5] == 0:
                currentData.currentGame[numberOfColumn - 1][5] = int(currentData.currentPlayer) + 1
                if currentData.currentPlayer: # green
                    imageLabels[numberOfColumn - 1][5]['image'] = greenCircle
                else: # red
                    imageLabels[numberOfColumn - 1][5]['image'] = redCircle
            elif currentData.currentGame[numberOfColumn - 1][4] == 0:
                currentData.currentGame[numberOfColumn - 1][4] = int(currentData.currentPlayer) + 1
                if currentData.currentPlayer: # green
                    imageLabels[numberOfColumn - 1][4]['image'] = greenCircle
                else: # red
                    imageLabels[numberOfColumn - 1][4]['image'] = redCircle
            elif currentData.currentGame[numberOfColumn - 1][3] == 0:
                currentData.currentGame[numberOfColumn - 1][3] = int(currentData.currentPlayer) + 1
                if currentData.currentPlayer: # green
                    imageLabels[numberOfColumn - 1][3]['image'] = greenCircle
                else: # red
                    imageLabels[numberOfColumn - 1][3]['image'] = redCircle
            elif currentData.currentGame[numberOfColumn - 1][2] == 0:
                currentData.currentGame[numberOfColumn - 1][2] = int(currentData.currentPlayer) + 1
                if currentData.currentPlayer: # green
                    imageLabels[numberOfColumn - 1][2]['image'] = greenCircle
                else: # red
                    imageLabels[numberOfColumn - 1][2]['image'] = redCircle
            elif currentData.currentGame[numberOfColumn - 1][1] == 0:
                currentData.currentGame[numberOfColumn - 1][1] = int(currentData.currentPlayer) + 1
                if currentData.currentPlayer: # green
                    imageLabels[numberOfColumn - 1][1]['image'] = greenCircle
                else: # red
                    imageLabels[numberOfColumn - 1][1]['image'] = redCircle
            elif currentData.currentGame[numberOfColumn - 1][0] == 0:
                currentData.currentGame[numberOfColumn - 1][0] = int(currentData.currentPlayer) + 1
                if currentData.currentPlayer: # green
                    imageLabels[numberOfColumn - 1][0]['image'] = greenCircle
                else: # red
                    imageLabels[numberOfColumn - 1][0]['image'] = redCircle

            # WIN VALIDATION
            if  checksFunctions.checkWin(): # win
                showWinGui(currentData.currentPlayer)
                endGame()
            else:
                zeros = 0
                for x in range(0, 7):
                    for y in range(0, 6):
                        if currentData.currentGame[x][y] == 0:
                            zeros += 1

                if zeros == 0:
                    showDrawGui()
                    endGame()

            # REST
            if currentData.currentPlayer: # player green
                if currentData.currentGameType == 1:
                    currentPlayerLbl['image'] = redSmallCircle
            else: # player red
                if currentData.currentGameType == 1:
                    currentPlayerLbl['image'] = greenSmallCircle

            currentData.currentPlayer = not currentData.currentPlayer

            refreshCurrentRound()

            # AI PLAY (ONLY WHEN GAMETYPE == 2)
            if currentData.currentGameType == 2 and currentData.currentPlayer == True:
                if checksFunctions.checkChangeToWin(True) != 0:
                    addPawn(0, checksFunctions.checkChangeToWin(True))
                elif checksFunctions.checkChangeToWin(False) != 0:
                    addPawn(0, checksFunctions.checkChangeToWin(False))
                elif checksFunctions.checkBlock(False) != 0:
                    addPawn(0, checksFunctions.checkBlock(False))
                else:
                    global MLPmodels
                    MLPmodel = joblib.load('model.joblib')

                    predictInput = []
                    predictInput.append(currentData.roundNumber)
                    for y in range(0, 6):
                        for x in range(0, 7):
                            predictInput.append(currentData.currentGame[x][y])

                    predict = MLPmodel.predict([predictInput])

                    addPawn(0, predict[0])

        else:
            if currentData.currentPlayer == True:
                if numberOfColumn == 7:
                    addPawn(0, 1)
                else:
                    addPawn(0, numberOfColumn + 1)

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

def playerVSplayer():
    currentData.currentGameType = 1
    clearAllWidgets()
    clearAllParameters()
    showGameGui()

def playerVSai():
    currentData.currentGameType = 2
    clearAllWidgets()
    clearAllParameters()
    showGameGui()

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////

showMenuGui()
window.mainloop()