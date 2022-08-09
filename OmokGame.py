class OmokGame:
    def __init__(self, s):
        self.u1 = []
        self.u2 = []
        self.cross1u1 = [ ]
        self.cross2u1 = [ ]
        self.cross1u2 = [ ]
        self.cross2u2 = [ ]
        self.set = s
        self.alp = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
        self.u1 = [[0 for i in range(self.set)] for j in range(self.set)]
        self.u2 = [[0 for i in range(self.set)] for j in range(self.set)]
        for i in range(self.set):
            for j in range(self.set):
                if i == j:
                    self.cross1u1[i] = self.u1[i][j]
                    self.cross1u2[i] = self.u2[i][j]
                if (i + j) == self.set:
                    self.cross2u1[i] = self.u1[i][j]
                    self.cross2u2[i] = self.u2[i][j]

    def checkWin(self):
        wonL1 = 0
        wonL2 = 0
        wonR1 = 0
        wonR2 = 0
        wonC1 = 0
        wonC2 = 0

        for i in range(self.set):
            for j in range(self.set):
                if self.u1[i][j]:
                    wonL1 += 1
                    wonL2 = 0

                else:
                    wonL1 = 0
                    if self.u2[i][j]:
                        wonL2 += 1
                    else:
                        wonL2 = 0

                if self.u1[j][i]:
                    wonR1 += 1
                    wonR2 = 0
                else:
                    wonR1 = 0
                    if self.u2[j][i]:
                        wonR2 += 1
                    else:
                        wonR2 = 0
                print(wonR1, wonR2, " ", wonL1, wonL2)
                if wonR1 == 5 or wonL1 == 5:
                    return True
                elif wonR2 == 5 or wonL2 == 5:
                    return True
                return False

    def checkBool(self, i, j):

        if self.u1[i][j] == 1:
            print("u\t", end="")
            return
        elif self.u2[i][j] == 1:
            if (i == j):
                self.cross1u2 = 1
            if (i + j) == self.set:
                self.cross2u1 = 1
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

        elif self.u1[n - 1][ap - 1] == 1 or self.u2[n - 1][ap - 1] == 1:
            print("Taken Seat")
            return -1
        return ap

    def askPlace(self):
        for i in range(2):
            place = str(input("Enter place (Ex - A1, C4):"))
            while len(place) != 2:
                print("Error, the name must be included one alphabet & integer")
                place = str(input("Enter place (Ex - A1, C4):"))
            p = place[0]
            n = int(place[1])
            ap = self.checkPlace(p, n)
            while(ap == -1):
                print("Error, the place is already taken, choose other place")
                place = str(input("Enter place (Ex - A1, C4):"))
                p = place[0]
                n = int(place[1])
                ap = self.checkPlace(p, n)

            if i == 0:
                self.u1[n - 1][ap - 1] = 1
            else:
                self.u2[n - 1][ap - 1] = 1


    def gameStart(self):
        self.makeTable()
        while not self.checkWin():
            self.checkWin()
            self.askPlace()
            self.makeTable()
            self.checkWin()