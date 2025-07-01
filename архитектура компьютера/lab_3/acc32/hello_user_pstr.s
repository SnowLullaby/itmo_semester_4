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

prefix_point:    .word  0x00               ; указатель на элемент префикса
buffer_point:    .word  0x00               ; указатель на элемент буфера
question_point:  .word  0x00               ; указатель на элемент вопроса
counter:         .word  0x00               ; счетчик для циклов
temp:            .word  0x00               ; временная переменная

cnst_buff_begin: .word  0x00
cnst_buff_size:  .word  0x20
cnst_qstion_len: .word  0x13
cnst_endline:    .word  0x0A               ; \n
cnst_overflow:   .word  0xCCCCCCCC         ; вывод для переполнения

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
    ; перекидываем указатель буфера
    load_addr    cnst_buff_begin
    add          const_1
    store_addr   buffer_point

    ; перекидываем указатель префикса
    load_imm     prefix
    store_addr   prefix_point

    ; копируем префикс в буфер
copying_prefix:
    ; читаем символ из prefix и проверяем на \n
    load_ind     prefix_point
    and          cnst_mask_begin
    sub          cnst_endline
    beqz         set_qstion_pointers

    ; маскируем и добавляем в буфер
    load_ind     prefix_point
    and          cnst_mask_begin
    store_ind    buffer_point

update_point:
    ; обновляем указатель на префикс и буфер
    load_addr    prefix_point
    add          const_1
    store_addr   prefix_point

    load_addr    buffer_point
    add          const_1
    store_addr   buffer_point

    jmp          copying_prefix

    ; выводим вопрос
set_qstion_pointers:
    ; устанавливаем указатель на начало вопроса
    load_imm     question
    store_addr   question_point

print_question:
    ; выводим очередной символвопроса
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

    ; вводим имя пользователя
reading_loop:
    ; проверяем, есть ли еще место в буфере
    load_addr    buffer_point
    sub          cnst_buff_size
    add          const_2
    bgt          overflow

    ; проверяем \n
    load_ind     input_addr
    store_addr   temp
    and          cnst_mask_begin
    sub          cnst_endline
    beqz         add_exclam_mark

    ; сохраняем значение и идем к следующему символу
    load_addr    temp
    and          cnst_mask_begin
    store_ind    buffer_point

    load_addr    buffer_point
    add          const_1
    store_addr   buffer_point
    jmp          reading_loop

    ; добавляем восклицательный знак
add_exclam_mark:
    load_addr    postfix
    and          cnst_mask_begin
    add          cnst_init_simbl
    store_ind    buffer_point

    ; записываем длину сообщения и перекидываем указатель на печать
set_size:
    load_addr    buffer_point
    store_addr   temp

    load_addr    const_1
    store_addr   buffer_point
    load_ind     buffer_point

    ; сдвигаем слово начиная со второго символа
    ; и складываем с размером строки что бы избежать перезаписи
    shiftl       const_8
    and          cnst_mask_end
    add          temp
    store_ind    cnst_buff_begin

    load_addr    const_0
    store_addr   counter

    ; выводим приветствие
output_loop:
    ; выводим текущий символ
    load_ind     buffer_point
    and          cnst_mask_begin
    store_ind    output_addr

    ; двигаем указатель
    load_addr    buffer_point
    add          const_1
    store_addr   buffer_point

    ; получаем длину строки из первого элемента буферу
    load_ind     cnst_buff_begin
    and          cnst_mask_begin
    store_addr   temp

    ; увеличиваем счетчик выведенных символов
    load_addr    counter
    add          const_1
    store_addr   counter
    sub          temp
    ble          output_loop

    halt

    ; обработка переполнения
overflow:
    load_addr    cnst_overflow
    store_ind    output_addr
    halt