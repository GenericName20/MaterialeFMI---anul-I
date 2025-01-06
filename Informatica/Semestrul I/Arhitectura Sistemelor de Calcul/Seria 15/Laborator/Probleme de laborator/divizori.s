.data
x: .space 4

fs1: .asciz "%ld"
print: .asciz "%ld\n"
.text
divisors: ;#8(%ebp) = x
pushl %ebp
movl %esp, %ebp

movl $1, %ecx
for_divizori:
    cmp 8(%ebp), %ecx
    je exit_for_divizori

    movl 8(%ebp), %eax
    xorl %edx, %edx
    divl %ecx

    cmp $0, %edx
    jne continue

    pushl %ecx
    pushl $print
    call printf
    pop %edx
    pop %ecx
    continue:
    incl %ecx
    jmp for_divizori
exit_for_divizori:
pop %ebp
ret
.global main
main:
pushl $x
pushl $fs1
call scanf
addl $8, %esp

pushl x
call divisors
addl $4, %esp

exit:
movl $1, %eax
xorl %ebx, %ebx
int $0x80