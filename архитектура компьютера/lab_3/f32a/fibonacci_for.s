    .data

input_addr:      .word  0x80
output_addr:     .word  0x84

const_overflow:  .word  0xCCCCCCCC
const_out_of_bnd: .word  0xFFFFFFFF

    \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    .text

dec:
    lit -1 +
    ;

inc:
    lit 1 +
    ;

    \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

_start:
    @p input_addr a! @
    fibonacci
    @p output_addr a! !
    halt

    \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

fibonacci:
    dup inv                  \ !n:n:[]
    -if invalid_input_end

    dup
    if fibonacci_return

    dup dec                  \ n-1:n:[]
    if fibonacci_return

fibonacci_init:
    dec                      \ n-1:[]
    lit 0                    \ x:n:[]
    lit 1                    \ y:x:n:[]

fibonacci_loop:
    dup a!                   \ A:y
    +                        \ x+y:n:[]

    check_overflow
    if overflow_end

    decrement_second         \ x+y:n-1:[]

    over                     \ n-1:x+y:[]
    dup
    if fibonacci_done
    over                     \ x+y:n-1:[]

    put_a_second             \ x+y:y:n-1:[] , A:y

    fibonacci_loop ;

fibonacci_done:
    over
    ;

fibonacci_return:
    ;

    \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    .text
    .org 0x88


invalid_input_end:
    drop
    @p const_out_of_bnd
    ;

    \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

check_overflow:
    dup
    inv inc
    -if check_overflow_true

    lit 1
    ;

check_overflow_true:
    lit 0
    ;

overflow_end:
    drop drop
    @p const_overflow
    ;

    \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

decrement_second:
    over
    dec
    over                     \ x:n-1:[]
    ;

put_a_second:
    a over
    ;
