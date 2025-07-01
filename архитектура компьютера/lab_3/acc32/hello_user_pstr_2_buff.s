    .data

buffer:          	.byte  '________________________________'
prefix:          	.byte  0x07, 'Hello, '
question:        	.byte  0x13, 'What is your name?\n'
postfix:         	.byte  0x01, '!'
name:            	.byte  '________________________________'

input_addr:      	.word  0x80
output_addr:     	.word  0x84

message_pointer: 	.word  0x00               ; pointer to message element
buffer_pointer:  	.word  0x00               ; pointer to buffer element
iterator:        	.word  0x00               ; loop counter
tmp:             	.word  0x00               ; temporary storage

const_0:         	.word  0x00
const_1:         	.word  0x01

    .data

.org             	0x88
const_symbols_left: .word  0x16               ; free space in buffer
const_endline:   	.word  0x0A               ; newline character
const_overflow:  	.word  0xCCCCCCCC         ; overflow output

const_byte_mask: 	.word  0x000000FF
const_rewrite_mask: .word  0xFFFFFF00


    .text

_start:
    load         question
    and          const_byte_mask
    store        iterator

    load_imm     question
    add          const_1
    store        message_pointer

print_question_loop:
    load_ind     message_pointer
    and          const_byte_mask
    store_ind    output_addr

    load         message_pointer
    add          const_1
    store        message_pointer

    load         iterator
    sub          const_1
    store        iterator

    bnez         print_question_loop

read_name:
    load         const_symbols_left
    store        iterator

    load_imm     name
    add          const_1
    store        message_pointer

read_name_loop:
    load_ind     input_addr
    store        tmp
    sub          const_endline
    beqz         store_name_len

    load_ind     message_pointer
    and          const_rewrite_mask
    or           tmp
    store_ind    message_pointer

    load         message_pointer
    add          const_1
    store        message_pointer

    load         iterator
    sub          const_1
    store        iterator

    ble          overflow
    jmp          read_name_loop

store_name_len:
    load         const_symbols_left
    sub          iterator
    store        tmp

    load         name
    and          const_rewrite_mask
    or           tmp
    store        name

store_full_len:
    load         prefix
    and          const_byte_mask
    store        tmp

    load         name
    and          const_byte_mask
    add          tmp
    store        tmp

    load         postfix
    and          const_byte_mask
    add          tmp
    store        buffer

copy_prefix:
    load         buffer_pointer
    add          const_1
    store        buffer_pointer

    load_imm     prefix
    add          const_1
    store        message_pointer

    load         prefix
    and          const_byte_mask
    store        iterator

copy_prefix_loop:
    load_ind     message_pointer
    and          const_byte_mask
    store        tmp

    load_ind     buffer_pointer
    and          const_rewrite_mask
    or           tmp
    store_ind    buffer_pointer

    load         buffer_pointer
    add          const_1
    store        buffer_pointer

    load         message_pointer
    add          const_1
    store        message_pointer

    load         iterator
    sub          const_1
    store        iterator

    beqz         copy_name

    jmp          copy_prefix_loop

copy_name:
    load_imm     name
    add          const_1
    store        message_pointer

    load         name
    and          const_byte_mask
    store        iterator

copy_name_loop:
    load         iterator
    beqz         copy_postfix

    load_ind     message_pointer
    and          const_byte_mask
    store        tmp

    load_ind     buffer_pointer
    and          const_rewrite_mask
    or           tmp
    store_ind    buffer_pointer

    load         buffer_pointer
    add          const_1
    store        buffer_pointer

    load         message_pointer
    add          const_1
    store        message_pointer

    load         iterator
    sub          const_1
    store        iterator

    jmp          copy_name_loop

copy_postfix:
    load_imm     postfix
    add          const_1
    store        message_pointer

    load_ind     message_pointer
    and          const_byte_mask
    store        tmp

    load_ind     buffer_pointer
    and          const_rewrite_mask
    or           tmp
    store_ind    buffer_pointer

output:
    load         const_1
    store        buffer_pointer

    load         buffer
    and          const_byte_mask
    store        iterator

output_loop:
    load_ind     buffer_pointer
    and          const_byte_mask
    store_ind    output_addr

    load         buffer_pointer
    add          const_1
    store        buffer_pointer

    load         iterator
    sub          const_1
    store        iterator

    bnez         output_loop

end:
    halt

overflow:
    load         const_overflow
    store_ind    output_addr
    halt
