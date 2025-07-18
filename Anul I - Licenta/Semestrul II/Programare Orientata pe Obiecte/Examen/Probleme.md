## Problema 1

```
#include <iostream>
using namespace std;
class cls1
{
protected:
    int x;

public:
    cls1() { x = 13; }
};
class cls2 : public cls1
{
    int y;

public:
    cls2() { y = 15; }
    int f(cls2 ob) { return (ob.x + ob.y); }
};
int main()
{
    cls2 ob;
    cout << ob.f(ob);
    return 0;
}
```

### Soluție:
1. Compilează
2. Afișează: 28

## Problema 2
```
#include <iostream>
using namespace std;

class A {
    static int x;

public:
    A(int i = 0) { x = i; }
    int get_x() { return x; }
    int& set_x(int i) { x = i; }
    A operator=(A a1)
    {
        set_x(a1.get_x());
        return a1;
    }
};
int main()
{
    A a(212), b;
    cout << (b = a).get_x();
    return 0;
}
```
### Soluție:
1. Nu compilează: `static int x` nu este inițializată by default.
2. Renunțăm la `static`.

## Problema 3
```
#include<iostream>
using namespace std;

class A
{ int i;
  public: A(int x=2):i(x+1) {}
  virtual int get_i() { return i; }};
class B: public A
{ int j;
  public: B(int x=20):j(x-2) {}
  virtual int get_j() {return A::get_i()+j; }};
int main()
{ A o1(5);
  B o2;
  cout<<o1.get_i()<<" ";
  cout<<o2.get_j()<<" ";
  cout<<o2.get_i();
  return 0;
}
```
### Soluție:
1. Compilează
2. 6 21 3
- `o1(5) -> A(5) -> i = 6 -> o1.get_1() = 6`
- `o2() -> B(20) : A(), j(20 - 2) -> A(default) -> i = 3; j = 18 -> o1.get_j() = 21`
- `o2.get_i() = 3`

## Problema 4
```
#include <iostream>
using namespace std;
class problema {
    int i;

public:
    problema(int j = 5) { i = j; }
    void schimba() { i++; }
    void afiseaza() { cout << "starea curenta " << i << "\n"; }
};
problema mister1() { return problema(6); }
void mister2(problema& o)
{
    o.afiseaza();
    o.schimba();
    o.afiseaza();
}
int main()
{
    mister2(mister1());
    return 0;
}
```
### Soluție:
1. Nu compilează: În `return problema(6)`, obiectul creat este temporar. Referințele la obiecte temporar sunt adresate prin &&., motiv pentru care schimbăm antetul funcției `mister2()`.
2. `void mister2(problema&& o)`

## Problema 6
```
#include <iostream>
using namespace std;
class B {
    int x;

public:
    B(int i = 7) { x = i; }
    int get_x() { return x; }
    operator int() { return x; }
};
class D : public B {
public:
    D(int i = -12)
        : B(i)
    {
    }
    D operator+(D a) { return get_x() + a.get_x() + 1; }
};
int main()
{
    D a;
    int b = 18;
    b += a;
    cout << b;
    return 0;
}
```
### Soluție:
1. Compilează: `b += a` încearcă o conversie implicită a lui a la int, ceea ce funcționează datorită `operator int() { return x; }` 
2. Afișează: 6

## Problema 7
```
#include <iostream>
using namespace std;
#include <typeinfo>
class B {
    int i;

public:
    B() { i = 1; }
    int get_i() { return i; }
};
class D : B {
    int j;

public:
    D() { j = 2; }
    int get_j() { return j; }
};
int main()
{
    B* p = new D;
    cout << p->get_i();
    if (typeid((B*)p).name() == "D*")
        cout << ((D*)p)->get_j();
    return 0;
}
```
### Soluție:
1. Nu compilează: error: ‘B’ is an inaccessible base of ‘D’
2. Derivăm class D : <b> public</b> B

## Problema 8
```
public:
    A(int i) { x = i; }
    int get_x() { return x; }
    int& set_x(int i) { x = i; }
    A operator=(A a1)
    {
        set_x(a1.get_x());
        return a1;
    }
};
class B : public A {
    int y;

public:
    B(int i = 0)
        : A(i)
    {
        y = i;
    }
    void afisare() { cout << y; }
};
int main()
{
    B a(112), b, *c;
    cout << (b = a).get_x();
    (c = &a)->afisare();
    return 0;
}
```
### Soluție:
1. Nu compilează: error: no matching function for call to ‘B::B()’
2. Setăm o valoare default pentru parametrul din constructorul `B(int i = 0)`

## Problema 12
```
#include <iostream>
using namespace std;
class cls {
    int x;

public:
    cls(int i) { x = i; }
    int set_x(int i)
    {
        int y = x;
        x = i;
        return y;
    }
    int get_x() { return x; }
};
int main()
{
    cls* p = new cls[10];
    int i = 0;
    for (; i < 10; i++)
        p[i].set_x(i);
    for (i = 0; i < 10; i++)
        cout << p[i].get_x();
    return 0;
}
```
### Soluție:
1. Nu compilează! <b>Dacă definim cel puțin un constructor, C++ nu mai creează un constructor default</b> (deci nu are cls::cls()).
2. Setăm o valoare default în constructor: cls(int i = 0)

## Problema 15 (foarte asemănătoare cu 12)
```
#include <iostream>
using namespace std;

struct cls {
    int x;

public:
    int set_x(int i)
    {
        int y = x;
        x = i;
        return x;
    }
    int get_x() { return x; }
};
int main()
{
    cls* p = new cls[100];
    int i = 0;
    for (; i < 50; i++)
        p[i].set_x(i);
    for (i = 5; i < 20; i++)
        cout << p[i].get_x() << " ";
    return 0;
}
```
### Soluție
1. Compilează: <b>Dacă nu definim constructor, C++ creează unul default</b>.
2. Afișează: 5 6 ... 19

## Problema 16
```
#include <iostream>
using namespace std;

class A {
protected:
    int x;

public:
    A(int i = 14) { x = i; }
};
class B : A {
public:
    B()
        : A(2)
    {
    }
    B(B& b) { x = b.x - 14; }
    void afisare() { cout << x; }
};
int main()
{
    B b1, b2(b1);
    b2.afisare();
    return 0;
}
```
### Soluție
1. Compilează
2. Afișează: -12

## Problema 17
```
#include <iostream>
using namespace std;

class A {
protected:
    static int x;

public:
    A(int i = 0) { x = i; }
    virtual A schimb() { return (7 - x); }
};
class B : public A {
public:
    B(int i = 0) { x = i; }
    void afisare() { cout << x; }
};
int A::x = 5;
int main()
{
    A* p1 = new B(18);
    *p1 = p1->schimb();
    ((B*)p1)->afisare();
    return 0;
}
```
## Soluție
1. Compilează. B(18) -> A(0) {x = 18} -> 7 - 18 = 11
2. Afișează: 11

## Problema 18
```
#include <iostream>
using namespace std;

template <class T, class U>
T fun(T x, U y)
{
    return x + y;
}
int fun(int x, int y)
{
    return x - y;
}
int fun(int x)
{
    return x + 1;
}
int main()
{
    int *a = new int(10), b(5);
    cout << fun(a, b);
    return 0;
}
```
## Soluție:
1. 


## Problema 19




## Probleme tutoriat
```
#include<iostream>
#include<vector>
using namespace std;

class Test{
    int i;
    public:
    Test(int x = 0) : i(x) { 
        cout << "C "; 
    };
    
    Test(const Test& x) {
        i=x.i;
        cout<<"CC ";
    }

    ~Test(){
        cout<<"D ";
    }
};

int main() {
    vector<Test> v;
    v.push_back(1);
    Test ob(3);
    v.push_back(ob);
    Test& ob2 = ob;
    v.push_back(ob2);
    return 0;}
```
## Soluție:
```
// Definiția funcției push_back
template<class type>
void vector<type>::push_back(const type& x) {
    if (size_ == capacity_) {
        capacity_ *= 2;
        contents_ = (type*)realloc(contents_, capacity_ * sizeof(type));
    }
    contents_[size_] = x;
    size_++;
}
```

### v.push_back(1);

- Încearcă o conversie implicită la Test(1). Merge, creează obiectul **(C)**.
- Observăm size = 0, capacity = 0.
- În v[0] se copiază obiectul, deci **(CC)**, apoi size = 1.
- Apoi, obiectul a fost creat prin conversie implicită, deci se șterge: **(D)**.

### Test ob(3);

- Creează obiectul ob cu x = 3 **(C)**.

### v.push_back(ob);
- Pasează prin referință obiectul ob.
- size = 1, capacity = 1 -> capacity = 2 -> Se dă realloc, deci se copiază elementul aflat în vector la acel moment, deci **(CC)**.
- În v[1] se copiază obiectul pasat prin referință, deci **(CC)**, apoi size = 2.
- Apoi, obiectul temporar creat în realloc se șterge **(D)**.

### Test& ob2 = ob;

- Se creează o referință la acel obiect ob, nu este copiat, doar adresa este copiată.

### v.push_back(ob2);
- Pasează prin referință obiectul ob.
- size = 2, capacity = 2 -> capacity = 4 -> Se dă realloc, deci se copiază elementele aflate în vector la acel moment, deci **(CC CC)**.
- În v[2] se copiază obiectul pasat prin referință, deci **(CC)**, apoi size = 3.
- Apoi, obiectele temporare create în realloc se șterg: **(D D)**.

La final, sunt șterse 4 obiecte:
- 3 obiecte din vectorul v **(D D D)**
- obiectul ob rămas în main **(D)**

### Răspuns final: C CC D C CC CC D CC CC CC D D D D D D



# Teorie
## Metode statice / nestatice:
- Cele statice sunt descriptive unei clase, iar cele nestatice unui obiect al unei clase.
- Cele statice au acces doar la datele membre statice din clasă, în timp ce acelea non-statice au acces la tot.
- Cele statice pot fi apelate în lipsa unui obiect, iar cele nestatice implică obiectul.
- Cele statice sunt partajate în toată clasa, ceea ce înseamnă că modificarea unei date statice este modificată pentru toate obiectele clasei.
- Având acces la date statice, e de folos pentru Singleton la getInstance().
- Sintaxă:
```
class C {
  static inline string base = "https://fmi.unibuc.ro";
  // definiție inline, teoretic e definită în afara clasei, dar practic e aici

  static C instance;
  // o instanță statică a obiectului C partajat de toate obiectele clasei C, definită în afara clasei

  C() = default;

public:
  // funcția e statică, poate fi apelată prin C::getInstance()
  // fiind statică, are acces la data statică 'instance'
  static C& getInstance() {
    return instance; // (e statică în C)
  }

  // funcția e non-statică, poate fi apelată doar prin obiect ce aparține clasei C
  void show(){
    cout << "da" << endl;
  }

  // funcția e non-statică, poate fi apelată doar prin obiect ce aparține clasei C
  // fiind non-statică, tot are acces la data statică 'instance'
  C& getInstanceTO() {
    return instance;
  }

  // IDEM, obiectului referit de 'this' are data 'base' partajată prin clasa C, deci are acces la ea
  string& getBase() {
    return this->base;
  }
};

C C::instance;

int main() {
  C& app = C::getInstance();
  app.show();   // "da"
  C& app2 = app.getInstanceTO();
  app2.show();  // "da"
  cout << app2.getBase();   // "fmi.unibuc.ro"
  return 0;
}
```