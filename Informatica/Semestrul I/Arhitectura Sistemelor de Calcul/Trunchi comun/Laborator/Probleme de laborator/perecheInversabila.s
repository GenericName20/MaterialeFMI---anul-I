.perecheInversabila
push %ebp
movl %ebp, %esp

pushl 20(%ebp)
pushl 12(%ebp)
pushl 8(%ebp)
call reciprocInverse
popl %ebx
popl %ebx
popl %ebx

cmp $1, %eax 
je m1_m2

pushl 20(%ebp)
pushl 16(%ebp)
pushl 12(%ebp)
call reciprocInverse
popl %ebx
popl %ebx
popl %ebx

cmp $1, %eax 
je m2_m3

pushl 20(%ebp)
pushl 16(%ebp)
pushl 8(%ebp)
call reciprocInverse
popl %ebx
popl %ebx
popl %ebx

cmp $1, %eax 
je m1_m3

movl $-1, %eax
movl $-1, %ecx

m1_m2:
lea 8(%ebp), %eax
lea 12(%ebp), %ecx
jmp et_exit

m1_m3:
lea 8(%ebp), %eax 
lea 16(%ebp), %ecx
jmp et_exit

m2_m3:
lea 12(%ebp), %ecx
lea 16(%ebp), %ecx
jmp et_exit

et_exit:
popl %ebx
popl %ebx
ret