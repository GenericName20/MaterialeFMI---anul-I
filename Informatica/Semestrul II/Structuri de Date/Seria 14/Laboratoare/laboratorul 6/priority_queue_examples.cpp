#include <fstream>
#include<iostream>
#include<unordered_map>
#include <queue>
 //https://en.cppreference.com/w/cpp/container/priority_queue
 //https://www.geeksforgeeks.org/custom-comparator-in-priority_queue-in-cpp-stl/
using namespace std;
class customLess
{
public:
    bool operator()(const int l, const int r);
} ;

bool customLess::operator()(const int l, const int r) {
    if (abs(l) == abs(r))
        return l>r;
    return abs(l) > abs(r);
}
struct customLess2
{
    bool operator()(const int l, const int r){
        if (abs(l) == abs(r))
            return l>r;
        return abs(l) > abs(r);
    }
} ;
struct MyPair{
    int info;
    int info2;
    bool operator <(const MyPair r)  const{ //!!!const

        return info2>r.info2;
    }
    /*bool operator()(const MyPair l, const MyPair r)  {
        return l.info2>r.info2;
    }*/
};
int main() {
    //max heap implicit
    priority_queue<int> pq;
    for(int i=1;i<4;i++)
        pq.push(i);

    while(!pq.empty()){
        cout<<pq.top()<<" ";
        pq.pop();
    }
    cout<<endl;
    //min heap
    //varianta 1- introducem numerele cu semn schimbat (inmultite cu -1)
    priority_queue<int> pqminus;
    for(int i=1;i<4;i++)
        pqminus.push(-i);

    while(!pqminus.empty()){
        cout<<-pqminus.top()<<" ";
        pqminus.pop();
    }
    cout<<endl;

    //varianta 2 - specificam functia de comparare greater
    priority_queue<int, vector<int>, greater<int>> pq1;
    for(int i=1;i<4;i++)
        pq1.push(i);

    while(!pq1.empty()){
        cout<<pq1.top()<<" ";
        pq1.pop();
    }
    cout<<endl;
    //varianta 2 - specificam functia de comparare proprie
    priority_queue<int, vector<int>, customLess2> pq2;
    //priority_queue<int, vector<int>, customLess> pq2;
    for(int i=1;i<4;i++) {
        pq2.push(i);
        pq2.push(-i);
    }

    while(!pq2.empty()){
        cout<<pq2.top()<<" ";
        pq2.pop();
    }
    cout<<endl;

    priority_queue<MyPair> pq_pair;
    MyPair t={4,5};
    pq_pair.push(t);
    pq_pair.push({3,6});
    pq_pair.push({5,1});
    while(!pq_pair.empty()){
        cout<<pq_pair.top().info<<" "<<pq_pair.top().info2<<endl;
        pq_pair.pop();
    }
    cout<<endl;
}
