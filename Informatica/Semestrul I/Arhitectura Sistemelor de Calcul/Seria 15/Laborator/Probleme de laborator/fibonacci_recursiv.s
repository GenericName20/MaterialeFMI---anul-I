.data
n: .space 4

t0: .long 0
t1: .long 1
fs1: .asciz "%ld"
afisare: .asciz "Al %ld-lea element din sirul lui Fibonacci este %ld\n" ;# {n} {x}
.text
fibonacci: ;# 8(%ebp) = n 
    pushl %ebp
    movl %esp, %ebp
    pushl %ebx

    movl 8(%ebp), %ecx

    cmp $0, %ecx
    jne verife

    movl $0, %eax
    jmp exit_fibonacci
    
    verife:
    cmp $1, %ecx
    jne continue

    movl $1, %eax
    jmp exit_fibonacci

    continue:
    
    decl %ecx

    
    xorl %ebx, %ebx

    pushl %ecx
    call fibonacci
    popl %ecx

    decl %ecx
    addl %eax, %ebx

    pushl %ecx
    call fibonacci
    pop %ecx

    addl %eax, %ebx

    movl %ebx, %eax

    
    exit_fibonacci:
    pop %ebx
    pop %ebp
ret
.global main
main:
pushl $n
pushl $fs1
call scanf
addl $8, %esp

movl n, %eax
cmp $0 , %eax
jne verif
jmp afisarea

verif:
cmp $1, %eax
jne fib
jmp afisarea

fib:
xorl %eax, %eax
xorl %ebx, %ebx
pushl n
call fibonacci ;# rez in eax
addl $4, %esp


afisarea:
pushl %eax
pushl n
pushl $afisare
call printf
addl $12, %esp

exit:
movl $1, %eax
xorl %ebx, %ebx
int $0x80