// Problem 29, solved 4-18-2024

#include <chrono>
#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <set>

using namespace std;

#define A_LO 2
#define A_HI 100
#define B_LO 2
#define B_HI 100

string multiply(string n1, string n2);
string exponent(int a, int b);

int main()
{
    auto start = chrono::steady_clock::now();

    set<string> results;
    for (int a = A_LO; a <= A_HI; a++)
    {
        for (int b = B_LO; b <= B_HI; b++)
        {
            results.insert(exponent(a, b));
        }
    }
    // we dont care about the order, just the number of unique items
    cout << "size: " << results.size() << endl;
    
    auto stop = chrono::steady_clock::now();
    auto diff = stop - start;
    cout << "\nProgram ran in ";
    cout << chrono::duration<double, milli>(diff).count() << "ms." << endl;
}

// Uses the string multiply function to
// find the exponent a^b. Works
// for a>0 and b>0 only.
string exponent(int a, int b)
{
    string sa = to_string(a);
    string res = sa;

    for(int i = b; i > 1; i--)
    {
        res = multiply(res, sa);
    }
    return res;
}

// Takes two strings containing the digits of a number
// and multiplies them together, returning the result
// number as a string. Works on positive numbers only, 
// but of unlimited length
string multiply(string n1, string n2)
{
    int len1 = n1.size();
    int len2 = n2.size();

    // Escape for multiplying a number by zero
    if (len1 == 0 || len2 == 0)
    {
        return "0";
    }

    vector<int> result(len1 + len2, 0);

    int idx1 = 0, idx2 = 0;

    // Traverse n1 from right to left
    for (int i = len1 - 1; i >= 0; i--)
    {
        int carry = 0;

        // Get the digit as a number, converting from ASCII to int
        int num1 = n1[i] - '0';

        // Shift position to left after every digitwise multiplication from n2
        idx2 = 0;

        // Traverse n2 from right to left
        for (int j = len2 - 1; j >= 0; j--)
        {
            int num2 = n2[j] - '0';

            int sum = num1 * num2 + result[idx1 + idx2] + carry;
            carry = sum / 10;
            result[idx1 + idx2] = sum % 10;

            idx2++;
        }

        if (carry > 0)
        {
            result[idx1 + idx2] += carry;
        }

        // Shift position left after every digitwise multiplication from n1
        idx1++;
    }

    // ignore zeros from the right
    int i = result.size() - 1;
    while (i >= 0 && result[i] == 0)
    {
        i--;
    }

    // if the whole thing is zeros then n1 or n2 was zero
    if (i == -1)
    {
        return "0";
    }

    // generate the result string
    string res = "";
    while (i >= 0)
    {
        res += to_string(result[i--]);
    }
    return res;
}