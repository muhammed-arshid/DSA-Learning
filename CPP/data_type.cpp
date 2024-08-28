#include<iostream>
using namespace std;

int main(){
    //int 
    int a = 10; // 4 bytes and only store range of -2^31 to 2^31-1 (-2147483648 to 2147483647)
    //long int
    long int b = 10; // 8 bytes and store range of -2^63 to 2^63-1
    long long int c = 10; // 8 bytes and store range of -2^63 to 2^63-1
    //create example for unsigned int, unsigned long int, unsigned long long int
    unsigned int d = 10; // 4 bytes and store range of 0 to 2^32-1
    unsigned long int e = 10; // 8 bytes and store range of 0 to 2^64-1
    unsigned long long int f = 10; // 8 bytes and store range of 0 to 2^64-1
    //float
    float g = 10.5; // 4 bytes and store range of 3.4e-38 to 3.4e+38 with 6 decimal places

    //double
    double h = 10.5; // 8 bytes and store range of 1.7e-308 to 1.7e+308 with 15 decimal places

    //long double

    long double i = 10.5; // 16 bytes and store range of 3.4e-4932 to 1.1e+4932 with 19 decimal places

    //char
    char j = 'A'; // 1 byte and store range of -128 to 127

    //bool

    bool k = true; // 1 byte and store true or false


    //below all change std::cout to std::std::cout
    std::cout<<"int: "<<a<<std::endl;
    std::cout<<"long int: "<<b<<std::endl;
    std::cout<<"long long int: "<<c<<std::endl;
    std::cout<<"unsigned int: "<<d<<std::endl;
    std::cout<<"unsigned long int: "<<e<<std::endl;
    std::cout<<"unsigned long long int: "<<f<<std::endl;
    std::cout<<"float: "<<g<<std::endl;
    std::cout<<"double: "<<h<<std::endl;
    std::cout<<"long double: "<<i<<std::endl;
    std::cout<<"char: "<<j<<std::endl;
    std::cout<<"bool: "<<k<<std::endl;
    return 0;
}