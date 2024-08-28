section .text
global index
index:
	imul ecx, edx
	add ecx, r8d
	mov eax, [rdi + 4 * rcx]
	; rdi: matrix
	; esi: rows
	; edx: cols
	; ecx: rindex, i
	; r8d: cindex, j
	ret

; write an assembly program which given a matrix M and the 
; row and coun indexes i and j, retrieves item at 
; M[i][j]

; rdi, rsi, rdx, rcx, r8, r9