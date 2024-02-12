#include <iostream>
#include <iomanip>
#include <chrono>

// solved 2-11-2024

using namespace std;

bool isPrime(int a);

#define A_MIN -999
#define A_MAX 999
#define B_MIN -1000
#define B_MAX 1000
#define SAFETY 1000

int main()
{
    const auto start = chrono::high_resolution_clock::now();

    int maxPrimesCount = 0;
    int maxProduct = 1;

    for (int a = A_MIN; a <= A_MAX; a++)
    {
        for (int b = B_MIN; b <= B_MAX; b++)
        {
            int n = -1;
            while (n < SAFETY)
            {
                n++;
                int result = (n * n) + (a * n) + b;
                // Just go until its not prime anymore
                if (isPrime(result) == false)
                {
                    break;
                }
            }

            // Lets see how we did
            // n should have the number of prime numbers found
            if (n >= maxPrimesCount)
            {
                maxPrimesCount = n;
                maxProduct = a * b;
            }
        }
    }

    cout << "a * b: " << maxProduct << " primes: " << maxPrimesCount << endl;

    const auto end = chrono::high_resolution_clock::now();
    auto durationMicroseconds = chrono::duration_cast<chrono::microseconds>(end - start);
    auto durationMilliseconds = chrono::duration_cast<chrono::milliseconds>(end - start);
    cout << endl << "Execution time: " << fixed << setprecision(5);
    cout << float(durationMicroseconds.count() / 1000.0f) << " ms / ";
    cout << float(durationMilliseconds.count() / 1000.0f) << " s." << endl;
    return 0;
}

bool isPrime(int a)
{
    if (a <= 1)
    {
        return false;
    }

    for (int i = 2; i <= a / 2; i++)
    {
        if (a % i == 0)
        {
            return false;
        }
    }

    return true;
}