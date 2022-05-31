# GENERAL
roundNumber = 1
currentPlayer = False  # False = player 1 (red), True = plaer 2 (green)
endGame = False

currentGameInString = []

currentGame = [[0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0]]  # max 42

# SETTINGS
darkMode = 0
currentGameType = 1 # 1 = playerVSplayer, 2 = playerVSai

# game TABLE in database:
# gameID INTEGER,
# roundID INTEGER,
# player TINYINT,
# A1 TINYINT, A2 TINYINT, A3 TINYINT, A4 TINYINT, A5 TINYINT, A6 TINYINT,
# B1 TINYINT, B2 TINYINT, B3 TINYINT, B4 TINYINT, B5 TINYINT, B6 TINYINT,
# C1 TINYINT, C2 TINYINT, C3 TINYINT, C4 TINYINT, C5 TINYINT, C6 TINYINT,
# D1 TINYINT, D2 TINYINT, D3 TINYINT, D4 TINYINT, D5 TINYINT, D6 TINYINT,
# E1 TINYINT, E2 TINYINT, E3 TINYINT, E4 TINYINT, E5 TINYINT, E6 TINYINT,
# F1 TINYINT, F2 TINYINT, F3 TINYINT, F4 TINYINT, F5 TINYINT, F6 TINYINT,
# G1 TINYINT, G2 TINYINT, G3 TINYINT, G4 TINYINT, G5 TINYINT, G6 TINYINT,
# decision TINYINT

# winner TABLE:
# gameID INTEGER,
# player TINYINT