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
    bool** u1;
    bool** u2;
    int set;
    char alp[8] = {' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G'};
    int num[7] = {1, 2, 3, 4, 5, 6, 7};
    void checkBool (int i, int j);
    bool checkPlace(string p, int u);
    bool checkWin();

public:
    OmokTable();
    OmokTable(int set);
    void askSet();
    void askPlace();
    void makeTable();
    ~OmokTable();
};


#endif //OMOK_OMOKTABLE_H
