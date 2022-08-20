from tkinter import *
from functools import partial
#from pydub import AudioSegment
#from pydub.playback import play

# Rule Change:
# the player must make a line with 5
class OmokOmokTkInter:
    def __init__(self):
        self.set = 0
        # player 1 = 1 & player 2 = -1
        self.cells = { }
        self.root = Tk()
        self.root.title("OMOK GAME")
        self.done = False

        self.eight = Button(self.root, text='8X8', width=25, command=lambda: self.setSet(8))
        self.nine= Button(self.root, text='9X9', width=25, command=lambda: self.setSet(9))
        self.ten = Button(self.root, text='10X10', width=25, command=lambda: self.setSet(10))


    def setSet(self, set):
        self.set = set
        self.omokTable = [[0 for i in range(self.set)] for j in range(self.set)]
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

    def checkCross1(self):
        stones11 = 0
        stones12 = 0
        stones21 = 0
        stones22 = 0
        for i in range(self.set - 4):
            for j in range(self.set - i):
                if self.omokTable[i + j][j] == 1:
                    stones11 += 1
                    stones21 = 0

                elif self.omokTable[i + j][j] == -1:
                    stones21 += 1
                    stones11 = 0

                else:
                    stones11 = 0
                    stones21 = 0
                if self.omokTable[j][i + j] == 1:
                    stones12 += 1
                    stones22 = 0
                elif self.omokTable[j][i + j] == -1:
                    stones22 += 1
                    stones12 = 0
                else:
                    stones12 = 0
                    stones22 = 0
                if stones11 == 5 or stones21 == 5:
                    self.identifyPlayer(stones11, stones21)
                    return True
                if stones12 == 5 or stones22 == 5:
                    self.identifyPlayer(stones12, stones22)
                    return True

        return False

    def checkCross2(self):
        stones11 = 0
        stones21 = 0
        stones12 = 0
        stones22 = 0
        for i in range(self.set - 4):
            for j in range(self.set - i):
                if self.omokTable[i + j][self.set - 1 - j] == 1:
                    stones11 += 1
                    stones21 = 0

                elif self.omokTable[i + j][self.set - 1 - j] == -1:
                    stones21 += 1
                    stones11 = 0
                else:
                    stones11 = 0
                    stones21 = 0
                if self.omokTable[j][self.set - 1 - j - i] == 1:
                    stones12 += 1
                    stones22 = 0
                elif self.omokTable[j][self.set - 1 - j - i] == -1:
                    stones22 += 1
                    stones12 = 0
                else:
                    stones12 = 0
                    stones22 = 0
                if stones12 == 5 or stones22 == 5:
                    self.identifyPlayer(stones12, stones22)
                    return True
                if stones11 == 5 or stones21 == 5:
                    self.identifyPlayer(stones11, stones21)
                    return True

        return False

    def checkWin(self):
        if self.drew():
            d = Label(self.root, text="Drew", font=('Aerial 17 bold italic'))
            d.grid()
            return True

        if self.checkCross1() or self.checkCross2():
            return True

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
                else:
                    win1C = 0
                    win2C = 0
                if win1C == 5 or win2C == 5:
                    self.identifyPlayer(win1C, win2C)
                    return True

        for i in range(self.set):
            win1R = 0
            win2R = 0
            for j in range(self.set):
                if self.omokTable[j][i] == 1:
                    win1R += 1
                    win2R = 0
                elif self.omokTable[j][i] == -1:
                    win2R += 1
                    win1R = 0
                else:
                    win1R = 0
                    win2R = 0
                if win1R == 5 or win2R == 5:
                    self.identifyPlayer(win1R, win2R)
                    return True

        return False

    def forgets(self):
        self.eight.grid_forget()
        self.nine.grid_forget()
        self.ten.grid_forget()

    def showTable(self):
        center = Frame(self.root, bg='white', width=500, height=500, padx=2, pady=2)
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
                                   width=3, height=3, padx=3, pady=3,
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

                else:
                    bname.configure(text="X")
                    self.omokTable[row][column] = -1


                if self.checkWin():
                    l2 = Label(self.root, text="Game End!", font=('Aerial 17 bold italic'))
                    l2.grid()

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


        self.eight.grid()
        self.nine.grid()
        self.ten.grid()

    def gameStart(self):
        self.askSet()
        self.root.mainloop()

