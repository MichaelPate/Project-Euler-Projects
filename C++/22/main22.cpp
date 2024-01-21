#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// solved 1-20-2024

bool stringCompare(string a, string b);
int getMin(int a, int b);
int sumString(string input);

int main()
{
    // We will need to parse input.txt and sanitize it
    // We need a string vector with only names, no commas or quotes
    // and only one name per entry within the vector
    vector<string> names;
    ifstream input("input.txt", ios::in);
    string line = "";
    while (!input.eof())
    {
        getline(input, line, ',');
        line.erase(remove(line.begin(), line.end(), '\"'), line.end());
        names.push_back(line);
    }

    // The requirement is that the vector is sorted, so
    // insertion sort because this computer is fast enough
    string temp = "";
    for (int i = 1; i < names.size(); i++)
    {
        for (int k = i; k > 0; k--)
        {
            if (stringCompare(names[k], names[k-1]))
            {
                temp = names[k];
                names[k] = names[k-1];
                names[k-1] = temp;
            }
        }
    }

    unsigned long totalScore = 0;
    int letterScore = 0;
    for (int idx = 0; idx < names.size(); idx++)
    {
        letterScore = sumString(names[idx]);
        totalScore += (idx+1) * letterScore;
    }

    cout << totalScore << endl;

    return 0;
}

// Returns true if string a comes before string b, alphabetically
// Returns false otherwise. Both strings must contain characters
bool stringCompare(string a, string b)
{
    // Both strings must contain characters
    if (a == "" || b == "")
    {
        return false;
    }

    // If we make sure the strings are uppercase, we can compare ASCII values
    transform(a.begin(), a.end(), a.begin(), ::toupper);
    transform(b.begin(), b.end(), b.begin(), ::toupper);

    // Check to see if a comes first alphabetically (lower ASCII value)
    // Probably not efficient but who's counting, it passed the tests
    for (int i = 0; i < getMin(a.size(), b.size()); i++)
    {
        //cout << a[i] << "\t" << b[i] << endl;
        // Try to find a letter in string a that comes before b
        if (int(a[i]) > int(b[i]))
        {
            //cout << "B comes before A - false" << endl;
            return false;
        }
        if (int(a[i]) < int(b[i]))
        {
            //cout << "A comes before B - true" << endl;
            return true;
        }
    }

    // ran out of letters before we could tell,
    // so the shorter word is considered first
    if (a.size() <= b.size())
    {
        return true;
    }
    else
    {
        return false;
    }
}

// Returns the minimum number between two
int getMin(int a, int b)
{
    if (a <= b)
    {
        return a;
    }
    else
    {
        return b;
    }
}

// Returns the sum of the letters based on their position in the alphabet
// ie A = 1, B = 2, etc.
// CAT = 3 + 1 + 20 = return 24
int sumString(string input)
{
    // Empty strings considered zero sum
    if (input == "")
    {
        return 0;
    }

    // We can only work with the ASCII values if we guarantee uppercase
    transform(input.begin(), input.end(), input.begin(), ::toupper);

    // subtract 64 from the ASCII value for each letter and sum
    // The 64 will properly align/offset the standard ASCII values to the alphabet
    int sum = 0;
    for(int i = 0; i < input.length(); i++)
    {
        sum += int(input[i]) - 64;
    }
    return sum;
}