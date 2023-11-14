from app.MainWindow import MainWindow

PLAYER_HUMAN = 'O'
PLAYER_AI = 'X'

if __name__ == "__main__":
    mainWindow = MainWindow(PLAYER_AI, PLAYER_HUMAN)
    mainWindow.open()