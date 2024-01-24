#include <iostream>
#include <vector>

using namespace std;

#define PERMUTATION 1000000
#define DIGITS 10

long factorial(int n);

int main()
{
    // I decided to work with chars to avoid any possible issues with leading zeros
    // and its way easier to work with specific digits of a number this way
    // because really all we are doing is swapping out digit places
    vector<char> input = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'};
    char output[DIGITS];

    // input<> is sorted, so that is permutation 0, so find PERMUTATION - 1
    int perm = PERMUTATION - 1;

    // Implement Lehmer code on input<> to get output[]
    for (int idx = 0; idx < DIGITS; idx++)
    {
        // (n-1)! = factorial((DIGITS - idx) - 1)
        int n = DIGITS - idx;
        n = factorial(n - 1);
        
        // quotient is the index of input<> that will be placed in the idx position in output[]
        int quotient = perm / n;
        perm = perm % n;
        output[idx] = input[quotient];

        // Then we remove the quotient index number from the vector
        input.erase(input.begin() + quotient);
    }

    // Now we can display our results
    for (char& x : output)
    {
        cout << x;
    }

    return 0;
}

// Quick n dirty, only works up to 16, but good enough for this.
long factorial(int n)
{
    long fact = 1;

    for (int i = 1; i <= n; i++)
    {
        fact *= i;
    }

    return fact;
}