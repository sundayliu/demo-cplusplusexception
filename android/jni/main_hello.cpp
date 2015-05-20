#include <iostream>
#include <cstdio>
#include <stdexcept>

using namespace std;

int hello(int a, int b)
{
    int r = 0;
    try
    {
        r = a / b;
    }
    catch(int IntegerException)
    {
        cout << "IntegerException" << endl;
    }
    catch(overflow_error& e)
    {
        cout << e.what() << endl;
        b = 2;
    }
    catch(...)
    {
        b = 1;
    }
    
    return r;
}

class A
{
public:
    A(){cout << "constructor" << endl;}
    A(int id):m_id(id){cout << "constructor" << endl;}
    ~A(){cout << "destructor" << endl;}
    
    int getId(){return m_id;}
    void setId(int id){m_id = id;}
    
private:
    int m_id;
    
};
int main(int argc, char* argv[])
{
    int r = hello(3,0);
    cout << r << endl;
    
    A a(3);
    
    cout << a.getId() << endl;

    return 0;
}

