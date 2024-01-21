#include <iostream>

using namespace std;

// solved 01-19-2024

int sumOfProperDivisors(int n);

int main()
{
    int sum = 0;
    for (int idx = 1; idx < 10001; idx++)
    {
        /*
            The goal here is to find amicable numbers,
            Where d(n) is the sum of proper divisors of n.
            
            Look for instances where d(a) = b and d(b) = a, a != b.
            When that happens, a and b are considered amicable numbers
        */
        int test = sumOfProperDivisors(idx);

        if (sumOfProperDivisors(test) == idx && test != idx)
        {
            sum += idx;
        }
    }
    
    cout << sum;

    return 0;
}

// Returns the sum of all numbers less than n that divide into n
int sumOfProperDivisors(int n)
{
    int sum = 0;

    for (int i = 1; i < n; i++)
    {
        if (n % i == 0)
        {
            sum += i;
        }
    }

    return sum;
}