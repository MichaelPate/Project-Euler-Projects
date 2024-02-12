#include <iostream>
#include <iomanip>
#include <chrono>

using namespace std;

int main()
{
    const auto start = chrono::high_resolution_clock::now();

    // Problem code goes here.

    const auto end = chrono::high_resolution_clock::now();
    auto durationMicroseconds = chrono::duration_cast<chrono::microseconds>(end - start);
    auto durationMilliseconds = chrono::duration_cast<chrono::milliseconds>(end - start);
    cout << endl << "Execution time: " << fixed << setprecision(5);
    cout << float(durationMicroseconds.count() / 1000.0f) << " ms / ";
    cout << float(durationMilliseconds.count() / 1000.0f) << " s." << endl;
    return 0;
}