board=   ["-","-","-", 
          "-","-","-", 
          "-","-","-"] 
 
currentPlayer = "X" 
winner = None 
gameRunner = True 
 
#printing game board------------------------------------------- 
def printBoard(board): 
    print(board[0] + " | " + board[1] + " | " + board[2]) 
    print("---------") 
    print(board[3] + " | " + board[4] + " | " + board[5]) 
    print("---------") 
    print(board[6] + " | " + board[7] + " | " + board[8]) 
     
#TAKE PLAYER INPUT--------------------------------------------- 
def playerinput(board): 
    inp = int(input("Enter a number from 1 to 9::")) 
    if inp >= 1 and inp <= 9 and board[inp-1] == "-": 
        board[inp-1] = currentPlayer 
    else: 
        print("Oops player is already in::") 
 
#check for win (horizontally) 
def checkHorizontel(board): 
    global winner 
    if board[0] == board[1] == board[2] and board[1] != "-": 
        winner = board[0] 
        return True 
    elif board[3] == board[4] == board[5] and board[3] != "-": 
        winner = board[3] 
        return True   
    elif board[6] == board[7] == board[8] and board[6] != "-": 
        winner = board[6] 
        return True        
     
#check for win (vertically) 
def chechRow(board): 
    global winner 
    if board[0] == board[3] == board[6] and board[0] != "-": 
         winner = board[0] 
         return True 
    elif board[1] == board[4] == board[7] and board[1] != "-": 
         winner = board[1] 
         return True   
    elif board[2] == board[5] == board[8] and board[2] != "-": 
         winner = board[2] 
         return True   
 
#check for win (dioganal) 
def checkDiago(board): 
     global winner 
     if board[0] == board[4] == board[8] and board[0] != "-": 
         winner = board[0] 
         return True 
     elif board[2] == board[4] == board[6] and board[2] != "-": 
         winner = board[2] 
         return True   
      
#check for tie 
def checkTie(board): 
    if "-" not in board: 
        printBoard(board) 
        print("------------------------") 
        print("GAME TIE") 
        print("------------------------") 
        gameRunner = False 
 
#check for winner 
def checkWin(): 
    if checkDiago(board) or checkHorizontel(board) or chechRow(board): 
        print(f"the winner is {winner}") 
 
#switching player 
def switchPlayer(): 
    global currentPlayer 
    if currentPlayer == "X": 
        currentPlayer = "O" 
    else: 
        currentPlayer = "X" 
 
while gameRunner:  
   printBoard(board) 
   if winner != None: 
       print(f"the winner is {winner}") 
       break 
   playerinput(board) 
   checkWin() 
   checkTie(board) 
   switchPlayer()
