
.data
x: .space 4
vector: .space 44
fs1: .asciz "%ld"
end: .asciz "\n"
.text
.global main
main:
;# citim numarul de la tastatura
pushl $x
pushl $fs1
call scanf
popl %ebx
popl %ebx

lea vector, %edi
xorl %ecx,%ecx

;#vectorul de frecventa---------------------

;#initializam vectorul cu 0
for_vector:
    cmp $10, %ecx
    je exit_for_vector

    movl $0, (%edi,%ecx,4)
    
    incl %ecx
    jmp for_vector
exit_for_vector:


xorl %ecx,%ecx
;#adaugam elementele din numar in vectorul de frecventa
for:
    movl x, %ecx
    cmp $0, %ecx
    je exit_for

    ;#edx = n%10 , eax = n/=10
    movl x, %eax
    xorl %edx,%edx
    movl $10, %ebx
    divl %ebx

    add $1, (%edi,%edx,4)
    
    movl %eax, x
    jmp for
exit_for:
;# end vectorul de frecventa --------------


;# problema in sine -------------------
xorl %ecx, %ecx
for_nr_min:
    cmp $10, %ecx
    je exit_for_nr_min

    ;# x devine nr de paaritii a fiecarei cifra de la 0 la 9
    movl (%edi,%ecx,4), %ebx
    movl %ebx, x

    xorl %ebx, %ebx
    for_afisare:
        cmp x, %ebx
        je exit_for_afisare

        cmp $0, %ecx
        je cont1

        pusha
        pushl %ecx
        pushl $fs1
        call printf
        popl %ebx
        popl %ebx
        popa

        cont1:

        incl %ebx
        jmp for_afisare
    exit_for_afisare:

    incl %ecx
    jmp for_nr_min

exit_for_nr_min:

pushl $end
call printf
popl %ebx

movl $9, %ecx
for_nr_max:
    cmp $-1, %ecx
    je exit_for_nr_max

    ;# x devine nr de paaritii a fiecarei cifra de la 0 la 9
    movl (%edi,%ecx,4), %ebx
    movl %ebx, x

    xorl %ebx, %ebx
    for_afisare1:
        cmp x, %ebx
        je exit_for_afisare1

        pusha
        pushl %ecx
        pushl $fs1
        call printf
        popl %ebx
        popl %ebx
        popa

        incl %ebx
        jmp for_afisare1
    exit_for_afisare1:

    decl %ecx
    jmp for_nr_max
exit_for_nr_max:

exit:
pushl $end
call printf
popl %ebx

movl $1, %eax
xorl %ebx,%ebx
int $0x80