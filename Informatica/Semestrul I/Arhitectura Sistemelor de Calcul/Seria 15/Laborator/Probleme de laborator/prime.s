.data
	x: .long 42
	message1: .asciz "prime"
	message2: .asciz "not prime"

.text

.global main

main:

	mov x, %eax
	mov $1, %ebx
	sub %ebx, %eax
	mov %eax, %ecx

etloop:
	mov $1, %eax
	cmp %eax, %ecx
	je etP

	mov x, %eax
	mov $0, %edx
	div %ecx

	mov $0, %eax	
	cmp %edx, %eax
	je etNP
	loop etloop

etNP: 
	mov $4, %eax
	mov $1, %ebx
	mov $message2, %ecx
	mov $10, %edx
	int $0x80
	jmp exit

etP:
	mov $4, %eax
	mov $1, %ebx
	mov $message1, %ecx
	mov $6, %edx
	int $0x80

exit:
	mov $1, %eax
	mov $0, %ebx
	int $0x80
	