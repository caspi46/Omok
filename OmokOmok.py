class OmokOmok:
    def __init__(self, s):
        self.set = s
        self.alp = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
        self.omokTable = [[0 for i in range(self.set)] for j in range(self.set)]
        # player 1 = 1 & player 2 = -1
        self.cross1 = [ ]
        self.cross2 = [ ]
        for i in range(self.set):
            for j in range(self.set):
                if (i == j):
                    self.cross1.append(self.omokTable[i][j])
                if (i + j) == (self.set - 1):
                    self.cross2.append(self.omokTable[i][j])


    def checkBool(self, i, j):

        if self.omokTable[i][j] == 1:
            print("u\t", end="")
            return
        elif self.omokTable[i][j] == -1:
            print("n\t", end="")
            return
        print("*\t", end="")


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

    def askPlace(self):
        for i in range(2):
            place = str(input("Enter place (Ex - A1, C4):"))
            while len(place) != 2:
                print("Error, the name must be included one alphabet & integer")
                place = str(input("Enter place (Ex - A1, C4):"))
            n = int(place[1])
            ap = self.checkPlace(place[0], n)
            while(ap == -1):
                print("Error, the place is already taken, choose other place")
                place = str(input("Enter place (Ex - A1, C4):"))
                n = int(place[1])
                ap = self.checkPlace(place[0], n)

            if i == 0:
                self.omokTable[n - 1][ap - 1] = 1
            else:
                self.omokTable[n - 1][ap - 1] = -1

    def checkWin(self):
        if 0 not in self.cross1:
            return all(element == self.cross1[0] for element in self.cross1)
        win1C = 0
        win2C = 0
        for i in range(self.set):
            for j in range(self.set):
                if self.omokTable[i][j] == 1:
                    win1C+= 1
                elif self.omokTable[i][j] == -1:
                    win2C += 1
                if win1C == self.set or win2C == self.set:
                    return True
        win1R = 0
        win2R = 0
        for i in range(self.set):
            for j in range(self.set):
                if self.omokTable[j][i] == 1:
                    win1R+= 1
                elif self.omokTable[j][i] == -1:
                    win2R += 1
                if win1R == self.set or win2R == self.set:
                    return True



    def gameStart(self):
        self.makeTable()
        while not self.checkWin():
            self.checkWin()
            self.askPlace()
            self.makeTable()
            self.checkWin()