N = 3   # размер поля (не более 9)
max_N = N ** 2  # макс. число ячеек
count = 0   # число ходов (занятых ячеек)
Null_Symbol = '-'
Symbols = ['X', 'O']     # допустимые символы

Gamer = False   # 0 - начинают крестики, 1 - начинают нолики
s_range = [str(i) for i in range(N)]    # допустимые значения для ввода координат
Field = [[Null_Symbol for j in range(N)] for i in range(N)]     # инициализация игрового поля


def print_field():  # печать текущего состояния игровго поля
    print(" \t", end='')
    for i in range(N):  # вынесение номеров столбцов
        print(i, "\t", end='')
    for i in range(N):
        print()
        print(i, "\t", end='')  # вынесение номеров строк
        for j in range(N):
            print(Field[i][j], "\t", end='')
    print()
    return


def check_input(string):
    string = string.strip()
    string = string.replace(',', ' ')
    string = string.replace('.', ' ')

    while '  ' in string:   # удаление лишних пробелов
        string = string.replace('  ', ' ')

    crd_list = string.split(' ')    # получение списка координат

    if crd_list[0] in s_range and crd_list[1] in s_range: # проверка, не превышают ли введённые значения размер игрового поля
        i = [int(crd_list[0]), int(crd_list[1])]
    else:
        i = [-1, -1]    # [-1, -1] - признак неверно введеного значения
    return i


def set_input(coords):  # занесение введённой координаты в игровое поле
    if Field[coords[1]][coords[0]] == Null_Symbol:
        Field[coords[1]][coords[0]] = Symbols[int(Gamer)]    # присвоение ячейке текущего символа
        print_field()
        return True
    else:
        print("Указанная ячейка ", coords, " уже отмечена! Повторите ввод координаты.")
        return False


def check():
    for i in range(N):
        if Field[i][0] != Null_Symbol and Field[i][0] == Symbols[int(Gamer)]:  # просмотр поля по горизонтали
            k = 1
            for j in range(1, N):
                if Field[i][j] != Symbols[int(Gamer)]:   # сравнение с текущим символом
                    break   # если символ в ряду отичается от предыдущего, дальнейшее сравннеие не имеет смысла
                else:
                    k += 1
            if k == N:  # все ячейки совпадают с текущим символом - победа!
                return True
        if Field[0][i] != Null_Symbol and Field[0][i] == Symbols[int(Gamer)]:  # просмотр поля по вертикали
            k = 1
            for j in range(1, N):
                if Field[j][i] != Symbols[int(Gamer)]:   # сравнение с текущим символом
                    break
                else:
                    k += 1
            if k == N:
                return True

    if Field[0][0] != Null_Symbol and Field[0][0] == Symbols[int(Gamer)]:  # просмотр поля по 1-й диагонали
        k = 1
        for j in range(1, N):
            if Field[j][j] != Symbols[int(Gamer)]:   # сравнение с текущим символом
                break
            else:
                k += 1
        if k == N:
            return True

    if Field[N-1][0] != Null_Symbol and Field[N-1][0] == Symbols[int(Gamer)]:  # просмотр поля по 2-й диагонали
        k = 1
        for j in range(1, N):
            if Field[N-1-j][j] != Symbols[int(Gamer)]:   # сравнение с текущим символом
                break
            else:
                k += 1
        if k == N:
            return True
    return False


print("Начинаем игру 'Крестики-нолики'!\n"
      "Ввод ходов производится через пробел или запятую.\n"
      "Первое значение - координата по горизонтали, второе - по вертикали.")

while True:
    while True:
        i = check_input(input(str("Введите ход игрока №" + str(int(Gamer) + 1) + " (" + Symbols[int(Gamer)] + "): ")))
        if i == [-1, -1]:   # введено неверное значение
            print("Ошибка ввода! Повторите ввод координаты.")
        else:
            if set_input(i):    # установка значения ячейки
                break

    count += 1  # счётчик ходов

    if check():     # проверка поля на наличие полных линий
        print(f"Игра закончена!\nПобедил игрок №{str(int(Gamer) + 1)} ('{Symbols[int(Gamer)]}')")
        break

    if count == max_N:  # все ячейки заполнены
        print("Игра закончена.\nНичья!")
        break

    Gamer = not Gamer
