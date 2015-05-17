#ifndef HELLO_TEST_H
#define HELLO_TEST_H

namespace hello
{
	class Test
	{
	public :
		Test();
		Test(int a);

		~Test();

		int getId();
		void setId(int ID);

	private:
		int ID;
	};

	class Person
	{
	public:
		Person();
		virtual ~Person();

	public:

		virtual void go()const{}
		const char* getName();
		int getId();

		void setName(const char* name);
		void setId(int ID);

	private:
		int ID;
		char* name;
	};

	class Man :public Person
	{
	public:
		Man();
		virtual ~Man();

	public:
		virtual void go()const;
	};

	class Woman :public Person
	{
	public:
		Woman();
		virtual ~Woman();

	public:
		virtual void go()const;
	};
}
#endif