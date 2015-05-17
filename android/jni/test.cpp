#include "test.h"
#include "utils.h"


namespace hello
{
	Test::Test() :ID(0)
	{
		const char* desc = "Test default constructor\n";
		print(desc, strlen(desc));
	}

	Test::Test(int a) : ID(a)
	{
		const char* desc = "Test 1 params constructor\n";
		print(desc, strlen(desc));
	}

	Test::~Test()
	{
		const char* desc = "Test destructor\n";
		print(desc, strlen(desc));
	}

	void Test::setId(int ID)
	{
		this->ID = ID;
	}

	int Test::getId()
	{
		return this->ID;
	}


	// Person Class
	Person::Person():ID(0),name(NULL)
	{
		const char* desc = "Person constructor\n";
		print(desc, strlen(desc));
	}

	Person::~Person()
	{
		const char* desc = "Person destructor\n";
		print(desc, strlen(desc));
	}


	void Person::setId(int ID)
	{
		this->ID = ID;
	}

	void Person::setName(const char* name)
	{
		this->name = (char*)name;
	}

	int Person::getId()
	{
		return ID;
	}

	const char* Person::getName()
	{
		return name;
	}
	// Man Class

	Man::Man()
	{
		const char* desc = "Man constructor\n";
		print(desc, strlen(desc));
	}

	Man::~Man()
	{
		const char* desc = "Man destructor\n";
		print(desc, strlen(desc));
	}

	void Man::go()const
	{
		const char* desc = "Man go\n";
		print(desc, strlen(desc));
	}
	// Woman Class

	Woman::Woman()
	{
		const char* desc = "Woman constructor\n";
		print(desc, strlen(desc));
	}

	Woman::~Woman()
	{
		const char* desc = "Woman destructor\n";
		print(desc, strlen(desc));
	}

	void Woman::go()const
	{
		const char* desc = "Woman go\n";
		print(desc, strlen(desc));
	}


}