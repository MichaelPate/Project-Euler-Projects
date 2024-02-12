#include <iostream>
#include <iomanip>
#include <chrono>
#include <math.h>

using namespace std;

#define SIDE_LENGTH 1001

int main()
{
    const auto start = chrono::high_resolution_clock::now();

    // Start with increments by 2: [1], 3, 5, 7 9
    // After 4 increments, incrase the incriment to 3, then 5, 7, 9, etc
    // after 4 increments, incrase layers
    // Problem code goes here.

    int side_length = 1;
    int sum = 1;
    int current_number = 1;
    int increment = 2;

    while (side_length < SIDE_LENGTH)
    {
        // 3, 5, 7, 9       <- adding 2 each time, 4 times
        // 13, 17, 21, 25   <- adding 4 each time, 4 times
        // 31, 37, 43, 49   <- adding 6 each time, 4 times

        for (int i = 0; i < 4; i++)
        {
            current_number += increment;
            sum += current_number;
        }
        increment += 2;
        side_length = sqrt(current_number);
    }

    cout << sum << endl;

    const auto end = chrono::high_resolution_clock::now();
    auto durationMicroseconds = chrono::duration_cast<chrono::microseconds>(end - start);
    auto durationMilliseconds = chrono::duration_cast<chrono::milliseconds>(end - start);
    cout << endl << "Execution time: " << fixed << setprecision(5);
    cout << float(durationMicroseconds.count() / 1000.0f) << " ms / ";
    cout << float(durationMilliseconds.count() / 1000.0f) << " s." << endl;
    return 0;
}