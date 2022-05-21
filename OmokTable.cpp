//
// Created by Kenny Kim on 5/20/22.
//

#include "OmokTable.h"
#include <iostream>

using namespace std;

void OmokTable::checkBool(int i, int j) {
    if (u1[i][j]){
        cout << "U\t";
        return;
    }
    else if(u2[i][j])
    {
        cout << "u\t";
        return;
    }
    cout << "*\t";
}

bool OmokTable::checkPlace(string p, int user) {
    int ap = -1, np = -1;
    for (int i = 0; i < 8; ++i)
    {
        if (alp[i] == p[0])
        {
            ap = i;
        }
        if (i < 7 && num[i] == p[1])
        {
            np = i;
        }
    }
    if (ap == -1 || np == -1) {
        return false;
    }
    else if (u1[np][ap] || u2[np][ap]) {
        return false;
    }
    if (user == 1)
    {
        u1[np][ap] = true;
    }
    else{
        u2[np][ap] = true;
    }
    return true;
}

bool OmokTable::checkWin()
{
    int won = 0;
    // check line
    // check row
    // check
    return false;
}

OmokTable::OmokTable() {
    u1 = nullptr;
    u2 = nullptr;
    set = -1;
}

OmokTable::OmokTable(int set) {
    this->set = set;
    u1 = new bool*[set];
    u2 = new bool*[set];

    for (int i = 0; i < set; ++i) {
        u1[i] = new bool[set];
        u2[i] = new bool[set];
    }
    for (int i = 0; i < set; ++i)
    {
        for (int j = 0; j < set; ++j)
        {
            u1[i][j] = false;
            u1[i][j] = false;
        }
    }
}

void OmokTable::askSet() {
    cout << "OMOK table (5x5, 6x6, 7x7): ";
    cin >> set;
    while (set < 5 || set > 7)
    {
        cout << "OMOK Table must be between 5x5 and 7x7" << endl;
        cout << "OMOK table (5x5, 6x6, 7x7): ";
        cin >> set;
    }

}

void OmokTable::makeTable() {
    for (int i = 0; i < set + 1; ++i) {
        for (int j = 0; j < set + 1; ++j) {

            if (i == 0) {
                cout << alp[j] << "\t";
            }
            else if (j == 0) {
                cout << num[i - 1] << "\t";
            }
            else {
                checkBool(i - 1, j);
            }
        }
        cout << endl;
    }
}

void OmokTable::askPlace()
{
    for (int i = 1; i < 2; ++i) {
        string place;
        cout << "Enter place (Ex - A1, C4): ";
        cin >> place;
        while (place.size() != 2) {
            cout << "Error, the name must be included one alphabet and one integer" << endl;
            cout << "Enter place (Ex - A1, C4): ";
            cin >> place;
        }
        while (!checkPlace(place, i)) {
            cout << "Error, the place is already taken, choose other place" << endl;
            cout << "Enter place (Ex - A1, C4): ";
            cin >> place;
        }
    }



}

OmokTable::~OmokTable() {
    for (int i = 0; i < set; ++i)
    {
        delete[] u1[i];
        delete[] u2[i];
        u1[i] = nullptr;
        u2[i] = nullptr;

    }
}



