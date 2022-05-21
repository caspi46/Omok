#include <iostream>
//OMOK PROJECT
//START DATE: MAY 17 2022

#include <iostream>
#include "OmokTable.h"


using namespace std;

int main()
{
    int set;
    cout << "OMOK table (5x5, 6x6, 7x7): ";
    cin >> set;
    while (set < 5 || set > 7)
    {
        cout << "OMOK Table must be between 5x5 and 7x7" << endl;
        cout << "OMOK table (5x5, 6x6, 7x7): ";
        cin >> set;
    }
    OmokTable game(set);
    game.makeTable();



}
