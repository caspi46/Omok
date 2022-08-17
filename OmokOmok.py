#OmokOmok class
class OmokOmok:
    def __init__(self, s):
        self.set = s # set (s x s table)
        self.alp = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G'] # 
        self.omokTable = [[0 for i in range(self.set)] for j in range(self.set)] # omok table 
        # player 1 = 1 & player 2 = -1
        self.cross1 = [ ]
        self.cross2 = [ ]
        for i in range(self.set):
            for j in range(self.set):
                if (i == j):
                    self.cross1.append(self.omokTable[i][j])
                if (i + j) == (self.set - 1):
                    self.cross2.append(self.omokTable[i][j])

    # Function: checkBool
    # Parameters: row & column
    # check if the position is taken by player
    # display u if player 1
    # display n if player 2
    # display * if no one 
    def checkBool(self, i, j):
        if self.omokTable[i][j] == 1:
            print("u\t", end="")
            return
        elif self.omokTable[i][j] == -1:
            print("n\t", end="")
            return
        print("*\t", end="")

    # Function: makeTable
    # parameter: None
    # display the table 
    def makeTable(self):
        for i in range(self.set + 1):
            for j in range(self.set + 1):
                if i == 0:
                    print(self.alp[j] + "\t", end = "")
                elif j == 0:
                    print(i, "\t", end = "")
                else:
                    self.checkBool(i - 1, j - 1)
            print("\n", end = "")
    
    # Function: checkPlace
    # parameters: p : alphabet & n: number
    # check if the place is already taken or not
    def checkPlace(self, p, n):
        ap = -1
        if n > self.set: # if the number that the user entered is the out of the range
            return -1

        for i in range(self.set + 1): 
            if self.alp[i] == p: # if the alphabet the user entered is not out of the range
                ap = i
                break

        if ap == -1: # the alphabet the user entered is out of the range
            return -1

        if self.omokTable[n - 1][ap - 1] != 0: # if the place is alraedy taken
            print("Taken Seat")
            return -1
        
        return ap
    
    # Function: askPlace
    # parameter: None
    #. aks the user the place they want to take 
    def askPlace(self):
        for i in range(2):
            place = str(input("Enter place (Ex - A1, C4):"))
            while len(place) != 2: # if the user entered invalid input
                print("Error, the name must be included one alphabet & integer")
                place = str(input("Enter place (Ex - A1, C4):"))
            n = int(place[1])
            ap = self.checkPlace(place[0], n)
            while(ap == -1): # if the user entered invalid input
                print("Error, the place is already taken, choose other place")
                place = str(input("Enter place (Ex - A1, C4):"))
                n = int(place[1])
                ap = self.checkPlace(place[0], n)
    
            if i == 0: # player 1
                self.omokTable[n - 1][ap - 1] = 1
                self.addCross(1, n - 1, ap - 1)
            else: # player 2
                self.omokTable[n - 1][ap - 1] = -1
                self.addCross(-1, n - 1, ap -1)
    
    # Function: checkWin
    # Parameter: None
    # check if some player won (or drew)
    def checkWin(self):
        # check if they drew
        if self.drew():
            print("Drew")
            return True
        
        # check crosses
        if 0 not in self.cross1:
            return all(element == self.cross1[0] for element in self.cross1)
        if 0 not in self.cross2:
            return all(element == self.cross2[0] for element in self.cross2)
        # check ranks
        win1C = 0
        win2C = 0
        for i in range(self.set):
            for j in range(self.set):
                if j == 0:
                    win1C = 0
                    win2C = 0
                if self.omokTable[i][j] == 1:
                    win1C+= 1
                elif self.omokTable[i][j] == -1:
                    win2C += 1
                if win1C == self.set or win2C == self.set:
                    return True
                
        # check stripes
        win1R = 0
        win2R = 0
        for i in range(self.set):
            for j in range(self.set):
                if i == 0:
                    win1R = 0
                    win2R = 0
                if self.omokTable[j][i] == 1:
                    win1R+= 1
                elif self.omokTable[j][i] == -1:
                    win2R += 1
                if win1R == self.set or win2R == self.set:
                    return True
                
    # Function: addCross
    # Parameters: player (int), row (int), column (int)
    # if the place that the user picked is in the cross
    # replace to the player number (1 or -1)
    def addCross(self, player, row, column):
        if row == column:
            self.cross1[row] = player
        if (row + column) == (self.set - 1):
            self.cross2[row] = player
    
    # Function: drew
    # Parameter: None
    # check if the game is drew or not
    def drew(self):
        d = 0
        for i in self.omokTable:
            if all(element != 0 for element in i):
                d += 1
        if d == 5:
            return True
        return False
    
    # Function: gameStart
    # Parameter: None
    # Start the game 
    def gameStart(self):
        self.makeTable()
        while not self.checkWin():
            self.checkWin()
            self.askPlace()
            self.makeTable()
            self.checkWin()
