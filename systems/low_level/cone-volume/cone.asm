default rel

section .data
	pi dd 3.14159 ; define pi
	three_single dd 3.0
section .text
global volume
volume:
	mulss xmm0, xmm0
	mulss xmm0, xmm1
	mulss xmm0, dword [pi]
	divss xmm0, dword [three_single]
 	ret

; d word is 4 bytes, 32 bit

;   pi * r * r * h / 3
