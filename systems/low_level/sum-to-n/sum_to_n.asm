; write an assembly program which computes 
; the sum of the numbers 1 to n in a loop

section .text
global sum_to_n
sum_to_n:
	mov r9, rdi ; move argument into register

	mov r10, 0 ; total
	mov r8, 0 ; initial counter
	cmp r9, 0;
	je done
sum:
	inc r8;

	add r10, r8 ;
	cmp r9, r8 ;

	jg sum
done:
	mov rax, r10
	ret
