// https://www.pbinfo.ro/probleme/3011/lastk
//
//Programul citește de la tastatură numerele n, k, A, B, C, D. Șirul de numere se va genera după formulele:
//a[1] = A
// a[i] = (B * a[i-1] + C) % D, pentru i=2..n
#include<iostream>


using namespace std;
const int MAXDIM=100005;
int parent(int i) {
    if(i==0)
        return 0;
    return (i-1)/2; }

int left(int i) { return (2*i + 1); }

int right(int i) { return (2*i + 2); }
void downKey (int h[MAXDIM], int dim_heap, int i) {
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
int minim(int h[]){
    return h[0];
}
int extractMin(int h[MAXDIM], int &dim_heap){
    if (dim_heap==0)
        return -1;
    int x=h[0];
    h[0] = h[dim_heap-1];
    dim_heap--;
    downKey(h,dim_heap,0);
    return x;
}

void upKey(int h[MAXDIM], int &dim_heap, int i){
    int j=parent(i);
    while (i != 0 && h[j] > h[i])
    {
        swap( h[i],  h[j]);
        i = j;
        j=parent(i);

    }
    //se poate fara swap, doar il cobor si pun pe h[i] cand ii gasesc locul
}
void insert(int h[MAXDIM], int &dim_heap, int x){
    h[dim_heap]=x;
    int i=dim_heap;
    dim_heap++;
    upKey(h,dim_heap,i);

}
void print(int h[MAXDIM], int  dim_heap){
    for(int i=0;i<dim_heap;i++)
        cout<<h[i]<<" ";
}

int main(){
    int n,k,A,B,C,D, h[MAXDIM],dim_h=0;
    cin>>n>>k>>A>>B>>C>>D;
    long long  x=A;
     for(int i=0;i<k;i++){
        insert(h,dim_h,x);
        x=(B * x + C) % D;
    }
    for(int i=k;i<n;i++){
        if(minim(h)<x){	
            insert(h,dim_h,x);
            extractMin(h,dim_h);
        }
        x=(B * x + C) % D;
    }


    for(int i=0;i<k;i++)
        cout<<extractMin(h,dim_h)<<" ";


}