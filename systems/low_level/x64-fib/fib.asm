section .text
global fib
fib:
	cmp rdi, 1
	jle .base_case

	; recursive case: fib(n)= fib(n-1) +fib(n-2)
	; save current n on stack
	push rdi

	; calculate fib(n-1)
	dec rdi
	call fib
	mov rbx, rax ; save fib(n-1) in RBX

	;restore rdi and calculate fib(n-2)
	pop rdi
	push rbx ; save fib(n-1) result on stack first
	sub rdi, 2
	call fib
	pop rbx

	add rax, rbx
	ret


.base_case:
	mov rax, rdi
	ret

;  int fib (int n) {
;  	if (n <= 1) return n;
;  	return fib(n - 1) + fib(n - 2);
;  } 