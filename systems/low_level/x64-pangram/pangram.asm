%define MASK 0x07fffffe

section .text
global pangram
pangram:
	; rdi: source string
	xor ecx, ecx ; bs = 0

.loop: 
	movzx edx, byte [rdi] ; fill eveyrthing else as 0  c = *s
	cmp edx, 0
	je .end

	add rdi, 1 ; s++
	cmp edx, '@' ; if c is in first 64 chars of ascii table
	jl .loop ; continue

	and edx, 0x1f 

	bts ecx, edx ; bitset
	jmp .loop

	; mov r8, 1
	; shl r8, edx
	; or ecx, r8

.end:
	xor eax, eax
	; TODO sometimes we should return 1
	and ecx, MASK
	cmp ecx, MASK
	sete al
	ret





; bool ispangram(char *s) {
;   uint32_t bs = 0;
;   char c;
;   while ((c = *s++) != '\0') {
;     if (c < '@')
;       continue; // ignore first 64 chars in ascii table
;     bs |= 1 << (c & 0x1f);
;   }
;   return (bs & MASK) == MASK;
; }