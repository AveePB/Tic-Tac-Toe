from app.TicTacToe import TicTacToe

import tkinter.messagebox as messagebox
import tkinter as tk


class MainWindow:
    
    def __init__(self, AIPlayerChar: str, humanPlayerChar: str) -> None:
        self.root = tk.Tk()
        self.btn = [tk.Button() for _ in range(9)]
        
        self.gameBoard = [" "] * 9
        self.playerAI = AIPlayerChar
        self.playerHuman = humanPlayerChar

        #sets the right init parameters to the buttons
        self.btn[0] = tk.Button(self.root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.buttonClick(0))
        self.btn[1] = tk.Button(self.root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.buttonClick(1))
        self.btn[2] = tk.Button(self.root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.buttonClick(2))
        self.btn[3] = tk.Button(self.root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.buttonClick(3))
        self.btn[4] = tk.Button(self.root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.buttonClick(4))
        self.btn[5] = tk.Button(self.root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.buttonClick(5))
        self.btn[6] = tk.Button(self.root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.buttonClick(6))
        self.btn[7] = tk.Button(self.root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.buttonClick(7))
        self.btn[8] = tk.Button(self.root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.buttonClick(8))

        #sets the postions of the buttons 
        self.btn[0].grid(row=0, column=0)
        self.btn[1].grid(row=0, column=1)
        self.btn[2].grid(row=0, column=2)
        self.btn[3].grid(row=1, column=0)
        self.btn[4].grid(row=1, column=1)
        self.btn[5].grid(row=1, column=2)
        self.btn[6].grid(row=2, column=0)
        self.btn[7].grid(row=2, column=1)
        self.btn[8].grid(row=2, column=2)

        #sets the esthetic parameters of the main window
        self.root.resizable(width=False, height=False)
        self.root.iconbitmap("./assets/img/icon.ico")
        self.root.title("Tic-Tac-Toe")


    def __restartGame(self) -> None:
        for btn in self.btn:
            btn["text"] = " "
        self.gameBoard = [" "] * 9 


    def __askToTryAgain(self) -> None:
        return messagebox.askyesno("Question", "Do you want to try again?")


    def buttonClick(self, pos: int) -> None:
        print(pos)
        #Player's turn
        if (self.btn[pos]["text"] == " "):
            self.gameBoard[pos] = self.playerHuman
            self.btn[pos]["text"] = self.playerHuman
            isOver = False 

            if (TicTacToe.isWin(self.playerHuman, self.gameBoard)):
                messagebox.showinfo("Tic-Tac-Toe", "Congratulations, you WON!!!")
                isOver = True

            elif (TicTacToe.isWin(self.playerAI, self.gameBoard)):
                messagebox.showinfo("Tic-Tac-Toe", "YOU LOST!!!")
                isOver = True

            elif (TicTacToe.isTie(self.playerHuman, self.playerAI, self.gameBoard)):
                messagebox.showinfo("Tic-Tac-Toe", "TIE!!!")
                isOver = True

            if (isOver):
                if (self.__askToTryAgain()):
                    self.__restartGame()
                else:
                    self.root.quit()
                return
            
        else:
            messagebox.showerror("Tic-Tac-Toe", "Hi! This field has already been selected.\n Please pick another one")
            return

        #AI's turn
        bestPos = TicTacToe.getBestMove(self.playerAI, self.gameBoard)
        
        self.gameBoard[bestPos] = self.playerAI
        self.btn[bestPos]["text"] = self.playerAI

        if (TicTacToe.isWin(self.playerHuman, self.gameBoard)):
            messagebox.showinfo("Tic-Tac-Toe", "Congratulations, you WON!!!")
            isOver = True

        elif (TicTacToe.isWin(self.playerAI, self.gameBoard)):
            messagebox.showinfo("Tic-Tac-Toe", "YOU LOST!!!")
            isOver = True

        elif (TicTacToe.isTie(self.playerHuman, self.playerAI, self.gameBoard)):
            messagebox.showinfo("Tic-Tac-Toe", "TIE!!!")
            isOver = True

        if (isOver):
            if (self.__askToTryAgain()):
                self.__restartGame()
            else:
                self.root.quit()
            return
    

    def open(self) -> None:
        self.root.mainloop()