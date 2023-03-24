INF = 100
TIE = "tie"
P1 = 'X'
P2 = 'O'

class Game:
    #creates a new instance of the game
    def __init__(self, state: str = "") -> None:
        self.state = ""
        if(len(state) < 9):
            for _ in range(9):
                self.state += ' '
        else:
            self.state = state
    

    def countFreePos(self) -> int:
        return self.state.count(' ')
    

    def isMovePossible(self, pos: int):
        if(self.state[pos] == ' '):
            return True
        return False


    def changeState(self, pos:int, team) -> None:
        new_state = ""
        for i in range(0, pos):
            new_state += self.state[i]
        new_state += team
        for i in range(pos+1, 9):
            new_state += self.state[i]
        self.state = new_state


    def getResult(self) -> str:
        """
            state:
            |---|---|---|
            | 0 | 1 | 2 |
            | 3 | 4 | 5 |
            | 6 | 7 | 8 |
            |---|---|---|        
        """
        #checks if somebody won
        if(self.state[0] != ' '):
            if(self.state[0] == self.state[1] and self.state[1] == self.state[2]): return self.state[0]
            if(self.state[0] == self.state[3] and self.state[3] == self.state[6]): return self.state[0]
        if(self.state[8] != ' '):
            if(self.state[6] == self.state[7] and self.state[7] == self.state[8]): return self.state[8]
            if(self.state[2] == self.state[5] and self.state[5] == self.state[8]): return self.state[8]
        if(self.state[4] != ' '):
            if(self.state[3] == self.state[4] and self.state[4] == self.state[5]): return self.state[4]
            if(self.state[1] == self.state[4] and self.state[4] == self.state[7]): return self.state[4]
            if(self.state[0] == self.state[4] and self.state[4] == self.state[8]): return self.state[4] 
            if(self.state[2] == self.state[4] and self.state[4] == self.state[6]): return self.state[4]
        
        #checks if it is a tie
        if((' ' in self.state) == False):
            return TIE
        return "continues"
    

    def getBestPos(self, ai, enemy) -> int:
        max_eval = (-1) * INF 
        best_pos = 0
        for i in range(9):
            if(self.isMovePossible(i) == False):
                continue
            new_game = Game(self.state)
            new_game.changeState(i, ai)
            curr_eval = new_game.__minmax(False, ai, enemy)
            
            if(curr_eval > max_eval):
                max_eval = curr_eval
                best_pos = i
        return best_pos
    
    
    def __minmax(self, is_maximizing: bool, ai, enemy) -> int: 
        game_res = self.getResult()
        if(game_res == ai):
            return 1 * (1 + self.countFreePos())
        if(game_res == enemy):
            return (-1) * (1 + self.countFreePos())
        if(game_res == TIE):
            return 0
        
        #chooses the best move for an AI
        if(is_maximizing):
            max_eval = (-1) * INF    
            for i in range(9):
                if(self.isMovePossible(i) == False):
                    continue
                new_game = Game(self.state)
                new_game.changeState(i, ai)

                curr_eval = new_game.__minmax(False, ai, enemy)
                max_eval = max(max_eval, curr_eval)
            return max_eval
        
        #chooses the best move for a player
        else:
            min_eval = INF
            for i in range(9):
                if(self.isMovePossible(i) == False):
                    continue
                new_game = Game(self.state)
                new_game.changeState(i, enemy)

                curr_eval = new_game.__minmax(True, ai, enemy)
                min_eval = min(min_eval, curr_eval)
            return min_eval
    