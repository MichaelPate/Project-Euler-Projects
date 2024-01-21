#include <iostream>
#include <cmath>

using namespace std;

// solved 1-19-2024

bool isLeapYear(int year);
int getDayOfWeek(int year, int month, int day);

int main()
{
    int year = 1901;
    int month = 1;
    int sundayCount = 0;

    while (year < 2001)
    {
        while (month < 13)
        {
            if (getDayOfWeek(year, month, 1) == 6) sundayCount++;
            month++;
        }

        year++;
        month = 1;
    }

    cout << sundayCount << endl;

    return 0;
}

// Given a year, returns true if the year is a leap year, otherwise returns false
// This function ended up not being used here but im keeping it for future reference for another program
bool isLeapYear(int year)
{
    // A year is a leap year if its divisible by 4 or its a century divisible by 400

    // The year must be divisible by 4.
    // If the year is also divisible by 100, 
    // its not a leap year unless its also divisible by 400.
    if (year % 4 == 0)
    {
        if (year % 100 == 0)
        {
            if (year % 400 == 0)
            {
                return true;
            }
            return false;
        }
        return true;
    }
    return false;
}

// Uses Zeller's Congruence to get day of the week
// Returns 6 if the date in question is a sunday
int getDayOfWeek(int year, int month, int day)
{
    if (month < 3)
    {
        month += 12;
        year--;
    }

    int k = year % 100;
    int j = year / 100;

    int dayOfWeek = (day + 13 * (month + 1) / 5 + k + k / 4 + j / 4 + 5 * j) % 7;

    // Adjust to fit the range [0, 6], where Sunday is 0 and Saturday is 6
    return (dayOfWeek + 5) % 7;
}