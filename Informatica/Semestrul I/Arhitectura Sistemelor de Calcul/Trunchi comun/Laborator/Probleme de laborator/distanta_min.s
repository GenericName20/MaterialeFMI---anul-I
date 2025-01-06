celeMaiApropiate:                      #pushl $matrice1
 pushl %ebp 
 movl %esp,%ebp
 pushl %ebx
 
 pushl 20(%ebp)
 pushl 16(%ebp)
 pushl 8(%ebp)
 call distantaCuvinte
 popl %ebx
 popl %ebx
 popl %ebx
 
 movl %eax,%edx           #val1
 
 pushl 20(%ebp)
 pushl 12(%ebp)
 pushl 8(%ebp)
 call distantaCuvinte
 popl %ebx
 popl %ebx
 popl %ebx
 
 movl %eax,%ecx        #val2
 jmp compar1

continuare: 
 pushl 16(%ebp)
 pushl 12(%ebp)
 pushl 8(%ebp)
 call distantaCuvinte
 popl %ebx
 popl %ebx
 popl %ebx
 
 movl %eax,%ecx
 jmp compar2

min_nou:
 movl %ecx,%edx 
 jmp continuare 

min_nou2:
 movl %ecx,%edx 
 jmp scot 
 
compar1:
 cmp %ecx,%edx              #%edx are val mai mica
 jl min_nou
 jmp continuare 
 
compar2:
 cmp %ecx,%edx
 jl min_nou2
 jmp scot
 
scot: 
 movl %edx,%eax
 popl %ebx
 popl %ebp
ret 