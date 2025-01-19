"""
COLECTII - obiect care memoreaza mai multe obiecte,
cu o anumita structura (sir de caractere, liste, multimi,dictionare)

SECVENTE - colectii indexate (de la 0)
    - pot accesa un element cu ajutorul indicelui: s[i]
"""
#sirul de caractere - clasa str
s="un exemplu"
print(s,type(s)) #str
#s[0]="A" - imutabil (nu pot modifica un caracter din sir)
ls = [1,6,2,9, "abc"] #lista - vector (tablou) - clasa list
print(ls,type(ls)) #list - pot fi neomogene
# (cu element de tipuri de diferite)
ls[0]=12 #se poate
print(ls)
t = (1,6,"abc") #tuplu
# tuplu- lista imutabila (nu putem modifica elementele t[i]=2)
print(t,type(t))
#t[0]=8

#Accesare
#indici 0,..len(s)-1
#indici negativi -1 = ultima pozitie
s="Programare"
print(s[0],s[-1],s[len(s)-1])
#print(s[12])
print("gata")

#Feliere s[i:j], s[i:j:pas], pas poate fi negativ
#i,j-pot lipsi
#prefix, sufix de lungime 3
print(s[:3],s[-3:])
s="abccbaw"
#test palindrom:

inv_s=s[::-1]
print(inv_s)
print(s==inv_s)
ls=[1,2,3,4,5,6]
#elementele de pe pozitii pare de la final la inceput
print(ls[6::-2])

s="Programare"
print(s[7:20]) #s[7:len(s)]

