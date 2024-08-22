    global _main
    extern _puts

    section .text
_main: push rbx ; call stack must be aligned
    lea rdi, [rel message] ; first argument is address of message
    call _puts ; puts(message)
    pop rbx ; fix up stack before returning
    ret

    section .data
message: db "Hola, mundo", 0