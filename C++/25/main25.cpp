// solved 01-23-2024
#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    // We can use Binet's Formula
    // and multiply it by log base 10 to get the number of digits.
    // Simplifying the math gives digits = [n * log10(phi)] - [(log10(5)) / 2]
    float phi = 1.6180339887498948;
    long double d = 0.0;
    int digits = 1;
    long long candidate = 1;

    do
    {
        candidate++;
        d = (candidate * log10(phi)) - (log10(5) / 2);
        digits = ceil(d);
    } while (digits < 1000);
    
    cout << candidate << endl;

    return 0;
}