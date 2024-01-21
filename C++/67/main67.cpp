#include <iostream>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

// solved 01-18-2024

// This is the same code from problem 18, it was designed to be flexible for any triangle that has more than 2 rows
// fill the input.txt file and then specify here how many rows there are
#define TOTAL_ROWS 100

int main()
{
    // The first thing we need to do is parse the input file into a vector of integers
    vector<int> input;
    ifstream inputFile("input.txt", ios::in);
    int i;
    while (inputFile >> i)
    {
        input.push_back(i);
    }

    int idx_left = 0;
    int idx_right = 0;

    // there are 100 rows, and we need to start at the second to last row. Find the index of the second to last row
    int start_index = 0;
    for (int x = 0; x < (TOTAL_ROWS - 1); x++)
    {
        start_index += x;
    }
    int idx = start_index;

    for (int row_num = TOTAL_ROWS - 1; row_num > 1; row_num--)   
    {
        while (idx < start_index + row_num)
        {
            // figure out what the left and right lower numbers are from the index
            idx_left = idx + row_num;
            idx_right = idx_left + 1;

            if (input[idx_left] > input[idx_right]) // left lower option better
            {
                input[idx] += input[idx_left];
            }
            else                                    // right lower option better
            {
                input[idx] += input[idx_right];
            }
            
            idx++;
        }

        // change index to the start of the previous row
        start_index = start_index - (row_num-1);
        idx = start_index;
    }

    // now look at index 1 and 2, and add the largest to the first item
    int sum = input[0];
    if (input[1] > input[2]) sum += input[1];
    else sum += input[2];

    cout << sum << endl;

    return 0;
}