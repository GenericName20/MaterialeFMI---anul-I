# Test de Laborator (3.1 & 3.2)

## Subiecte
- [Test 3.1](./Test%20Laborator%203.1.pdf)
- [Test 3.2](./Test%20Laborator%203.2.pdf)

---

1. (3.1) Fie codul de mai jos. Care este valoarea lui s când execuția ajunge la `et_exit`?

```
.data
s: .long 0

.text
.global main
main:
    mov $1, %edx
    mov $0, %eax
    movl $0xffffffff, %ebx
    divl %ebx
    mov %eax, %ecx

et_loop:
    add %ecx, s
    loop et_loop

et_exit:
    mov $1, %eax
    mov $0, %ebx
    int $0x80
```

Grilă:
A) 1
B) 0
C) 0xffffffff
D) 15

Rezolvare:
```
Observăm cum evoluează codul:
mov $1, %edx        <=> %edx = 1
mov $0, %eax        <=> %eax = 0
movl $0xffffffff    <=> %ebx = 2^32
divl %ebx           <=> (%eax, %edx) = (%eax / %ebx, %eax % %ebx)
                    Ne trebuie doar %eax
                    <=> %eax = (edx * 2^32 + %eax) / 2^32 = 2^32 / (2^32 - 1) = 1

mov %eax, %ecx      <=> %ecx = %eax = 1
(et_loop):
    add %ecx, s
    loop et_loop    <=> %ecx = %ecx - 1 = 0 -> sare la et_exit

et_exit:
    mov $1, %eax
    mov $0, %ebx
    int $0x80
```

Răspuns:
A) 1

---

1. (3.2) Fie codul de mai jos. Care sunt valorile lui `%eax` și `%edx` când execuția ajunge la `label`?

```
.data
    x: .long 17
    y: .long 6
.text
.global main
main:
    mov $1, %edx
    mov x, %eax
    jmp et
    mov $0, %edx
et:
    divl y
label:
    mov $1, %eax
    mov $0, %ebx
    int $0x80
```

Grilă:
A) eax = 0x2aaaaaad, edx = 0x3
B) eax = 0x2, edx = 0x5
C) eax = 0x5, edx = 0x2
D) eax = 0x3, edx = 0x2aaaaaad

Rezolvare:
```
Urmărim instrucțiunile din cod:
mov $1, %edx    <=> %edx = 1
mov x, %eax     <=> %eax = x = 17 = 2^4 + 1
jmp et           -> sare la et, este salt necondiționat

divl y          <=> %eax = (1 * 2^32 + 2^4 + 1) / (2^2 + 2)

eax:
(OF1).0000.0000.0000.0000.0000.0000.0001.0001 :
                                          101
----------------------------------------------
      0010.1010.1010.1010.1010.1010.1010.1101 = 0x2aaaaad = %eax
                                           011 (rest) = 3 = %edx
```

Răspuns:
A) %eax = 0x2aaaaaad, edx = 0x3

---

2. (3.1) Se stochează în registrul `eax valoarea 0x40000000`, în `ebx 0x8`, în `ecx 0x1` și în edx `0x8`. Ce valori vor avea regiștrii eax și edx după executarea instrucțiunii `mul %edx`?

Grilă:
A) eax = 0, edx = 2
B) eax = 32, edx = 0
C) eax = 32, edx = 2
D) eax = 2, edx = 0

Rezolvare:
```
eax = 0x4000.0000 = 4 * 16^7 = 2^2 * (2^4)^7 = 2^30
ebx = 0x0000.0008 = 8 * 16^0 = 2^3
ecx = 0x0000.0001 = 1 * 16^0 = 2^0
edx = 0x0000.0008 = 2^3

mul %edx <=> eax = eax * edx = 2^30 * 2^3 = 2^33 (Overflow -> restul intră în edx -> edx = 2^33/2^32 = 2)

```

Răspuns:
A) eax = 0, edx = 2

---

3. (3.1) Se stochează în `%edx valoarea 0`, în `eax 47` și în `ebx 15`. Ce valori vor avea regiștrii `eax` și `edx` după executarea instrucțiunii `div %ebx`?

Grilă:
A) eax = 3, edx = 2
B) eax = 3, edx = 0
C) eax = 2, edx = 0
D) eax = 2, edx = 3

Rezolvare:
```
%eax = 47
%ebx = 15
%edx = 0

div %ebx <=>   (%eax, %edx) = (%eax / %ebx, %eax % %ebx)
                            = (47 / 15, 47 % 15)
                            = (3, 2)

Deci, %eax = 3 și %edx = 2
```

Răspuns:
A) eax = 3, edx = 2

---

4. (3.1) Fie codul de mai jos. Care este valoarea depozitată la final în `ecx` (în dreptul etichetei `exit`)?

Grilă:
A) 5
B) 6

```
.data
x: .long 0x80000000
y: .long 0x70000000

.text
.global main
main:
    mov x, %eax
    cmp y, %eax
    jge label
    mov  $5, %ecx
    jmp exit

label:
    mov $6, %ecx

exit:
    mov $1, %eax
    mov $0, %ebx
    int $0x80
```

Rezolvare:
```
Observăm că %eax primește toți biții din reprezentarea valorii de la adresa lui x. (Se folosește comanda mov, iar destinația este un registru întreg %eax, deci e pe 4 bytes).

Comparația se realizează pe un tip de date nespecificat, deci se vor compara toți biții din reprezentarea lui y cu toți biții din reprezentarea lui %eax.

Valorile comparate nu sunt egale, așadar nu se va face jump la label.

Valoarea lui %ecx la etexit este, așadar, $5.
```

Răspuns:
A) 5

---

5. (3.1) Fie următorul program. Ce valoare vom obține dacă vom rula cu debuggerul următoarele comenzi?

```
b et_exit
run
i r ebx
```
Cod:
```
.data
.text
.global main
main:
    mov $3, %eax
    shl $2, %eax
    mov $2, %ebx
    mul %ebx
    mov $0, %ebx
    mov $8, %ebx
    div %ebx
    sub %eax, %ebx

et_exit:
    mov $1, %eax
    mov $0, %ebx
    int $0x80
```

Grilă:
A) 5
B) 2
C) 3
D) 8

Rezolvare:
```
Observăm comportamentul comenzilor pe care le folosim:
b et_exit - Setează un breakpoint la eticheta et_exit
run - Setează un instruction pointer la prima instrucțiune după eticheta et_exit
i r ebx - Fără a face niciun pas suplimentar, se interoghează registrul %ebx (încercăm să aflăm valoarea lui).

Așadar, trebuie să 'rulăm' codul manual, până la eticheta et_exit.

mov $3, %eax    <=> %eax = 3
shl $2, %eax    <=> %eax = %eax << 2 = 3 * 2^2 = 3 * 4 = 12
mov $2, %ebx    <=> %ebx = 2
mul %ebx        <=> %eax = %eax * %ebx = 12 * 2 = 24
mov $0, %edx    <=> %edx = 0
mov $8, %ebx    <=> %ebx = 8
div %ebx        <=> (%eax, %edx) = (%eax / %ebx, %eax % %ebx)
                                 = (24 / 8, 24 % 8) => %eax = 3, %edx = 0
sub %eax, %ebx  <=> %ebx - %eax = 8 - 3 = 5
```

Răspuns:
A) 5

---

6. (3.1) Care este ordinea de trecere prin etichete?

```
.data
.text
global main
main:
    mov $1, %eax
    mov $2, %ebx
    mov $3, %ecx
    mov $4, %edx
    cmp %ebx, %eax
    je etx

ety:
    cmp %ecx, %edx
    jg etz
    jmp ett

etx:
    jmp ety

etz:
    jmp %ebx, %edx
    jmp ety

ett:
    mov $1, %eax
    mov $0, %ebx
    int $0x80
```

Grilă:
A) ety, etz, ety, ett
B) etx, ety, etz, ety, ett
C) etx, ety, ett
D) ety, etx, etz, ett

Rezolvare:
```
Urmărim instrucțiunile din cod:
movl $1, %eax   <=> %eax = 1
movl $2, %ebx   <=> %ebx = 2
movl $3, %ecx   <=> %ecx = 3
movl $4, %edx   <=> %edx = 4

cmp %ebx, %eax  <=> %eax == %ebx ? <=> 1 == 2? false
je etx           -> nu sare

(1! ety):
cmp %ecx, %edx  <=> %edx > %ecx ? <=> 4 > 3 true
jg etz           -> sare la etz
jmp ett

(2! etz):
mov %ebx, %edx  <=> %edx = %ebx <=> %edx = 2
jmp ety          -> sare la ety

(3! ety):
cmp %ecx, %edx  <=> %edx > %ecx ? <=> 2 > 3 false
jg etz
jmp ett          -> sare la ett

(4! ett):
exit(0)
```

Răspuns: 
A) ety, etz, ety, ett