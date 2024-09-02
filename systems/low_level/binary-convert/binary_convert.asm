section .text
global binary_convert
binary_convert:
	xor eax, eax

.loop:
	movzx edx, byte [rdi] ; c = *s
	cmp edx, 0
	je .end

	shl rax, 1
	cmp edx, '0'
	je .next_char

	cmp edx, '1'
	je .add_one

.add_one:
	add eax, 1

.next_char:
	inc rdi
	jmp .loop

.end:
	ret





; eg string 10101
; div -> ax / operand, dx = remainder

; write a program to convert a string of ascii 
; 1s and 0s to the corresponding integer value

; 0 is 48 in ascii
; 1 is 49
; null is 0
