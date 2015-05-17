#ifndef HELLO_UTILS_H
#define HELLO_UTILS_H


namespace hello
{
#define NULL 0
	void print(const char* s, int len);

	__attribute__((noinline))bool predicate(int a, int b);

	int strlen(const char* s);
}

#endif