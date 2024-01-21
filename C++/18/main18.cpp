#include <iostream>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

// solved 01-18-2024
/*
The goal here is to find the maximum path through the triangle given.
First we start at the bottom and work our way up.

For each number in a row, we find the left and right numbers under it, 
and we take the biggest number, and add it to the number we are looking at.
Then we do this from the second to last row up towards the first row.

We iterate across all indexes for each row from row 2 to row n-1
adding the maximum adjacent number to the index as we go

As we go up the rows, the size of the triangle decreases (not really, since we dont delete anything, we just stop caring)
And eventually we are left with a two row triangle, so we find the largest item in row 1 and add it to the first item in the list (row 0)
*/

// Problem 67 is basically the same as this so the code is the same, just with bigger numbers.

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

    // there are 15 rows, and we need to start at the second to last row. Find the index of the second to last row
    int total_rows = 15;
    int start_index = 0;
    for (int x = 0; x < (total_rows - 1); x++)
    {
        start_index += x;
    }
    int idx = start_index;

    for (int row_num = total_rows - 1; row_num > 1; row_num--)   
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