// solved 01-23-2024

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

// Set to a stupid high number because I didnt know what it could be
// but it wont matter, the program stops as soon as a number is found
#define MAX_CANDIDATE 2517480000

string intToDigitsString(int input);

int main()
{
    string candidateDigits = "";
    string testDigits = "";
    int multiple = 0;
    bool equal = true;

    for (int candidate = 1; candidate < MAX_CANDIDATE; candidate++)
    {
        candidateDigits = intToDigitsString(candidate);

        // Test the other multiples
        multiple = 2;
        equal = true;
        while (multiple <= 6)
        {
            testDigits = intToDigitsString(candidate * multiple);

            if (candidateDigits.compare(testDigits) != 0)
            {
                // The strings are different, this one is invalid
                equal = false;
            }
            multiple++;
        }

        // If we got through all multiples and equal is still true, we have a winner
        if (equal == true)
        {
            cout << candidate << endl;

            // return now, we wanted the smallest number so no point continuing
            return 0;
        }
    }

    return 0;
}

string intToDigitsString(int input)
{
    // Input to a string
    string in = to_string(input);

    // Now we need to sort the characters in the string
    // Same insertion sort method from problem 22
    char temp = '-';
    for (int i = 0; i < in.length(); i++)
    {
        for (int j = i; j > 0; j--)
        {
            if (int(in[j]) < int(in[j-1]))
            {
                temp = in[j];
                in[j] = in[j-1];
                in[j-1] = temp;
            }
        }
    }

    return in;
}