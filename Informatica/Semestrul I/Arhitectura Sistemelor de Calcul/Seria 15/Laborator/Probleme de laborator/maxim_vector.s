.data
    n: .long 3
    arr: .long 8, 16, 16, 16
    maxim: .long 0
    occ: .long 1

.text
.global main

main:
    lea arr, %edi
    mov n, %ecx
    mov $0, %ebx
    jmp etloop

etmax:
    movl %edx, %ebx
    mov $1, %eax
    loop etloop

jmp compare

cnt:
    add $1, %eax
    loop etloop

compare:
    mov $0, %eax
    cmp %ecx, %eax
    je exit
    
etloop:
    movl (%edi, %ecx, 4), %edx
    cmp %ebx, %edx
    jg etmax
    je cnt
    loop etloop

exit:
    mov $1, %eax
    xor %ebx, %ebx
    int $0x80