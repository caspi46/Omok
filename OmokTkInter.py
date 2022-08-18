from tkinter import *
from functools import partial

class OmokTkInter:
    def __init__(self):
        self.set = 0
        # player 1 = 1 & player 2 = -1
        self.cross1 = []
        self.cross2 = []
        self.cells = { }
        self.root = Tk()
        self.root.title("OMOK GAME")
        self.done = False

        self.five = Button(self.root, text='7X7', width=25, command=lambda: self.setSet(7))
        self.six = Button(self.root, text='8X8', width=25, command=lambda: self.setSet(8))
        self.seven = Button(self.root, text='9X9', width=25, command=lambda: self.setSet(9))




    def setSet(self, set):
        self.set = set
        self.omokTable = [[0 for i in range(self.set)] for j in range(self.set)]
        for i in range(self.set):
            for j in range(self.set):
                if (i == j):
                    self.cross1.append(self.omokTable[i][j])
                if (i + j) == (self.set - 1):
                    self.cross2.append(self.omokTable[i][j])
        self.forgets()
        self.showTable()


    def identifyPlayer(self, p1, p2):
        self.done = True
        if p1 == self.set:
            winPlayer1 = Label(self.root, text="Player 1 Won", font=('Aerial 17 bold italic'))
            winPlayer1.grid()
        elif p2 == self.set:
            winPlayer2 = Label(self.root, text="Player 2 Won",  font=('Aerial 17 bold italic'))
            winPlayer2.grid()

    def checkCross(self, n):
        if n == 1:
            checkList = self.cross1
        else:
            checkList = self.cross2
        if 0 not in checkList and all(element == checkList[0] for element in checkList):
            if checkList[0] == 1:
                self.identifyPlayer(self.set, 0)
            elif checkList[0] == -1:
                self.identifyPlayer(0, self.set)
            return True

    def checkWin(self):
        if self.drew():
            d = Label(self.root, text="Drew", font=('Aerial 17 bold italic'))
            d.grid()
            return True

        self.checkCross(1)
        self.checkCross(-1)

        for i in range(self.set):
            win1C = 0
            win2C = 0
            for j in range(self.set):
                if self.omokTable[i][j] == 1:
                    win2C = 0
                    win1C+= 1
                elif self.omokTable[i][j] == -1:
                    win1C = 0
                    win2C += 1
                if win1C == self.set or win2C == self.set:
                    print("winC")
                    self.identifyPlayer(win1C, win2C)
                    return True

        for i in range(self.set):
            win1R = 0
            win2R = 0
            for j in range(self.set):
                if self.omokTable[j][i] == 1:
                    win1R += 1
                elif self.omokTable[j][i] == -1:
                    win2R += 1
                if win1R == self.set or win2R == self.set:
                    print("winR")
                    self.identifyPlayer(win1R, win2R)
                    return True

        return False

    def forgets(self):
        self.five.grid_forget()
        self.six.grid_forget()
        self.seven.grid_forget()

    def showTable(self):
        center = Frame(self.root, bg='white', width=900, height=900, padx=3, pady=3)
        # layout all of the main containers
        self.root.grid_rowconfigure(9, weight=1)
        self.root.grid_columnconfigure(9, weight=1)
        center.grid(row=1, sticky="nsew")

        # create the center widgets
        center.grid_rowconfigure(0, weight=1)
        center.grid_columnconfigure(1, weight=1)

        for row in range(self.set):
            for column in range(self.set):
                self.cell = Button(center, bg='white', highlightbackground="black",
                                   highlightcolor="black", highlightthickness=1,
                                   width=5, height=5, padx=3, pady=3,
                                   command=partial(self.gogoButton, row, column))
                self.cell.grid(row=row, column=column)
                self.cells[(row, column)] = self.cell

        l3 = Label(self.root, text="Player 1: O\nPlayer 2: X")
        l3.grid()





    def gogoButton(self, row, column):
        if self.done == False:
            bname = (self.cells[(row, column)])
            if self.omokTable[row][column] == 0:
                if self.checkPlayer():
                    bname.configure(text="O")
                    self.omokTable[row][column] = 1
                    self.addCross(1, row, column)
                else:
                    bname.configure(text="X")
                    self.omokTable[row][column] = -1
                    self.addCross(-1, row, column)

                if self.checkWin():
                    l2 = Label(self.root, text="Game End!", font=('Aerial 17 bold italic'))
                    l2.grid()

    def addCross(self, player, row, column):
        if row == column:
            self.cross1[row] = player
        if (row + column) == (self.set - 1):
            self.cross2[row] = player

    def checkPlayer(self): # identify player
        numTaken = 0
        for i in self.omokTable:
            for j in i:
                if j == -1 or j == 1:
                    numTaken += 1
        if numTaken % 2 == 0: # player 1
            return True
        else: # player 2
            return False

    def drew(self):
        d = 0
        for i in self.omokTable:
            if not all(element != 0 for element in i):
                return False
            d += 1
        if d == 5:
            for i in self.omokTable:
                print(i)
            return True
        return False

    def askSet(self):
        l1 = Label(self.root, text="Welcome to Omok Game!", font=('Aerial 17 bold italic'))
        l1.grid()

        l2 = Label(self.root, text= "Click Set:")
        l2.grid()


        self.five.grid()
        self.six.grid()
        self.seven.grid()

    def gameStart(self):
        self.askSet()
        self.root.mainloop()



