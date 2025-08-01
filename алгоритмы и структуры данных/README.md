# Алгоритмы. Контест

## 0. Квадратная строка?

**Ограничение времени:** 2 секунды  
**Ограничение памяти:** 256 Мб  
**Ввод:** стандартный ввод или `input.txt`  
**Вывод:** стандартный вывод или `output.txt`

### Легенда

Строка называется *квадратной*, если она состоит из двух одинаковых половин, записанных дважды подряд. Например, строки `"aa"`, `"abcabc"`, `"abab"` и `"baabaa"` — квадратные. Строки `"aaa"`, `"abaaab"` и `"abcdabc"` квадратными не являются.

Для заданной строки `s` определите, является ли она квадратной.

### Формат ввода

В первой строке входных данных записано целое число `t` (`1 ≤ t ≤ 100`) — количество наборов входных данных.

Далее следует `t` строк, каждая из которых содержит одну строку (только строчные буквы латинского алфавита), длина которой от 1 до 100.

### Формат вывода

Для каждого набора входных данных выведите:

- `YES`, если строка является квадратной,
- `NO` — в противном случае.

Регистр букв в ответе значения не имеет: система распознаёт как `YES`, так и `Yes`, `yEs`, `yes` и т.д.

### Пример

**Ввод:**
```
10
a
aa
aaa
aaaa
abab
abcabc
abacaba
xxyy
xyyx
xyxy
```

**Вывод:**
```
NO
YES
NO
YES
YES
YES
NO
NO
NO
YES
```

---

## A. Агроном-любитель

**Ограничение времени:** 2 секунды  
**Ограничение памяти:** 64 Мб  
**Ввод:** стандартный ввод или `agro.in`  
**Вывод:** стандартный вывод или `agro.out`

Городской школьник Лёша поехал на лето в деревню и занялся выращиванием цветов. Он посадил `n` цветков вдоль одной длинной прямой грядки, и они успешно выросли. Каждый цветок имеет вид `a_i`, где `a_i` — целое число, обозначающее тип цветка.

Лёша хочет сделать фотографию отрезка грядки. Он считает, что фотография будет неинтересной, если на ней встречается три одинаковых цветка подряд. Помогите ему найти самый длинный участок без трёх одинаковых цветков подряд (то есть такой, где нет последовательности вида `x x x`).

Если существует несколько таких участков одинаковой максимальной дины, выведите тот, который начинается раньше.

### Формат ввода

- Первая строка содержит целое число `n` (`1 ≤ n ≤ 200000`) — количество цветов.
- Вторая строка содержит `n` целых чисел `a_1, a_2, ..., a_n` (`1 ≤ a_i ≤ 10^9`), где каждое значение представляет вид цветка.

### Формат вывода

Выведите два целых числа — номер первого и последнего цветка на найденном участке. Цветки нумеруются с 1.

### Пример

**Ввод:**
```
6
5 6 6 6 23 9
```

**Вывод:**
```
3 6
```
---
## B. Зоопарк Глеба

**Ограничение времени:** 1 секунда  
**Ограничение памяти:** 256 Мб  
**Ввод:** стандартный ввод или `input.txt`  
**Вывод:** стандартный вывод или `output.txt`

### Условие

Глеб открыл зоопарк, построенный в форме круга. Все животные и ловушки расположены на краю окружности. Животные обозначаются маленькими буквами латинского алфавита, а соответствующие им ловушки — большими.

Порядок объектов задан строкой длины `2 * n`, где каждый символ — либо животное (маленькая буква), либо ловушка (большая буква). Порядок указан в порядке обхода по окружности из центра.

Вы хотите понять, возможно ли отправить каждое животное в свою ловушку так, чтобы пути между ними не пересекались. Если это возможно, выведите схему поимки.

### Формат ввода

- Одна строка длиной `2 * n` (`n ≤ 50000`), состоящая из маленьких и больших латинских букв.
- Маленькие буквы — животные, большие — ловушки.

### Формат вывода

- Выведите `Impossible`, если невозможно вернуть всех животных в свои ловушки без пересечений.
- Иначе выведите `Possible`, а затем через пробел номера позиций животных, попавших в ловушки, в порядке обхода ловушек.

> **Примечание:** индексы животных указываются в исходной строке (нумерация с 1).

### Примеры

**Пример 1**

**Ввод:**
```
ABba
```

**Вывод:**
```
Possible
2 1
```

**Пример 2**

**Ввод:**
```
ABab
```

**Вывод:**
```
Impossible
```
---
## C. Конфигурационный файл

**Ограничение времени:** 1 секунда  
**Ограничение памяти:** 64 Мб  
**Ввод:** стандартный ввод или `input.txt`  
**Вывод:** стандартный вывод или `output.txt`

### Условие

Вы разрабатываете парсер конфигурационных файлов, поддерживающий вложенные блоки и временное изменение значений переменных внутри этих блоков.

Формат строки:

- `{` — начало блока;
- `}` — конец блока;
- `<variable>=<number>` — присваивание числового значения переменной;
- `<variable1>=<variable2>` — присваивание значения другой переменной.

Изначально все переменные имеют значение `0`.

При выходе из блока все переменные, изменённые внутри него, восстанавливают свои значения, действовавшие **до входа в блок**.

Для каждой строки вида `<variable1>=<variable2>` требуется вывести значение, которое на момент выполнения этой операции имела переменная `<variable2>`.

### Формат ввода

Вход содержит не более `10^5` строк. Каждая строка — один из следующих типов:

- `{` — начало блока;
- `}` — конец блока;
- `имя_переменной=число` — присвоение числа;
- `имя_переменной1=имя_переменной2` — присвоение значения другой переменной.

Гарантируется корректность входных данных.

### Формат вывода

Для каждой строки вида `<variable1>=<variable2>` выведите значение, которое было взято у `<variable2>` на момент присваивания.

### Пример

**Ввод:**
```
a=b
b=123
var=b
b=-34
{
c=b
b=1000000000
d=b
{
a=b
e=var
}
}
b=b
```

**Вывод:**
```
0
123
-34
1000000000
1000000000
-34
```
---
## D. Профессор Хаос

**Ограничение времени:** 1 секунда  
**Ограничение памяти:** 64 Мб  
**Ввод:** стандартный ввод или `chaos.in`  
**Вывод:** стандартный вывод или `chaos.out`

### Условие

У профессора Хаоса есть эксперимент с бактериями, который длится несколько дней.

- В начале первого дня у него **`a`** бактерий.
- Каждый день:
    1. Все бактерии извлекаются из контейнера и помещаются в инкубатор, где каждая делится на **`b`** новых.
    2. После этого извлекается **`c`** бактерий для опытов. Если их меньше, чем `c`, эксперимент заканчивается.
    3. Оставшиеся бактерии кладутся обратно в контейнер, но не более **`d`** штук (остальные уничтожаются).

Вам нужно определить, сколько бактерий будет в контейнере после **`k`**-го дня.

Если к какому-либо дню бактерий станет меньше, чем `c`, выведите `0`.

### Формат ввода

Единственная строка содержит пять целых чисел:

```
a b c d k
```

Где:
- `a` — начальное количество бактерий
- `b` — коэффициент размножения
- `c` — количество используемых ежедневно бактерий
- `d` — максимальное количество бактерий в контейнере
- `k` — номер дня, для которого нужно определить результат

**Ограничения:**  
`1 ≤ a, b ≤ 1000`  
`0 ≤ c ≤ 1000`  
`1 ≤ d ≤ 1000`  
`a ≤ d`  
`1 ≤ k ≤ 10^18`

### Формат вывода

Выведите одно число — количество бактерий в контейнере после `k`-го дня или `0`, если эксперимент завершился раньше.

### Примеры

**Пример 1**

**Ввод:**
```
1 3 1 5 2
```

**Вывод:**
```
5
```

**Пример 2**

**Ввод:**
```
1 2 0 4 3
```

**Вывод:**
```
4
```

**Пример 3**

**Ввод:**
```
1 2 3 5 2
```

**Вывод:**
```
0
```
---
## E. Коровы в стойла

**Ограничение времени:** 0.1 секунды  
**Ограничение памяти:** 256 Мб  
**Ввод:** стандартный ввод или `input.txt`  
**Вывод:** стандартный вывод или `output.txt`

### Условие

На прямой расположены стойла, в которые нужно расставить `K` коров так, чтобы **минимальное расстояние между любыми двумя коровами** было **максимальным**.

### Формат ввода

- Первая строка содержит два целых числа: `N` — количество стойл (`2 < N ≤ 100000`), `K` — количество коров (`1 < K < N`).
- Вторая строка содержит `N` целых чисел в порядке возрастания — координаты стойл (не превосходят `10^9`).

### Формат вывода

Выведите одно число — наибольшее возможное минимальное расстояние между коровами.

### Примеры

**Пример 1**

**Ввод:**
```
6 3
2 5 7 11 15 20
```

**Вывод:**
```
9
```

**Пример 2**

**Ввод:**
```
5 3
1 2 3 100 1000
```

**Вывод:**
```
99
```
---
## F. Число

**Ограничение времени:** 1 секунда  
**Ограничение памяти:** 256 Мб  
**Ввод:** стандартный ввод или `number.in`  
**Вывод:** стандартный вывод или `number.out`

### Условие

После того как Васино число было разрезано на части, осталось несколько строк, каждая из которых содержит последовательность цифр. Ваша задача — определить **максимальное число**, которое можно составить, **склеив все эти кусочки в некотором порядке**.

### Формат ввода

- Первая строка: количество строк `t` (`1 ≤ t ≤ 100`)
- Далее `t` строк, каждая содержит от `1` до `100` цифр (от `'0'` до `'9'`).
- Гарантируется, что хотя бы одна строка **не начинается с нуля**.

### Формат вывода

- Выведите одну строку — максимальное возможное число, полученное конкатенацией всех частей в некотором порядке.

### Примеры

**Пример 1**

**Ввод:**
```
4
2
20
004
66
```

**Вывод:**
```
66220004
```

**Пример 2**

**Ввод:**
```
2
3
3
```

**Вывод:**
```
33
```
---
## G. Кошмар в замке

**Ограничение времени:** 2 секунды  
**Ограничение памяти:** 256 Мб  
**Ввод:** стандартный ввод или `aurora.in`  
**Вывод:** стандартный вывод или `aurora.out`

### Условие

Дана строка `s`, состоящая из строчных букв латинского алфавита (`1 ≤ |s| ≤ 100000`). Каждой букве от `'a'` до `'z'` назначен неотрицательный вес `c_i`, не превосходящий `2^31 - 1`.

Вес строки определяется следующим образом:

> Для каждой буквы в строке вычисляется **максимальное расстояние между двумя одинаковыми буквами** (разность между самой правой и самой левой позицией этой буквы). Это значение умножается на вес буквы. Общий вес строки — сумма таких значений по всем типам букв.

Ваша задача — переставить буквы в строке так, чтобы полученная строка имела **максимально возможный вес**. Если существует несколько вариантов, выведите любой.

### Формат ввода

- Первая строка: исходная строка `s`.
- Вторая строка: 26 целых чисел — веса букв от `'a'` до `'z'`.

### Формат вывода

Выведите одну строку — любую перестановку `s`, имеющую максимальный возможный вес.

### Пример

**Ввод:**
```
lkshrules
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25
```

**Вывод:**
```
slkhruels
```
---
## H. Магазин

**Ограничение времени:** 2 секунды  
**Ограничение памяти:** 256 Мб  
**Ввод:** стандартный ввод или `shop.in`  
**Вывод:** стандартный вывод или `shop.out`

### Условие

Билл хочет купить `n` товаров и разбить их на несколько чеков, чтобы воспользоваться акцией:

> В каждом чеке каждый `k`-й товар (округление вниз) бесплатно — то есть оплачиваются только самые дорогие товары, а самые дешевые из каждой группы по `k` штук достаются бесплатно.

Цель — минимизировать общую сумму, которую заплатит Билл за все товары, используя оптимальное разбиение на чеки.

### Формат ввода

- Первая строка содержит два целых числа: `n`, `k` (`1 ≤ n ≤ 100000`, `2 ≤ k ≤ 100`)
- Вторая строка содержит `n` целых чисел: `a_1, a_2, ..., a_n` — цены товаров (`1 ≤ a_i ≤ 10000`)

### Формат вывода

Выведите одно число — минимальную сумму, которую придется заплатить Биллу.

### Пример

**Ввод:**
```
5 2
200 100 1000 400 100
```

**Вывод:**
```
1300
```

### Пояснение к примеру:

Если оформить один чек:
- Товары: [100, 100, 200, 400, 1000] (отсортированы)
- Бесплатными будут 2 самых дешевых (по 100)
- Сумма: 200 + 400 + 1000 = 1600

Если оформить два чека:
- Чек 1: [1000, 400, 200, 100] → 1 бесплатный (100) → сумма: 1300
- Чек 2: [100] → 0 бесплатных → сумма: 100
- Итого: 1400 → не лучший вариант

> **Примечание:** Лучшая стратегия — разбить так, чтобы максимальное количество самых дешевых товаров стало бесплатными.

---
## I. Машинки

**Ограничение времени:** 1 секунда  
**Ограничение памяти:** 256 Мб  
**Ввод:** стандартный ввод или `input.txt`  
**Вывод:** стандартный вывод или `output.txt`

### Условие

У Пети есть `N` различных машинок, которые хранятся на полке, недоступной для него. На полу может одновременно находиться не более `K` машинок.

Петя играет с машинками в порядке, заданном последовательностью из `P` запросов. Если нужная машинка уже на полу — он берет её сам. Если её нет — мама должна **достать эту машинку с полки и убрать одну из тех, что на полу**, по своему выбору.

Задача: определить **минимальное количество операций**, которые маме придётся выполнить (т.е. сколько раз ей нужно будет поменять машинку на полке), чтобы удовлетворить всю последовательность запросов.

Изначально все машинки находятся на полке.

### Формат ввода

- Первая строка: три целых числа `N`, `K`, `P`  
  (`1 ≤ K, N ≤ 100000`, `1 ≤ P ≤ 500000`)
- Следующие `P` строк: номера машинок, в порядке, в котором Петя захочет с ними играть

### Формат вывода

- Одно целое число — минимальное количество операций

### Пример

**Ввод:**
```
3 2 7
1
2
3
1
3
1
2
```

**Вывод:**
```
4
```
---
## J. Гоблины и очереди

**Ограничение времени:** 0.6 секунд  
**Ограничение памяти:** 256 Мб  
**Ввод:** стандартный ввод или `input.txt`  
**Вывод:** стандартный вывод или `output.txt`

### Условие

Гоблины приходят к шаману и формируют очередь по следующим правилам:

- Обычные гоблины (`+ i`) встают **в конец очереди**.
- Привилегированные гоблины (`* i`) встают **ровно в середину очереди**:
  - При нечётной длине очереди — **сразу после центра**.

Требуется обрабатывать запросы и для каждого типа `-` выводить номер гоблина, выходящего из очереди (первый в очереди).

### Формат ввода

- Первая строка: целое число `N` (`1 ≤ N ≤ 100000`) — количество запросов
- Далее `N` строк с запросами одного из видов:
  - `+ i` — обычный гоблин с номером `i`
  - `* i` — привилегированный гоблин с номером `i`
  - `-` — первый гоблин уходит к шаману

Гарантируется корректность запросов (например, что очередь не пуста при `-`).

### Формат вывода

Для каждого запроса вида `-` выведите номер гоблина, который ушёл к шаману.

### Примеры

**Пример 1**

**Ввод:**
```
7
+ 1
+ 2
-
+ 3
+ 4
-
-
```

**Вывод:**
```
1
2
3
```

**Пример 2**

**Ввод:**
```
2
* 1
+ 2
```

**Вывод:**
(нет вывода, так как нет запроса `-`)
---
## K. Менеджер памяти-1

**Ограничение времени:** 1 секунда  
**Ограничение памяти:** 64 Мб  
**Ввод:** стандартный ввод или `input.txt`  
**Вывод:** стандартный вывод или `output.txt`

### Условие

Реализуйте простой **менеджер памяти**, управляющий выделением и освобождением блоков памяти в массиве из `N` ячеек.

#### Операции:

- **Запрос на выделение памяти (`K`)**:
  - Нужно найти **свободный блок** из `K` последовательных ячеек.
  - Если такой блок существует, выделите его и верните **номер первой ячейки** этого блока.
  - При выборе блока приоритет отдается такому, что **непосредственно перед первой ячейкой нет свободной ячейки** (то есть он находится "вплотную" к занятым блокам).
  - Если таких блоков несколько — выберите тот, который начинается с **наименьшей позиции**.
  - Если выделить невозможно, выведите `-1`.

- **Запрос на освобождение памяти (`-T`)**:
  - Освобождает блок, выделённый при запросе номер `T`.
  - Если запрос `T` был отклонён (вернул `-1`) — игнорируйте текущий запрос.
  - Освобождённые блоки снова доступны для выделения.

### Формат ввода

- Первая строка: два целых числа `N`, `M`:
  - `N` — размер памяти (`1 ≤ N ≤ 2^31 - 1`)
  - `M` — количество запросов (`1 ≤ M ≤ 100000`)
- Следующие `M` строк содержат по одному числу:
  - Положительное число `K` — запрос на выделение `K` ячеек
  - Отрицательное число `-T` — запрос на освобождение, соответствующий запросу `T`

> Гарантируется корректность входных данных.

### Формат вывода

Для каждого запроса на выделение памяти:

- Выведите номер первой ячейки выделенного блока, либо `-1`, если выделить не удалось.

### Примеры

**Пример 1**

**Ввод:**
```
42 9
7
3
8
-2
6
5
-5
9
4
```

**Вывод:**
```
1
8
11
19
25
30
19
```

**Пример 2**

**Ввод:**
```
128 12
1
2
4
-2
8
-3
16
-5
32
-7
64
-1
```

**Вывод:**
```
1
2
4
8
16
32
64
```
---
## L. Минимум на отрезке

**Ограничение времени:** 0.5 секунд  
**Ограничение памяти:** 256 Мб  
**Ввод:** стандартный ввод или `input.txt`  
**Вывод:** стандартный вывод или `output.txt`

### Условие

Дана последовательность целых чисел длины `N`. По ней двигается "окно" длины `K`: сначала видны первые `K` элементов, затем — следующие `K`, начиная со второго элемента, и так до конца.

Требуется для каждого положения окна вывести **минимальное значение** в этом окне.

### Формат ввода

- Первая строка: два целых числа `N` и `K` (`1 ≤ N ≤ 150000`, `1 ≤ K ≤ 10000`, `K ≤ N`)
- Вторая строка: `N` целых чисел — элементы последовательности (по модулю не превосходят `10^5`)

### Формат вывода

- `N - K + 1` строк — минимумы для каждого положения "окна"

### Пример

**Ввод:**
```
7 3
1 3 2 4 5 3 1
```

**Вывод:**
```
1
2
2
3
5
3
1
```

> **Примечание:** Для эффективного решения используйте структуру данных **дек (deque)** для хранения индексов минимальных значений в текущем окне.
---
## M. Цивилизация

**Ограничение времени:** 1.5 секунд  
**Ограничение памяти:** 256 Мб  
**Ввод:** стандартный ввод или `input.txt`  
**Вывод:** стандартный вывод или `output.txt`

### Условие

Карта мира в игре представляет собой прямоугольник размером `N x M`, разбитый на квадратные клетки.

- Каждая клетка может быть:
  - `.` — поле (стоимость перемещения: **1**)
  - `W` — лес (стоимость перемещения: **2**)
  - `#` — вода (нельзя перемещаться)

Поселенец начинает с заданной стартовой клетки и должен добраться до конечной, затратив **минимальное время**.

Перемещение возможно только в соседние по стороне клетки.

### Формат ввода

- Первая строка: два целых числа `N`, `M` (`≤ 1000`) — размеры карты
- Вторая строка: `x_start y_start` — координаты начальной точки
- Третья строка: `x_end y_end` — координаты конечной точки
- Далее `N` строк: карта (`'.'`, `'W'`, `'#'`)

> ⚠️ **Важно:** координаты даны как `(строка, столбец)`, нумерация с **1**, строки сверху вниз, столбцы слева направо.

### Формат вывода

- В первой строке: минимальное время пути (или `-1`, если путь невозможен)
- Во второй строке: строка из символов `'N'`, `'E'`, `'S'`, `'W'`, описывающая маршрут

### Пример

**Ввод:**
```
4 8 1 1 4 8
....WWWW
.######.
.#..W...
...WWWW.
```

**Вывод:**
```
13
SSSEENEEEEES
```
---
## N. Свинки-копилки

**Ограничение времени:** 1 секунда  
**Ограничение памяти:** 256 Мб  
**Ввод:** стандартный ввод или `input.txt`  
**Вывод:** стандартный вывод или `output.txt`

### Условие

У Васи есть `n` свинок-копилок, пронумерованных от `1` до `n`. Каждая копилка может быть открыта:

- Либо с помощью ключа (если он доступен),
- Либо разбита.

Ключ от каждой копилки хранится в какой-то другой копилке (возможно, даже в самой себе).

Вася хочет достать все деньги из копилок, разбив их минимальное количество. Остальные копилки он сможет открыть с помощью найденных ключей.

Ваша задача — определить **минимальное количество копилок, которые нужно разбить**, чтобы получить доступ ко всем деньгам.

### Формат ввода

- В первой строке: целое число `n` (`1 ≤ n ≤ 100`) — количество копилок
- В следующих `n` строках: для каждой копилки указан номер той, в которой лежит её ключ

### Формат вывода

- Одно целое число: минимальное количество копилок, которые нужно разбить

### Пример

**Ввод:**
```
4
2
1
2
4
```

**Вывод:**
```
2
```

### Пояснение

Можно, например, разбить копилки `1` и `4`. Тогда:
- Из `1` получаем ключ от `2`
- Из `2` — ключ от `1` (уже открыта), и ключ от `3`
- Из `4` — ключ от `4` (уже открыта)

Таким образом, все копилки становятся доступны.

---
## O. Долой списывание!

**Ограничение времени:** 2 секунды  
**Ограничение памяти:** 64 Мб  
**Ввод:** стандартный ввод или `input.txt`  
**Вывод:** стандартный вывод или `output.txt`

### Условие

Учитель заметил, что во время теста некоторые ученики обменивались записками. Теперь он хочет разделить всех учеников на **две группы**:

- Одни — только **дают списывать**,
- Другие — только **списывают**.

Обмен запиской всегда должен происходить **от одного к другому**, то есть от одного типа ученика — к другому (никаких обменов внутри одной группы).

Задача: определить, возможно ли разделить учеников на две такие группы, чтобы все обмены записками были **в направлении "из одной группы — в другую"**.

Это сводится к задаче проверки **ориентированного графа на двудольность**.

---

### Формат ввода

- Первая строка: два целых числа `N`, `M` (`1 ≤ N ≤ 100`, `0 ≤ M ≤ N*(N-1)/2`) — количество учеников и количество пар
- Следующие `M` строк: по две различные целые числа — номера учеников, между которыми был обмен записками

---

### Формат вывода

- Выведите `"YES"` если разделение возможно
- Иначе выведите `"NO"`

---

### Пример

**Ввод:**
```
3 2
1 2
2 3
```

**Вывод:**
```
YES
```

> Это означает, что граф можно разделить на две доли так, чтобы каждое ребро шло из одной доли в другую — граф является **двудольным ориентированным графом**.
---
## P. Авиаперелёты

**Ограничение времени:** 2 секунды  
**Ограничение памяти:** 256 Мб  
**Ввод:** стандартный ввод или `avia.in`  
**Вывод:** стандартный вывод или `avia.out`

### Условие

Дана матрица стоимости перелётов между `n` городами (`1 ≤ n ≤ 1000`).

- Расход топлива на перелёт из города `i` в город `j` задан как `cost[i][j]`.
- Все значения неотрицательны и меньше `10^9`.
- Расход из города в себя равен нулю: `cost[i][i] = 0`.

Требуется найти **минимальный размер топливного бака**, при котором можно долететь **из любого города в любой другой**, совершая дозаправки по пути.

Это эквивалентно нахождению **максимального веса ребра в минимальном остове графа**, то есть решается задачей построения **минимального остовного дерева (Minimum Spanning Tree, MST)**.

---

### Формат ввода

- Первая строка: целое число `n` — количество городов
- Следующие `n` строк: по `n` чисел в каждой — матрица смежности графа

---

### Формат вывода

- Одно число — минимальный возможший размер топливного бака

---

### Пример

**Ввод:**
```
4
0 10 12 16
11 0 8 9
10 13 0 22
13 10 17 0
```

**Вывод:**
```
10
```

> Это максимальный вес ребра в минимальном остовном дереве графа.
