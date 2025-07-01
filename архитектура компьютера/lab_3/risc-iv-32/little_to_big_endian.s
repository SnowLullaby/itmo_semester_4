    .data

input_addr:      .word  0x80
output_addr:     .word  0x84

number_of_swaps: .word  0x04
byte_mask:       .word  0x000000FF

const_8:         .word  0x08

    .text
	
read_from_input:
    lui      t0, %hi(input_addr)
    addi     t0, t0, %lo(input_addr)         ; t0 <- &input_addr;
    lw       t0, 0(t0)                       ; t0 <- *input_addr;

    lw       a0, 0(t0)                       ; a0 <- *t0;
    jr       ra

write_to_output:
    lui      t0, %hi(output_addr)
    addi     t0, t0, %lo(output_addr)        ; t0 <- output_addr;
    lw       t0, 0(t0)                       ; t0 <- *output_addr;

    sw       a0, 0(t0)                       ; *t0 <- a0;
    jr       ra


    ; args: a0 - number to shift
    ; return: a0 - zero, a1 - number of swaps, a2 - number to shift
	
prepare_arguments:
    mv       a2, a0

    lui      t0, %hi(number_of_swaps)
    addi     t0, t0, %lo(number_of_swaps)    ; t0 <- &number_of_swaps;
    lw       a1, 0(t0)                       ; a1 <- *number_of_swaps;

    mv       a0, zero
    jr       ra

    .text
    .org     0x200

_start:
    lui      sp, %hi(_start)
    addi     sp, sp, %lo(_start)             ; sp <- &_start;

    jal      ra, read_from_input
    jal      ra, prepare_arguments
    jal      ra, little_to_big
    jal      ra, write_to_output

    halt


    ; args: a0 - current result, a1 - number of swaps, a2 - number to shift
    ; return: a0 - full result
	
little_to_big:
    addi     sp, sp, -16
    sw       ra, 0(sp)
	sw		 a0, 4(sp)
	sw 		 a1, 8(sp)
	sw		 a2, 12(sp)
	
    ble      a1, zero, little_to_big_return

	mv		 a0, a1
	mv		 a1, a2

	jal		 ra, shifts
	
	mv		 t0, a0
	lw	     a0, 4(sp)
	lw		 a1, 8(sp)
	lw		 a2, 12(sp)

	add      a0, a0, t0

little_to_big_next:
    addi     a1, a1, -1
    jal      ra, little_to_big

little_to_big_return:
    lw       ra, 0(sp)
    addi     sp, sp, 16
    jr       ra


	; args: a0 - number of swaps, a1 - number to shift
    ; return: a0 - byte on new position

shifts:
	lui      t0, %hi(byte_mask)
    addi     t0, t0, %lo(byte_mask)
    lw       t0, 0(t0)

    lui      t1, %hi(const_8)
    addi     t1, t1, %lo(const_8)
    lw       t1, 0(t1)
	
shifts_shifts:
	addi     t2, a0, -1                      ; t2 <- (a0 - 1)
    mul      t2, t2, t1                      ; t2 <- (a0 - 1) * 8

    srl      t2, a1, t2                      ; target to last
    and      t0, t2, t0                      ; mask

    addi     t2, zero, 4
    sub      t2, t2, a0                      ; t2 <- (4 - a0)
    mul      t2, t2, t1                      ; t2 <- (4 - a0) * 8

    sll      t0, t0, t2                      ; target to position
    mv		 a0, t0
	
	jr		 ra