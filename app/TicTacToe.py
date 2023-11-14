
class TicTacToe:
    #Constants:
    INF = 100000000 

    UNPLACED = 0
    PLAYER_HUMAN = 1
    PLAYER_AI = 2

    def __minmax(player: int, board: list) -> int:
        """
        Returns the minmax score.
        """
        if (TicTacToe.isWin(TicTacToe.PLAYER_HUMAN, board)):
            return -(board.count(TicTacToe.UNPLACED) + 1)

        if (TicTacToe.isWin(TicTacToe.PLAYER_AI, board)):
            return board.count(TicTacToe.UNPLACED) + 1

        if (TicTacToe.isTie(TicTacToe.PLAYER_HUMAN, TicTacToe.PLAYER_AI, board)):
            return 0
        
        #Minimizing (HUMAN)
        if (player == TicTacToe.PLAYER_HUMAN):
            minScore = TicTacToe.INF

            for i in range(9):
                if (board[i] != TicTacToe.UNPLACED):
                    continue

                board[i] = TicTacToe.PLAYER_HUMAN
                minScore = min(minScore, TicTacToe.__minmax(TicTacToe.PLAYER_AI, board))
                board[i] = TicTacToe.UNPLACED
                
            return minScore
        
        #Maximizing (AI)
        else:
            maxScore = -TicTacToe.INF

            for i in range(9):
                if (board[i] != TicTacToe.UNPLACED):
                    continue

                board[i] = TicTacToe.PLAYER_AI
                maxScore = max(maxScore, TicTacToe.__minmax(TicTacToe.PLAYER_HUMAN, board))
                board[i] = TicTacToe.UNPLACED

            return maxScore


    def isWin(player: str, board: list) -> bool:
        """
        Checks if the current game state is a win.
        """
        if(board[0] == player):
            if(board[0] == board[1] and board[1] == board[2]): return True
            if(board[0] == board[3] and board[3] == board[6]): return True
        if(board[8] == player):
            if(board[6] == board[7] and board[7] == board[8]): return True
            if(board[2] == board[5] and board[5] == board[8]): return True
        if(board[4] == player):
            if(board[3] == board[4] and board[4] == board[5]): return True
            if(board[1] == board[4] and board[4] == board[7]): return True
            if(board[0] == board[4] and board[4] == board[8]): return True
            if(board[2] == board[4] and board[4] == board[6]): return True

        return False
    

    def isTie(player1: str, player2: str, board: list) -> bool:
        """
        Checks if the current game state is a tie.
        """
        if (TicTacToe.isWin(player1, board) or TicTacToe.isWin(player2, board)):
            return False
        
        return (board.count(player1) + board.count(player2) == 9)


    def getBestMove(AISign: str, board: list):
        """
        Returns the best position for the AI player.
        """
        convertedBoard = []

        for sign in board:
            if (sign == AISign):
                convertedBoard.append(TicTacToe.PLAYER_AI)
            elif (sign == ' '):
                convertedBoard.append(TicTacToe.UNPLACED)
            else:
                convertedBoard.append(TicTacToe.PLAYER_HUMAN)
        
        move = -1 
        maxScore = -TicTacToe.INF

        for i in range(9):
            if (convertedBoard[i] != TicTacToe.UNPLACED):
                continue

            convertedBoard[i] = TicTacToe.PLAYER_AI
            currScore = TicTacToe.__minmax(TicTacToe.PLAYER_HUMAN, convertedBoard)
            convertedBoard[i] = TicTacToe.UNPLACED

            if (currScore > maxScore):
                maxScore = currScore
                move = i

        return move