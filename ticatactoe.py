import random
import copy


gameBoard = []
row = []

for i in range(3):
  row = []
  for j in range(3):
    row.append(" ")
  gameBoard.append(row)

def printBoard(gameBoard):
  for i in range(3):
    for j in range(3):
      print(" " + gameBoard[i][j], end = " ")
      if j < 2:
        print("|", end = "")
    print()
    if i < 2:
      print("---+---+---")


firstTurn = random.randint(1,2)

def scoring(gameBoard, player):
  if gameBoard[0][0] == gameBoard[0][1] == gameBoard[0][2] == player:
    return True
  if gameBoard[1][0] == gameBoard[1][1] == gameBoard[1][2] == player:
    return True
  if gameBoard[2][0] == gameBoard[2][1] == gameBoard[2][2] == player:
    return True
  if gameBoard[0][0] == gameBoard[1][0] == gameBoard[2][0] == player:
    return True
  if gameBoard[0][1] == gameBoard[1][1] == gameBoard[2][1] == player:
    return True
  if gameBoard[0][2] == gameBoard[1][2] == gameBoard[2][2] == player:
    return True
  if gameBoard[0][0] == gameBoard[1][1] == gameBoard[2][2] == player:
    return True
  if gameBoard[0][2] == gameBoard[1][1] == gameBoard[2][0] == player:
    return True
    
  return False

def compTryToWin(gameBoard):
  for i in range(len(gameBoard)):
    for j in range(len(gameBoard[i])):
      newGrid = copy.deepcopy(gameBoard)
      newGrid[i][j] = "X"
      # print("NewGrid: ")
      # print(newGrid)
      if scoring(newGrid, "X") == True and gameBoard[i][j] != "X" and gameBoard[i][j] != "O":
        gameBoard[i][j] = "X"
        return True
  
  return False

def compStoppingWin(gameBoard):
  for i in range(len(gameBoard)):
    for j in range(len(gameBoard[i])):
      newGrid = copy.deepcopy(gameBoard)
      newGrid[i][j] = "O"
      if scoring(newGrid, "O") == True and gameBoard[i][j] != "X" and gameBoard[i][j] != "O":
        gameBoard[i][j] = "X"
        return True
        
  return False

def compPlayInCenter(gameBoard):
  if gameBoard[1][1] != "X" and gameBoard[1][1] != "O":
    gameBoard[1][1] = "X"
    return True
  else:
    return False

turnCounter = 0
while turnCounter < 9:
  printBoard(gameBoard)
  print()
  if firstTurn == 1:
    while True:
      winningResult = compTryToWin(gameBoard)
      if winningResult == True:
        break
      else:
        stoppingWinResult = compStoppingWin(gameBoard)
        if stoppingWinResult == True:
          break
        else:
          playInCenterResult = compPlayInCenter(gameBoard)
          if playInCenterResult == True:
            break
          else:
            column = random.randint(0,2)
            row = random.randint(0,2)
            if gameBoard[row][column] != "X" and gameBoard[row][column] != "O":
              gameBoard[row][column] = "X"
              break
    if scoring(gameBoard, "X") == True:
      print("Player X won the game!")
      break
    turnCounter += 1
    firstTurn = 2
  else:
    while True:
        row = int(input("Enter the row of the place you want to play: "))
        column = int(input("Enter the column of the place you want to play: "))
        if gameBoard[row - 1][column - 1] != "X" and gameBoard[row - 1][column - 1] != "O":
            gameBoard[row - 1][column - 1] = "O"
            break
        print("That square is already occupied. Pick another square.")
    if scoring(gameBoard, "O") == True:
        print("Player O won the game!")
        break
    else:
        turnCounter += 1
        firstTurn = 1

printBoard(gameBoard)

if turnCounter == 9:
    print("Nice Job! There was a draw!")