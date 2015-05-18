#include "utils.h"
#include "test.h"
#include <stdio.h>
using namespace hello;

void HandlePerson(const Person& person)
{
	person.go();
}

int hello_main()
{
    const char* desc = "Hello,world\n";
	print(desc, strlen(desc));

	Test a;
	Test b(1);

	int ID_a = a.getId();
	int ID_b = b.getId();

	int ID_sum = ID_a + ID_b;

	a.setId(ID_sum);
	b.setId(ID_sum);

	printf("a id:%d\n", a.getId());
	printf("b id:%d\n", b.getId());

	Man man;
	Woman woman;
	HandlePerson(man);
	HandlePerson(woman);

    return 0;
}

