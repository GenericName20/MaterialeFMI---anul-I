.data
n: .space 4
z: .space 4

x: .long 1
y: .long 1
fs1: .asciz "%ld"
print: .asciz "%ld\n"
.text
aduna: ;# 8(%ebp) = a, 12(%ebp) = b, return in %eax
    pushl %ebp
    movl %esp, %ebp

    xorl %eax, %eax
    movl 8(%ebp), %ecx
    movl 12(%ebp), %edx

    addl 0(%ecx), %eax
    addl 0(%edx), %eax ;# eax = a + b
    pop %ebp
ret

iteratie: ;# 8(%ebp)= a, 12(%ebp)=b, -4(%ebp) = c
    push %ebp
    movl %esp, %ebp

    subl $4, %esp
    
    movl 12(%ebp), %eax
    movl 8(%ebp), %ecx
    pushl %eax ;#c=aduna(*a, *b);
    pushl %ecx
    call aduna
    addl $8, %esp
    p:
    movl %eax, -4(%ebp)
    
    movl 8(%ebp), %eax ;# (*a)=(*b);
    movl 12(%ebp), %ecx
    movl 0(%ecx), %edx
    movl %edx, 0(%eax)

    movl -4(%ebp), %eax ;# (*b)=c;
    movl %eax, 0(%ecx)

    addl $4, %esp
    pop %ebp
ret
.global main
main:
pushl $n
pushl $fs1
call scanf
addl $8, %esp

movl $2, %ecx
for_fibonacci:
    cmp %ecx, n
    je exit_for_fibonacci
    push %ecx

    pushl $y
    pushl $x
    call iteratie
    addl $8, %esp

    pop %ecx
    movl y, %eax
    movl %eax, z

    incl %ecx
    jmp for_fibonacci
exit_for_fibonacci:

pushl z
push $print
call printf
addl $8, %esp
exit:
movl $1, %eax
xorl %ebx, %ebx
int $0x80