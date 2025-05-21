#include<fstream>
 
using namespace std;
const long MAXDIM = 1000000;
long h[MAXDIM];
int parent(int i) {
    if(i==0)
        return 0;
    return (i-1)/2; }

int left(int i) { return (2*i + 1); }

int right(int i) { return (2*i + 2); }
void downKey ( long dim_heap, int i) {
    //fiul minim
    while (left(i) < dim_heap) {
        int min_desc = left(i);
        int r = right(i);

        if (r < dim_heap && h[r] < h[min_desc])
            min_desc = r;
        if (h[i] > h[min_desc])
            swap(h[i], h[min_desc]);
        i = min_desc;
    }
}
 
int extractMin( int &dim_heap){
 
    int x=h[0];
    h[0] = h[dim_heap-1];
    dim_heap--;
    downKey( dim_heap,0);
    return x;
}
void heapSort( long dim_heap){
    for(int i=dim_heap/2-1;i>=0; i--){
        downKey( dim_heap,i);
        }
}

int main(){
    ifstream f("heap_sort.in");
    ofstream g("heap_sort.out");
    long n;
    
    f>>n;

    for(int i=0;i<n;i++)
        f>>h[i];
    f.close();
    heapSort(n);
    int dim_h=n;
    for(int i=0;i<n;i++)
        g<<extractMin( dim_h)<<" ";
    g.close();
}