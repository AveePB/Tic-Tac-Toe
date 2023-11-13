from app.TicTacToe import TicTacToe

import tkinter.messagebox as messagebox
import tkinter as tk


PLAYER_HUMAN = 'O'
PLAYER_AI = 'X'

root = tk.Tk() #initializes the main window
btn = [tk.Button() for _ in range(9)]
gameBoard = [" "] * 9


def init():
    #sets the right init parameters to the buttons
    btn[0] = tk.Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: buttonClick(0))
    btn[1] = tk.Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: buttonClick(1))
    btn[2] = tk.Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: buttonClick(2))
    btn[3] = tk.Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: buttonClick(3))
    btn[4] = tk.Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: buttonClick(4))
    btn[5] = tk.Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: buttonClick(5))
    btn[6] = tk.Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: buttonClick(6))
    btn[7] = tk.Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: buttonClick(7))
    btn[8] = tk.Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: buttonClick(8))

    #sets the postions of the buttons 
    btn[0].grid(row=0, column=0)
    btn[1].grid(row=0, column=1)
    btn[2].grid(row=0, column=2)
    btn[3].grid(row=1, column=0)
    btn[4].grid(row=1, column=1)
    btn[5].grid(row=1, column=2)
    btn[6].grid(row=2, column=0)
    btn[7].grid(row=2, column=1)
    btn[8].grid(row=2, column=2)

    #sets the esthetic parameters of the main window
    root.resizable(width=False, height=False)
    root.iconbitmap("./assets/img/icon.ico")
    root.title("Tic-Tac-Toe")
    
def buttonClick(pos: int):
    
    #Player's turn
    if(btn[pos]["text"] == " "):
        gameBoard[pos] = PLAYER_HUMAN
        btn[pos]["text"] = PLAYER_HUMAN

        if(TicTacToe.isWin(PLAYER_HUMAN, gameBoard)):
            messagebox.showinfo("Tic-Tac-Toe", "Congratulations, you WON!!!")
            root.quit()
            return
        
        if(TicTacToe.isWin(PLAYER_AI, gameBoard)):
            messagebox.showinfo("Tic-Tac-Toe", "YOU LOST!!!")
            root.quit()
            return

        if(TicTacToe.isTie(PLAYER_HUMAN, PLAYER_AI, gameBoard)):
            messagebox.showinfo("Tic-Tac-Toe", "TIE!!!")
            root.quit()
            return
    else:
        messagebox.showerror("Tic-Tac-Toe", "Hi! This field has already been selected.\n Please pick another one")
        return

    #AI's turn
    bestPos = TicTacToe.getBestMove(PLAYER_AI, gameBoard)
    
    gameBoard[bestPos] = PLAYER_AI
    btn[bestPos]["text"] = PLAYER_AI

    if(TicTacToe.isWin(PLAYER_HUMAN, gameBoard)):
        messagebox.showinfo("Tic-Tac-Toe", "Congratulations, you WON!!!")
        root.quit()
        
    if(TicTacToe.isWin(PLAYER_AI, gameBoard)):
        messagebox.showinfo("Tic-Tac-Toe", "YOU LOST!!!")
        root.quit()

    if(TicTacToe.isTie(PLAYER_HUMAN, PLAYER_AI, gameBoard)):
        messagebox.showinfo("Tic-Tac-Toe", "TIE!!!")
        root.quit()

if __name__ == "__main__":
    init()
    root.mainloop()