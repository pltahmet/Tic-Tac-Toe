from board import boardGame

game1 = boardGame()

while True:
    game1.showBoard()
    game1.player1Choice()
    game1.showBoard()
    if game1.gameState == 1:
        print("""********* \nPLAYER 1 WON\n*********""")
        break
    if game1.gameState == 2:
        print("""********* \nTHE GAME DRAW\n*********""")
        break
    game1.player2Choice()
    if game1.gameState == 1:
        game1.showBoard()
        print("""********* \nPLAYER 2 WON\n*********""")
        break
    if game1.gameState == 2:
        game1.showBoard()
        print("""********* \nTHE GAME DRAW\n*********""")
        break