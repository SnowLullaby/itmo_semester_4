    .data
input_addr:      .word  0x80
output_addr:     .word  0x84

cnst_overflow:   .word  0xCCCCCCCC
cnst_out_of_bnd: .word	0xFFFFFFFF

    .text
_start:
	@p input_addr a! @
	
	fibonacci
	
	@p output_addr a! !
	halt
	
fibonacci:
    dup inv         
    -if invalid_output_end    

	dup lit -1 +
	if zero_and_unit
	
	dup
	if zero_and_unit
	
	dup lit -1 +  
	fibonacci 
	
	over
	lit -2 +  
	fibonacci 
	
	+ dup inv lit 1 +         
    -if overflow_end  
	;

zero_and_unit:
	;

invalid_output_end:
	drop 
	@p cnst_out_of_bnd
	@p output_addr a! !
	halt
	;
	
overflow_end:
	drop 
	@p cnst_overflow
	@p output_addr a! !
	halt
	;
	