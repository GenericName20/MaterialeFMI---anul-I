.data
sir: .space 80
number: .space 4

fs1: .asciz "%s"
print: .asciz "%ld\n"
.text
atoi_replica:
    pushl %ebp
    movl %esp, %ebp

    subl $8, %esp
    push %edi
    push %ebx
    
    pushl 8(%ebp)
    call strlen
    addl $4, %esp
    
    movl %eax, -4(%ebp) ;# -4(%ebp) = strlen(sir)

    movl $0, -8(%ebp) ;# initializam numarul cu 0
    mov 8(%ebp), %edi
    xorl %ecx, %ecx
    for_atoi:
        cmp %ecx, -4(%ebp)
        je exit_for_atoi

        mov (%edi, %ecx, 1), %bl
        
        cmp $'0', %bl
        jl brute_exit

        cmp $'9', %bl
        jg brute_exit

        subb $'0', %bl
        movl -8(%ebp), %eax
        movl $10, %edx
        mull %edx
        movl %eax, -8(%ebp)

        addb %bl, -8(%ebp)

        continue: ;# used in brute exit, if in the beginning are spaces, it will ignore them
        incl %ecx
        jmp for_atoi

        brute_exit: ;#cand un caracter nu este number
            cmp $' ', %bl
            jne reset
            
            movl -8(%ebp), %eax
            cmp $0, %eax
            jne reset

            jmp continue ;# if there is a space in the beginning then will continue the for
            reset:
            movl $0, -8(%ebp)
    exit_for_atoi:

    movl -8(%ebp), %eax ;# return number

    pop %ebx
    pop %edi

    addl $8, %esp
    pop %ebp
ret
.global main
main:

push $sir
call gets
push $sir
call atoi_replica
pop %ebx

movl %eax, number ;# the result of the function will be in %eax

pushl number
pushl $print
call printf
addl $8, %esp
exit:
movl $1, %eax
xorl %ebx, %ebx
int $0x80