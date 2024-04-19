// Problem 30, solved 4-18-2024

#include <chrono>
#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <set>

using namespace std;

#define POWER 5
#define MAX_C 1000000  // arbitrary high number

int main()
{
    auto start = chrono::steady_clock::now();

    int totalSum = 0; 
    for (int candidate = 2; candidate < MAX_C; candidate++)
    {
        int sumPowers = 0;
        string test = to_string(candidate);
        for (char x : test)
        {
            sumPowers += pow(x - '0', POWER);
        }

        if (sumPowers == candidate)
        {
            totalSum += candidate;
        }
    }
    cout << totalSum << endl;
    
    auto stop = chrono::steady_clock::now();
    auto diff = stop - start;
    cout << "\nProgram ran in ";
    cout << chrono::duration<double, milli>(diff).count() << "ms." << endl;
}