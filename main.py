# Omok Project Python Ver
from OmokGame import OmokGame
from OmokOmok import OmokOmok
def main():
    set = int(input("Enter set (5, 6, 7): "))
    while set < 5 or set > 7:
        print("Error, the range is 5 - 7\n")
        set = int(input("Enter set (5, 6, 7): "))

    omok = OmokOmok(set)
    omok.gameStart()
    ''''
    set = int(input("Enter set (5, 6, 7): "))
    while set < 5 or set > 7:
        print("Error, the range is 5 - 7\n")
        set = int(input("Enter set (5, 6, 7): "))

    omok = OmokGame(set)
    omok.gameStart()
'''
main()

