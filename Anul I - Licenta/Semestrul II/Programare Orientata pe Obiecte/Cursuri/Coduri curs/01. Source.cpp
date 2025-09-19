#include <iostream>

using namespace std;

/*
class baza
{
public:
    virtual void afis(){cout<<"parinte\n";}
};

class derivata : public baza
{
public:
    void afis(){cout<<"copil\n";}
};

int main()
{
    baza b;
    b.afis();
    derivata d;
    d.afis();

    baza* p = new derivata(); /// upcasting
    p->afis();
}
*/

class test
{
  int x,y,z;
public:
///    test(){cout<<"init\n";}
///    test(int a){cout<<"1\n";}
///    test(int a, int b){cout<<"2\n";}
    test(int a = 300, int b = 200, int c = 100){cout<<"3\n";}
};

int main()
{
    test A;
    test B(1);
    test C(2,3);
    test D(4,5,6);

    return 0;
}

/*****************/
/*
class test
{
 private:
     char y;
    long long x;
    int z;
 public:
    virtual void set_x(int a){
        ///x = a;
        } /// set - functie membra
    int get_x(){
        ///return x;
        } /// get - functie membra
        void f1(){}
        int f2(){return 1;}
};

int main()
{
    cout<<sizeof(test)<<endl;
    test A; ///constructor de initializare - implicit
///    A.x = 10;
///    A.set_x(10);

    test B(A); ///constructor de copiere - implicit
    test C = A; ///constructor de copiere - implicit
    test D; /// constructor de initializare - implicit
    D = A; /// operator de atribuire - implicit

///    cout<<D.get_x();

    return 0;
}
*/
