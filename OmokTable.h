//
// Created by Kenny Kim on 5/20/22.
//

#ifndef OMOK_OMOKTABLE_H
#define OMOK_OMOKTABLE_H

#include <string>
#include <iostream>

using namespace std;

class OmokTable {
private:
    int** omokTable;
    int set = -1;
    char alp[8] = {' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G'};
    //int num[7] = {1, 2, 3, 4, 5, 6, 7};



public:
    OmokTable();
    OmokTable(int set);
    void askSet();
    void setSet();
    bool checkCross1();
    bool checkCross2();
    bool checkColumn();
    bool checkRow();
    bool checkDrew();
    bool checkWin();
    int checkPlayer();
    void checkBool(int i, int j);
    bool identifyPlayer(int p1, int p2);
    int checkPlace(char p, int n);
    void askPlace();
    void makeTable();
    void gameStart();

    ~OmokTable();
};


#endif //OMOK_OMOKTABLE_H
