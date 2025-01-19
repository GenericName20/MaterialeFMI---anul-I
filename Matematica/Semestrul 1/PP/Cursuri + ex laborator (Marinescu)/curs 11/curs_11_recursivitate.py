def afisare(n):
    if n==1:
        print(n, end=" ")
    else:
        #print(n, end=" ") - ar afisa descrescator
        afisare(n-1) #afisez 1...n-1 -> problema mai mica de acelasi fel
        print(n, end=" ")

afisare(4)
print()
#al n-lea termen fibonacci
#1,1,2,3,5
def fibo(n):
    if n<=2:
        return 1
    return fibo(n-1)+fibo(n-2)
print(fibo(6)) #complexitate exponantial - repeta calculul de subroobleme fibo(x)

#al n-lea termen nerecursiv - liniar - numar de operatii proportinal cu n
def fibo_nerec(n):

    f1,f2=1,1
    for i in range(3,n+1):
        """f3=f1+f2
        f1=f2
        f2=f3
        """
        f1,f2=f2,f1+f2
    return f2
print(fibo_nerec(6))

