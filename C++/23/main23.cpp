// solved 1-22-2024
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool isAbundant(int n);

// We know from the problem statement that all numbers above MAX 
//  can definitely be expressed as the sum of two abundant 
//  numbers, so its not worth checking beyond MAX
#define MAX 28123

int main()
{
    // Good to know ahead of time which numbers are abundant
    // We only go up to MAX because all integers above that can
    //  be written as the sum of two abundant numbers, so 
    //  we dont need to go above it.
    vector<int> abundantNumbers;
    for (int n = 0; n <= MAX; n++)
    {
        if (isAbundant(n) == true)
        {
            abundantNumbers.push_back(n);
        }
    }

    // Here we will scan through the abundant numbers,
    //  trying to find two that sum up to the candidate.
    // If we find two, then we discard the candidate and do
    //  not add it to the sum, since we want the sum of numbers
    //  that CANNOT be expressed as a sum of 2 abundant numbers.
    int sumNonAbundantSum = 0;
    for (int candidate = 0; candidate < MAX; candidate++)
    {
        for (int i = 0; i < abundantNumbers.size() && abundantNumbers[i] < candidate; i++)
        {
            for(int j = 0; j < abundantNumbers.size() && abundantNumbers[j] < candidate; j++)
            {
                if (abundantNumbers[i] + abundantNumbers[j] == candidate)
                {
                    // The only real use for a goto: escaping nested loops
                    goto sumFound;
                }
            }
        }
        sumNonAbundantSum += candidate;

        // Since we found a sum, dont add the candidate and just move onto the next candidate
        sumFound:;
    }

    cout << sumNonAbundantSum << endl;

    return 0;
}

// Returns true if the sum of the proper divisors of n is greater than n.
bool isAbundant(int n)
{
    int sum = 0;

    for (int i = 1; i < n; i++)
    {
        if (n % i == 0)
        {
            sum += i;
        }
    }

    if (sum > n)
    {
        return true;
    }
    else
    {
        return false;
    }
}