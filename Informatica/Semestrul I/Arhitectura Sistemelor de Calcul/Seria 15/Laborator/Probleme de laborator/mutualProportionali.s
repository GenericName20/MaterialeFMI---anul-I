.mutualProportionali
 push %ebp
 movl %ebp, %esp

 pushl 20(%ebp)
 pushl 16(%ebp)
 pushl 12(%ebp)
 call factorProportionalitate
 popl %ebx
 popl %ebx
 popl %ebx

 cmp $0, %eax
 je nu_sunt_proportionali

 pushl 20(%ebp)
 pushl 16(%ebp)
 pushl 8(%ebp)
 call factorProportionalitate
 popl %ebx
 popl %ebx
 popl %ebx

 cmp $0, %eax
 je nu_sunt_proportionali

 pushl 20(%ebp)
 pushl 12(%ebp)
 pushl 8(%ebp)
 call factorProportionalitate
 popl %ebx
 popl %ebx
 popl %ebx

 cmp $0, %eax
 je nu_sunt_proportionali

 movl $1, %eax
 popl %ebx
 ret


nu_sunt_proportionali:
 movl $1, %eax
 popl %ebx
 ret
