# tictactoe
tictactoe using python

The first part of the code defines the game board as a list of strings, with "-" representing an empty slot. It also initializes variables such as the current player, winner, and gameRunner.
The code then defines various functions for the game, such as printBoard(), which prints the current state of the game board, playerinput(), which takes the user's input and places their symbol (either X or O) on the board if it is a valid move, checkHorizontel(), checkRow(), and checkDiago(), which check for horizontal, vertical, and diagonal wins, respectively. 
The checkTie() function checks if the game has resulted in a tie. The checkWin() function calls these functions and checks if a winner has been found.
Finally, there is a loop that runs the game while gameRunner is True. It calls the printBoard() function to print the current state of the game board, calls playerinput() to get the player's move, checks for a winner with checkWin(), checks for a tie with checkTie(), and switches the current player with switchPlayer().
Overall, this code allows two players to play Tic Tac Toe against each other in the console. It keeps track of the state of the game, checks for wins and ties, and allows players to take turns placing their symbol on the board.

   +--------+       +-------------------+
   | Start  |------>| printBoard(board)  |
   +--------+       +-------------------+
         |                         |
         |                         |
         v                         v
   +--------+             +-----------------------+
   | winner |<------------| checkHorizontel(board) |
   +--------+             +-----------------------+
         |                         |
         |                         |
         v                         v
   +--------+             +---------------------+
   | winner |<------------| chechRow(board)      |
   +--------+             +---------------------+
         |                         |
         |                         |
         v                         v
   +--------+             +---------------------+
   | winner |<------------| checkDiago(board)    |
   +--------+             +---------------------+
         |                         |
         |                         |
         v                         v
   +--------+             +---------------------+
   |        |<------------| checkTie(board)      |
   |        |             +---------------------+
   |        |                         |
   |        |                         |
   | Yes    |                         | No
   v        v                         v
+--------+  +----------+         +------------+
| Print  |  | Switch   |         | playerInput |
| winner |  | player   |         +------------+
+--------+  +----------+                 |
      |             |                     |
      |             v                     v
      |         +--------+           +--------------+
      +-------->| winner |<----------| checkWin()   |
                +--------+           +--------------+
                       |                     |
                       |                     |
                       v                     v
                 +-------+            +---------------+
                 |  End  |            |  Switch player|
                 +-------+            +---------------+


