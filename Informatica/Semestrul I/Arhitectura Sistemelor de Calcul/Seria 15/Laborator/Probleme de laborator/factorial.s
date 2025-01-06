.data
n: .space 4
fs1: .asciz "%ld"
print: .asciz "%ld\n"
.text
factorial: 
;# in ecx am un contor
;# in eax inmultirea
;# 8(%ebp) = n
    pushl %ebp
    movl %esp, %ebp

    movl 8(%ebp), %ecx
    cmp $0, %ecx
    jg continue

    movl $1, %eax ;# cazul cand n = 0
    jmp exit_factorial

    continue: ;# cazul cand n > 0
    movl 8(%ebp), %edx
    decl %edx

    push %edx
    call factorial
    addl $4, %esp

    movl 8(%ebp),%edx
    mull %edx
    
    exit_factorial:
    pop %ebp
ret
.global main
main:
pushl $n ;# read the number
push $fs1
call scanf
addl $8, %esp

push n 
call factorial
add $4, %esp

push %eax ;# print facotrial
push $print
call printf
add $8, %esp

exit:
movl $1, %eax
xorl %ebx, %ebx
int $0x80