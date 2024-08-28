; write an assembly program which computes 
; the sum of the numbers 1 to n in a loop

section .text
global sum_to_n
; sum_to_n:
; 	mov r9, rdi ; move argument into register

; 	mov r10, 0 ; total
; 	mov r8, 0 ; initial counter
; 	cmp r9, 0;
; 	je done
; sum:
; 	inc r8;

; 	add r10, r8 ;
; 	cmp r9, r8 ;

; 	jg sum
; done:
; 	mov rax, r10
; 	ret

; int sum = N*(N+1)/2

sum_to_n:
	lea rax, [rdi + 1] ; load effective address to add 1 to rdi, reuslt stored in rax
	; computes effective address second operate and stores it in the first
	imul rax, rdi ; imul is signed multiplication
	sar rax, 1 ; sar is arithmetic shift right
	ret