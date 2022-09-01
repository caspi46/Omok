//
// Created by Kenny Kim on 5/20/22.
// 5/24/22
// 9/1/22 - convert from python ver


#include "OmokTable.h"
#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <array>

using namespace std;

OmokTable::OmokTable(){
    askSet();
    setSet();
}

OmokTable::OmokTable(int set){
    if (set == -1){
        askSet();
        return;
    }
    this->set = set;
    setSet();
}

void OmokTable::setSet(){
    omokTable = new int*[set];
    for (int i = 0; i < set; ++i) {
        omokTable[i] = new int[set];
    }
    for (int i = 0; i < set; ++i)
    {
        for (int j = 0; j < set; ++j)
        {
            omokTable[i][j] = 0;
        }
    }
}

void OmokTable::askSet(){
    cout << "OMOK table (6x6, 7x7, 8x8): ";
    cin >> set;
    while (set < 6 || set > 8) {
        cout << "OMOK Table must be between 6x6, 7x7 and 8x8" << endl;
        cout << "OMOK table (6x6, 7x7, 8x8): ";
        cin >> set;
    }

}

bool OmokTable::identifyPlayer(int p1, int p2){
    makeTable();
    if (p1 == 5){
        cout << "Player 1 Won" << endl;
        return true;
    }
    else if (p2 == 5){
        cout << "Player 2 Won" << endl;
        return true;
    }
    return false;
}

bool OmokTable::checkCross1(){
    int stones11 = 0, stones12 = 0, stones21 = 0, stones22 = 0;
    for (int i = 0; i < (set - 4); ++i){
        for (int j = 0; j < (set - i); ++j){
            if (omokTable[i + j][j] == 1){
                ++stones11;
                stones21 = 0;
            }
            else if (omokTable[i + j][j] == -1){
                ++stones21;
                stones11 = 0;
            }
            else{
                stones11 = 0;
                stones21 = 0;
            }

            if (omokTable[j][i + j] == 1){
                ++stones12;
                stones22 = 0;
            }
            else if (omokTable[j][i + j] == -1){
                ++stones22;
                stones12 = 0;
            }
            else{
                stones12 = 0;
                stones22 = 0;
            }
            if (stones11 == 5 || stones21 == 5){
                return identifyPlayer(stones11, stones21);
            }
            if (stones12 == 5 or stones22 == 5){
                return identifyPlayer(stones12, stones22);
            }
        }
    }
    return false;
}

bool OmokTable::checkCross2(){
    int stones11 = 0, stones12 = 0, stones21 = 0, stones22 = 0;
    for (int i = 0; i < (set - 4); ++i){
        for (int j = 0; j < (set - i); ++j){
            if (omokTable[i + j][set - 1 - j] == 1){
                ++stones11;
                stones21 = 0;
            }
            else if (omokTable[i + j][set - 1 - j] == -1){
                ++stones21;
                stones11 = 0;
            }
            else{
                stones11 = 0;
                stones21 = 0;
            }

            if (omokTable[j][set - 1 - j - i] == 1){
                ++stones12;
                stones22 = 0;
            }
            else if (omokTable[j][set - 1 - j - i] == -1){
                ++stones22;
                stones12 = 0;
            }
            else{
                stones12 = 0;
                stones22 = 0;
            }
            if (stones11 == 5 || stones21 == 5){
                return identifyPlayer(stones11, stones21);
            }
            if (stones12 == 5 or stones22 == 5){
                return identifyPlayer(stones12, stones22);
            }
        }
    }
    return false;
}

bool OmokTable::checkColumn(){
    int win1C, win2C;
    for (int i = 0; i < set; ++i){
        win1C = 0;
        win2C = 0;
        for (int j = 0; j < set; ++j) {
            if (omokTable[i][j] == 1) {
                win2C = 0;
                ++win1C;
            } else if (omokTable[i][j] == -1) {
                win1C = 0;
                ++win2C;
            } else {
                win1C = 0;
                win2C = 0;
            }
            if (win1C == 5 || win2C == 5) {
                return identifyPlayer(win1C, win2C);
            }
        }
    }
}

bool OmokTable::checkRow(){
    int win1R, win2R;
    for (int i = 0; i < set; ++i){
        win1R = 0;
        win2R = 0;
        for (int j = 0; j < set; ++j) {
            if (omokTable[j][i] == 1) {
                win2R = 0;
                ++win1R;
            } else if (omokTable[j][i] == -1) {
                win1R = 0;
                ++win2R;
            } else {
                win1R = 0;
                win2R = 0;
            }
            if (win1R == 5 || win2R == 5) {
                return identifyPlayer(win1R, win2R);
            }
        }
    }
}
bool OmokTable::checkWin(){
    if (checkDrew()){
        cout << "Drew" << endl;
        return true;
    }

    if (checkCross1() || checkCross2()){
        return true;
    }
    int win1C, win2C, win1R, win2R;
    if (checkColumn()){
        return true;
    }
    if (checkRow()){
        return true;
    }

    return false;
}

bool OmokTable::checkDrew(){
    for(int x = 0; x < set; x++){
        for(int y = 0; y < set; y++){
            if(omokTable[x][y] == 0){
                return false;
            }
        }
    }
    return true;
}

int OmokTable::checkPlace(char p, int n) {
    int ap = -1;
    if (n > set) { return -1; }
    for (int i = 0; i < set + 1; ++i)
    {
        if (alp[i] == p)
        {
            ap = i;
            break;
        }
    }
    if (ap == -1) { return -1; }
    else if (omokTable[n - 1][ap - 1] != 0) {
        cout << "taken seat" << endl;
        return -1;
    }
    return ap;
}

void OmokTable::askPlace()
{
    int pnum = checkPlayer();
    string place;
    cout << "Player " << pnum << " Enter place (Ex - A1, C4): ";
    cin >> place;
    while (place.size() != 2) {
        cout << "Error, the name must be included one alphabet and one integer" << endl;
        cout << "Enter place (Ex - A1, C4): ";
        cin >> place;
    }
    char p = place[0];
    int n = (place[1] - 48);
    int ap = checkPlace(p, n);
    while (ap == -1) {
        cout << "Error, the place is already taken, choose other place" << endl;
        cout << "Enter place (Ex - A1, C4): ";
        cin >> place;
        p = place[0];
        n = place[1] - 48;
        ap = checkPlace(p, n);
    }
    if (pnum == 1) { omokTable[n - 1][ap - 1] = 1; }
    else { omokTable[n - 1][ap - 1] = -1; }
}
void OmokTable::checkBool(int i, int j){
    if (omokTable[i][j] == 1){
        cout << "O\t";
        return;
    }
    else if (omokTable[i][j] == -1) {
        cout << "X\t";
        return;
    }
    cout << "*\t";
}
void OmokTable::makeTable() {
    for (int i = 0; i < set + 1; ++i) {
        for (int j = 0; j < set + 1; ++j) {
            if (i == 0) {
                cout << alp[j] << "\t";
            }
            else if (j == 0) {
                cout << i << "\t";
            }
            else {
                checkBool(i - 1, j - 1);
            }
        }
        cout << endl;
    }
}


int OmokTable::checkPlayer(){
    int numTaken = 0;
    for (int i = 0; i < set; ++i){
        for (int j = 0; j < set; ++j){
            if (omokTable[i][j] == -1 or omokTable[i][j] == 1){
                numTaken += 1;
            }
        }
    }
    if (numTaken % 2 == 0){
        return 1; // player 1
    }
    return 2; // player 2
}
void OmokTable::gameStart()
{
    setSet();
    makeTable();

    while (true){
        askPlace();
        if (checkPlayer() == 1){
            makeTable();
        }
        if (checkWin()){
            cout << "GAME END!" << endl;
            break;
        }
    }
}

OmokTable::~OmokTable() {
    for (int i = 0; i < set; ++i)
    {
        delete[] omokTable[i];
        omokTable[i] = nullptr;

    }
}






