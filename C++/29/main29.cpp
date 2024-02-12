#include <iostream>
#include <iomanip>
#include <chrono>
#include <set>
#include <math.h>

using namespace std;

int main()
{
    const auto start = chrono::high_resolution_clock::now();

    set<long> terms;

    for (int a = 2; a <= 10; a++)
    {
        for (int b = 2; b <= 10; b++)
        {
            cout << "a " << a << " b " << b << " a^b " << pow(a,b) << endl;
            terms.insert(long(pow(a, b)));
        }
    }

    cout << terms.size() << endl;

    for (long x : terms)
    {
        cout << " " << x;
    }

    const auto end = chrono::high_resolution_clock::now();
    auto durationMicroseconds = chrono::duration_cast<chrono::microseconds>(end - start);
    auto durationMilliseconds = chrono::duration_cast<chrono::milliseconds>(end - start);
    cout << endl << "Execution time: " << fixed << setprecision(5);
    cout << float(durationMicroseconds.count() / 1000.0f) << " ms / ";
    cout << float(durationMilliseconds.count() / 1000.0f) << " s." << endl;
    return 0;
}