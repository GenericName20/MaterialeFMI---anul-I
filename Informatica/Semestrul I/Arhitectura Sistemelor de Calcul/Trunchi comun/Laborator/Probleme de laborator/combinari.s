.data
n: .space 4
k: .space 4

fs1: .asciz "%ld"
print: .asciz "combinari de %ld luate cate %ld sunt %ld\n" ;# {n} {k} {%eax = rezolvarea}
.text
combinari: ;# 8(%ebp) = n, 12(%ebp) = k
;# cand k == 0 return 1
;# cand k == n return 1
pushl %ebp
movl %esp, %ebp
pushl %ebx
movl 8(%ebp), %ecx
movl 12(%ebp), %edx

cmp %ecx, %edx  ;#cand k == n return 1
jne verif

movl $1, %eax 
jmp exit_combinari

verif:
cmp $0, %edx ;# cand k == 0 return 1
jne continue

movl $1, %eax
jmp exit_combinari
continue: ;# C(n, k) = C(n − 1, k) + C(n − 1, k − 1).
;# folosesc %ebx pentru adunarea celor 2 valori
;# folosesc %ecx = n, %edx = k
;# folosesc %eax pentru returnare

decl %ecx
pushl %edx
pushl %ecx
call combinari
pop %ecx
pop %edx

movl %eax, %ebx
decl %edx

pushl %edx
pushl %ecx
call combinari
pop %ecx
pop %edx

addl %eax, %ebx

movl %ebx, %eax
exit_combinari:
pop %ebx
pop %ebp
ret
.global main
main:
;#citesc n
pushl $n
pushl $fs1
call scanf
addl $8, %esp
;# citesc k
pushl $k
pushl $fs1
call scanf
addl $8, %esp

xorl %ebx, %ebx
pushl k
pushl n
call combinari ;# return %eax
addl $8, %esp

pushl %eax
pushl k
pushl n
pushl $print
call printf
addl $12, %esp

exit:
movl $1, %eax
xorl %ebx, %ebx
int $0x80