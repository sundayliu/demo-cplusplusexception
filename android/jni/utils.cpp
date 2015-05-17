#include "utils.h"
#include <stdio.h>

namespace hello
{
	void print(const char* s, int len)
	{
		if (s == NULL || len == 0)
		{
			return;// NULL;
		}
		int a = 0;
		int b = 100;
		if (s != NULL)
		{
			printf("%s", s);
		}

		if (predicate(a,b+len))
		{
			printf("[print]%s", s);
		}
	}

	bool predicate(int a, int b)
	{
		int c = a + b;
		int d = a - b;
		int e = a * 8;
		double f = (c + a) / c;
		int g = (c + d) % e;

		if (f >= 0)
		{
			return true;
		}

		if (g == 0)
		{
			return true;
		}

		return false;
	}

	int strlen(const char* s)
	{
		if (s == NULL)
		{
			return 0;
		}

		int cnt = 0;
		while (*(s + cnt) != '\0')
		{
			cnt++;
		}
		return cnt;
	}
}