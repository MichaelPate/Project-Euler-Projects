// Problem 31, solved 4-19-2024

#include <chrono>
#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <set>

using namespace std;

int main()
{
    auto start = chrono::steady_clock::now();

    long numWays = 0;
    long totalWays = 0;
    for (int p1 = 0; p1 <= 200; p1++)
    {
        for (int p2 = 0; p2 <= 200; p2 += 2)
        {
            for (int p5 = 0; p5 <= 200; p5 += 5)
            {
                for (int p10 = 0; p10 <= 200; p10 += 10)
                {
                    for (int p20 = 0; p20 <= 200; p20 += 20)
                    {
                        for (int p50 = 0; p50 <= 200; p50 += 50)
                        {
                            for (int p100 = 0; p100 <= 200; p100 += 100)
                            {
                                for (int p200 = 0; p200 <= 200; p200 += 200)
                                {
                                    if ((p1 + p2 + p5 + p10 + p20 + p50 + p100 + p200) == 200)
                                    {
                                        //cout << p1 << " " << p2 << " " << p5 << " " << p10 << " " << p20 << " " << p50 << " " << p100 << " " << p200 << endl;
                                        numWays++;
                                    }
                                    totalWays++;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    cout << numWays << "/" << totalWays << endl;
    
    auto stop = chrono::steady_clock::now();
    auto diff = stop - start;
    cout << "\nProgram ran in ";
    cout << chrono::duration<double, milli>(diff).count() << "ms." << endl;
}