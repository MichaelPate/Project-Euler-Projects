// Project 14 for "Project Euler.net"

/*
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
*/

#include "stdafx.h"
#include <iostream>

using namespace std;

int main()
{
	static unsigned long startNumber = 1;
	unsigned int chainLength = 0;
	unsigned int longestChain = 0;
	unsigned long longestChainNumber = 0;
	long n = 1;

	for (startNumber = 1; startNumber < 1000000; startNumber++)
	{
		if (startNumber > 1)
		{
			n = startNumber;

			//Loop until 1 is reached, signalling the end of the chain
			do
			{
				//Check for even
				if (n % 2 == 0)
				{
					//Is even
					n = n / 2;
				}
				else
				{
					//Is odd
					n = (n * 3) + 1;
				}

				chainLength += 1;

				if (chainLength > longestChain)
				{
					longestChain = chainLength;
					longestChainNumber = startNumber;
				}

			} while (n > 1);
		}
	}

	cout << "Starting number:\t" << startNumber << endl;
	cout << "Length of chain:\t" << longestChain << endl;

	system("pause");
    return 0;
}

