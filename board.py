class boardGame:
    
    def __init__(self):
        self.board = [[" 1 " , " 2 " , " 3 "] , [" 4 " , " 5 " , " 6 "] , [" 7 " , " 8 " , " 9 "]]
        self.gameState = -1

    #newGame

    #showBoard
    def showBoard(self):
        for row in range(3):
            for column in range(3):
                print(self.board[row][column], end=' ')
            print()


    #checkEmpty
    def checkEmpty(self,row,column):
        # if(select == "1" or select == "2" or select == "3"):
        #     satır = 0
        # elif(select == "4" or select == "5" or select == "6"):
        #     satır = 1
        # elif(select == "7" or select == "8" or select == "9"):
        #     satır = 2
        # if(select == "1" or select == "4" or select == "7"):
        #     column = 0
        # elif(select == "2" or select == "5" or select == "8"):
        #     column = 1
        # elif(select == "3" or select == "6" or select == "9"):
        #     column = 2
        # else:
        #     print("Doğru tuşlama yapmadınız")
        #     return False
        if(self.board[row][column] == " X " or self.board[row][column] == " O "):
            return False
        else: 
            return True


    #checkWin
    def checkWin(self,row,column):
        if self.board[row][0] == self.board[row][1] == self.board[row][2]:
            self.gameState = 1
            return 0
        if self.board[0][column] == self.board[1][column] == self.board[2][column]:
            self.gameState = 1
            return 0
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            self.gameState = 1
            return 0
        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            self.gameState = 1
            return 0

        #checkDraw
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != " X " and self.board[i][j] != " O ":
                    self.gameState = 0
                    return 0                
        self.gameState = 2


    #p1
    def player1Choice(self):
        select = input("Select a box for X")
        if(select == "1" or select == "2" or select == "3"):
            row = 0
        elif(select == "4" or select == "5" or select == "6"):
            row = 1
        elif(select == "7" or select == "8" or select == "9"):
            row = 2
        if(select == "1" or select == "4" or select == "7"):
            column = 0
        elif(select == "2" or select == "5" or select == "8"):
            column = 1
        elif(select == "3" or select == "6" or select == "9"):
            column = 2
        else:
            print("Invalid move")
            self.player1Choice()
        if self.checkEmpty(row,column):
            self.board[row][column] = " X "
        else:
            print("This box is not empty")
            self.player1Choice()
        self.checkWin(row,column)


    #p2
    def player2Choice(self):
        select = input("Select a box for O")
        if(select == "1" or select == "2" or select == "3"):
            row = 0
        elif(select == "4" or select == "5" or select == "6"):
            row = 1
        elif(select == "7" or select == "8" or select == "9"):
            row = 2
        if(select == "1" or select == "4" or select == "7"):
            column = 0
        elif(select == "2" or select == "5" or select == "8"):
            column = 1
        elif(select == "3" or select == "6" or select == "9"):
            column = 2
        else:
            print("Invalid move")
            self.player2Choice()
        if self.checkEmpty(row,column):
            self.board[row][column] = " O "
        else:
            print("This box is not empty")
            self.player2Choice()
        self.checkWin(row,column)

