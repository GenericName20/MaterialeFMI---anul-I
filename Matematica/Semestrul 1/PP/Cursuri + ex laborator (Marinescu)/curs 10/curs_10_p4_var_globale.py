#DOMENIUL (SPATIUL) DE VIZIBILITATE AL VARIABILELOR
"""
def f():
    print(x)
x=10
f()

O variabila se creeaza la prima atribuire
Daca prima atrbuire este in functie -variabila locala functiei
Altfel -globala

La accesarea(interogarea) valorii unei variabile,
aceasta este cautata in local (daca suntem in functie),
apoi in global,
mai exact dupa regula LEGB (local, enclosing,global, builtin)
"""
def f():
    print(x) #x este intai cautat in local, apoi in global, unde este gasit
x=10 #fiind prima atribuire, x se creeaza in global
print(globals())
f()

print()

def f():
    x=5 #prima atribuire-se creeaza x in local cu valoarea 5, deci nu modifica x din global
    print(locals())
    print(x)

x=11
print(x)
f()
print(x) #ramane cu valoarea 11
"""
Daca la atribuire vrem sa se modifice variabila x din global (nu sa creeze una in local)
putem folosi instr
global x
(putem specifica in ce spatiu se uita dupa var la atribuire)
"""
def f():
    global x
    x=5 #modifica x din global
    print(locals())
    print(x)

x=11
print(x)
f()
print("in global",x) #x a devenit 5