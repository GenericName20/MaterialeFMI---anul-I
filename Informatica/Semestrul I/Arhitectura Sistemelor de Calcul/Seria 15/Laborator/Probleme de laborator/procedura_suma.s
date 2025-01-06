.data
n: .space 4
a: .space 4
s: .space 4
vector: .space 400

fs1: .asciz "%ld"
print: .asciz "%ld\n"

.text
aduna: ;# 8(%ebp) = $s, 12(%ebp) = n; 16,20... x1, x2,...
    pushl %ebp
    movl %esp, %ebp

    ;# initializam suma cu primul numar
    movl 8(%ebp), %eax ;# valoarea s
    movl 16(%ebp), %ecx
    movl %ecx, 0(%eax) ;# punem x1 in s

    addl $4, 12(%ebp) ;# -1 deoarece am folosit x1
    movl $5, %ecx
    for_aduna:
        cmp 12(%ebp), %ecx
        je exit_for_aduna
        
        movl (%ebp, %ecx,4), %edx
        addl %edx, 0(%eax)

        addl $1, %ecx
        jmp for_aduna
    exit_for_aduna:
    
    pop %ebp
ret
.global main
main:
;# citim n
pushl $n
pushl $fs1
call scanf
addl $8, %esp

;#cream vector
xorl %ecx, %ecx
lea vector, %edi
for_i:
    cmp %ecx, n
    je exit_for_i

    pusha
    pushl $a
    pushl $fs1
    call scanf
    add $8, %esp
    popa

    movl a, %eax
    movl %eax, (%edi, %ecx, 4)

    incl %ecx
    jmp for_i
exit_for_i:


;# incepe sa punem pe stiva
movl n, %ecx
for_push:
    decl %ecx
    movl (%edi, %ecx, 4), %eax

    pushl %eax

    incl %ecx
loop for_push

pushl n
push $s
call aduna

;#calculam cate popuri trb sa facem 4 + 4 + 4 *n = 4(n+2)
movl n, %eax
addl $2, %eax
movl $4, %edx
mull %edx

addl %eax, %esp

pushl s
pushl $print
call printf
addl $8, %esp

exit:
movl $1, %eax
xorl %ebx, %ebx
int $0x80