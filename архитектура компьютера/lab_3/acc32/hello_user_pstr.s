    .data
.org             0x00
buffer:          .byte  '________________________________', 0, 0, 0
prefix:          .byte  'Hello, \n', 0, 0, 0
question:        .byte  'What is your name?\n', 0, 0, 0
postfix:         .byte  '!\n', 0, 0, 0

    .data
.org             0x90
input_addr:      .word  0x80
output_addr:     .word  0x84

prefix_point:    .word  0x00               ; 㪠��⥫� �� ����� ��䨪�
buffer_point:    .word  0x00               ; 㪠��⥫� �� ����� ����
question_point:  .word  0x00               ; 㪠��⥫� �� ����� �����
counter:         .word  0x00               ; ���稪 ��� 横���
temp:            .word  0x00               ; �६����� ��६�����

cnst_buff_begin: .word  0x00
cnst_buff_size:  .word  0x20
cnst_qstion_len: .word  0x13
cnst_endline:    .word  0x0A               ; \n
cnst_overflow:   .word  0xCCCCCCCC         ; �뢮� ��� ��९�������

cnst_mask_begin: .word  0xFF
cnst_mask_end:   .word  0xFFFFFF00
cnst_init_simbl: .word  0x5F5F5F00

const_0:         .word  0x00
const_1:         .word  0x01
const_2:         .word  0x02
const_8:         .word  0x08

    .text
    .org         0x190
_start:
    ; ��४��뢠�� 㪠��⥫� ����
    load_addr    cnst_buff_begin
    add          const_1
    store_addr   buffer_point

    ; ��४��뢠�� 㪠��⥫� ��䨪�
    load_imm     prefix
    store_addr   prefix_point

    ; �����㥬 ��䨪� � ����
copying_prefix:
    ; �⠥� ᨬ��� �� prefix � �஢��塞 �� \n
    load_ind     prefix_point
    and          cnst_mask_begin
    sub          cnst_endline
    beqz         set_qstion_pointers

    ; ��᪨�㥬 � ������塞 � ����
    load_ind     prefix_point
    and          cnst_mask_begin
    store_ind    buffer_point

update_point:
    ; ������塞 㪠��⥫� �� ��䨪� � ����
    load_addr    prefix_point
    add          const_1
    store_addr   prefix_point

    load_addr    buffer_point
    add          const_1
    store_addr   buffer_point

    jmp          copying_prefix

    ; �뢮��� �����
set_qstion_pointers:
    ; ��⠭�������� 㪠��⥫� �� ��砫� �����
    load_imm     question
    store_addr   question_point

print_question:
    ; �뢮��� ��।��� ᨬ��������
    load_ind     question_point
    and          cnst_mask_begin
    store_ind    output_addr

update_qwtion_pointer:
    load_addr    question_point
    add          const_1
    store_addr   question_point

    load_addr    counter
    add          const_1
    store_addr   counter
    sub          cnst_qstion_len
    ble          print_question              ; if acc < 0 then pc <- <address>

    ; ������ ��� ���짮��⥫�
reading_loop:
    ; �஢��塞, ���� �� �� ���� � ����
    load_addr    buffer_point
    sub          cnst_buff_size
    add          const_2
    bgt          overflow

    ; �஢��塞 \n
    load_ind     input_addr
    store_addr   temp
    and          cnst_mask_begin
    sub          cnst_endline
    beqz         add_exclam_mark

    ; ��࠭塞 ���祭�� � ���� � ᫥���饬� ᨬ����
    load_addr    temp
    and          cnst_mask_begin
    store_ind    buffer_point

    load_addr    buffer_point
    add          const_1
    store_addr   buffer_point
    jmp          reading_loop

    ; ������塞 ��᪫��⥫�� ����
add_exclam_mark:
    load_addr    postfix
    and          cnst_mask_begin
    add          cnst_init_simbl
    store_ind    buffer_point

    ; �����뢠�� ����� ᮮ�饭�� � ��४��뢠�� 㪠��⥫� �� �����
set_size:
    load_addr    buffer_point
    store_addr   temp

    load_addr    const_1
    store_addr   buffer_point
    load_ind     buffer_point

    ; ᤢ����� ᫮�� ��稭�� � ��ண� ᨬ����
    ; � ᪫��뢠�� � ࠧ��஬ ��ப� �� �� �������� ��१����
    shiftl       const_8
    and          cnst_mask_end
    add          temp
    store_ind    cnst_buff_begin

    load_addr    const_0
    store_addr   counter

    ; �뢮��� �ਢ���⢨�
output_loop:
    ; �뢮��� ⥪�騩 ᨬ���
    load_ind     buffer_point
    and          cnst_mask_begin
    store_ind    output_addr

    ; ������� 㪠��⥫�
    load_addr    buffer_point
    add          const_1
    store_addr   buffer_point

    ; ����砥� ����� ��ப� �� ��ࢮ�� ����� �����
    load_ind     cnst_buff_begin
    and          cnst_mask_begin
    store_addr   temp

    ; 㢥��稢��� ���稪 �뢥������ ᨬ�����
    load_addr    counter
    add          const_1
    store_addr   counter
    sub          temp
    ble          output_loop

    halt

    ; ��ࠡ�⪠ ��९�������
overflow:
    load_addr    cnst_overflow
    store_ind    output_addr
    halt