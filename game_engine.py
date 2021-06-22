import os

PLAYERS = ['Х', 'O']    # Массив игроков


def set_size_map():
    '''
        Функция выбора размера карты
        :return: размер карты - int
    '''
    try:
        error = False
        replay = True
        count = 3
        while replay:
            os.system("cls")
            print("Добро пожаловать в крестики-нолики!\n")
            if error:
                print("Вы выбрали слишком маленький размер карты.")
                error = False
            count = int(input("Введите размер карты.\nПо-умолчанию - 3: "))
            if count < 3:
                error = True
                continue
            replay = False
        return count
    except ValueError:
        return 3
    

def instruction(size_map):
    '''
        Инструкция
        :size_map: размер карты - int
        :return: Правила игры
    '''
    text_intro = f"""Крестики-Нолики.
Правила:
1) Игроки ходят по очереди. Первым ходит игрок, ставящий крестик (X).
2) Ходить можно только в пустую клетку. За раз можно сделать только один ход.
3) На каждом ходу игроку нужно ввести две цифры без пробела:
   первая: номер по горизонтали
   вторая: номер по вертикали
4) Побеждает тот, кто раньше выстроит свои символы в линию длины {size_map}:
   по горизонтали,
   по вертикали,
   по диоганали.
   Удачной игры!
    """
    return text_intro


def outro(player, win, dead_heat=False):
    '''
        Текст для окончания игры
        :player: текущий игрок - элемент массива PLAYERS
        :win: проверка победы - bool
        :dead_heat: проверка ничьи - bool
        :return: текст окончания игры в зависимости от ситуации:
            Ничья или Победа.
    '''
    if not win and dead_heat:
        text_outro = "Ничья!"
    else:
        text_outro = f"""
Пободитель - игрок, ставящий {player}.
Поздравляем!
    """
    return text_outro


def draw(table, size_map):
    '''
        Функция отрисовки поля
        :table: игровое поле - [char][char]
        :size_map: размер карты - int
        :return: None
    '''
    os.system("cls")
    print(instruction(size_map))
    
    head_line = " "
    for i in range(size_map):
        head_line += f" {i}"
    print(head_line)

    for i in range(size_map):
        main_lines = f"{i}"
        for j in range(size_map):
            main_lines += f" {table[i][j]}"
        print(main_lines)


def player_input(player):
    '''
        Ввод значений с клавиатуры
        :player: текущий игрок - элемент массива PLAYERS
        :return: координаты хода игрока - (int, int)
    '''
    _input = input(f"Ходит {player}: ")
    _input = tuple(map(int, _input))
    return _input


def check_move(position, possible_position):
    '''
        Проверка доступности хода
        :position: координаты хода игрока - (int, int)
        :possible_position: список доступных ходов -
        :return: None
    '''
    return position in possible_position


def move(table, player, position, possible_position):
    '''
        Функция фиксации хода грока
        :table: игровое поле - [char][char]
        :player: текущий игрок - элемент массива PLAYERS
        :position: координаты хода игрока - (int, int)
        :possible_position: список доступных ходов -
        :return: изменённые массивы table, possible_position
    '''
    possible_position.remove(position)
    table[position[0]][position[1]] = player
    return table, possible_position


def winning(table, player, winning_combinations):
    '''
        Проверка победы
        :table: игровое поле - [char][char]
        :player: текущий игрок - элемент массива PLAYERS
        :winning_combinations: список хранящий списки выигрышных комбинаций -
                                [[(int, int), (int, int), (int, int)]]
        :return: True/False
    '''
    for comb in winning_combinations:
        check_comb = []
        for i, j in comb:
            check = True if table[i][j] == player else False
            check_comb.append(check)
        if False in check_comb:
            continue
        else:
            return True
    return False
    

def set_winning_combinations(size_map):
    '''
        Функция генерирует выигрышные комбинации для переданного размера карты
        :size_map: размер карты - int
        :return: список хранящий списки выигрышных комбинаций -
                    [[(int, int), (int, int), (int, int)]]
    '''
    winning_combinations = [[(i, j) for j in range(size_map)] for i in range(size_map)]
    winning_combinations += [[(i, j) for i in range(size_map)] for j in range(size_map)]
    winning_combinations += [[(i, i) for i in range(size_map)]]
    winning_combinations += [[(i, size_map - 1 - i) for i in range(size_map)]]
    return winning_combinations
