#include <iostream>

using namespace std;

int* factorialArray(int n, int& result_size);
int multiply(int x, int result[], int result_size);

#define MAX_SIZE 500

int main()
{
    int* result;
    int result_size = 1;

    result = factorialArray(100, result_size);

    int sum = 0;

    for(int idx = result_size - 1; idx >= 0; idx--)
    {
        sum += result[idx];
    }

    cout << sum << endl;
    return 0;
}

int* factorialArray(int n, int& result_size)
{
    static int result[MAX_SIZE];

    result[0] = 1;

    for (int x = 2; x <= n; x++)
    {
        result_size = multiply(x, result, result_size);
    }

    return result;
}

int multiply(int x, int result[], int result_size)
{
    int carry = 0;

    for (int i = 0; i < result_size; i++)
    {
        int product = result[i] * x + carry;

        result[i] = product % 10;

        carry = product / 10;
    }

    while (carry)
    {
        result[result_size] = carry % 10;
        carry = carry / 10;
        result_size++;
    }

    return result_size;
}