from tkinter import *
from tkinter import messagebox
from functools import partial
class OmokTkInter:
    def __init__(self, set):
        self.set = set
        self.omokTable = [[0 for i in range(self.set)] for j in range(self.set)]
        # player 1 = 1 & player 2 = -1
        self.cross1 = []
        self.cross2 = []
        self.cells = { }
        self.root = Tk()
        self.root.title("OMOK GAME")
        self.size = ""

        if self.set == 5:
            self.space = '600x600'
        elif self.set == 6:
            self.space = '700x700'
        else:
            self.space = '800x800'

        self.root.geometry(self.space)

        for i in range(self.set):
            for j in range(self.set):
                if (i == j):
                    self.cross1.append(self.omokTable[i][j])
                if (i + j) == (self.set - 1):
                    self.cross2.append(self.omokTable[i][j])

    def checkPlace(self, p, n):
        ap = -1
        if n > self.set:
            return -1

        for i in range(self.set + 1):
            if self.alp[i] == p:
                ap = i
                break

        if ap == -1:
            return -1

        elif self.omokTable[n - 1][ap - 1] != 0:
            print("Taken Seat")
            return -1
        return ap

    def checkWin(self):
        d = 0
        for i in self.omokTable:
            if all(element != 0 for element in i):
                d += 1
        if d == 5:
            self.drew()
            return True
        if 0 not in self.cross1:
            return all(element == self.cross1[0] for element in self.cross1)
        if 0 not in self.cross2:
            return all(element == self.cross2[0] for element in self.cross2)
        win1C = 0
        win2C = 0
        for i in range(self.set):
            for j in range(self.set):
                if j == 0:
                    win1C = 0
                    win2C = 0
                if self.omokTable[i][j] == 1:
                    win2C = 0
                    win1C+= 1
                elif self.omokTable[i][j] == -1:
                    win1C = 0
                    win2C += 1
                if win1C == self.set or win2C == self.set:
                    print(self.omokTable, win1C, win2C)
                    print("WinC")
                    return True
        win1R = 0
        win2R = 0
        for i in range(self.set):
            for j in range(self.set):
                if i == 0:
                    win1R = 0
                    win2R = 0
                if self.omokTable[j][i] == 1:
                    win1R += 1
                    win2R = 0
                elif self.omokTable[j][i] == -1:
                    win2R += 1
                    win1R = 0
                if win1R == self.set or win2R == self.set:
                    print("WinR")
                    return True


        return False


    def showTable(self):

        # create all of the main containers
        l1 = Label(self.root, text="Welcome to Omok Game!", font=('Aerial 17 bold italic'))
        l1.grid()
        center = Frame(self.root, bg='white', width=900, height=900, padx=3, pady=3)

        # layout all of the main containers
        self.root.grid_rowconfigure(9, weight=1)
        self.root.grid_columnconfigure(9, weight=1)
        center.grid(row=1, sticky="nsew")

        # create the center widgets
        center.grid_rowconfigure(0, weight=1)
        center.grid_columnconfigure(1, weight=1)

        for row in range(5):
            for column in range(5):
                cell = Button(center, bg='white', highlightbackground="black",
                              highlightcolor="black", highlightthickness=1,
                              width=5, height=5, padx=3, pady=3, command=partial(self.gogoButton, row, column))
                cell.grid(row=row, column=column)
                self.cells[(row, column)] = cell

    def gogoButton(self, row, column):
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
        d = Label(self.root, text="Drew", font=('Aerial 17 bold italic'))
        d.grid()

    def gameStart(self):
        print("First player: O\nSecond player: X")
        self.showTable()

        self.root.mainloop()

