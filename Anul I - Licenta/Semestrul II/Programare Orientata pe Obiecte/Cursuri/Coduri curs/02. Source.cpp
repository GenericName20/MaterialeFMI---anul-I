#include <iostream>

using namespace std;

class serie
{
    int x;
public:
    serie(int a = 0){x = a;}
    serie(const serie& ob){x = ob.x; ob.x = 152;}
    int get_x(){return x;}
};

int main()
{
    serie A(15);
    serie B = A;
    cout<<B.get_x()<<" "<<A.get_x();
}

/*
int f(int x){ cout<<"int ";return x;}
float f(float x){cout<<"float ";return x;}
int main()
{
    /// f(12);
    float y = (float)12.34;
    f(y);
    /// f(12.34);
}
*/
/***** recap ambiguitate la supraincarcarea functiilor ****/
/*
int f(int x){ return x;}
float f(int x){return x;}
int main()
{
///    f(12);
///    f(12.34);
}
*/

/***** operatorul :: si clasele; utilizare compunere/agregare ******/
/*
class student{
    ///student* Y;
public:
    void citire(){cout<<"\ncitire student";}
    void afisare();
};
class serie
{
    student S; ///compunere/agregare
    student v[100];
public:
    void citire(){cout<<"\ncitire serie";}
    void afisare();
};
void serie::afisare(){cout<<"\nafisare serie"; S.afisare();}
void student::afisare(){cout<<"\nafisare student";}

int main()
{
    serie A;
    A.citire();
    A.afisare();
}
*/
/***** operatorul de rezolutie de scop :: ********/
/*
int x = 10;

void f(int x)
{
    cout<<"\nx local = "<<x;
    x = 20;
    cout<<"\nx local = "<<x;
    ::x = 40;
    cout<<"\n vreau sa modific x global in functie = "<<::x;
}

int main()
{
    cout<<"\n x global = "<<x;
    int x = 30;
    cout<<"\n x global = "<<x;
    cout<<"\n x in main = "<<x;
    f(x);
}
*/
/****** ascunderea informatiei - modificatori de acces *******/
/*
class serie
{ /// private:
protected:
    int nr; /// data membra
public:
    void citire(){cin>>nr;}  /// functie membra
    void afisare(){cout<<nr<<" ";} /// functie membra

};

class serie15 : public serie
{
    int nota;
public:
    void citire(){cin>>nr>>nota;}
    void afisare_derivata(){cout<<nr<<" "<<nota<<endl;}
};

int main()
{
    serie15 B;
    B.citire(); /// din derivata
    B.serie::citire();  /// din baza
    B.afisare_derivata();
}
*/

/******** ascunderea informatiei **********/
/*
class serie
{ /// private:
    int nr; /// data membra
public:
    void citire(){cin>>nr;}  /// functie membra
    void afisare(){cout<<nr<<" ";} /// functie membra
    friend void citire_si_afisare(serie& X);
};

void citire_si_afisare(serie& X){cin>>X.nr; cout<<X.nr;}
int main()
{
    serie A;
///    A.citire();
///    A.afisare();
    citire_si_afisare(A);
    return 0;
}
*/
/******** incapsulare *********/
/*
struct serie
{
    int nr;
    void citire(){cin>>nr;}
    void afisare(){cout<<nr<<" ";}
};
int main()
{
    serie A;
    A.citire();
    A.afisare();
    return 0;
}
*/
/*
struct serie
{
    int nr;
};

void citire(serie& x){cin>>x.nr;}
void afisare(serie x){cout<<x.nr<<" ";}

int main()
{
    serie A;
    citire(A);
    afisare(A);
    return 0;
}
*/
